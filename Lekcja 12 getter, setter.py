#
# class Temperatura:
#
#     def __init__(self, temperatura=0):
#         self.__temperatura=temperatura
#     def get_temperatura(self):
#         return self.__temperatura
#     def set_temeperatura(self, t):
#         if t <= -273:
#             print("nie wlasciwa temperatura")
#         else:
#             self.__temperatura=t
#     def zamiania_tem_na_faranthite(self):
#         return self.__temperatura*1.8+32
#
#
#
#
# temperatura=Temperatura(temperatura=28)
# print(temperatura.get_temperatura())
# temperatura.set_temeperatura(-10)
# # temperatura.__temperatura=15
# temperatura.set_temeperatura(-275)
# print(temperatura.get_temperatura())
#
# print(temperatura.zamiania_tem_na_faranthite())


class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.__imie=imie
        self.__nazwisko=nazwisko
        self.__pensja=pensja
    def get_imie(self):
        return self.__imie
    def get_nazwisko(self):
        return self.__nazwisko
    def get_pensja(self):
        return self.__pensja

    def set_imie(self, nowe_imie):
        self.__imie=nowe_imie
    def set_nazwisko(self, nowe_nazwisko):
        self.__nazwisko=nowe_nazwisko
    def set_pensja(self, nowa_pensja):
        self.__pensja=nowa_pensja

pracownik=Pracownik("Stachu","Czerstwy",2)
pracownik2=Pracownik("Rychu", "Kot",3)


c=[pracownik,pracownik2]


class Przelozony(Pracownik):

    def __init__(self, imie, nazwisko, pensja, lista_pracownikow):
        super().__init__(imie, nazwisko, pensja)
        self.lista_pracownikow = lista_pracownikow
    def wyswietl_liste_pracownikow(self):
        for i in range(len(self.lista_pracownikow)):
            print(self.lista_pracownikow[i].get_nazwisko())

    def dodaj_pracownika(self, pracownik):
        self.lista_pracownikow.append(pracownik)

przelozony=Przelozony("Edward", "Nowak", 23, lista_pracownikow=c)

przelozony.wyswietl_liste_pracownikow()

pracownik=Pracownik("zbychu","Kowalski", 55555)

przelozony.dodaj_pracownika(pracownik)
przelozony.wyswietl_liste_pracownikow()





