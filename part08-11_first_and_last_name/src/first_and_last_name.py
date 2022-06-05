# Write your solution here:

class Person:
    def __init__(self, name :str):
        self.name = name
    def return_first_name(self):
        splitted = self.name.split(" ")
        return splitted[0]
    def return_last_name(self):
        splitted = self.name.split(" ")
        return splitted[1]











