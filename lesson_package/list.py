# r = [1, 2, 3, 4, 5, 1, 2, 3]
# r.index(3)

# print(r.index(3, 3))

# print(r.count(3))

# if 5 in r:
#     print('exist')

# r.sort()
# print(r)
# r.sort(reverse=True)
# print(r)
# r.reverse()
# print(r)

# s = 'My name is Mike'
# to_split = s.split(' ')
# print(to_split)
# x = '#####'.join(to_split)
# print(x)

# print(help(list))

# i = [1, 2, 3, 4, 5]
# j = i
# j[0] = 100
# print('j=',j)
# print('i=',i)
# print(id(i))
# print(id(j))

# x = [1, 2, 3, 4, 5]
# y = x.copy()
# # y = x[:]
# y[0] = 100
# print('x=',x)
# print('y=',y)
# print(id(x))
# print(id(y))

seat = []
min = 0
max = 5
print(min <= len(seat) < max)
seat.append('p')
seat.append('p')
print(min <= len(seat) < max)
seat.append('p')
seat.append('p')
seat.append('p')
print(min <= len(seat) < max)
seat.pop(0)
print(min <= len(seat) < max)