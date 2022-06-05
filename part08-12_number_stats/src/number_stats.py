# Write your solution here!
class NumberStats:
    def __init__(self):
        self.numbers = 0
        self.counter = 0
    def add_number(self, number:int):
        self.numbers += number
        self.counter += 1
        
    def count_numbers(self):
        return self.counter
        
    def get_sum(self):
        if self.counter>0:
            return self.numbers
        return 0
    def average(self):
        if self.counter>0:
            return self.numbers/self.counter
        return 0


numbers = NumberStats()
odd_numbers = NumberStats()
even_numbers = NumberStats()
print("please type in integer numbers")
while True:
    number = int(input())
    if number == -1:
        break
    numbers.add_number(number)
    if number % 2 == 0:
        even_numbers.add_number(number)
    else:
        odd_numbers.add_number(number)
print(f"Sum of numbers: {numbers.get_sum()}")
print(f"Mean of numbers: {numbers.average()}")
print(f"Sum of even numbers: {even_numbers.get_sum()}")
print(f"Sum of odd numbers: {odd_numbers.get_sum()}")