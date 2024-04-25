# множественное наследование
class Base1:
    pass

class Base2:
    pass

class MultiDerived(Base1, Base2):
    pass

# миксин
from datetime import date

class MixinExempl:
    def info(self):
        print(f'Я {self.name}, я из города {self.city}')

class Person(MixinExempl):
    def __init__(self, name, city, born_year) -> None:
        self.name = name
        self.city = city
        self.born_year = born_year

    def age(self):
        current_year = date.today().year
        if current_year < self.born_year:
            print('Ошибка')
        else:
            print(current_year - self.born_year)

person = Person('Alex', 'Ufa', 1990)
person.info()
