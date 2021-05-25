
class Converter:
    def __init__(self, minuty):
        self.__minuty=minuty

    def set_minuty(self, nowe_minuty):
        self.__minuty=nowe_minuty

    def get_sekundy(self):
        self.__convertuj()
        return self.__sekundy



    def __convertuj(self):
        self.__sekundy=self.__minuty*60



converter=Converter(1)
print(converter.get_sekundy())



def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return (fib(n-1)+fib(n-2))

print(fib(20))


