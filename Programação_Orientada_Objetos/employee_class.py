from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name

    def set_first_name(self, new_name):
        self.first_name = new_name

    def set_last_name(self, new_name):
        self.last_name = new_name

    @abstractmethod
    def compute_salary(self):
        pass
    def full_name(self):
        full_name = self.first_name + " " + self.last_name
        return full_name
    
class FullTime(Employee):
    def __init__(self, first_name, last_name, base_salary=2000, bonus=100):
        super().__init__(first_name, last_name)
        self.base_salary = base_salary
        self.bonus = bonus

    def get_base_salary(self):
        return self.base_salary
    
    def get_bonus(self):
        return self.bonus
    
    def set_base_salary(self, new_base_salary):
        if float(new_base_salary) < 0:
            print('Erro! Salário não pode ser menor que 0.')
        else:
            self.base_salary = new_base_salary

    def set_bonus(self, new_bonus):
        self.bonus = new_bonus

    def compute_salary(self):
        return self.base_salary + self.bonus
    
class Hourly(Employee):
    def __init__(self, first_name, last_name, time, salaryhour=20):
        super().__init__(first_name, last_name)
        self.time = time
        self.salaryhour = salaryhour

    def get_time(self):
        return self.time
    
    def get_salaryhour(self):
        return self.salaryhour
    
    def set_time(self, new_time):
        self.time = new_time

    def set_salaryhour(self, new_salaryhour):
        if float(new_salaryhour) < 0:
            print('Erro! Salário não pode ser menor que 0.')
        else:
            self.salaryhour = new_salaryhour

    def compute_salary(self):
        return self.salaryhour * self.time