numeros = [2,3,4,5,6]

cuadrados = list(map(lambda x: x*x, numeros))

print(cuadrados)


numeros = [1,2,3,4]
cuadrados = [] # cuadrado1, cuadrados2, cuadrados3....

for x in numeros:
    cuadrados.append(x*x)

print(cuadrados)


x = 5

def funcion():
    #global x
    #x = x*2
    return x*x

print(funcion())

numeros = [1,2,3]
print(numeros)
nuevos_numeros = [10,2,3]
print(nuevos_numeros)

nuevos = []

print(nuevos)

nuevos.append(2)

nueva_lista = nuevos

print(nueva_lista)

def saludar(x):
    print(x, "hola")

funcion = saludar

funcion(3)

def cuadrado(x):
    return x*x

def cubo(x):
    return x*x*x

def aplicar(funcion, numero):
    return funcion(numero)

print(aplicar(cuadrado, 5))
