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

import os
class Ferma:
    ferma=[]
    def __init__(self, name, sound, weight):
        self.name = name
        self.sound = sound
        self.weight = weight
        Ferma.ferma.append(self)

    def info(self):
       print(f"{self.name}: weight= {self.weight},", end =" ")
       
class Gooses(Ferma):
    def __init__(self, name, weight=0,  sound="Ga-ga", eggs=0):
        Ferma.__init__(self, name,  sound, weight)
        self.eggs=eggs
    
    def get_eggs(self):
        egg=1
        self.eggs -= egg
        print(f"get egg {egg} {self.name}: eggs= {self.eggs}")
    
    def info(self):
        Ferma.info(self)
        print(f"eggs= {self.eggs}")

class Cows:
    def __init__(self, name, weight=0, milk=0, sound="Mu-u"):
        Ferma.__init__(self, name,  sound, weight)
        self.milk = milk

    def get_milk(self):
        milk=5
        self.milk -= milk
        print(f"get milk {milk} {self.name}: milk= {self.milk}")

    def info(self):
        Ferma.info(self)
        print(f"milk= {self.milk}")

class Sheeps:
    def __init__(self, name, weight=0, wool=0, sound="Bhe-he"):
        Ferma.__init__(self, name,  sound, weight)
        self.wool = wool

    def get_wool(self):
        wool=2
        self.wool -= wool
        print(f"get wool {wool} {self.name}: wool= {self.wool}")

    def info(self):
        Ferma.info(self)
        print(f"wool= {self.wool}")

class Chicken:
    def __init__(self, name, weight=0, eggs=0, sound="Kho-ko"):
        Ferma.__init__(self, name,  sound, weight)
        self.eggs=eggs
        
    def get_eggs(self):
        egg=1
        self.eggs -= egg
        print(f"get egg {egg} {self.name}: eggs= {self.eggs}")

    def info(self):
        Ferma.info(self)
        print(f"eggs= {self.eggs}")

class Goats:
    def __init__(self, name, weight=0, milk=0, sound="Mhe-he"):
        Ferma.__init__(self, name,  sound, weight)
        self.milk = milk

    def get_milk(self):
        milk=1
        self.milk -= milk
        print(f"get milk {milk} {self.name}: milk= {self.milk}")

    def info(self):
        Ferma.info(self)
        print(f"milk= {self.milk}")

class Ducks:
    def __init__(self, name, weight=0, eggs=0, sound="Krya-krya"):
        Ferma.__init__(self, name,  sound, weight)
        self.eggs=eggs
        
    def get_eggs(self):
        egg=1
        self.eggs -= egg
        print(f"get egg {egg} {self.name}: eggs= {self.eggs}")

    def info(self):
        Ferma.info(self)
        print(f"eggs= {self.eggs}") 

def feed(name):
    if  isinstance(name, Gooses):
        name.weight +=2
        name.eggs +=1
        print(name.sound)
    elif isinstance(name, Cows):
        name.weight +=5
        name.milk +=3
        print(name.sound)
    elif isinstance(name, Sheeps):
        name.weight +=3
        name.wool +=2
        print(name.sound)
    elif isinstance(name, Chicken):
        name.weight +=0.5
        name.eggs +=1
        print(name.sound)
    elif isinstance(name, Goats):
        name.weight +=3
        name.milk +=0.5
        print(name.sound)
    elif isinstance(name, Ducks):
        name.weight +=1
        name.eggs +=0.5    
        print(name.sound)

def total_weight():
    sum_weight=0
    max=0
    max_name =""
    for item in Ferma.ferma:
        sum_weight +=item.weight
        if item.weight > max:
            max=item.weight
            max_name= item.name
    print(f"Total weight : {sum_weight}")
    print(f"Max weight : {max} - {max_name}")


goose1 = Gooses("Gray")
goose2 = Gooses("White")
sheep1 = Sheeps("Lamb_baby")
sheep2 = Sheeps("Curly")
cow1 = Cows("Manyka")
chicken1 = Chicken("Ko-ko")
chicken2 = Chicken("Kukareku")
goat1 = Goats("Horns")
goat2 = Goats("Hoofs")
duck1 = Ducks("Kryakva")

os.system('cls||clear')
print(len(Ferma.ferma))
feed(cow1)
feed(cow1)
feed(cow1)
feed(cow1)
feed(cow1)
feed(goose1)
feed(sheep1)
feed(sheep1)
feed(chicken1)
feed(chicken1)
feed(chicken1)
feed(goat1)
feed(goat1)
feed(goat1)
feed(goat1)
feed(duck1)
feed(duck1)
print('') 
cow1.info()
goose1.info()
sheep1.info()
chicken1.info()
goat1.info()
duck1.info()
print('') 
chicken1.get_eggs()
chicken1.get_eggs()
cow1.get_milk()
sheep1.get_wool()
goat1.get_milk()
duck1.get_eggs()
print('') 
total_weight()