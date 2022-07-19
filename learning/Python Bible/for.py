for number in range(1, 101):
    print(number)

for number in [1, 2, 3, 4]:
    print(number)

for letter in "ABCD":
    print(letter)

vowels = 0
consonants = 0

for letter in "supercalifragilisticexpialidocious":
    if letter.lower() in "aeiou":
        vowels = vowels + 1
    elif letter == " ":
        pass
    else:
        consonants = consonants + 1
print("There are {} vowels.".format(vowels))
print("There are {} consonants.".format(consonants))