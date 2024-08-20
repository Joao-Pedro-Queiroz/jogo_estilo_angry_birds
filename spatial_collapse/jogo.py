from Classes import Jogo

def main():
    j = Jogo()
    Jogo.atual = j
    j.game_loop()

if __name__ == '__main__':
    main()