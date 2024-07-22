import pygame
import random
import Constantes
import spritesheet

class Snake:
    def __init__(self, x, y):
        self.velocidadeX = 0
        self.velocidadeY = 0
        self.tamanho = 1
        self.pixels = []
        self.direcao = 'direita'
        self.x = x
        self.y = y

    def atualizar_direcao(self, nova_direcao):
        if (nova_direcao == 'direita' and self.direcao != 'esquerda'):
            self.velocidadeX = Constantes.TamanhoQuadrado
            self.velocidadeY = 0
            self.direcao = nova_direcao
        elif (nova_direcao == 'esquerda' and self.direcao != 'direita'):
            self.velocidadeX = -Constantes.TamanhoQuadrado
            self.velocidadeY = 0
            self.direcao = nova_direcao
        elif (nova_direcao == 'baixo' and self.direcao != 'cima'):
            self.velocidadeX = 0
            self.velocidadeY = Constantes.TamanhoQuadrado
            self.direcao = nova_direcao
        elif (nova_direcao == 'cima' and self.direcao != 'baixo'):
            self.velocidadeX = 0
            self.velocidadeY = -Constantes.TamanhoQuadrado
            self.direcao = nova_direcao

    def mover(self):
        self.x += self.velocidadeX
        self.y += self.velocidadeY
        self.pixels.append([self.x, self.y])
        if len(self.pixels) > self.tamanho:
            del self.pixels[0]

    def desenhar(self, tela, sprites, frame):
        for pixel in self.pixels[:-1]:
            if self.direcao == 'direita':
                tela.blit(Constantes.corpoDireita, pixel)
            elif self.direcao == 'esquerda':
                tela.blit(Constantes.corpoEsquerda, pixel)
            elif self.direcao == 'baixo':
                tela.blit(Constantes.corpoBaixo, pixel)
            elif self.direcao == 'cima':
                tela.blit(Constantes.corpoCima, pixel)
        if self.direcao == 'direita':
            tela.blit(sprites['direita'][frame], self.pixels[-1])
        elif self.direcao == 'esquerda':
            tela.blit(sprites['esquerda'][frame], self.pixels[-1])
        elif self.direcao == 'baixo':
            tela.blit(sprites['baixo'][frame], self.pixels[-1])
        elif self.direcao == 'cima':
            tela.blit(sprites['cima'][frame], self.pixels[-1])

    def checar_colisao(self, largura, altura):
        if self.x < 40 or self.x >= largura or self.y < 40 or self.y >= altura:
            return True
        for pixel in self.pixels[:-1]:
            if pixel == [self.x, self.y]:
                return True
        return False

class Comida:
    def __init__(self):
        self.x, self.y = self.gerar()

    def gerar(self):
        comidaX = round(random.randrange(40, Constantes.ComidaLargura - Constantes.TamanhoQuadrado) / 20.0) * 20
        comidaY = round(random.randrange(40, Constantes.ComidaAltura - Constantes.TamanhoQuadrado) / 20.0) * 20
        return comidaX, comidaY

    def desenhar(self, tela):
        tela.blit(Constantes.nRosca, [self.x, self.y])

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Snake')
        self.tela = pygame.display.set_mode((Constantes.largura, Constantes.altura))
        self.relogio = pygame.time.Clock()
        self.fimJogo = False
        self.snake = Snake(Constantes.largura / 2, Constantes.altura / 2)
        self.comida = Comida()
        self.sprites = self.carregar_sprites()
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 100
        self.velocidade = 7  # Velocidade inicial do jogo

    def carregar_sprites(self):
        sprites = {
            'direita': [],
            'esquerda': [],
            'cima': [],
            'baixo': []
        }
        animation_steps = 16
        for x in range(animation_steps):
            sprites['direita'].append(Constantes.sprite_sheet_dir.get_image(x, 40, 40, 1, Constantes.branco))
            sprites['esquerda'].append(Constantes.sprite_sheet_esq.get_image(x, 40, 40, 1, Constantes.preta))
            sprites['cima'].append(Constantes.sprite_sheet_cima.get_image(x, 40, 40, 1, Constantes.branco))
            sprites['baixo'].append(Constantes.sprite_sheet_baixo.get_image(x, 40, 40, 1, Constantes.branco))
        return sprites

    def desenhar_pontuacao(self, pontuacao):
        fonte = pygame.font.SysFont('Arial', 20)
        texto = fonte.render(f'Pontos: {pontuacao}', True, Constantes.branco)
        self.tela.blit(texto, [270, 15])

    def atualizar_frame(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_cooldown:
            self.frame += 1
            self.last_update = current_time
            if self.frame >= len(self.sprites['cima']):
                self.frame = 0

    def rodar(self):
        while not self.fimJogo:
            self.tela.fill(Constantes.cinza)
            pygame.draw.rect(self.tela, Constantes.vermelho, (50, 50, Constantes.ComidaAltura, Constantes.ComidaLargura))
            self.atualizar_frame()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.fimJogo = True
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RIGHT:
                        self.snake.atualizar_direcao('direita')
                    elif evento.key == pygame.K_LEFT:
                        self.snake.atualizar_direcao('esquerda')
                    elif evento.key == pygame.K_UP:
                        self.snake.atualizar_direcao('cima')
                    elif evento.key == pygame.K_DOWN:
                        self.snake.atualizar_direcao('baixo')

            self.comida.desenhar(self.tela)
            self.snake.mover()
            self.snake.desenhar(self.tela, self.sprites, self.frame)

            if self.snake.checar_colisao(Constantes.ComidaLargura + 30, Constantes.ComidaAltura + 30):
                self.fimJogo = True

            if self.snake.x == self.comida.x and self.snake.y == self.comida.y:
                self.snake.tamanho += 1
                self.comida = Comida()
                if self.snake.tamanho %5 == 0:
                    self.velocidade += 1  # Aumenta a velocidade ao comer comida
            self.desenhar_pontuacao(self.snake.tamanho - 1)
            pygame.display.update()
            self.relogio.tick(self.velocidade)

game = Game()
game.rodar()
