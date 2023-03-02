def fibonacci(n):
    print(n)
    if n==0 or n==1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input('Escribe un numero para ver la sucesion de fibonacci: '))

print(f'el numero siguiente en la sucesion de fibonacci para {n} es {fibonacci(n)}')