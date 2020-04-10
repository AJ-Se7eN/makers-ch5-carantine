"""Создайте класс Student, конструктор которого имеет параметры name, lastname,
department, year_of_entrance. Добавьте метод get_student_info, который
возвращает имя, фамилию, год поступления и факультет в
отформатированном виде: “Вася Иванов поступил в 2017 г. на факультет:
Программирование.”"""

class student:
    def __init__(self, name, lastname, departament, year_of_entarance):
        self.name = name 
        self.lastname = lastname
        self.departament = departament
        self.year_of_entarance = year_of_entarance
    def get_student_info(self):
        print(self.name,self.lastname,"поступил в", self.year_of_entarance + "г. на факультет:", self.departament)


student1=student("Вася", "Иванов", "Программирование", "2017")
student1.get_student_info()
student2=student("sergey", "Иванов", "Программирование", "2017").get_student_info()
