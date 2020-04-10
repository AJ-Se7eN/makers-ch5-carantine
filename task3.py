"""Создайте класс Car. Пропишите в конструкторе параметры make, model, year,
odometer, fuel. Пусть у показателя odometer будет первоначальное значение 0,
а у fuel 70. Добавьте метод drive, который будет принимать расстояние в км. В
самом начале проверьте, хватит ли вам бензина из расчета того, что машина
расходует 10 л / 100 км (1л - 10 км) . Если его хватит на введенное расстояние,
то пусть этот метод добавляет эти километры к значению одометра, но не
напрямую, а с помощью приватного метода __add_distance. Помимо этого
пусть метод drive также отнимет потраченное количество бензина с помощью
приватного метода __subtract_fuel, затем пусть распечатает на экран “Let’s
drive!”. Если же бензина не хватит, то распечатайте “Need more fuel, please, fill
more!”"""

class Car:
    def __init__(self, make, model, year,):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.fuel= 70

    def drive(self,way):
        all_way=self.fuel*10
        if all_way<way:
            print("Need more fuel, please, fill more!")
        else:
            self.__add_distance(way)
            self.__subtract_fuel(way)
            print("Let’s drive!")
            
    def __add_distance(self,way):
            self.odometer += way
    def __subtract_fuel(self,way):
            self.fuel -= way/10


Car1=Car('mers', 's-class', '2020').drive(7001)
Car1=Car('BMW', 'X5', '2007').drive(71)