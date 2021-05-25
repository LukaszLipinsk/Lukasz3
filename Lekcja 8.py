
# i =0
# while True:
#     print(i, end=" ")
#     if i<=100:
#         i=i+1
#     else:break


from pprint import pprint
def funkcja1():
    i=0
    a={}
    while True:
        # print(i)
        a[i]=i**2
        if i>99:
            return a
        i=i+1
a=funkcja1()

pprint(a)

