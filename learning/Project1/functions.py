# functions
# code inside of the function has to be indented
# have to 'call' the function to execute
# parameter is information passed through function
#

def say_hi():
    print("Hello User")

say_hi()


def say_hi(name):
    print("Hello " + name)


say_hi("Justin")
say_hi("Leeloo")

def say_hi(name, age):
    print("Hello " + name + ", you are " + age)


say_hi("Justin", "34")
say_hi("Leeloo", "2")

def say_hi(name, age):
    print("Hello " + name + ", you are " + str(age))


say_hi("Justin", 34.5)
say_hi("Leeloo", 2.5)