## 1. Conversion a dolar 
Pesos = float(input("Ingrese el monto en pesos el cual desea convertir a dolar: "))
Dolar = 0.0012 * Pesos
print(f"La cantidad de dolares es de: {Dolar}")

## 2. Inversion de numeros
N1 = int(input("Ingresa el numero de tres digitos que desea invertir: "))
N2 = (N1//1)%10
N3 = (N1//10)%10
N4 = (N1//100)%100
print(f"El numero invertido es: {str(N2)+str(N3)+str(N4)}")

## 3. Repeticion
Palabra = input("Ingrese la palabra a repetir: ") + " "
Repeticion = int(input("Ingrese la cantidad de repeticiones: "))
print(Repeticion * Palabra)

## 4. Perimetro y area
import math
Radio = float(input("Indique el radio del circulo: "))
Perimetro = round(math.pi * Radio * 2,2)
Area = round(math.pi * Radio ** 2,2)
print(f"""El perimetro del circulo es: {Perimetro}
El area del circulo es: {Area}""")    

## 5. Mascotas
GP = 12482679
P = 8306650
C = 4176029
Pcat = round(((C/GP)*100),2)
Pdog = round(((P/GP)*100),2)
Chip = int((GP)*(100-27)/100)
print(f"De todas las mascotas con dueño, el porcentaje de perros  es {Pdog}% y el de gatos es {Pcat}%, Ademas, {Chip} de gatos y perros no tienen microchip y no estan inscritos.")

## 6. Hamburguesas
Clasica = int(input("Cuantas hamburguesas clasicas quiere? "))
Italiana = int(input("Cuantas hamburguesas italianas quiere? "))
Vegana = int(input("Cuantas hamburguesas veganas quiere? "))
Precio = (4600 * Clasica) + (5500 * Italiana) + (5000 * Vegana)
print(f"El costo total es de ${Precio} pesos")
