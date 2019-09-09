# 1.  Написати функцію, яка знаходить факторіал числа.

def fact(x):
    if x == 1 or x == 0:
        return 1
    else: return x * fact(x - 1)


# 2.  Написати функцію, яка повертає абсолютне значення числа

def absolute(x):    
    print(abs(x))   

absolute(int(input("Enter number: ")))

# 3.  Написати функцію, яка знаходить максимальне число з двох чисел, а також в функції використати рядки документації DocStrings.   


def max_num(*args):
    """ This function calculates the arithmetic mean of a non-empty
        arbitrary number of numerical values """
    return  max(args)
 
print(max_num(45,32,89,78))


# 4.  Написати програму, яка обчислює площу прямокутника, трикутника та кола 
# (написати три функції для обчислення площі, і викликати їх в головній програмі в залежності від вибору користувача)


def sq_rect(l,h):  
    return l*h

def sq_triang(a,h,f=0.5):
    return a*h*f

def sq_circle(r):
    pi=3.14
    return pi*r**2    

# 5.  Написати функцію, яка обчислює суму цифр введеного числа

def func(nums):
    sum=0
    for i in nums:
        sum+=int(i)
    return sum
print(func(input("Enter number: ")))


# 6.  Написати програму калькулятор, яка складається з наступних функцій: 
# головної, яка пропонує вибрати дію та додаткових, які реалізовують вибрані дії, калькулятор працює доти, 
# поки ми не виберемо дію вийти з калькулятора, після виходу, користувач отримує повідомлення з подякою за вибір нашого програмного продукту!!!

def my_calc(action, num1, num2):
    if action == "+":
        print(num1+num2)
    elif action == "-":
        print(num1-num2)
    elif action == "*":
        print(num1*num2) 
    elif action == "/":
        print(num1/num2) 
    else:
        print("Incorrect input")   

choice = input("Дія: ")
a = float(input("num1: "))
b = float(input("num2: "))
my_calc(choice, a, b)


# 8.  Написати програму, яка обчислює дискримінант квадратного рівняння

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = b**2-4*a*c
print(d)