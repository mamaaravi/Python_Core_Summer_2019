# 1.  Напишіть програму, яка пропонує користувачу ввести ціле число і визначає чи це число парне чи непарне, чи введені дані коректні.


try:
    num=int(input("Enter number: "))
except ValueError:
    print("You should enter numbers, not letters.")
else:
    if num%2==0:
        print("Number is even")
    else:
        print("Number is odd")



# 2.  Напишіть програму, яка пропонує користувачу ввести свій вік, після чого виводить повідомлення про те чи вік є парним чи непарним числом.
#  Необхідно передбачити можливість введення від’ємного числа,
#  в цьому випадку згенерувати власну виняткову ситуацію. Головний код має викликати функцію, яка обробляє введену інформацію.

def age_check():
    try:
        age=int(input("Enter your age: "))
        if age<0:
            raise Exception()
    except ValueError:
        print("You should enter numbers, not letters.")
    except Exception:
        print("Your age must be >=0 :)")
    else:
        if age%2==0:
            print("Number is even")
        else:
            print("Number is odd")

age_check()


# 3.  Напишіть програму для обчислення частки двох чисел, які вводяться користувачем послідовно через кому, передбачити випадок ділення на нуль,
#  випадки синтаксичних помилок та випадки інших виняткових ситуацій. Використати блоки else та finaly.



str_nums=input("Enter two numbers: ")
str_nums=str_nums.split(',')

try:
    a,b=eval(input("Enter two numbers: "))
    # a=int(str_nums[0])
    # b=int(str_nums[1])
    result=a/b
except ZeroDivisionError:
    print("Division by 0 is not allowed")
except SyntaxError:
    print("Incorrect input")
except NameError:
    print("We can't divide letters, sorry. Please enter two numbers.")
else:
    print("Result: ", result)
finally:
    print("The end!")


# 4.  Написати  програму, яка аналізує введене число та в залежності від числа видає день тижня, який відповідає цьому числу (1 це Понеділок, 2 це Вівторок і т.д.) .
#  Врахувати випадки введення чисел від 8 і більше, а також випадки введення не числових даних.


d={
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}


class CustomError(Exception):
    def __init__(self, info):
        self.info=info
    def __str__(self):
        return repr(self.info)

while True:
    try:
        i=int(input("Enter the day of the week: "))
        # if i>7 or i<1:
        #     raise CustomError("Not allowed number greater than 7 and less than 1!")
    except ValueError:
        print("You didn't enter a number")
    # except CustomError as cust_err:
    #     print(cust_err.info)
    else:
        print(d.get(i, "There is no such day of a week."))