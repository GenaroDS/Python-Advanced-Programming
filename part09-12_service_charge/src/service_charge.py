# WRITE YOUR SOLUTION HERE:
class BankAccount:
    def __init__(self, owner : str , number : int , balance: float):
        self.__owner = owner
        self.__number = number
        self.__balance = balance

    def deposit(self, amount:float):
        if amount >= 0:
            self.__balance += amount
            self.__service_charge()
    
    def withdraw(self, amount: float):
        if amount <= self.__balance:            
            self.__balance -= amount
            self.__service_charge()
    @property
    def balance(self):
        return self.__balance

    def __service_charge(self):
        self.__balance *= 0.99

