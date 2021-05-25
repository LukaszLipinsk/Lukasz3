# napsiac w zbiroze okresliony liczby parzyste


# def parzysta():
#     b=[]
#     for a in range(1, 100):
#         if a % 5 == 0:
#             b.append(a)
#     return b
# c=parzysta()
# print(c)
# del c[-2]
# print(c)


# def parzysta():
#     b=[]
#     for a in range(1, 100):
#         if a % 5 == 0:
#             b.append(a)
#     return b
# c=parzysta()
# print(c)
# # del c[-2]
# # print(c)
# for a in range(0,len(c)):
#     if c[a] % 10==0:
#         del c[a]
# print(c)

# napisz funkcje kotra pobiera argumenty a b c i zwraca sume liczb ktore sa podizelne przez c  z zakresu a,b wlacznie

def zakres(a,b,c):
    suma=0
    for i in range (a,b+1):
        if i%c==0:
            suma+=i
    return suma
e=zakres(1,1,8)
print(e)

#odworc strin dostajesz string i od konca wypisuje

string="domek"
print(string)
for i in range(len(string)-1,-1,-1):
    print(string[i])





