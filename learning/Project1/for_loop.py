# for loops change for each iteration of running the loop
#
#

for letter in "Leeloo Dallas Multipass":
    print(letter)

friends = ["Leeloo", "Kimo", "Korben"]
for friend in friends:
    print(friend)

for index in range(10):
    print(index)

for index in range(3, 10):
    print(index)


for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("first iteration")
    else:
        print("not first")