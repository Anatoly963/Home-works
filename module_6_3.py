
import random

class Animal:
    live = True
    sound = None            #- звук(изначально отсутствует)
    _DEGREE_OF_DANGER = 0   #- степень опасности существа
    _cords = [0, 0, 0]
    speed = None

    def __init__(self, speed):
        self.speed = speed
        #print(speed)

    def move(self, dx, dy, dz):
        self.dx = dx * self.speed
        self.dy = dy * self.speed
        self.dz = dz * self.speed
        self._cords[0] = self.dx
        self._cords[1] = self.dy
        self._cords[2] = self.dz
        #print(self._cords)

    def get_cords(self):
        print(f"X:{self.dx} Y:{self.dy} Z:{self.dz}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(f'{self.sound}')      #  выводит строку со звуком sound.

class Bird(Animal):         # - класс описывающий птиц
    beak = True     #- наличие клюва
    sound = None    #- звук(изначально отсутствует)

    def lay_eggs(self):
        self.eggs = random.randint(1,4)
        print(f"Here are(is) {self.eggs} eggs for you")




class AquaticAnimal(Animal):      # - класс описывающий плавающего животного.
    _DEGREE_OF_DANGER = 3         # - степень опасности существа

    def dive_in(self, dz):        # dz изменение координаты z в _cords
        self._cords[2] -= abs(dz*self.speed//2)
        if self._cords[2] < 0:
            print("It's too deep, i can't dive :(")
            self._cords[2] += abs(dz * self.speed // 2)
        else:
            self.dz = self._cords[2]
        return self._cords


class PoisonousAnimal(Animal):     # - класс описывающий ядовитых животных.
    _DEGREE_OF_DANGER = 8          # - степень опасности существа


class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):   # - класс описывающий утконоса. Наследуется от классов
    sound = "Click-click-click"                         # - звук, который издаёт утконос


# Пример работы программы:
db = Duckbill(10)
#
print(db.live)
print(db.beak)
#
db.speak()
db.attack()
#
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
#
db.lay_eggs()


# Вывод на консоль:
# True
# True
# Click-click-click
# Be careful, i'm attacking you 0_0
# X: 10 Y: 20 Z: 30
# X: 10 Y: 20 Z: 0
# Here are(is) 3 eggs for you           # Число может быть другим (1-4)