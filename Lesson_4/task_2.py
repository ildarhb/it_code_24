from datetime import date

class Person:
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
person.age()