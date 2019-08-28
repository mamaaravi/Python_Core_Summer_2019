# 1.  Створити список цілих чисел, які вводяться з терміналу та визначити серед них максимальне та мінімальне число.

# numbers=[]
# length=int(input("Input length: "))
# # for i in range(length):
# #     num=int(input("Enter number: "))
# #     numbers.append(num)



# numbers=[int(input("Enter number: ")) for i in range(length)]

# print(numbers)
# print(max(numbers))
# print(min(numbers))

# 2.  В інтервалі від 1 до 10 визначити числа 
# •  парні, які діляться на 2,
# •  непарні, які діляться на 3, 
# •  числа, які не діляться на 2 та 3.


# sequence=list(range(11))
# print(sequence)
# print("парні, які діляться на 2:")
# for i in sequence:
#     if sequence[i]%2==0:
#         print(sequence[i])

# print("непарні, які діляться на 3:") 
# for i in sequence:
#     if sequence[i]%3==0 and sequence[i]%2!=0:
#        print(sequence[i])

# print("числа, які не діляться на 2 та 3")
# for i in sequence:
#     if sequence[i]%3!=0 and sequence[i]%2!=0:
#        print(sequence[i])


# 3.  Написати програму, яка обчислює факторіал числа, яке користувач вводить.(не використовувати рекурсивного виклику функції)
# fact=1
# num=int(input("Enter number: "))
# for i in range(num):
#     while num!=1:
#         fact*=num 
#         num=num-1

# print(fact)

# 4.  Напишіть скрипт, який перевіряє логін, який вводить користувач. 
# Якщо логін вірний (First), то привітайте користувача. 
# Якщо ні, то виведіть повідомлення про помилку. 
# (використайте цикл while)

# login="admin"
# user_input=""
# while user_input!=login:
#     user_input=input("Enter login: ")
# print("Hello, admin!")

# 5.  Перший випадок. 
# Написати програму, яка буде зчитувати числа поки не зустріне від’ємне число.
# При появі від’ємного числа програма зупиняється (якщо зустрічається 0 програма теж зупиняється).

# nums=[1]
# while nums.pop()>0:
#     num=int(input("Enter number: "))
#     nums.append(num)

# 6.  Другий випадок. 
# На початку на вхід подається кількість елементів послідовності, а потім самі елементи. 
# При появі від’ємного числа програма зупиняється (якщо зустрічається 0 програма теж зупиняється).

# leng=int(input("Enter length of sequence: "))
# nums=[]
# for i in range(leng):
#     num=int(input("Enter number: "))
#     if num<=0:
#         break
#     nums.append(num)

#  7.  Знайти прості числа від 10 до 30, а всі решта чисел представити у вигляді добутку чисел 
# (наприклад 10 equals 2 * 5

# for number in range(10, 30):
#     if number > 1:
#         for i in range(2, number):
#             if number % i == 0:
#                 print(number, ' equals 2 * {}'.format(number/2))
#                 break
#         else:
#             print(number, 'is a prime number')


#8.  Відсортувати слова в реченні в порядку їх довжини (використати List Comprehensions)

# print(" ".join(sorted(input().split(), key = len)))