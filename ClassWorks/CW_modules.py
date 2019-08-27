
# Напишіть скрипт-гру, яка генерує випадковим чином число з діапазону чисел від 1 до 100 і пропонує
#  користувачу вгадати це число. Програма зчитує числа, які вводить користувач і видає користувачу підказки про те
#   чи загадане число більше чи менше за введене користувачем. Гра має тривати до моменту поки користувач не введе число,
#    яке загадане програмою, тоді друкує повідомлення привітання. 
# (для виконання завдання необхідно імпортувати  модуль random, а з нього функцію randint())



import random as rd

ans=rd.randint(1, 100)
user_input=0
while user_input!=ans:
    user_input=int(input("Guess number from 1 to 100:"))
    if user_input>ans:
        print("Try smaller number")
    elif user_input<ans:
        print("Try larger number")
print("YOU WIN!")


# Напишіть скрипт, який обчислює площу прямокутника a*b, площу трикутника 0.5*h*a, площу кола pi*r**2. 
# (для виконання завдання необхідно імпортувати  модуль math, а з нього функцію pow() та значення змінної пі).
from math import pow, pi

def sq_rectangle(a, b):
    return a*b

def s_triangle(a,h):
    return 0.5*h*a

def s_circle(r):
    return pi*r**2


# Weather 

import pyowm
owm=pyowm.OWM('ef2206ff5da67de63306d0b143e20872')
choice=input("Enter your city: ")
obs=owm.weather_at_place(choice)
w=obs.get_weather()
temp=w.get_temperature('celsius')['temp']
print("Temperature in  "+choice+": " +str(temp)
+ "\nLevel of humidity: "+ str(w.get_humidity()))