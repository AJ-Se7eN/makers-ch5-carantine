"""Implement Students room using OOP:
Steve = Student("Steven Schultz", 23, "English")
Johnny = Student("Jonathan Rosenberg", 24, "Biology")
Penny = Student("Penelope Meramveliotakis", 21, "Physics")
print(Steve)
<name: Steven Schultz, age: 23, major: English>
print(Johnny)
<name: Jonathan Rosenberg, age: 24, major: Biology>
"""
class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def __str__(self):
        return (f'<name:{self.name}, age:{self.age}, major:{self.major}>')




Steve = Student("Steven Schultz", 23, "English")
Johnny = Student("Jonathan Rosenberg", 24, "Biology")
Penny = Student("Penelope Meramveliotakis", 21, "Physics")

print(Steve)
# <name: Steven Schultz, age: 23, major: English>