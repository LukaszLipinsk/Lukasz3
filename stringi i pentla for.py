# j=1
# for i in range(1, 9):
#     print(j)
#     j*=10
#


# a="ala ma kota"
# #print(a[0])
# for i in range(0,len(a)):
#     print(a[i])
#
#
# a="ala ma kota"
# for i in a:
#     print (i)

#Lekcja3

#zadanie1

# j=1
# for i in range(1,11):
#     print(j)
#     j*=-1
#
#
# j=0
# for i in range(0,100000000):
#     j+=((-1)**i)/(2*i+1)
# print(j*4)


#Zadanie#2


# def ala():
#     print("ala ma kota")
# # ala()
#
# for i in range(1,11):
#     ala()
#

def dom(i):
    print(i)
dom(5)

for i in range(0,20):
   if i% 2 == 0:
    dom(i)
#
#
# def imie_i_nazwisko(imie, nazwisko):
#     print(imie, nazwisko)
# imie_i_nazwisko("Jas","Kowalski")
#
#
def calculation(a,b):
    sum=a+b
    difference=a-b
    return sum,difference
print(calculation(2,5))

def rekurencja(a):
    if a==0:
        return 0
    else:
        return a+rekurencja(a-1)
b=rekurencja(10)
print(b)


