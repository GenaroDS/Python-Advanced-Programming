# WRITE YOUR SOLUTION HERE:

class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.persons = []
    def add(self,person:Person):
        self.persons.append(person)
    def is_empty(self):
        if len(self.persons) == 0:
            return True
        return False 
    def print_contents(self):
        totalHeight = 0
        for person in self.persons:
            totalHeight += person.height
        print(f"There are {len(self.persons)} persons in the room, and their combined hegiht is {totalHeight} cm")
        for person in self.persons:
            print(f"{person.name} ({person.height} cm)")
    def shortest(self):
        if self.is_empty():
            return None
        enano = self.persons[0]
        for person in self.persons:
            if int(person.height) < int(enano.height):
                enano = person
        return enano

    def remove_shortest(self):
        if not self.is_empty():
            corito = self.shortest()
            self.persons.remove(corito)
            return corito
        else:
            return None
        
    