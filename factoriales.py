
def factorial(n):
    """ Calcula el factorial de n.

        n int>0
        returns n!
        n es un entero que es mayor que 0, regresa n factorial.
    """
    print(n)
    if n == 1:  
        return 1
    
    return n * factorial(n - 1)

n = int(input('Escribe un numero entero: '))

print(f'El resultado de tu numero factorial es : {factorial(n)}')
    
    