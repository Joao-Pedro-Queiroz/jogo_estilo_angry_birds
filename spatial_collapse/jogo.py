from Classes import Jogo

def main():
    j = Jogo()
    Jogo.atual = j
    j.game_loop()