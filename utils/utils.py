import random


def random_choice(data: str):
    if ';' in data:
        choices = data.split(';')
        choice = random.choice(choices)
    elif '-' in data:
        choices = data.split('-')
        choice = random.randint(int(choices[0]), int(choices[1]))
    return choice
