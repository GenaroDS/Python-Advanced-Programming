import random

def word_generator(characters: str, length: int, amount: int):
    for _ in range(amount):
        word = "".join(random.choice(characters) for _ in range(length))
        yield word
