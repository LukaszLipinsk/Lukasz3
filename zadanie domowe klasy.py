class Pracownik:

    # imie=""
    # nazwisko=""
    # numer_pesel=""

    def __init__(self, imie, nazwisko, numer_pesel):
        self.imie=imie
        self.nazwisko=nazwisko
        self.numer_pesel=numer_pesel

    def wyswietl(self):
        print(self.imie, self.nazwisko, self.numer_pesel)


pracownik1=Pracownik("jas", "kowalski", 1234)
# pracownik1.imie="jas"
# pracownik1.nazwisko="Kowalski"
# pracownik1.numer_pesel=1234

pracownik2=Pracownik("stach","malina",5555)
# pracownik2.imie="stach"
# pracownik2.nazwisko="malina"
# pracownik2.numer_pesel=555


pracownik3=Pracownik("rychu", "bak", "0001111")
# pracownik3.imie="rychu"
# pracownik3.nazwisko="bak"
# pracownik3.numer_pesel="00011111"

pracownik4=Pracownik("andrzej", "czerstwy", 234)
# pracownik4.imie="andzej"
# pracownik4.nazwisko="czerstwy"
# pracownik4.numer_pesel=234

pracownik5=Pracownik("alu", "bahu", 11)
# pracownik5.imie="alu"
# pracownik5.nazwisko="bahu"
# pracownik5.numer_pesel=11

print(pracownik1.imie)

c=[pracownik1,pracownik2, pracownik3, pracownik4, pracownik5]
for i in range(len(c)):
    c[i].wyswietl()

    # print(c[i].imie, c[i].nazwisko, c[i].numer_pesel)



class Biuro:

    # nazwa_biura=""

    # biuro1=hellios
    # biuro2=orbit

    # imie=""
    # nazwisko=""
    # pesel=""
    # lista_pracownikow=0


    def __init__(self, nazwa_biura, pracownicy):
        self.nazwa_biura=nazwa_biura
        self.pracownicy=pracownicy

    def wyswietl(self):
        print(self.nazwa_biura)
    def wyswietl1(self):
        # print(self.pracownicy)
        for i in range(len(self.pracownicy)):
            self.pracownicy[i].wyswietl()



pracownicy=[pracownik1,pracownik2,pracownik3,pracownik4,pracownik5]
pracownicy1=[pracownik4, pracownik5]
biuro1=Biuro("Helsios", pracownicy1) #pracownicy=[pracownik1])
biuro2=Biuro("Orbit", pracownicy)


biuro1.wyswietl1()
biuro2.wyswietl1()

