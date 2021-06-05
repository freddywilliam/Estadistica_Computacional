import sys, time
def fibonacci_recursivo(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

def fibonacci_dinamico(n, memo = {}):
    if n == 0 or n == 1:
        return 1
    
    try:
        return memo[n]
    except KeyError:
        resultado = fibonacci_dinamico(n - 1, memo) + fibonacci_dinamico(n - 2, memo)
        memo[n] = resultado

        return resultado

def run():
    n = int(input('Escoge numero: '))

    t1 = time.time()

    resultado = fibonacci_recursivo(n)
 
    t2 = time.time()
    
    resultado_di = fibonacci_dinamico(n)

    t3 = time.time()

    total_uno = round(t2 - t1, 10) 
    total_dos = round(t3 -t2, 10)

    print('Recursivo: ' + str(resultado) + ' Tiempo: ' + str(total_uno))
    print('Dinamico: ' + str(resultado_di) + ' Tiempo: ' + str(total_dos))
if __name__ == '__main__':
    run()
   