Persona_1 = input('Dime tu nombre: ')
Persona_2 = input('Dime tu nombre p2: ')

Edad_Persona_1 = int(input(f'{Persona_1} Dime tu edad: '))
Edad_Persona_2 = int(input(f'{Persona_2} Dime tu edad: '))

if Edad_Persona_1 > Edad_Persona_2:
    print(f'{Persona_1} Con {Edad_Persona_1}  de edad, es mayor que {Persona_2} que tiene {Edad_Persona_2} Anos')
elif Edad_Persona_2 > Edad_Persona_1:
    print(f'{Persona_2} Con {Edad_Persona_2}  de edad es mayor que {Persona_1} que tiene {Edad_Persona_1} Anos')
else:
    print(f'{Persona_1} y {Persona_2} Tienen la misma edad')