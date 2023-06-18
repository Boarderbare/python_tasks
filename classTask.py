# Вы приехали помогать на ферму Дядюшки Джо и видите вокруг себя множество разных животных:
# гусей "Серый" и "Белый", корову "Маньку", овец "Барашек" и "Кудрявый", кур "Ко-Ко" и "Кукареку"
# коз "Рога" и "Копыта", и утку "Кряква"
# ​Со всеми животными вам необходимо как-то взаимодействовать:
# кормить, корову и коз доить, овец стричь, собирать яйца у кур, утки и гусей
# различать по голосам(коровы мычат, утки крякают и т.д.)​
# Задание 1:
# Нужно реализовать классы животных и определить методы взаимодействия с животными.
# ​Для каждого животного из списка должен существовать экземпляр класса.
# Каждое животное требуется накормить и подоить/постричь/собрать яйца, если надо.​
# Задание 2:
# У каждого животного должно быть определено имя(self.name) и вес(self.weight).
# Необходимо посчитать общий вес всех животных(экземпляров класса);
# Вывести название самого тяжелого животного.

milk = 0
wool = 0

class Ferma:
    def __init__(self, name, sound, weight=1, food=1):
        self.name = name
        self.sound = sound
        self.weight = weight
        self.food=food

    def feed(self):
        self.food += 1

class Gooses(Ferma):
    def __init__(self, name, weight=1, food=0, sound="Ga-ga", eggs=0):
        Ferma.__init__(self, name,  sound, weight, food )
        self.eggs=eggs
        
    def collect_eggs(self):
        self.eggs -= 1

class Cows:
    def __init__(self, name, weight, food, milk, sound="Mu-u"):
        Ferma.__init__(self, name, weight, food)
        self.sound = sound
        self.milk = milk

    def milk(self):
        self.milk -= 10

class Sheeps:
    def __init__(self, name, weight, food, sound="Bhe-he"):
        Ferma.__init__(self, name, weight, food)
        self.sound = sound
        self,

    def cuts(self):
        self.wool -= 100

class Chicken:
    def __init__(self, name, weight=1, food=0, sound="Kho-ko"):
        self.name = name
        self.weight = weight
        self.food = food
        self.sound = sound

    def feed(self):
        self.food += 1

    def collect_eggs(self):
        self.eggs -= 1

class Goats:
    def __init__(self, name, weight=1, food=0, sound="Mhe-he"):
        self.name = name
        self.weight = weight
        self.food = food
        self.sound = sound

    def feed(self):
        self.food += 1

    def milk(self):
        self.milk -= 10

class Ducks:
    def __init__(self, name, weight=1, food=0, sound="Krya-krya"):
        self.name = name
        self.weight = weight
        self.food = food
        self.sound = sound

    def feed(self):
        self.food += 1

    def collect_eggs(self):
        self.eggs -= 1


goose1 = Gooses("Gray")
# goose2 = Gooses("White")
# sheep1 = Sheeps("Lamb_baby")
# sheep2 = Sheeps("Curly")
# cows1 = Cows("Maniaka")
# chick1 = Chicken("Ko-ko")
# chick2 = Chicken("Kukareku")
# goat1 = Goats("Horns")
# goat2 = Goats("Hoofs")
# duck1 = Ducks("Kryakva")

goose1.feed()
goose1.feed()

print(goose1.food)

print(goose1.name)
