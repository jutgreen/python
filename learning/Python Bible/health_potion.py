# random number generator for player walking over health potion

import random

# initial player health

health = 50

# difficulty level reduces potion health effectiveness
difficulty = 3

# random health potion increase
# force integer because dividing creates a float
potion_health = int(random.randint(25,50) / difficulty)

# update health variable with potion health
health = health + potion_health

print(health)