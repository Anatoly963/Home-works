
class Vehicle:  # Любой транспорт
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.get_model = __model
        self.get_horsepower = __engine_power
        self.get_color = __color

    def get_model(self):
        return self.get_model()

    def get_horsepower(self):
        return self.get__engine_power

    def set_color(self, __color):
        if __color.lower() in self.__COLOR_VARIANTS:
            self.get_color = __color
            return
        else:
            print(f'Нельзя сменить цвет на {__color}')
            print()
            return

    def get_color(self):
        return self.__color

    def print_info(self):
        print(f'Модель: {self.get_model}')
        print(f'Мощность двигателя: {self.get_horsepower}')
        print(f'Цвет: {self.get_color}')
        print(f'Владелец: {self.owner}')

class Sedan(Vehicle):  # автомобили класса Седан
    __PASSENGERS_LIMIT = 5

    def print_pas_lim(self):
        print()
        print(f'Вместимость пассажиров {self.__PASSENGERS_LIMIT}')



__COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']  # Текущие цвета
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

vehicle1.print_pas_lim()