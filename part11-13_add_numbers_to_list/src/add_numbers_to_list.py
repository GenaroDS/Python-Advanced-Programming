# WRITE YOUR SOLUTION HERE:
def add_numbers_to_list(numbers: list):
    while len(numbers) % 5 != 0:
        toAdd = numbers[len(numbers)-1]+1
        numbers.append(toAdd)
        print(len(numbers))
        toAdd += 1
        add_numbers_to_list(numbers)
        print(len(numbers))

