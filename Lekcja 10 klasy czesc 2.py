

class Pojazd:
    # przebieg=0
    # marka=""
    # pojemnosc_silnika=0
    # ilosc_siedzen=0

    def __init__(self, przebieg, marka, silnik,ilosc_siedzen=5):            # KONSTRUKTOR
        self.przebieg=przebieg
        self.marka=marka
        self.silnik=silnik
        self.ilosc_siedzen=ilosc_siedzen
    def jedz(self):
        print(self.marka, "jedzie")

class Silnik:

    def __init__(self, pojemnosc, konie_mechaniczne, paliwo="diesel"):
        self.pojemnosc=pojemnosc
        self.konie_mechaniczne=konie_mechaniczne
        self.paliwo=paliwo

    def informacje(self):
        print(self.pojemnosc,self.konie_mechaniczne, self.paliwo)

silnik_opla=Silnik(1.1,85,"benzyna")
silnik_smarta=Silnik(2.9, 100, "hybryda")
silnik_poloneza=Silnik(11,2, "gas")

opel=Pojazd(300000, "opel", silnik_opla)                                                        # WYWOLANIE KONSTRUKTORA PRZSEKAZANIE PARAMETRU
smart=Pojazd(przebieg=10000, marka="smart",silnik=silnik_smarta,ilosc_siedzen=2)
polonez=Pojazd(1,"polonez",silnik_poloneza,3)

# opel.przebieg=300000
# opel.marka="opel"
# opel.pojemnosc_silnika=1.6

print(opel.przebieg)
print(opel.ilosc_siedzen)
print(smart.silnik)
opel.jedz()

tablica=[opel, smart,polonez]

for i in range (len(tablica)):
    tablica[i].jedz()

for i in range(len(tablica)):
    tablica[i].silnik.informacje()


