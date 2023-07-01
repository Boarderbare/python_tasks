import os

class Ferma:
    ferma = []

    def __init__(self, name, sound, weight):
        self.name = name
        self.sound = sound
        self.weight = weight
        Ferma.ferma.append(self)

    def info(self):
        print(f"{self.name}: weight= {self.weight},", end=" ")

    def get_sound(self,amount):
        self.sound +=" " 
        print(f"{self.name} - {self.sound*amount}")

    def get_eggs(self):
        egg = 1
        self.eggs -= egg
        print(f"get egg {egg} {self.name}: eggs= {self.eggs}")

    def get_milk(self,milk):
        self.milk -= milk
        print(f"get milk {milk} {self.name}: milk= {self.milk}")

class Gooses(Ferma):

    def __init__(self, name, weight=0, sound="Ga-ga", eggs=0):
        Ferma.__init__(self, name, sound, weight)
        self.eggs = eggs

    def info(self):
        Ferma.info(self)
        print(f"eggs= {self.eggs}")


class Cows(Ferma):

    def __init__(self, name, weight=0, milk=0, sound="Mu-u"):
        Ferma.__init__(self, name, sound, weight)
        self.milk = milk

    def info(self):
        Ferma.info(self)
        print(f"milk= {self.milk}")

    def get_milk(self):
        Ferma.get_milk(self,milk =5)



class Sheeps(Ferma):

    def __init__(self, name, weight=0, wool=0, sound="Bhe-he"):
        Ferma.__init__(self, name, sound, weight)
        self.wool = wool

    def get_wool(self):
        wool = 2
        self.wool -= wool
        print(f"get wool {wool} {self.name}: wool= {self.wool}")

    def info(self):
        Ferma.info(self)
        print(f"wool= {self.wool}")


class Chicken(Ferma):

    def __init__(self, name, weight=0, eggs=0, sound="Kho-ko"):
        Ferma.__init__(self, name, sound, weight)
        self.eggs = eggs

    def info(self):
        Ferma.info(self)
        print(f"eggs= {self.eggs}")


class Goats(Ferma):

    def __init__(self, name, weight=0, milk=0, sound="Mhe-he"):
        Ferma.__init__(self, name, sound, weight)
        self.milk = milk

    def get_milk(self):
        Ferma.get_milk(self,milk =1)

    def info(self):
        Ferma.info(self)
        print(f"milk= {self.milk}")


class Ducks(Ferma):
    def __init__(self, name, weight=0, eggs=0, sound="Krya-krya"):
        Ferma.__init__(self, name, sound, weight)
        self.eggs = eggs

    def info(self):
        Ferma.info(self)
        print(f"eggs= {self.eggs}")

def feed(name,amount=1):
    if isinstance(name, Gooses):
        name.weight += 2*amount
        name.eggs += 1*amount
        name.get_sound(amount)
    elif isinstance(name, Cows):
        name.weight += 5
        name.milk += 3
        name.get_sound(amount)
    elif isinstance(name, Sheeps):
        name.weight += 3
        name.wool += 2
        name.get_sound(amount)
    elif isinstance(name, Chicken):
        name.weight += 0.5
        name.eggs += 1
        name.get_sound(amount)
    elif isinstance(name, Goats):
        name.weight += 3
        name.milk += 0.5
        name.get_sound(amount)
    elif isinstance(name, Ducks):
        name.weight += 1
        name.eggs += 0.5
        name.get_sound(amount)

def feed_all():
    for item in Ferma.ferma:
        feed(item)

def info_all():
    for item in Ferma.ferma:
        item.info()

def total_weight():
    sum_weight = 0
    max = 0
    max_name = ""
    for item in Ferma.ferma:
        sum_weight += item.weight
        if item.weight > max:
            max = item.weight
            max_name = item.name
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
print(f"Amount of animals:  {len(Ferma.ferma)}")
feed_all()
feed_all()
feed(cow1,2)
feed(chicken1)
feed(goat1,2)

print('')
info_all()
print('')
chicken1.get_eggs()
chicken1.get_eggs()
goose1.get_eggs()
cow1.get_milk()
sheep1.get_wool()
goat1.get_milk()
duck1.get_eggs()
print('')
total_weight()