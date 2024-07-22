import pygame
import sys
import Constantes
pygame.init()


BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)

LARGURA_TELA = 600
ALTURA_TELA = 600
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Menu de Jogo")


fonte = pygame.font.Font(None, 74)
fonte_pequena = pygame.font.Font(None, 50)

def desenhar_texto(texto, fonte, cor, superficie, x, y):
    objeto_texto = fonte.render(texto, True, cor)
    retangulo_texto = objeto_texto.get_rect()
    retangulo_texto.topleft = (x, y)
    superficie.blit(objeto_texto, retangulo_texto)


opcoes_menu = ["Iniciar Jogo", "Sair"]
opcao_selecionada = 0

def iniciar_jogo():
    import Main
    Main.game.rodarJogo()


executando = True
while executando:
    tela.fill(PRETO)

    
    desenhar_texto("Jogo da Cobrinha", fonte, BRANCO, tela, 100, 50)
    tela.blit(Constantes.cobrinha_oficial, [0, 100])
    for i, opcao in enumerate(opcoes_menu):
        cor = VERDE if i == opcao_selecionada else BRANCO
        desenhar_texto(opcao, fonte_pequena, cor, tela, 350, 200 + i * 60)


    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                opcao_selecionada = (opcao_selecionada + 1) % len(opcoes_menu)
            if evento.key == pygame.K_DOWN:
                opcao_selecionada = (opcao_selecionada + 2 ) % len(opcoes_menu)
            if evento.key == pygame.K_RETURN:
                if opcao_selecionada <= 1:
                    iniciar_jogo()
                    executando = False
                if opcao_selecionada > 1:
                    pygame.quit()
                    sys.exit()

    pygame.display.update()
