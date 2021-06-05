import sys, time

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

    sys.setrecursionlimit(10002)

    n = int(input('Escoge numero: '))

    t1 = time.time()
    
    resultado_di = fibonacci_dinamico(n)

    t2 = time.time()

    total_uno = round(t2 - t1, 10)     
    print('Dinamico: ' + str(resultado_di) + ' Tiempo: ' + str(total_uno))

if __name__ == '__main__':
    run()
   