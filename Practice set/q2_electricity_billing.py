from Demos.SystemParametersInfo import x

class ElectricityBilling:
    def __init__(self, units):
        self.units = units

    def bill(self):
        first = lambda x: x*3 if x <= 100 else second(x)
        second = lambda y: (y-100)*5 + 100*3 if y <= 200 else third(y)
        third = lambda z: 100*5 + 100*3 + (z-200)*8 if z <= 300 else fourth(z)
        fourth = lambda a: (100*5 + 100*3 + (a-200)*8) + (a-300)*8 + (a-300)/10
        return first(self.units)

units_used: int = int(input())
bill = ElectricityBilling(units_used)
print(bill.bill())