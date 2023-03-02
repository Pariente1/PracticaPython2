minutos = 0
segundos = 0

while minutos < 60 :
    while segundos < 60 :
        print(f'Van {minutos} minutos, {segundos} segundos transcurridos')
        segundos += 1

        if segundos >= 60:
            break
    
    minutos += 1
    segundos = 0

