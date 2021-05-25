
#klasa to jest struktura danych w ktorej mozemy przekochowywac dane i dodatkowo przechwoawyac operacje tych klas czyli fukncje (metody)

class MojaKlasa1C:
    zmienna=1
    b="ala ma kota"
    c=True

klasa=MojaKlasa1C()
print(klasa.b)
klasa.b="ela ma psa"
print(klasa.b)
print(klasa.b)

klasa2=MojaKlasa1C()
print(klasa2.b)

class Uczen:

    imie=""
    naziwsko=""
    nr_index=0

    def wagaruj(self):
        print(self.imie, self.nazwisko, "wagaruje")
    def odrabia_lekcje(self):
        print(self.imie, self.nazwisko, "odrabia leckje")
        self.otworz_zeszyt()
    def otworz_zeszyt(self):
        print("otworzyl zeszyt")


uczen1=Uczen()
uczen1.imie="jas"
uczen1.nazwisko="Kowalski"
uczen1.nr_index=1234

print(uczen1.imie,uczen1.nazwisko, uczen1.nr_index)

uczen2=Uczen()

uczen2.imie="Harrry"
uczen2.nazwisko="Potter"
uczen2.nr_index=9999

#print(uczen2.imie,uczen2.nazwisko, uczen2.nr_index)

c=[uczen1, uczen2]
for i in range(len(c)):
    print(c[i].nazwisko)

for uczen in c:
    print(uczen.nazwisko)

uczen1.wagaruj()

for i in range(len(c)):
    c[i].wagaruj()


uczen2.odrabia_lekcje()

for i in range(len(c)):
    c[i].odrabia_lekcje()


class Samochod:
    marka=""

    def start(self):
        print(self.marka, "jedz")
    def stop(self):
        print(self.marka, "zatrzymaj sie")
opel=Samochod()
fiat=Samochod()
opel.marka="opel"
fiat.marka="fiat"


samochody=[opel, fiat]
for i in range (len(samochody)):
    samochody[i].start()

for i in range (len(samochody)):
    samochody[i].stop()
for i in samochody:
    i.start()