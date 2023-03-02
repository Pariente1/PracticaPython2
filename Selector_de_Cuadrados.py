Seleccion_Numero = int(input('Escribe un numero para buscar su raiz cuadrada: '))
print(f'Opciones para encontrar la raiz cuadrada de un numero. \n 1: enumeracion \n 2: aproximacion \n 3: busquedaBinaria \n')   
Seleccion_algoritmo = int(input('Selecciona escribiendo un numero del logaritmo a usar: '))

epsilon = 0.01

def enumeracion(objetivo):
    respuesta = 0

    while respuesta**2 < objetivo:
        respuesta += 1

    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'El {objetivo} no tiene raiz cuadrada')

def aproximacion(Seleccion_Numero):
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - Seleccion_Numero) >= epsilon and respuesta <= Seleccion_Numero: 
        print(abs(respuesta**2 - Seleccion_Numero), respuesta)
        respuesta += paso

    if abs(respuesta**2 - Seleccion_Numero) >= epsilon:
        print(f'No encontramos la raiz cuadrada de {Seleccion_Numero}')
    else:
        print(f'La raiz cuadrada del {Seleccion_Numero} es {respuesta}')

def busquedaBinaria(Seleccion_Numero):
    bajo = 0.0
    alto = max(1.0, Seleccion_Numero)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - Seleccion_Numero) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta**2 < Seleccion_Numero:
            bajo = respuesta
        else:
            alto = respuesta
    
        respuesta = (alto + bajo) / 2 

    print(f'La raiz cuadrada del {Seleccion_Numero} es la {respuesta}')

if Seleccion_algoritmo == 1:
  enumeracion(Seleccion_Numero)
elif Seleccion_algoritmo == 2:
  aproximacion(Seleccion_Numero)
elif Seleccion_algoritmo == 3:
  busquedaBinaria(Seleccion_Numero)
else:
  print('Opcion no valida.')