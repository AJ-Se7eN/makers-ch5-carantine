"""Создайте класс ContactList, который должен наследоваться от
встроенного класса list. В нем должен быть реализован метод
search_by_name, который должен принимать имя, и возвращать список
всех совпадений. Замените all_contacts = [ ] на all_contacts =
ContactList(). Создайте несколько контактов, используйте метод
search_by_name."""

class ContactList:
    def __init__(self,names):
        self.names = names
    def search_by_name(self,search):
        for name in self.names:
            if name == search:
                print(name)
all_contacts=ContactList(['Саша','Саша','Саша','Коля','Миша','Саша','Света','Никита','Миша',
                'Валера','Валера','Юля','Юля','Саша','Саша','Саша','Оля','Юля','Саша','Оля','Петя',
                'Петя','Юля','Антон','Антон','Маша','Гоша','Оля','Юля','Гоша','Оля','Юля'])
all_contacts.search_by_name("Антон")