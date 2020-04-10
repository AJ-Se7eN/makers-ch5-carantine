"""Создайте новый класс Airplane. Создайте следующие характеристики (полей)
объекAта:
● make (марка)
● model
● year
● max_speed
● odometer
● is_flying
и методы имитирующих поведение самолета take off (взлет), fly (летать), land
приземление). Метод take off должен изменить is_flying на True, а land на False. По
умолчанию поле is_flying = False. Метод fly должен принимать расстояние полета и
изменять показания одометра (километраж). Создайте 1 объект класса и используйте
все методы класса."""

class Airaplane :
    def __init__(self, make, model, year, max_speed):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = 0
        self.is_flying = False
    def take_off(self):
        self.is_flying = True
        print("Самолет вылетел!")
    def fly(self,km):
        self.odometer+=km
    def land(self):
        self.is_flying = False
        print("Самолет приземлился!")
Airaplane1=Airaplane("Airbus","a310","1998","860 км/ч")
Airaplane1.take_off()
Airaplane1.fly(368)
Airaplane1.land()










