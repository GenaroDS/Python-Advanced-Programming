# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    def __init__(self, week: int, numbers : list):
        self._week = week
        self._numbers = numbers
    def number_of_hits(self, numbers: list):        
        return len([number for number in numbers if number in self._numbers])

    def hits_in_place(self, numbers : list):
        return [listNumber if listNumber in self._numbers else -1 for (listNumber, selfNumber) in zip(numbers, self._numbers)]
