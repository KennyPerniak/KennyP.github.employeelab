import time
import os
import employ
print("Programmer:" + os.getlogin())
print(time.strftime("Lab 19.2 %B %m,%Y @ %H:%M:%S\n"))


user = input("Enter your name: ")
name = input("Enter the employee's name: ")
number = eval(input("Enter the ID number: "))
shift = eval(input("Enter the shift number: "))
rate = eval(input("Enter the hourly pay rate: "))

p = employ.ProductionWorker(name, number, shift, rate)

print(f"{user}, here is the production worker, {p.get_name()}'s information:\n")
print(f"Name: {p.get_name()}")
print(f"ID number: {p.get_number()}")
print(f"Shift: {p.get_shift_number()}")
print(f"Hourly Pay Rate: ${format(p.get_pay_rate(), ',.2f')}")