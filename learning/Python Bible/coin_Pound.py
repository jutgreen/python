import random

class Pound():

    def __init__(self, rare=False):

        self.rare = rare

        if self.rare:
            self.value = 1.25
        else:
            self.value = 1.00

        self.value = 1.00
        self.color = "gold"
        self.num_edges = 1
        self.diameter = 22.5  # mm
        self.thickness = 3.15  # mm
        self.heads = True

    def __del__(self):
        print("Coin Spent!")

    def rust(self):
        self.color = "greenish"

    def clean(self):
        self.color = "gold"

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice




coin1 = Pound()
coin2 = Pound()
print(coin1.color)
print(coin2.color)
coin1.rust()
print(coin1.color)
coin1.clean()
print(coin1.color)
print(coin1.heads)
print(coin2.heads)
coin1.flip()
coin2.flip()
print(coin1.heads)
print(coin2.heads)
del coin1


# coin1 = Pound(rare=True)
# print(type(coin1))
# print(coin1.value)
# print(coin1.color)
# coin1.color = "greenish"
# print(coin1.color)
# coin2 = Pound()
# print(coin2.color)