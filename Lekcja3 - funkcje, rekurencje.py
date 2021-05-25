#Zadanie#2


# def ala():
#     print("ala ma kota")
# # ala()
#
# for i in range(1,11):
#     ala()
#

# def dom(i):
#     print(i)
# dom(5)
#
# for i in range(1,6):
#     dom(i)
#
#
# def imie_i_nazwisko(imie, nazwisko):
#     print(imie, nazwisko)
# imie_i_nazwisko("Jas","Kowalski")
#
#
# def calculation(a,b):
#     sum=a+b
#     difference=a-b
#     return sum,difference
# print(calculation(2,5))

def rekurencja(a):
    if a==0:
        return 0
    else:
        return a+rekurencja(a-1)
b=rekurencja(10)
print(b)


def funkcja(a, napis="ala ma kota"):
    for _ in range(a):
        print(napis)
funkcja(5,"dom")
funkcja(6,"cos")

funkcja(a=5, napis="cos")

funkcja(a=2)


def podniescdokwadratu(b):
    return b**2
a=podniescdokwadratu(5)
print(a)


def zwracaliczby(a,b):
    if a>b:
        return a
    else:
        return b
c=zwracaliczby(2,100)
print(c)

def zwraca3liczby(a,b,c):
    d=zwracaliczby(a,b)
    return zwracaliczby(d,c)
e=zwraca3liczby(5,1000,1000000000)
print(e)


