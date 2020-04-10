"""Soldier Ryan has an AK47
Soldiers can fire ("tigi-tigitishh").
Guns can fire bullets.
Guns can fill bullets - increase the number of bullets(reloads)

Create class Act_of_Shooting, which will inheritates from class Soldier, class Guns.
Where soldier will fire from a gun and reload, and fire one more time."""

import time
class Soldier:
    def __init__(self, name):
        self.name = name
    
class Guns:
    def __init__(self, bullets, magazine):
        self.bullets = bullets
        self.magazine = magazine
    def pih_pah(self):
        for i in range (self.magazine):
            for x in range (self.bullets):
                print("tigi-tigitishh")
                time.sleep(0.3)
            if i != 1:
                print("Перезаряжаюсь!")
                time.sleep(3)
            else:
                print("Патронов нет!")
                
class Act_of_shooting(Soldier, Guns):
    def __init__(self, name, bullets, magazine):
        Soldier.__init__(self, name)
        Guns.__init__(self, bullets, magazine)
        
a=Act_of_shooting("sdf", 2, 2)
a.pih_pah()

