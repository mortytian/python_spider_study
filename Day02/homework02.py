L = [1,3,2,4,1,1,3,2,4,1,3,1,5,11,12,14,14,1,3,2,4,1,91]
L2 = []
L3 = []
for i in L:
    if i not in L2:
        L2.append(i)

dil = {}
for i in L:
    if str(i) not in dil:
        dil[str(i)] = 1
    else:
        dil[str(i)] += 1

for key,value in dil.items():
    if value == 2:
        L3.append(int(key))

print(L)
print(L2)
print(L3)
