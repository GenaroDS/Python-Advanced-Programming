# WRITE YOUR SOLUTION HERE:
import collections
class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list : list):
        return max(set(my_list), key = my_list.count)
    @classmethod
    def doubles (cls, my_list : list):
        frequency = collections.Counter(my_list)
        amount = 0
        for items in frequency.items():
            if items[1] > 1:
                amount += 1
        return amount

