lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Nate", "Justin", "Brittany", "Stephanie", "Nick"]
friends.extend(lucky_numbers)
print(friends)

friends.append("Leeloo")
print(friends)

friends.insert(1, "Kimo")
print(friends)

friends.remove("Kimo")
print(friends)

print(friends.index("Nick"))

friends.clear()
print(friends)