a=[1,2,3,4]
a[0]=5
print(a)
for i in range(3): #len(a)):
    a[i]=7
print(a)
a.append(10)
a.append(10)
for i in range(5):
    a.append(10)

print(a)

for i in a:
    print(i)

def funkcjalista(a):
    return max(a)
print(funkcjalista([1,6,55]))




