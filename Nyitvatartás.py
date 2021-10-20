time = int(input('Hány ora van?'))

if  8 < time < 16 :
  print('Nyitva még:', 16 - time , 'óráig...') 

else:
  print(('Nincs nyitva.'))
if time > 16 :
    print (32 - time , 'óra múlva lesz nyitva! ')
else:
    print (8 - time, 'óra múlva lesz nyitva!' )