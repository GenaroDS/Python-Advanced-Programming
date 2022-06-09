# Write your solution here:
from turtle import window_height


class Item:
    def __init__(self, name : str, weight : int):
        self.__name = name
        self.__weight = weight    
    def name(self):
        return self.__name

    
    def weight(self):
        return self.__weight
    
    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"
    
class Suitcase:
    def __init__(self, max_weight : int):
        self.__items = []
        self.__max_weight = max_weight

    def combined_weight(self):
        total_weight = 0
        for item in self.__items:
            total_weight += item.weight()
        return total_weight
        
    def add_item(self, item : Item):
        if self.combined_weight() + item.weight() <= self.__max_weight:        
            self.__items.append(item)

    def __str__(self):        
        if (len(self.__items)) == 1:
            return f"{len(self.__items)} item ({self.combined_weight()} kg)"
        else:
            return f"{len(self.__items)} items ({self.combined_weight()} kg)"

    def print_items(self):
        for item in self.__items:
            print(item)

    def weight(self):
        return self.combined_weight()
    
    def heaviest_item(self):
        heaviest = 0
        returnItem = 0
        for item in self.__items:
            if item.weight() > heaviest:
                heaviest = item.weight()
                returnItem = item
        return returnItem

class CargoHold:
    def __init__(self, max_weight : int):
        self.__max_weight = max_weight
        self.__suitcases = []
    def weight(self):
        weight = 0
        for suitcase in self.__suitcases:
            weight += suitcase.weight()
        return weight
    def add_suitcase(self, suitcase : Suitcase):
        if suitcase.weight() + self.weight() <= self.__max_weight:
            self.__suitcases.append(suitcase)
    def __str__(self) -> str:
        if len(self.__suitcases) == 1:
             return f"{len(self.__suitcases)} suitcase, space for {self.__max_weight - self.weight()} kg" 
        return f"{len(self.__suitcases)} suitcases, space for {self.__max_weight - self.weight()} kg"       
    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()

