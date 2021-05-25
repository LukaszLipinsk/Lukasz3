

class Samochod:


    def __init__(self, marka, rocznik):
        self.__marka=marka
        self.__rocznik=rocznik

    def czy_nowe(self):
        if self.__rocznik>= 2015:
           return True
        else:
            return False
    def get_marka(self):
        return self.__marka
    def set_marka(self, nowa_marka):
        self.__marka=nowa_marka
    def get_rocznik(self):
        return  self.__rocznik
    def set_rocznik(self, nowy_rocznik):
        self.__rocznik=nowy_rocznik

class SamochodOsobowy(Samochod):

    def __init__(self,marka, rocznik, liczba_siedzen, przebieg):
        super().__init__(marka, rocznik)            #odwolanie do konstruiktora samochu klasy nadrzednej
        self.__przebieg = przebieg
        self.__liczba_siedzen=liczba_siedzen


    def get_liczba_siedzen(self):
        return self.__liczba_siedzen
    def set_liczba_siedzen(self, nowa_liczba_siedzen):
        self.__liczba_siedzen=nowa_liczba_siedzen

    def get_przebieg(self):
        return self.__przebieg
    def set_przebieg(self, nowy_przebieg):
        self.__przebieg=nowy_przebieg


class SamochodCiezarowy(Samochod):

    def __init__(self, marka, rocznik, ladownosc):
        super().__init__(marka, rocznik)
        self.__ladownosc=ladownosc

