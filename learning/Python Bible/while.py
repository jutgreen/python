num1 = 1
while num1 <= 10:
    if num1 % 2 != 0:
        print(num1)
    num1 = num1 + 1
print(num1)

L = []
while len(L) < 3:
    new_name = input("Please add a new name: ").strip().capitalize()
    L.append(new_name)

print("Sorry, list is full.")
print(L)
