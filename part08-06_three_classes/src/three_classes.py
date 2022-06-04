# Write your solution here
import string


class Checklist:
    def __init__(self, header : int, entries : list):
        self.header = header
        self.entries = entries
class Customer:
    def __init__(self, id : string , balance: float, discount  : list):
        self.id = id
        self.balance = balance
        self.discount = discount 

class Cable:
    def __init__(self, model : string, length : float, max_speed : int , bidirectional : bool):
        self.model = model
        self.length = length
        self.max_speed = max_speed
        self.bidirectional = bidirectional
