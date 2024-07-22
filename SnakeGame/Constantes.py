import pygame
import spritesheet

#Dimenções
largura, altura = 600, 600
ComidaAltura = altura - 100
ComidaLargura = largura - 100
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

#Cores RGB
preta = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
amarelo = (0, 0, 255)
azul = (0, 255, 255)
cinza = (50, 50, 50)


#Parametros da Cobra
TamanhoQuadrado = 20
Velocidade = 7


#Arquivos de Imagens
sprite_sheet_image_direita = pygame.image.load('Sprites/cobraSpritesheetDireita.png').convert_alpha()
sprite_sheet_image_esquerda = pygame.image.load('Sprites/cobraSpritesheetEsquerda.png').convert_alpha()
sprite_sheet_image_cima = pygame.image.load('Sprites/cobraSpritesheetCima.png').convert_alpha()
sprite_sheet_image_baixo = pygame.image.load('Sprites/cobraSpritesheetBaixo.png').convert_alpha()
sprite_sheet_dir = spritesheet.SpriteSheet(sprite_sheet_image_direita)
sprite_sheet_esq = spritesheet.SpriteSheet(sprite_sheet_image_esquerda)
sprite_sheet_cima = spritesheet.SpriteSheet(sprite_sheet_image_cima)
sprite_sheet_baixo = spritesheet.SpriteSheet(sprite_sheet_image_baixo)
fundo = pygame.image.load("Sprites/Fundo.png")
novaImg = pygame.transform.scale(fundo, (largura, altura))
rosca = pygame.image.load("Sprites/Rosca.png")
nRosca = pygame.transform.scale(rosca, (32, 32))
corpoDireita = pygame.image.load("Sprites/CorpoRIGHT.png")
corpoEsquerda = pygame.image.load("Sprites/CorpoLEFT.png")
corpoCima = pygame.image.load("Sprites/CorpoUP.png")
corpoBaixo = pygame.image.load("Sprites/CorpoDOWN.png")
cobrinha_oficial = pygame.image.load("Sprites/Cobrinha_oficial.png")