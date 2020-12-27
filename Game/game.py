''' game.py - основной исполняемый файл, в котором запускается игровой процесс. '''


def play():
    i = 1
    score = 0
    # name = input('Введите Ваше имя: ')
    from models import Player
    from exceptions import EnemyDown
    while True:
        try:
            Player.attack()
            Player.defence()
        except EnemyDown:
            score += 5
            Player.lives_enemy = 2


if __name__ == '__main__':
    try:
        play()
        from exceptions import GameOver
    except GameOver:
        print('game.py GameOver!')
    finally:
        print('Good bye!')
        # KeyboardInterrupt pass
