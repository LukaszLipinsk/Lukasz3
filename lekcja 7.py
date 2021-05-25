
a=[2,4,6,6,2,2,2,8,8,8,8]

a=sorted(a)
b=a[0]
print(b)
for i in range(len(a)):
    c=a[i]
    if b!=c:
        print(c)
        b=c
print(a)
a=set(a)
a=sorted(a)
print(a)
#
# b={"ala":2, "ela":5, "JAs":20}
# b["Kunegunda"]=30
# c=[5]
# print(b)
# c[0]=20
# b["klucz wartosc"]=20
# b["Kunegunda"]=50
# print(b)
# print(c)
#
# if "ola" in b:
#     print("ala jest w b")
# else:
#     print("ala nie jest w b")
#
# print(b.values())
# print(b.keys())
# # b.clear()
# print(b)
# b.pop("ela")
# print(b)
#
# for k,v in b.items():
#     # v+=20
#     b[k]+=20
#     print(b[k])
# print(b)
#     # print(k,v)


a=[2,1,6,6,52,6,5525,8,11,233]
def funkcjasortowania(a):
    for i in range(len(a))
        a[i]