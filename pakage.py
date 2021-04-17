# import lesson_package.utils
# from lesson_package import utils
from lesson_package.talk import human
try:
    from lesson_package import animal
except ImportError:
    from lesson_package.talk import animal

# from lesson_package.talk import *

# r = human.say_twice('Hi')

# print(r)

# print(human.sing())

print(human.cry())
print(animal.cry())