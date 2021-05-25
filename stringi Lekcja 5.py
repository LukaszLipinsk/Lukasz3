a=38
a=float(38)
print(a)
a=38.0
print(a)

b=False
c=True
if not b:
    print("ala")

if b or c:
    print("ela")

# a="ala"
# print("a= ",a, "b=", b)
# print("a={}, b={}".format(a,b))
# print("a="+str(a))
#
# ala=input("podaj liczbe")
#
#
# def funkcjazmieniania(napis: str): # napis musi byc zawsze liczba zeby zadzialao
#     return int(napis)
# print(funkcjazmieniania(ala)*22)
#
#
# z=input("podaj napis")
# if z=="ola":
#     print("uzytkownik podal imie ola")
# else: print("uzytkownik wpisal inne dane")
#
# z=input("podaj napis")
# print("nuzytkownik podal:"+z)


# print(0,100)
# for i in range(0,101):
#     if i % 3==1:
#         print(i
#



z=input("podaj minuty")

def funkcjasekundy(a):
   # a=int(a) drugi sposob zamieninia a na intigera jak liczbe
    return int(a)*60

print(funkcjasekundy(z))


#zadanie2 oblicza pole trojka

a=input("podaj podstawe ")
h=input("podaj wysokosc")

def funkcjatrojkata(a,h):
    return 1/2*float(a)*float(h)
print(funkcjatrojkata(a,h))

a=input("podaj bok 1")
b=input("podaj bok 2")
c=input("podaj bok 3")

def funkcjaboku(a,b,c):
    a=float(a)
    b=float(b)
    c=float(c)

    if (a+b>c) and (a+c>b) and (b+c>a):
        return True
    else: return False

print(funkcjaboku(a,b,c))


# zliczyc ilosc samoglosek w stringu ile podal uzytkownik
# zwroci odwrotny string podaj napis i napis kt too tok


