contador_externo = 0 #inicia en 0
contador_interno = 0 #inicia en 0

while contador_externo < 5 : #mientras que contador_externo sea menor que 5, haz lo siguiente.
    while contador_interno < 6 : #mientras que contador interno sea menor a 6, haz lo siguiente. 
        print(contador_externo, contador_interno) #imprime en consola contador_externo, y contador_interno.
        contador_interno +=1 #sumale 1 a contador interno.
        
        if contador_interno >= 3:
            break #si, contador interno es igual o mayor a 3 Detente. 
        
    contador_externo += 1 # a contador_externo sumale uno. Al terminar la condicion de contador_interno<6
    contador_interno = 0 #Contador interno asignale el valor 0.

    #inicia en Contador externo = 0 
    #          Contador interno = 0 
    # contador interno +1 = 1
    # Contador interno es menor que 3, el ciclo sigue.
    # Contador externo sumale 1. 
    # contador interno asignale 0.
