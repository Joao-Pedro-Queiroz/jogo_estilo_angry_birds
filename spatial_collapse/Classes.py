import pygame
from random import randint, random
import numpy as np
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
class Buraco:
    def __init__(self,tamanho,posicao,gravidade):
        img_path = os.path.join(base_dir, 'assets', 'img', 'buraco_minhoca.png')
        self.imagem = pygame.image.load(img_path)
        self.tamanho = tamanho 
        self.posicao =posicao
        self.gravidade = gravidade

    def calcula_atracao(self, posicao_jogador):
        # Calcular vetor de distância
        d_vec = self.posicao[0] - posicao_jogador
        d = np.linalg.norm(d_vec)

        # Calcular aceleração gravitacional
        if d > 0:
            a = (self.gravidade / d**2) * (d_vec / d)
        else:
            a = np.array([0, 0])

        return a
    def desenha(self,window):
        for i in range(len(self.posicao)):
            buraco = pygame.transform.scale(self.imagem, self.tamanho) # Redefinir dimensão da imagem
            window.blit(buraco, self.posicao[i]-30) # Desenha a imagem já carregada por pygame.image.load em window na posição (x, y).

class Torre:
    def __init__(self,tamanho,posicao):
        img_path = os.path.join(base_dir, 'assets', 'img', 'torre.png')
        self.imagem = pygame.image.load(img_path)
        self.tamanho = tamanho 
        self.posicao =posicao

    def desenha(self,window):
        torre = pygame.transform.scale(self.imagem, self.tamanho) # Redefinir dimensão da imagem
        window.blit(torre, self.posicao) # Desenha a imagem já carregada por pygame.image.load em window na posição (x, y).


class Canhao:
    def __init__(self,tamanho,posicao):
        img_path = os.path.join(base_dir, 'assets', 'img', 'canhao.png')
        self.imagem = pygame.image.load(img_path)
        self.imagem = pygame.transform.flip(self.imagem, True, False)
        self.tamanho_imagem= tamanho
        self.posicao = posicao

    def desenha(self, window):
        canhao = pygame.transform.scale(self.imagem, self.tamanho_imagem) # Redefinir dimensão da imagem
        window.blit(canhao, self.posicao) # Desenha a imagem já carregada por pygame.image.load em window na posição (x, y).


        

class Atrator:
    def __init__(self, posição, raio, gravidade, tamanho):
        img_path = os.path.join(base_dir, 'assets', 'img', 'planeta1.png')
        self.imagem_atrator = pygame.image.load(img_path)
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

class Bolinha:
    def __init__(self,s0,v0,posicao_torre,tamanho):
        img_path = os.path.join(base_dir, 'assets', 'img', 'bola_canhao.png')
        self.imagem = pygame.image.load(img_path)
        self.s0 = np.array(s0)
        self.v0 = np.array(v0)
        self.torre=np.array(posicao_torre)
        self.tamanho=tamanho
        self.posicoes = self.s0
        self.velocidade = self.v0

    
    def atualiza_estado(self,aceleracao,atrator,buraco,reiniciou):
            if reiniciou:
                self.velocidade = pygame.mouse.get_pos() - self.s0
            if buraco[0][0]-20 <= self.posicoes[0] <= buraco[0][0] + 40 and buraco[0][1]-20 <= self.posicoes[1] <= buraco[0][1] + 40:
                self.posicoes = buraco[1] 
                
            elif self.posicoes[0]<10 or self.posicoes[0]>540 or self.posicoes[1]<10 or self.posicoes[1]>590 or ((self.posicoes[0]>=atrator[0]-20 and self.posicoes[0]<=atrator[0]+20) and (self.posicoes[1]>=atrator[1]-10 and self.posicoes[1]<=atrator[1]+10)): # Se eu chegar ao limite da tela, reinicio a posição do personagem
                self.posicoes= self.s0
                return False
            else:
                self.velocidade = self.velocidade + aceleracao
                self.velocidade = self.velocidade * 10 / np.linalg.norm(self.velocidade)
                self.posicoes = self.posicoes + self.velocidade * 0.25
            return True
    def desenha(self,window):
        bolinha = pygame.transform.scale(self.imagem, self.tamanho) # Redefinir dimensão da imagem
        window.blit(bolinha, self.posicoes) # Desenha a imagem já carregada por pygame.image.load em window na posição (x, y).


class TelaInicial:
    def __init__(self, largura_jogo, altura_jogo, fonte_padrao, FPS):
        self.largura_jogo = largura_jogo
        self.altura_jogo = altura_jogo
        self.font_texto = pygame.font.Font(fonte_padrao, 18)
        self.font_cabecalho =  pygame.font.Font(fonte_padrao, 55)
        img_path = os.path.join(base_dir, 'assets', 'img', 'starfield.png')
        self.image_fundo = pygame.image.load(img_path) # Carrega uma imagem
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

        cabeçalho = self.font_cabecalho.render(f'Spacial Collapse', True, (0, 0, 0)) # Cria uma imagem do texto
        window.blit(cabeçalho, (50, 220)) # Desenha a imagem já carregada por pygame.image.load em window na posição (x, y).

        texto_inicio = self.font_texto.render(f'CLIQUE "ENTER" PARA INICIAR O JOGO', True, (255, 255, 255)) # Cria uma imagem do texto
        window.blit(texto_inicio, (100, 295)) # Desenha a imagem já carregada por pygame.image.load em window na posição (x, y).

        pygame.display.update()


class telaJogo:
    def __init__(self, largura_jogo, altura_jogo, fonte_padrao, FPS):
        self.largura_jogo = largura_jogo
        self.altura_jogo = altura_jogo
        self.font_texto = pygame.font.Font(fonte_padrao, 18)
        img_path = os.path.join(base_dir, 'assets', 'img', 'starfield.png')
        self.image_fundo = pygame.image.load(img_path) # Carrega uma imagem
        self.tamanho_fundo = np.array([largura_jogo, altura_jogo])
        self.fps = FPS
        self.clock = pygame.time.Clock()
        self.s0 = np.array([88, self.altura_jogo - 80])
        self.v0 = pygame.mouse.get_pos() - self.s0
        self.tamanho_bola = np.array([35, 35])
        self.tamanho_torre = np.array([100, 100])
        self.posicao_torre = np.array([430, 50])
        self.tamanho_canhao = np.array([80, 80])
        self.posicao_canhao = np.array([8, self.altura_jogo - self.tamanho_canhao[1]])
        self.tamanho_atrator = np.array([80, 80])
        self.posicao_atrator = np.array([350, 200])
        self.tamanho_buraco = np.array([80, 80])
        self.posicao_buraco = [np.array([100, 100]),np.array([450, 450])]
        self.raio_atrator = 40
        self.gravidade_atrator = 500
        self.gravidade_buraco = 1000
        self.bolinha = Bolinha(self.s0, self.v0, self.posicao_torre, self.tamanho_bola)
        self.torre = Torre(self.tamanho_torre, self.posicao_torre)
        self.canhao = Canhao(self.tamanho_canhao, self.posicao_canhao)
        self.atrator = Atrator(self.posicao_atrator, self.raio_atrator, self.gravidade_atrator, self.tamanho_atrator)
        self.atirou = False
        self.buraco = Buraco(self.tamanho_buraco,self.posicao_buraco,self.gravidade_buraco)
        self.reiniciou = False

    def atualiza_estado(self):
        for event in pygame.event.get(): # Retorna uma lista com todos os eventos que ocorreram desde a última vez que essa função foi chamada
            self.reiniciou = False
            if event.type == pygame.QUIT: 
                return -1                                                                                                                                                                                       
                        
            if event.type ==pygame.MOUSEBUTTONDOWN:
                self.atirou = True
                self.reiniciou = True 
        
        if self.posicao_torre[0] <= self.bolinha.posicoes[0] <= self.posicao_torre[0] + self.tamanho_torre[0] - 10 and self.posicao_torre[1] <= self.bolinha.posicoes[1] <= self.posicao_torre[1] + self.tamanho_torre[1]:
                return 2

        a1 = self.atrator.calcula_atracao(self.bolinha.posicoes)
        a2 = self.buraco.calcula_atracao(self.bolinha.posicoes)
        v = a1+a2
        if self.atirou:
            if not self.bolinha.atualiza_estado(v,self.posicao_atrator,self.posicao_buraco,self.reiniciou):
                self.atirou = False
        self.clock.tick(self.fps)


        return 1


    def desenha(self, window):
        window.fill((0, 0, 0))

        fundo = pygame.transform.scale(self.image_fundo, self.tamanho_fundo) # Redefinir dimensão da imagem
        window.blit(fundo, (0, 0)) # Desenha a imagem já carregada por pygame.image.load em window na posição (x, y).
        if self.atirou:
            self.bolinha.desenha(window)

        self.torre.desenha(window)

        self.atrator.desenha(window)

        self.canhao.desenha(window)
        self.buraco.desenha(window)

        pygame.display.update()


class TelaFinal:
    def __init__(self, largura_jogo, altura_jogo, fonte_padrao, FPS):
        self.largura_jogo = largura_jogo
        self.altura_jogo = altura_jogo
        self.font_texto = pygame.font.Font(fonte_padrao, 18)
        self.font_cabecalho =  pygame.font.Font(fonte_padrao, 55)
        img_path = os.path.join(base_dir, 'assets', 'img', 'starfield.png')
        self.image_fundo = pygame.image.load(img_path) # Carrega uma imagem
        self.tamanho_fundo = np.array([largura_jogo, altura_jogo])
        self.fps = FPS
        self.clock = pygame.time.Clock()
    

    def atualiza_estado(self):
        for event in pygame.event.get(): # Retorna uma lista com todos os eventos que ocorreram desde a última vez que essa função foi chamada
            if event.type == pygame.QUIT: 
                return -1

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return -1
        
        self.clock.tick(self.fps)
        
        return 2
        

    def desenha(self, window):
        window.fill((0, 0, 0))

        fundo = pygame.transform.scale(self.image_fundo, self.tamanho_fundo) # Redefinir dimensão da imagem
        window.blit(fundo, (0, 0)) # Desenha a imagem já carregada por pygame.image.load em window na posição (x, y).

        cabeçalho = self.font_cabecalho.render(f'Parabéns', True, (255, 255, 0)) # Cria uma imagem do texto
        window.blit(cabeçalho, (150, 220)) # Desenha a imagem já carregada por pygame.image.load em window na posição (x, y).

        texto_inicio = self.font_texto.render(f'CLIQUE "ENTER" PARA FECHAR O JOGO', True, (255, 255, 255)) # Cria uma imagem do texto
        window.blit(texto_inicio, (100, 295)) # Desenha a imagem já carregada por pygame.image.load em window na posição (x, y).

        pygame.display.update()


class Jogo:
    def __init__(self):
        pygame.init()
        self.largura_jogo = 550
        self.altura_jogo = 600
        self.fonte_padrao = pygame.font.get_default_font() # Carrega a fonte padrão
        self.window = pygame.display.set_mode((self.largura_jogo, self.altura_jogo))
        self.fps = 60
        self.indice_tela_atual = 0
        self.telas = [TelaInicial(self.largura_jogo, self.altura_jogo, self.fonte_padrao, self.fps), telaJogo(self.largura_jogo, self.altura_jogo, self.fonte_padrao, self.fps), TelaFinal(self.largura_jogo, self.altura_jogo, self.fonte_padrao, self.fps)]

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
                
