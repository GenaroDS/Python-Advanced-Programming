# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents

    def __str__(self):
        money = (self._euros)*100+(self._cents)     
        money =  money/100
        return f"{money:.2f} eur"
         #Arreglar
    @property
    def _float(self):
        money = (self._euros)*100+(self._cents)      
        money =  money/100
        return money

    def __eq__(self, another) -> bool:
        return self._float == another._float

    def __lt__(self, another):
        return self._float < another._float

    def __gt__(self, another):
        return self._float > another._float

    def __ne__(self,another):
        return self._float != another._float

    def __add__(self,another):

        #Arreglar
        pesos = self._euros + another._euros
        centavos = self._cents + another._cents        
        return Money(pesos,centavos)

    def __sub__(self,another):
        if self._float - another._float < 0:
            raise ValueError
        else:
            newMoney = round(self._float-another._float,2)
            newMoney = f"{newMoney:.2f}"
            newMoney = newMoney.split(".")
            return Money(int(newMoney[0]),int(newMoney[1]))
