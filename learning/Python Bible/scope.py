

def f1():
    a = 100 # function creates a LOCAL scope
    print(a)

def f2():
    a = 50
    print(a)

f1()
f2()