
class House():

    def __init__(self, name, number_of_floors ):
        self.name=name
        self.number_of_floors=number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print (f'Такого этажа не существует')
        else:
            for i in range(1, new_floor+1):
                print(i)
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f"Название: {self.name}, кол-во этажей: {self.number_of_floors}")

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
hous = House('ЖК Москва',25)

print (h1.name, 'количество этажей: ', h1.number_of_floors)
print (h2.name, 'количество этажей: ', h2.number_of_floors)
print (hous.name, 'количество этажей: ', hous.number_of_floors)
h1.go_to(5)
h2.go_to(10)
hous.go_to(4)

print(h1)
print(h2)
print(hous)
print(len(h1))
print(len(h2))
print(len(hous))