films = {
    "Toy Story": [3, 5],
    "Black Panther": [18, 5],
    "Idiocracy": [13, 5],
    "Religulous": [13, 5]
    }

while True:
    choice = input("Which film would you like to watch?").strip().title()

    if choice in films:
        age = int(input("How old are you? ").strip())

        # check user age
        if age >= films[choice][0]:

            # check enough seats
            num_seats = films[choice][1]

            if num_seats > 0:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1] - 1
            else:
                print("Sorry, we are sold out!")
        else:
             print("You are too young to see that film.")
    else:
      print("We don't have that film... ¯\_(ツ)_/¯")