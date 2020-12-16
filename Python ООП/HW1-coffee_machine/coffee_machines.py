''' Кофе машину, кофе машину которая умеет работать с молоком (латте, капучино),
 и кофемашину, которая умеет рабоатть с молоком и коньяком :)'''


class CoffeeMachine:  # умеет работать с Американо и Эспрессо
    water = 100  # все показатели в процентах
    corn = 100  # зёрна кофе
    __now_trash = 5  # мусор
    __max_trash = 90

    def clean(self):  # самоочистка машины от мусора, если мусора больше 70 %
        if self.__now_trash >= 70:
            self.__now_trash = 0
            print('----- \n Trash in machine is full. We clean... \n Done! Trash is clear! \n -----')

    def americano(self):
        if self.water < 20:
            print('!!!!! water < 20, pour water pls!\n')
        elif self.corn < 20:
            print('!!!!! corn < 20, pour coffee corn pls!\n')
        else:
            print('( -20 water , -20 corn , +10 trash )\n*** AMERICANO is done! ***\n')
            self.water -= 20
            self.corn -= 20
            self.__now_trash += 10
        self.clean()  # проверка на мусор после приготовления

    def espresso(self):
        if self.water < 10:
            print('!!!!! water < 10, pour water pls!\n')
        elif self.corn < 20:
            print('!!!!! corn < 20, pour coffee corn pls!\n')
        else:
            print('( -10 water , -20 corn , +10 trash ) \n *** ESPRESSO is done! ***\n')
            self.water -= 10
            self.corn -= 20
            self.__now_trash += 10
        self.clean()

    def add_water(self):  # сама машина воды и кофе не добавит
        self.water = 100
        print('--- You added water! Water = 100% ---\n')

    def add_corn(self):
        self.corn = 100
        print('--- You added corn! Corn = 100% ---\n')


class CoffeeMachineMilk(CoffeeMachine):  # умеет работать ещё с Капучино и Латте
    milk = 100
    __now_trash_cmm = 10
    __max_trash_cmm = 90

    def clean_cmm(self):  # разные машины, разный мусор
        if self.__now_trash_cmm >= 70:
            self.__now_trash_cmm = 0
            print('----- \n Trash in machine is full. We clean... \n Done! Trash is clear! \n -----')

    def cappuccino(self):
        if self.water < 20:
            print('!!!!! water < 20, pour water pls!\n')
        elif self.corn < 10:
            print('!!!!! corn < 10, pour coffee corn pls!\n')
        elif self.milk < 20:
            print('!!!!! milk < 20, pour milk pls!\n')
        else:
            print('( -20 water , -10 corn , -20 milk , +10 trash ) \n *** CAPPUCCINO is done! ***\n')
            self.water -= 20
            self.corn -= 10
            self.milk -= 20
            self.__now_trash_cmm += 10
        self.clean_cmm()

    def latte(self):
        if self.water < 20:
            print('!!!!! water < 20, pour water pls!\n')
        elif self.corn < 10:
            print('!!!!! corn < 10, pour coffee corn pls!\n')
        elif self.milk < 20:
            print('!!!!! milk < 20, pour milk pls!\n')
        else:
            print('( -20 water , -10 corn , -20 milk , +10 trash ) \n *** LATTE is done! ***\n')
            self.water -= 20
            self.corn -= 10
            self.milk -= 20
            self.__now_trash_cmm += 10
        self.clean_cmm()

    def add_milk(self):
        self.milk = 100
        print('--- You added milk! Milk = 100% ---\n ')


class CoffeeMachineCognac(CoffeeMachineMilk):  # умеет работать и с коньком
    cognac = 100
    __now_trash_cmc = 15
    __max_trash_cmc = 90

    def clean_cmc(self):  # разные машины, разный мусор
        if self.__now_trash_cmc >= 70:
            self.__now_trash_cmc = 0
            print('----- \n Trash in machine is full. We clean... \n Done! Trash is clear! \n -----')

    def coffee_with_cognac(self):
        if self.water < 20:
            print('!!!!! water < 20, pour water pls!\n')
        elif self.corn < 10:
            print('!!!!!corn < 10, pour coffee corn pls!\n')
        elif self.cognac < 10:
            print('!!!!!cognac < 10, pour cognac pls!\n')
        else:
            print('( -20 water , -10 corn , -10 cognac , +10 trash ) \n *** COFFEE WITH COGNAC is done! ***\n')
            self.water -= 20
            self.corn -= 10
            self.cognac -= 10
            self.__now_trash_cmc += 10
        self.clean_cmc()

    def add_cognac(self):
        self.cognac = 100
        print('--- You added cognac! Cognac = 100% ---\n')


def user_input():  # кнопочки для управления машинами
    user = input('What do you want to do? (Type number) \
    \n 0 - turn off coffee machines \n 1 - americano \n 2 - espresso \n 3 - cappuccino \n 4 - latte\
     \n 5 - coffee with cognac \n ADD: 6 - water , 7 - corn , 8 - milk , 9 - cognac \n')
    if user == '0':
        print('Coffee machines are off.')
    elif user == '1':
        cm.americano()
        user_input()
    elif user == '2':
        cm.espresso()
        user_input()
    elif user == '3':
        cmm.cappuccino()
        user_input()
    elif user == '4':
        cmm.latte()
        user_input()
    elif user == '5':
        cmc.coffee_with_cognac()
        user_input()
    elif user == '6':
        cm.add_water()   # можно сделать, чтобы добавляло только в ту машину, где ->
        cmm.add_water()  # -> закончилось, но так долго, по этому сразу во все
        cmc.add_water()
        user_input()
    elif user == '7':
        cm.add_corn()
        cmm.add_corn()
        cmc.add_corn()
        user_input()
    elif user == '8':
        cmm.add_milk()
        cmc.add_milk()
        user_input()
    elif user == '9':
        cmc.add_cognac()
        user_input()
    else:
        print('Wrong button! Try again!')
        user_input()


cm = CoffeeMachine()
cmm = CoffeeMachineMilk()
cmc = CoffeeMachineCognac()
user_input()
