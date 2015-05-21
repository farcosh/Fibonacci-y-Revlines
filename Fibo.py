#Metodo para multiplicar dos matrices
def multiplica_matriz(A, B):
    resultado = [
        [0, 0],
        [0, 0]]
    resultado[0][0] += (A[0][0] * B[0][0]) + (A[0][1] * B[1][0])
    resultado[0][1] += (A[0][0] * B[0][1]) + (A[0][1] * B[1][1])
    resultado[1][0] += (A[1][0] * B[0][0]) + (A[1][1] * B[1][0])
    resultado[1][1] += (A[1][0] * B[0][1]) + (A[1][1] * B[1][1])
    return resultado
  
#Metodo que hace la multiplicacion esponencial de la matriz, donde:
#B es la matriz recibida
#n es el exponente al que esta elevado
def exp(n , B):
    if n == 0:
        return 0
    if n == 1:
        return B
    if n % 2 == 1:
        n = n - 1
        return multiplica_matriz(exp(n,B), B)
    else:
        n = n / 2
        C = exp(n,B)
        return multiplica_matriz(C, C)

#Metodo el cual definimos la matriz que codifica a fibonacci
#y llamamos el metodo "exponencial"
def Llamada(n):
    B = [[1, 1],[1, 0]]
    if n == 0:
        return 1
    M = exp(n,B)
    return M[0][0]

#Metodo que da el valor de fibonacci
def Fibo(n):
    print("El de digitos en Fibonacci de " + str(n) + " es:")
    if n == 0:
        return 0
    n -= 1
    return Llamada(n)
  
#Pedimos al usuario que ingrese el indice que desea calcular
n = int(input("Introduzca el indice de Fibonacci a calcular: "))

#Imprimimos la cantidad de digitos  
print(len(str(Fibo(n))))
