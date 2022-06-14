# TEE RATKAISUSI TÄHÄN:
import datetime
from operator import truediv
class SimpleDate:
    def __init__(self, day:int, month:int , year:int):
        self._day = day
        self._month = month
        self._year = year
    
    def __str__(self):
        return f"{self._day}.{self._month}.{self._year}"

    def __lt__(self, another):
        if self._year < another._year:
            return True
        elif self._year > another._year:
            return False
        if self._month < another._month:
            return True
        elif self._month > another._month:
            return False
        if self._day < another._day:
            return True
        elif self._day > another._day:
            return False
    def __gt__(self, another):
        if self._year < another._year:
            return False
        elif self._year > another._year:
            return True
        if self._month < another._month:
            return False
        elif self._month > another._month:
            return True
        if self._day < another._day:
            return False
        elif self._day > another._day:
            return True
    def __eq__(self,another):
        if (self._year == another._year) and (self._month == another._month) and (self._day == another._day):
            return True
        else:
            return False

    def __ne__(self,another):
        return not (self == another)

    def __add__(self, num : int):
        newReturn = SimpleDate(self._day, self._month, self._year)
        newReturn._day += num
        while newReturn._day > 30:
            newReturn._month += 1
            newReturn._day -= 30
        while newReturn._month > 12:
            newReturn._year += 1
            newReturn._month -= 12
        return newReturn

    def __sub__(self, another):
        totalSelf = self._day + self._month * 30 + self._year * 360
        anotherSelf = another._day + another._month * 30 + another._year * 360
        return abs(totalSelf-anotherSelf)
