from random import choice

questions = ["Why do dogs stare into your eyes while pooping? ",
             "Why is the sky blue? ",
             "Why is grass green? ",
             "Where do babies come from? ",
             "Why do I have to eat vegetables? ",
             "Where are all the dinosaurs? "]

question = choice(questions)

answer = input(question).strip().lower()

while answer != "just because":
    answer = input("Why? ").strip().lower()
print("Oh... Okay then")