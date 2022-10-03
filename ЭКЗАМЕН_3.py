# 1. Напишите функцию, которая будет принимать номер кредитной карты и
# показывать только последние 4 цифры. Остальные цифры должны заменяться
# звездочками

def card_hide(card):
    return '*' * len(card[:-4]) + card[-4:]
print(card_hide('123455973105678'))

# 2. Напишите функцию, которая проверяет: является ли слово палиндромом

# возвращает обратную строку
def reverse(s):
    return s[::-1]


def is_palindrome(s):
    rev = reverse(s)

#     # проверка на совпадение 2х строк
    if (s == rev):
        return True
    return False


# запуск кода
s = "qweelq"
print(is_palindrome(s))

# Класс Tomato:
# 1. Создайте класс Tomato
# 2. Создайте статическое свойство states, которое будет содержать все стадии
# созревания помидора
# 3. Создайте метод __init__(), внутри которого будут определены два динамических
# protected свойства: 1) _index - передается параметром и 2) _state - принимает первое
# значение из словаря states
# 4. Создайте метод grow(), который будет переводить томат на следующую стадию
# созревания
# 5. Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг
# последней стадии созревания)

class Tomato:

    # Стадии созревания помидора
    states = {0: 'садим рассаду', 1: 'цветение', 2: 'зеленые плоды', 3: 'красные плоды - можно собирать'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    # Метод для переход к следующей стадии созревания
    def grow(self):
        self._change_state()

    # Метод для проверки, зрелости томата
    def is_ripe(self):
        if self._state == 3:
            return True
        return False

    # Защищенные(protected) методы

    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()

    def _print_state(self):
        print(f'Tomato {self._index} is {Tomato.states[self._state]}')

# Класс TomatoBush
# 1. Создайте класс TomatoBush
# 2. Определите метод __init__(), который будет принимать в качестве параметра
# количество томатов и на его основе будет создавать список объектов класса
# Tomato. Данный список будет храниться внутри динамического свойства tomatoes.
# 3. Создайте метод grow_all(), который будет переводить все объекты из списка
# томатов на следующий этап созревания
# 4. Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из
# списка стали спелыми
# 5. Создайте метод give_away_all(), который будет чистить список томатов после
# сбора урожая

class TomatoBush:

    # Создаем список из объектов класса Tomato
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num)]

    # Переводим все томаты из списка на следующий этап созревания
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # Проверяем, все ли помидоры созрели
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    # Собираем урожай
    def give_away_all(self):
        self.tomatoes = []

# Класс Gardener
# 1. Создайте класс Gardener
# 2. Создайте метод __init__(), внутри которого будут определены два динамических
# свойства: 1) name - передается параметром, является публичным и 2) _plant -
# принимает объект класса Tomato, является protected
# 3. Создайте метод work(), который заставляет садовника работать, что позволяет
# растению становиться более зрелым
# 4. Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все -
# садовник собирает урожай. Если нет - метод печатает предупреждение.
# 5. Создайте статический метод knowledge_base(), который выведет в консоль справку
# по садоводству.

class Gardener:

    # Выдаем садовнику растение для ухода
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    # Ухаживаем за растением
    def work(self):
        print('''Фермер проводит агротехнические
мероприятия по выращиванию томатов...''')
        self._plant.grow_all()
        print('Ура, томаты созрели, начинаем уборку')

    # Собираем урожай
    def harvest(self):
        print('''Внимание!!!!! Все на уборку томатов... ''')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Уборка завершина!!!!')
        else:
            print('''Извините, но томаты еще зеленые
и не годятся для приема в пищу,
надо немножко подождать''')

    # Статический метод
    # Выводит справку по садоводству
    @staticmethod
    def knowledge_base():
        print('''ДОЖИНКИ 2022,
КАК ФЕРМЕР - АЛЕКСАНДР
ВЫРАЩИВАЛ ТОМАТЫ!!!!!''')




Gardener.knowledge_base()
tomatoBush = TomatoBush(3)
gardener = Gardener('Александр', tomatoBush)
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
print(tomatoBush.tomatoes)