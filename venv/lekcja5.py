
#zliczyc ilosc samoglosek w stringu ile podal uzytkownik
# zwroci odwrotny string podaj napis i napis kt too tok

a=["jabłko", "banan", "truskawka", "porzeczka"]
a.sort()
print(a)
a.remove("truskawka")
for owoc in a:
    print(owoc)

a=[1,4,6,23,55,121231,-24,3,-44,5,2,888,0,23,1, None]
# "".sort(reverse=False)
print(a)
if -23 in a:
    print("-23 jest w liscie")
else:
    print("nie ma -23")
b=[5,55555]
b.extend(a)
# for liczba in a :
#     if liczba is not None:
#         b.append(liczba)
print(b)

string="Litwo Ojczyzno moja"
string2=""
a=len(string)
# len(string)
print(a)
c=0
# for znak in string:
#     print(znak)
#     if znak!=" ":
#         c+=1
print(c)
c=""
for znak in string:
    if znak.lower() in ["a","e","i","u", "ę", "ą", "o", "y"]:
        c+="_"
    else:
        c+=znak
print(c)

#napisz funkcje która pobiera liste zawierajaca tylko liczby i zwraca pierwszy element

def liczby(a):
    return a[1]
a=[111,222,23,87]
b=liczby(a)
print(b)

#napisz funkcje która pobiera ziemnna bulowska i zwraca ją jako string

def zmienna(a):
    if a:
        return "prawda"
    else:
        return "fałsz"
  #  return str(a)

b=zmienna("zero"=="zero")
print(b)


#boolean=True and False

#napisz funkcje ktoa sprawdza czy przekazana lcizba jest parzysta czy nie i wyswietla odpowiedni komyunikat


def parzysta(a):
    if a%2==0:
        return "liczba parzysta"
    else: return "fałsz"
b=parzysta(27)
print(b)


