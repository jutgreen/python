import random, sys, os, math, pyperclip
from random import * # will not need to type random.

# print('Hello')
# sys.exit()
# print('Goodbye')


pyperclip.copy('Hello world!')
pyperclip.paste()


def hello():
    print('howdy!')
    print('hello!!!')
    print('hello there!')


hello()
hello()
hello()


def hello(name):
    print ('Hello ' + name)


print(hello('justin'))
print(hello('leeloo'))