
class Recording:
    def __init__(self, amount : int):
        if amount >= 0: 
            self.__length = amount
        else:
            raise ValueError

    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, amount : int):
        if amount >= 0:
            self.__length = amount
        else: 
            raise ValueError
