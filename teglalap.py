def kerulet (a,b):
    return(2*(a+b))
def terulet(a,b):
    return(a*b)
a= float(input("A oldal: "))
b= float(input("B oldal: "))
K = kerulet(a,b)
T = terulet(a,b)
print("A téglalap kerülete:[0]egység.".format(K))
print("A téglalap terület:[0] egység.".format(T))