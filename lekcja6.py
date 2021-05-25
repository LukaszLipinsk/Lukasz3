# # zadanie domowe lekcja 6
# *****
# ****
# ***
# **
# *
#
# *
# **
# ***
# ****
# *****
for i in range(5):
    #print("*", end="")
    for b in range(i+1):
        print("*",end="")
    print()


def fun_rekurencja(a):
#    for a in range(1,2):
    if a ==0:
        return 1
    c=fun_rekurencja(a-1)*a
    return c
print(fun_rekurencja(5))


c=1
for i in range (1):
    if i>0:
        c*=i
print(c)


