class MyList:
    def __init__(self,iterable = ()):
        self.list = []
        for i in iterable:
            self.list.append(i)


    def __str__(self):
        return 'MyList('+self.list.__str__()+')'

    def __add__(self, other):
        if  isinstance(other,MyList):
            newlist = list(self.list)
            newlist.extend(other.list)
        return MyList(newlist)

    # def __m

L1  = MyList([1,2,3])
L2 = MyList(range(2,5))
L3 = L1 + L2
L4 = L2 + L1

# print(d)