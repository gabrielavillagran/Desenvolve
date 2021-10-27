import pygame
from pygame.locals import *
from sys import exit
from random import randint

# "*" importando todas funções e constantes
# As variaveis x e y vão controlar o movimento do retangulo
pygame.init()

pygame.mixer.music.set_volume(0.03)
pygame.mixer.music.load('jazz.mp3.mp3')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('smw_chuck_whistle.wav')
barulho_colisao.set_volume(0.2)

largura = 640
altura = 480

x_cobra = int(largura / 2)
y_cobra = int(altura / 2)
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

velocidade = 5
x_controle = velocidade
y_controle = 0

# desconsideramos a altura do retangulo na tela
x_maca = randint(40, 600)
y_maca = randint(50, 430)

# Pontos e texto
pontos = 0
fonte = pygame.font.SysFont('arial', 40, bold=True, italic=True)

# Para alterar o nome da janela

pygame.display.set_caption('Jogo')

# o 'for' vai detectar se o evento ocorreu
# o primeiro valor da tupla é referente ao x e o segundo ao y
# tela.fill((0,0,0)) para "limpar a tela", temos o loop infinito preenchendo a tela de preto, sensação de movimento
# Para o retangulo continuar na janela

lista_cobra = []
comprimento_inicial = 10
morreu = False


def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 20, 20))


def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cabeca, lista_cobra, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial = 10
    x_cobra = int(largura / 2)
    y_cobra = int(altura / 2)
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    morreu = False


while True:
    relogio.tick(60)
    tela.fill((0, 0, 0))

    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = - velocidade
                    y_controle = 0
            if event.key == K_d or event.key == K_RIGHT:
                if x_controle == - velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w or event.key == K_UP:
                if y_controle == velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = - velocidade
            if event.key == K_s or event.key == K_DOWN:
                if y_controle == - velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = velocidade

    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle

    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20))
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 17, 17))

    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos += 1
        barulho_colisao.play()
        comprimento_inicial = comprimento_inicial + 2

    # posição x e y atual
    lista_cabeca = [x_cobra, y_cobra]

    # posição assumida

    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('Arial', 20, True, False)
        mensagem = 'Game over! Pressione a tecla R para jogar novamente '
        texto_formatado = fonte2.render(mensagem, True, (0, 0, 0))
        ret_texto = texto_formatado.get_rect()

        morreu = True
        while morreu:
            tela.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura // 2, altura // 2)
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()

    if x_cobra > 624:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = 624
    if y_cobra < 0:
        y_cobra = 464
    if y_cobra > 464:
        y_cobra = 0

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    # aumenta cobra
    aumenta_cobra(lista_cobra)
    tela.blit(texto_formatado, (420, 10))

    pygame.display.update()
    """pygame.draw.circle(tela, (0, 0, 200), (300, 260), 40)
    pygame.draw.line(tela, (255, 255, 0), (390, 0), (390, 600), 5)"""
