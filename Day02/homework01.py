def fib(n):
    a,b = 0,1
    c = a
    i = 0
    while i < n:
        c = b
        b += a
        a = c
        i +=1
        yield a


f = fib(40)
mylist = []
for i in range(40):
    mylist.append(next(f))

print(mylist)