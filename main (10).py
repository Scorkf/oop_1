# Принцип ООП Полиморфзим (поли - много, морфизм - образ) - одноименные методы в разных классах 
# (метод с одним именем может выполнять разные функции в классах)

class Car:
    def move(self):
        print('Едет по дороге')

class Moto:
    def move(self):
        print('Едет по дороге')

class Train:
    def move(self):
        print('Едет по железной дороге')

class Boat:
    def move(self):
        print('Идет по воде')


lada = Car()
voshod = Moto()
lastochka = Train()
salut = Boat()

print(lada.move())
print(voshod.move())
print(lastochka.move())
print(salut.move())