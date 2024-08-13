import pygame
from random import randint, random


class TelaInicial:
    def __init__(self, largura_jogo, altura_jogo, fonte_padrao):
        self.largura_jogo = largura_jogo
        self.altura_jogo = altura_jogo
        self.font_texto = pygame.font.Font(fonte_padrao, 18)
        self.image_fundo = pygame.image.load('assets/img/starfield.png') # Carrega uma imagem
        self.tamanho_fundo = (largura_jogo, altura_jogo)
    

    def atualiza_estado(self):
        for event in pygame.event.get(): # Retorna uma lista com todos os eventos que ocorreram desde a última vez que essa função foi chamada
            if event.type == pygame.QUIT: 
                return -1

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return 1
        
        return 0
        

    def desenha(self, window):
        window.fill((0, 0, 0))

        fundo = pygame.transform.scale(self.image_fundo, self.tamanho_fundo) # Redefinir dimensão da imagem
        window.blit(fundo, (0, 0)) # Desenha a imagem já carregada por pygame.image.load em window na posição (x, y).

        texto_inicio = self.font_texto.render(f'CLIQUE "EBTER" PARA INICIAR O JOGO', True, (255, 255, 255)) # Cria uma imagem do texto
        window.blit(texto_inicio, (100, 300)) # Desenha a imagem já carregada por pygame.image.load em window na posição (x, y).

        pygame.display.update()