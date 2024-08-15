import pygame
from random import randint, random
import numpy as np
class Torre:
    def __init__(self,tamanho,posicao):
        self.imagem = pygame.image.load('jogo_estilo_angry_birds/assets/img/torre.png')
        self.tamanho = tamanho 
        self.posicao =posicao

    def desenha(self,window):
        torre = pygame.transform.scale(self.imagem, self.tamanho) # Redefinir dimensão da imagem
        window.blit(torre, self.posicao) # Desenha a imagem já carregada por pygame.image.load em window na posição (x, y).


class Canhao:
    def __init__(self,tamanho,posicao):
        self.imagem = pygame.image.load('jogo_estilo_angry_birds/assets/img/canhao.png')
        self.tamanho_imagem= tamanho
        self.posicao = posicao

    def desenha(self, window):
        canhao = pygame.transform.scale(self.imagem, self.tamanho_imagem) # Redefinir dimensão da imagem
        window.blit(canhao, self.posicao) # Desenha a imagem já carregada por pygame.image.load em window na posição (x, y).


        

class Atrator:
    def __init__(self, posição, raio, gravidade, tamanho):
        self.imagem_atrator = pygame.image.load('jogo_estilo_angry_birds/assets/img/planeta1.png')
        self.tamanho_imagem = tamanho
        self.posicao = posição   
        self.raio = raio
        self.gravidade = gravidade
        

        
    def calcula_atracao(self, posicao_jogador):
        # Calcular vetor de distância
        d_vec = self.posicao - posicao_jogador
        d = np.linalg.norm(d_vec)

        # Calcular aceleração gravitacional
        if d > 0:
            a = (self.gravidade / d**2) * (d_vec / d)
        else:
            a = np.array([0, 0])

        return a
    

    def desenha(self, window):
        nave = pygame.transform.scale(self.imagem_atrator, self.tamanho_imagem) # Redefinir dimensão da imagem
        window.blit(nave, self.posicao) # Desenha a imagem já carregada por pygame.image.load em window na posição (x, y).

class Bolinha():
    def __init__(self,s0,v0,posicao_torre,tamanho):
        self.imagem = pygame.image.load('jogo_estilo_angry_birds/assets/img/bola_canhao.png')
        self.s0 = np.array(s0)
        self.v0 = np.array(v0)
        self.torre=np.array(posicao_torre)
        self.tamanho=tamanho
        self.posicoes = self.s0
        self.velocidade = self.v0

    
    def atualiza_estado(self,torre,aceleracao):
            if self.posicoes[0]<10 or self.posicoes[0]>390 or self.posicoes[1]<10 or self.posicoes[1]>390: # Se eu chegar ao limite da tela, reinicio a posição do personagem
                self.posicoes= self.s0
                self.velocidades = torre-self.v0
                self.velocidades= self.velocidades*0.05
            else:
                self.velocidades= self.velocidades + aceleracao
                self.posicoes = self.posicoes + self.velocidades

    def desenha(self,window):
        bolinha = pygame.transform.scale(self.imagem, self.tamanho) # Redefinir dimensão da imagem
        window.blit(bolinha, self.posicoes) # Desenha a imagem já carregada por pygame.image.load em window na posição (x, y).


class TelaInicial:
    def __init__(self, largura_jogo, altura_jogo, fonte_padrao, FPS):
        self.largura_jogo = largura_jogo
        self.altura_jogo = altura_jogo
        self.font_texto = pygame.font.Font(fonte_padrao, 18)
        self.image_fundo = pygame.image.load('jogo_estilo_angry_birds/assets/img/starfield.png') # Carrega uma imagem
        self.tamanho_fundo = np.array([largura_jogo, altura_jogo])
        self.fps = FPS
        self.clock = pygame.time.Clock()
    

    def atualiza_estado(self):
        for event in pygame.event.get(): # Retorna uma lista com todos os eventos que ocorreram desde a última vez que essa função foi chamada
            if event.type == pygame.QUIT: 
                return -1

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return 1
        
        self.clock.tick(self.fps)
        
        return 0
        

    def desenha(self, window):
        window.fill((0, 0, 0))

        fundo = pygame.transform.scale(self.image_fundo, self.tamanho_fundo) # Redefinir dimensão da imagem
        window.blit(fundo, (0, 0)) # Desenha a imagem já carregada por pygame.image.load em window na posição (x, y).

        texto_inicio = self.font_texto.render(f'CLIQUE "EBTER" PARA INICIAR O JOGO', True, (255, 255, 255)) # Cria uma imagem do texto
        window.blit(texto_inicio, (100, 300)) # Desenha a imagem já carregada por pygame.image.load em window na posição (x, y).

        pygame.display.update()


class telaJogo:
    def __init__(self, largura_jogo, altura_jogo, fonte_padrao, FPS, s0, v0, tamanho_bola, tamanho_torre, posicao_torre, tamanho_canhao, posicao_canhao, posicao_atrator, raio_atrator, gravidade_atrator, tamanho_atrator):
        self.largura_jogo = largura_jogo
        self.altura_jogo = altura_jogo
        self.font_texto = pygame.font.Font(fonte_padrao, 18)
        self.image_fundo = pygame.image.load('jogo_estilo_angry_birds/assets/img/starfield.png') # Carrega uma imagem
        self.tamanho_fundo = np.array([largura_jogo, altura_jogo])
        self.fps = FPS
        self.clock = pygame.time.Clock()
        self.s0 = np.array(s0)
        self.v0 = np.array(v0)
        self.tamanho_bola = np.array(tamanho_bola)
        self.tamanho_torre = np.array(tamanho_torre)
        self.posicao_torre = np.array(posicao_torre)
        self.tamanho_canhao = np.array(tamanho_canhao)
        self.posicao_canhao = np.array(posicao_canhao)
        self.posicao_atrator = np.array(posicao_atrator)
        self.tamanho_atrator = np.array(tamanho_atrator)
        self.raio_atrator = raio_atrator
        self.gravidade_atrator = gravidade_atrator
        self.bolinha = Bolinha(self.s0, self.v0, self.posicao_torre, self.tamanho_bola)
        self.torre = Torre(self.tamanho_torre, self.posicao_torre)
        self.canhao = Canhao(self.tamanho_canhao, self.posicao_canhao)
        self.atrator = Atrator(self.posicao_atrator, self.raio_atrator, self.gravidade_atrator, self.tamanho_atrator)


    def atualiza_estado(self):
        for event in pygame.event.get(): # Retorna uma lista com todos os eventos que ocorreram desde a última vez que essa função foi chamada
            if event.type == pygame.QUIT: 
                return -1                                                                                                                                                                                       
        
        a = self.atrator.calcula_atracao(self.s0)

        self.bolinha.atualiza_estado(self.posicao_torre, a)

        self.clock.tick(self.fps)

        return 1


    def desenha(self, window):
        window.fill((0, 0, 0))

        fundo = pygame.transform.scale(self.image_fundo, self.tamanho_fundo) # Redefinir dimensão da imagem
        window.blit(fundo, (0, 0)) # Desenha a imagem já carregada por pygame.image.load em window na posição (x, y).

        self.bolinha.desenha(window)

        self.torre.desenha(window)

        self.atrator.desenha(window)

        self.canhao.desenha(window)


        pygame.display.update()


class Jogo:
    def __init__(self):
        pygame.init()
        self.largura_jogo = 550
        self.altura_jogo = 600
        self.fonte_padrao = pygame.font.get_default_font() # Carrega a fonte padrão
        self.window = pygame.display.set_mode((self.largura_jogo, self.altura_jogo))
        self.fps = 60
        self.s0 = np.array([50, 550])
        self.v0 = np.array([-5, -5])
        self.tamanho_bola = np.array([30, 30])
        self.tamanho_torre = np.array([100, 100])
        self.posicao_torre = np.array([500, 50])
        self.tamanho_canhao = np.array([80, 80])
        self.posicao_canhao = np.array([self.largura_jogo - self.tamanho_canhao[0], self.altura_jogo - self.tamanho_canhao[1] ])
        self.posicao_atrator = np.array([350, 200])
        self.tamanho_atrator = np.array([80, 80])
        self.raio_atrator = 40
        self.gravidade_atrator = 1000
        self.indice_tela_atual = 0
        self.telas = [TelaInicial(self.largura_jogo, self.altura_jogo, self.fonte_padrao, self.fps), telaJogo(self.largura_jogo, self.altura_jogo, self.fonte_padrao, self.fps, self.s0, self.v0, self.tamanho_bola, self.tamanho_torre, self.posicao_torre, self.tamanho_canhao, self.posicao_canhao, self.posicao_atrator, self.raio_atrator, self.gravidade_atrator, self.tamanho_atrator)]

    def game_loop(self):
        tela_atual = self.telas[self.indice_tela_atual]

        rodando = True
        while rodando:
            self.indice_tela_atual = tela_atual.atualiza_estado()

            if self.indice_tela_atual == -1:
                rodando = False
            else:
                tela_atual = self.telas[self.indice_tela_atual]
                tela_atual.desenha(self.window)
                
