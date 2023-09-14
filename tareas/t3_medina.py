## 1. Validacion de palindromos 
Palabra = input("Ingrese la palabra: ")
count = 0
for x in range(0,len(Palabra)-1):
    if Palabra.lower()[x] == Palabra.lower()[-1-x]:
        count += 1
if count == len(Palabra)-1:
    print("Es un polindromo")
else:
    print("No es un polindromo")

## 2. Contador de vocales 
Palabra2 = input("\nIngrese la palabra para contar las vocales: ")
Vocal = "aeiou"
Vocales = 0
for c in Palabra2.lower():
    if c in Vocal:
        Vocales += 1
print(f"La palabra tiene {Vocales} vocales")

## 3. Contraseña aleatoria
from random import randint
a = "abcdefghijklmnopqrstuvwxyz"
b = "1234567890"
d = "!@#$%^&*" 
c = int(input("\nCuantos caracteres quiere que tenga su contraseña aleatoria: "))
Ps = ""

for p in range(0,c):
    Serie1 = randint(0,2)
    if Serie1 == 0:                           #Serie1 selecciona si es letra, numero o simbolo
        Serie2 = randint(0,1)
        if Serie2 == 0:                       #Serie2 selecciona si es mayuscula o minuscula
            Ps = Ps + a[randint(0,len(a)-1)]
        else:
            Ps = Ps + a.upper()[randint(0,len(a)-1)]
    elif Serie1 == 1:
        Ps = Ps + d[randint(0,len(d)-1)]
    else:
        Ps = Ps + b[randint(0,len(b)-1)]

print(Ps)