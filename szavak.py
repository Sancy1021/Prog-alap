szavak1 = input('első szó')
szavak2 = input('második szó')

szavak1_hossza = len( szavak1 )
szavak2_hossza = len( szavak2 )
if ( szavak1_hossza > szavak2_hossza  ):
    print('A hosszab szó' + szavak1)
elif szavak2_hossza > szavak1_hossza:
    print('A hosszab szó' + szavak2)
else:
    print('A két szó egy forma hosszú.')