# 1.  Спробуйте переписати наступний код через map. Він приймає список реальних імен і замінює їх прізвищами, використовуючи  більш надійний метод.

# names = ['Sam', 'Don', 'Daniel'] 
# for i in range(len(names)): 
#     names[i] = hash(names[i]) 
# print(names) 



# names = ['Sam', 'Don', 'Daniel'] 
# result=map(lambda x: hash(x), names)

# print(list(result))


# 2.  Вивести список кольору “red”, 
# який найчастіше зустрічається в даному списку  
# [“red”, “green”, “black”, “red”, “brown”, “red”, “blue”, “red”, “red”, “yellow” ] використовуючи функцію filter.



# colors=["red", "green", "black", "red", "brown", "red", "blue", "red", "red", "yellow"]
# def is_red(str):
#     return str=="red"

# print(list(filter(is_red, colors)))


# 3. Всі ці числа в списку мають стрічковий тип даних, наприклад  [‘1’,’2’,’3’,’4’,’5’,’7’], перетворити цей список  в список, всі числа якого мають тип даних integer:
# 1)  використовуючи метод  append
# 2)  використовуючи метод  map

# nums=['1','2','3','4','5','7']

# res=map(int, nums)
# print(list(res))


# 4. Перетворити список, який містить милі ,  в список, який містить кілометри (1 миля=1.6 кілометра)
#    a) використовуючи функцію map
#   b) використовуючи функцію map та lambda

# miles=[1, 2, 3, 4]
# print(list(map(lambda m: round(m*1.6, 2), miles)))

# 5.  Знайти найбільший елемент в списку  використовуючи функцію reduce

# nums=[11, 5, 8, 2]
