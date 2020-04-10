"""Разработайте программу по следующему описанию.
В некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее
уникальный номер объекта, и свойство, в котором хранится принадлежность команде. У
солдат есть метод "иду за героем", который в качестве аргумента принимает объект типа
"герой". У героев есть метод увеличения собственного уровня.
В основной ветке программы создается по одному герою для каждой команды. В цикле
генерируются объекты-солдаты. Их принадлежность команде определяется случайно.
Солдаты разных команд добавляются в разные списки.
Измеряется длина списков солдат противоборствующих команд и выводится на экран. У
героя, принадлежащего команде с более длинным списком, поднимается уровень.
Отправьте одного из солдат первого героя следовать за ним. Выведите на экран
идентификационные номера этих двух юнитов.
"""

import random

class unit: 
    def __init__(self, n,team):
        self.n=n
        self.team=team
class heroes(unit): 
    def __init__(self,name,n,team,level=0):
        self.name=name
        self.level = level
        self.team=team
    def level_up(self, incr): 
        self.level+=incr
 
class soldier(unit): 
    def follow_heroes(self,heroes):
        print("\n"+"Для охраны своих владений герой {} выбрал опытного воина № {} и отправился с ним в поход.".format(heroes.name, self.n))
Reychel,Molchanov=heroes("Reychel",1,"red"),heroes("Molchanov",2,"green") 
red_team=[] 
green_team=[] 
quantity=int(input("Количество воинов:"))+1 
for i in range(1,quantity): 
    t=random.randint(0,1)
    i=soldier(i,t)
    if i.team==0:
        red_team.append(i)
        i.team="red"
    else:
        green_team.append(i)
        i.team="green"
if len(red_team)>len(green_team): 
    Reychel.level_up(1)
elif len(red_team)<len(green_team):
    Molchanov.level_up(1)
if len(red_team) >= 10:
    Reychel.level_up(len(red_team) // 5)
if len(green_team)>=10:
    Molchanov.level_up(len(green_team)//5)
 
print("В войске героя по имени",Reychel.name+",",str(Reychel.level)+"-го уровня,",len(red_team),"знатных воинов!")
for i in red_team:
    print(i.n, i.team, end=", ")
print("\n"+"В войске героя по имени",Molchanov.name+",",str(Molchanov.level)+"-го уровня,",len(green_team),"знатных воинов!")
for i in green_team:
    print(i.n,i.team, end=", ")

who=random.randint(0,1)
if who==1:
    t=red_team
    h=Reychel
else:
    t=green_team
    h=Molchanov
random.choice(t).follow_heroes(h)

