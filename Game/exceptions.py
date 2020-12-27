''' exceptions.py должен содержать кастомные исключения созданные для контроля
игрового процесса и необходимый для них функционал. '''


class GameOver(Exception):
    ''' сохранение счета по завершению игры в scores.txt '''
    def __init__(self, text):
        self.txt = text


class EnemyDown(Exception):
    ''' 10 лучших счетов игроков. Можно реализовать через класс Score '''
    def __init__(self, text):
        self.txt = text


