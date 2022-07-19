#

print("hello".count("e"))

text = "happy birthday"
print(text.count("a"))
print(text.count("day"))

x = "Happy Birthday"
print(x.lower())
print(x.upper())
print(x)
print(x.capitalize())
print(x.title())
print(x.isupper())
print(x.islower())
print(x.istitle())
print(x.isalpha())
print("abcd".isalpha())
print("1234".isdigit())

print(x.index("Birthday"))

# index will error if string is not found, can use find instead

print(x.find("asdfghjkl"))

y = "0000000happybirthday"
print(y.strip("0"))

name = input("what is your name? ").strip()
print(name)
print(len(name))