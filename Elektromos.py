print('Elektromos teljesitmény és ellenálás számolás, bekért áramerősség')
while True:
    i= int(input('Kérem adjon meg az áramerősség értékét (egász szám legyen):'))
    u= int(input('Kérem adjon meg az feszültség értékét (egász szám legyen):'))

    print('Az elektromos teljesítmény végrehajtani? (i/n)')
    print('Az ellenállás:' ,u/i,'ohm ')
    sz= input('Szeretne még egy számítást végrehajtani? (i/n)')
    if sz== 'n' :
        break