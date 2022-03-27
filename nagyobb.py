Egyik = int(input('Adj meg egy számot!'))
Masik = int(input('Adj meg egy másik számot!'))

if Masik>Egyik:
    print('A nagyobb érték {0}'.format(Masik))

elif Egyik>Masik:
    print('A nyagyobb érték {0}'.format(Egyik))

else:
    print('A két szám egyenlő')