class Employees:
    def __init__(self, n, num):
        self.__name = n
        self.__number = num

    def set_name(self, n):
        self.__name = n
    def set_number(self, num):
        self.__number = num
    def get_name(self):
        return self.__name
    def get_number(self):
        return self.__number

class ProductionWorker(Employees):
    def __init__(self, n, num, shift_num, pay_r):
        Employees.__init__(self, n, num)
        self.__shift_number = shift_num
        self.__pay_rate = pay_r

    def set_shift_number(self, shift_num):
        self.__shift_number = shift_num
    def set_pay_rate(self, pay_r):
        self.__pay_rate = pay_r
    def get_shift_number(self):
        return self.__shift_number
    def get_pay_rate(self):
        return self.__pay_rate

class ShiftSupervisor(Employees):
    def __init__(self, n, num, sal, b):
        Employees.__init__(self, n, num)
        self.__salary = sal
        self.__bonus = b

    def set_salary(self, sal):
        self.__salary = sal
    def set_bonus(self, b):
        self.__bonus = b
    def get_salary(self):
        return self.__salary
    def get_bonus(self):
        return self.__bonus