# from pprint import pprint
# lista1=[4,3,2,3,3333333]
# with open("liczby.txt") as pliczek:
#     # pliczek.readlines()
#     linie= pliczek.readlines()
#     for linia in linie:
#         ilinia=int(linia)
#         lista1.append(ilinia)
#         # print(ilinia)
# pprint(lista1)
from operator import itemgetter
from pprint import pprint
# lista1=[4,3,2,3,3333333]
a={}
with open("liczby.txt") as pliczek:
    # pliczek.readlines()
    linie= pliczek.readlines()
    for linia in linie:
        ilinia=int(linia)
        # lista1.append(ilinia)
        if ilinia not in a:
            a[ilinia]=0
        a[ilinia]+=1
        # print(ilinia)
# pprint(sorted(lista1))
# pprint(a)

b=sorted(a.items(), key=itemgetter(1), reverse=True) # a.items zwroci liste krotek w nawaisie okaglym klucz wartosc, domyslnie sortuje wedlug zerowego elemntu jak chcemny zeby wedlug wartoswci czyli drugie elementu to trzeby napisac key po jakim kluczu ma spoortowac robimy itemgetter (mowi nam po kotrej wartosci ma sarotwac 0 lub 1 w tym przypadku 0 = key , 1 = value
# reverse=True odwraca od najwiekszych do najmnijeszy)

for c in range(4):
    print(b[c])

# pprint(b)