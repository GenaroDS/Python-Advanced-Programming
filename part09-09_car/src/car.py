# WRITE YOUR SOLUTION HERE:
class Car:
    def __init__(self):
        self.__tank = 0
        self.__km = 0
    def fill_up(self):
        self.__tank = 60
    def drive(self, km:int):
        if km >= self.__tank:    
            amount = self.__tank
            self.__tank = 0
            self.__km += amount
        else:
            self.__tank -= km
            self.__km += km
    def __str__(self):
        return f"Car: odometer reading {self.__km} km, petrol remaning {self.__tank} litres"

