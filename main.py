message = ['One', 'Two', 'Three']
class Reader:
    def __init__(self, blist):
        self.blist = blist
        self.clist = []

    def read(self):
        for item in self.blist:
            if item in self.clist:
               False
            else:
                self.clist.append(item)
                print(item)
        print("\n")

class Adder:
    def more(self, dlist,element):
        dlist.append(element)

print(message)
print("*"*30)
l1 = Reader(message)
l1.read()
l1.read()
Adder.more(l1,message,'Four')
print("*"*30)
print(message)
print("*"*30)
l1.read()
l1.read()

l2 = Reader(message)
l2.read()
l2.read()
