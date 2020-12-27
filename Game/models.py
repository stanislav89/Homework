''' models.py должен содержать классы игрока и противника. '''
import random


class Enemy:
    level_enemy = 1
    lives_enemy = 1

    @staticmethod
    def select_attack():
        return random.randint(1, 3)

    def decrease_lives_enemy(self):
        self.lives_enemy -= 1
        print(self.lives_enemy)
        if self.lives_enemy == 0:
            from exceptions import EnemyDown
            raise EnemyDown('EnemyDown!')


class Player(Enemy):
    lives_player = 3
    allowed_attacks = 1

    @staticmethod
    def fight(attack, defence):
        if attack == defence:
            return 0
        elif (attack == 1 and defence == 2) or (attack == 2 and defence == 3) or (attack == 3 and defence == 1):
            return 1
        else:
            return -1

    def decrease_lives_player(self):
        self.lives_player -= 1
        print(self.lives_player)
        if self.lives_player == 0:
            from exceptions import GameOver
            raise GameOver('GameOver!')

    def attack(self):
        attack = int(input('Вы атакуете! Нажмите, чтобы выбрать: 1 - волшебника, 2 - воина, 3 - разбойника\n '))
        defence = Enemy.select_attack()
        result = Player.fight(attack, defence)
        if result == 0:
            print('Its a draw! Ничья!')
        elif result == 1:
            print('Your attacked successfully! Успешно!')
            Player.decrease_lives_enemy(self)
        else:
            print('You missed! Промах!')

    def defence(self):
        attack = Enemy.select_attack()
        defence = int(input('Вы защищаетесь! Нажмите, чтобы выбрать: 1 - волшебника, 2 - воина, 3 - разбойника\n'))
        result = Player.fight(attack, defence)
        if result == 0:
            print('Its a draw! Ничья!')
        elif result == 1:
            print('You missed! Промах!')
            Player.decrease_lives_player(self)
        else:
            print('Your defence successfully! Успешно!')
