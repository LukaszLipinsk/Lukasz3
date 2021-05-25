# class Danie:
#
#     def __init__(self, nazwa, cena=5):
#         self.nazwa=nazwa
#         self.cena=cena
#     def wyswietl(self):
#         print(self.nazwa, self.cena)
#
#
# danie=Danie("pizza", cena=10)
# danie2=Danie("kebab")
# danie3=Danie("Hamburger", cena=2)
#
# c=[danie,danie2, danie3]
# class Restauracja:
#     #pass
#     def __init__(self, nazwa, menu):
#         self.nazwa=nazwa
#         self.menu=menu
#     def wyswietl_menu(self):
#         for i in range(len(self.menu)):
#             self.menu[i].wyswietl()
#
#
# restauracja1=Restauracja("Gospoda", menu=c)
#
# restauracja1.wyswietl_menu()
#
# class Zwierze:
#
#     def __int__(self, waga, color, imie):
#         self.waga=waga
#         self.color=color
#         self.imie=imie
#
#     def jedz(self):
#         print("zwierze_je")
# # zwierze1=Zwierze()
#
# class Pies(Zwierze):
#
#     def __init__(self, waga, color, imie, zabawka):
#         # self.waga = waga
#         # self.color = color
#         # self.imie = imie
#         # super(Pies.__int__())
#         super().__int__(waga,color,imie)
#         self.zabawka=zabawka
#
#     def baw_sie(self):
#         print("Pies sie bawi")
#
# # class Kun(Zwierze):
# #
# #     def __init__(self, waga, color, imie, wlasiciel):
# #         super().__init__(waga,color,imie)
# #         self.wlasciciel=wlasiciel
# #
# #     def ciagnij(self):
# #         print("kon ciagnie woz")
#
# class Kot(Zwierze):
#     def __init__(self, waga, color, imie, wlasiciel):
#         super().__init__(waga, color, imie)
#         self.wlasciciel=wlasiciel
#     def mialczy(self):
#         print("Kocur mialczy")
#
#
# pies=Pies(50,"czarny","Reksio","smycz")
# # kun=Kun(200, "Bialy", "Baska", "Stachu")
#
# kot=Kot(10, "Bialy", "Mruczek", "Rys")
#
# pies.baw_sie()
# kot.mialczy()

class Zwierze:
    def __init__(self, imie, kolor):
        self.kolor = kolor
        self.imie=imie
    def wydajdzwiek(self):

        # return # wychodzi z funkcji


        # return
        # getpass

        print("harczy")
       # print("warczy")


class Pies(Zwierze):
    def __init__(self, imie) -> None:
        super().__init__(imie, "biały")
    def wydajdzwiek(self):
        print("HAUHAU")

class Kot(Zwierze):
    def __init__(self, imie, wlasciciel) -> None:
        super().__init__(imie, "biały")
        self.wlasciciel=wlasciciel

    def wydajdzwiek(self):
        print("mialmial")


kot=Kot("mruczaek", "ja")
pies=Pies("szczekacz")
zwierze=Zwierze("ogolnie", "")

c=[kot, pies, zwierze]
for i in range(len(c)):
    c[i].wydajdzwiek()


