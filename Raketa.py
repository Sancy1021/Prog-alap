indlulas = int(input("hány órás visszaszámlálást tervezünk?"))
kesleltetes=0
for szamlalo in range(indlulas,0,-1):
    print("Visszaszámlálás:",szamlalo)
    felf=(input("Fel kell függeszteni a visszaszámlálást (i/n)?"))
    if felf.lowler()=='i':
        kesleltetes+=1
    print("A rakéta a visszaszámlálást követően ennyi órával indult:" ,indlulas+kesleltetes)
    
