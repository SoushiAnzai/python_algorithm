# count = 0
# while count < 5:
#     print(count)
#     count += 1
# else:
#     print('done')

# while True:
#     word = input('Enter:')
#     if word == 'ok':
#         break
#     print('next')

# some_list = [1, 2, 3, 4, 5]
# i = 0
# while i < len(some_list):
#     print(some_list[i])
#     i += 1

# for i in some_list:
#     print(i)

# for i in range(2, 10, 3):
#     print(i)

# for i, fruit in enumerate(['apple', 'banana', 'orange']):
#     print(i, fruit)

# days = ['Mon', 'Tue', 'Wed']
# fruits = ['apple', 'banana', 'orange']
# drinks = ['coffee', 'tea', 'beer']

# for day, fruit, drink in zip(days, fruits, drinks):
#     print(day, fruit, drink)

# d = {'X': 100, 'Y': 200}
# for k, v in d.items():
#     print(k, v)

# def menu(entree, drink, dessert):
#     print('entree:' + entree)
#     print('drink:' + drink)
#     print('dessert:' + dessert)

# menu(entree='beef', dessert='ice', drink='beer')

# def menu(**kwargs):
#     print(kwargs)
#     for k, v in kwargs.items():
#         print(k,v)

# d = {
#     'entry': 'beef',
#     'drink': 'coffee',
#     'dessert': 'ice'
# }

# menu(**d)

# def outer(a, b):

#     def innner():
#         return a + b

#     return innner

# print(outer(1, 2)

# f = outer(1, 2)
# r = f()
# print(r)

# def circle_area_func(pi):
#     def circle_area(radius):
#         return pi * radius * radius
    
#     return circle_area

# ca1 = circle_area_func(3.14)
# ca2 = circle_area_func(3.141592)

# print(ca1(10))
# print(ca2(10))

# def print_info(func):
#     def wrapper(*arg, **kwarg):
#         print('start')
#         print('func:', func.__name__)
#         print('args:', arg)
#         print('kwarg:', kwarg)
#         result = func(*arg, **kwarg)
#         print('result:', result)
#         print('end')
#         return result
#     return wrapper

# @print_info
# def add_num(a, b):
#     return a + b

# r = add_num(10, 20)
# print(r)

# l = ['Mon', 'tue', 'Web', 'Thu', 'fri', 'sat', 'Sun']
# def change_words(words, func):
#     for word in words:
#         print(func(word))

# # def sample_func(word):
# #     return word.capitalize()

# # sample_func = lambda word: word.capitalize()

# change_words(l, lambda word: word.capitalize())

l = ['Good morning', 'Good afternoon', 'Good nigth']
for i in l:
    print(i)

print('#########################')

def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'
# for g in greeting():
#     print(g)

g = greeting()
print(next(g))
print('@@@@@@@@@@')
print(next(g))
print('@@@@@@@@@@')
print(next(g))
