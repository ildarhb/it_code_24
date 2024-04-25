class Employee:
    def get_paid(self):
        pass

class Manager(Employee):
    def get_paid(self):
        print(f'ЗП 60000')

class Worker(Employee):
    def get_paid(self):
        print(f'ЗП 40000')

worker = Worker()
worker.get_paid()