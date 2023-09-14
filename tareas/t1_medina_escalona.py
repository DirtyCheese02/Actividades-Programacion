## 1. Factorial de un numero 
NF = int(input("Ingrese un numero entero y positivo: "))
e=1
if NF < 0:
    print("Error: Ingrese un numero positivo")
else:
    for i in range(1,NF+1):
        e = e * i
    print(e)

## 2. Secuencia de Fibonacci 
Terminos = int(input("Ingrese la cantidad de terminos que desea ver: "))
s = 0
w = 1
if Terminos < 0:
    print("Error: Ingrese un numero positivo")
else:
    for l in range(0,Terminos):
        d = s + w 
        s = w 
        w = d
        print(d)
        
## 3. Numeros primos en un rango 
I = int(input("Ingrese el numero inicial: "))
F = int(input("Ingrese el numero final: "))
contador = 0
restas = 0
for rango in range(I,F+1):
    for division in range(1,rango+1):
        if rango % division == 0:
            restas = restas + 1
    if restas == 2:
        contador = contador + 1
    restas = 0
print(contador)

