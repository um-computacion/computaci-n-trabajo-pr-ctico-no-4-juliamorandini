def fibonacci_recursivo(n: int) -> int:
    if n < 0:
        raise ValueError("La secuencia de Fibonacci no se puede hacer con números negativos")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

def fibonacci_iterativo(n: int) -> int:
    if n < 0:
        raise ValueError("La secuencia de Fibonacci no se puede hacer con números negativos")
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b