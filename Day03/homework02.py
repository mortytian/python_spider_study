import math
L = [(1, 5), (3, 9), (4,1), (3,6), (5,3)]

L.sort( key = lambda x : x[1])
print(L)

L.sort( key = lambda x : x[1], reverse= True)
print(L)

L.sort( key = lambda x : math.sqrt(x[0]**2 + x[1]**2))
print(L)