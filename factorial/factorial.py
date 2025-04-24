#de forma recursiva 
def factorial_recursivo(n: int) -> int:
    if n < 0:
        raise ValueError("El factorial no funciona con numeros negativos")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursivo(n - 1)
#de forma iteariva con while (puede hacerse con un for de otra forma)
def factorial_iterativo(n: int) -> int:
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    total = 1
    while n > 0:
        total *= n
        n -= 1
    return total