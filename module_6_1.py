
class Animal:

    alive = True   #(живой)
    fed = False     #(накормленный),
    def __init__(self, name):    #name - индивидуальное название каждого животного.
        self.name = name
        print('0', self.name)

    def eat(self, food):
        self.food = food
        if food.edible == True:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Mammal(Animal):
    def __init__(self, name):
        self.name = name

class Predator(Animal):
    def __init__(self, name):
        self.name = name

class Plant:
    edible = False    #(съедобность),
    def __init__(self, name):    # name - индивидуальное название каждого растения
        self.name = name

class Flower(Plant):
    edible = False
    def food(self, name):
        self.name = name

class Fruit(Plant):
    edible = True
    def food(self, name):
        self.name = name


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')

p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
