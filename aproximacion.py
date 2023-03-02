objetivo = int(input('Escoge un numero: '))
epsilon = 0.1
paso = epsilon**2
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo: 
    print(abs(respuesta**2 - objetivo), respuesta)
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No encontramos la raiz cuadrada de {objetivo}')
else:
    print(f'La raiz cuadrada del {objetivo} es {respuesta}')

#Abs significa valor absoluto, es decir un valor siempre positivo.
#mientras (2) sea >= 0.1 Y 0 <= 2:
#while {2,01} Y {0,2}
#imprime 2, 0
# Respuesta += 0.01
#Siguiente bucle.
#mientras 1.9999 sea >= 0.1 Y 0.01 <= 2:

#Mientras (0.01**2 - 2)
#Si 0 - 2 Es mayor que 0.1 imprime.
