## 1. Nota Final
guias = float(input("Ingrese la nota de las guias de ayudantia: "))
part = float(input("Ingrese la nota de la participacion: "))
tarea1 = float(input("Ingrese la nota de la tarea 1: "))
tarea2 = float(input("Ingrese la nota de la tarea 2: "))
nexamen = float(input("Ingrese la nota de el examen: "))
npresentacion = (guias * 0.3) + (part * 0.1) + (tarea1 * 0.3) + (tarea2 * 0.3)
nfinal = (npresentacion * 0.7) + (nexamen * 0.3)
print(f"Tu nota final es {nfinal}")
if nfinal < 4:
    print("Reprobaste")
elif nfinal > 7:
    print("Error: Numero ingresado erroneo, por favor vuelva a intentarlo. ")
else:
    print("Aprobaste")
    
## 2. Codigo Morse
n1 = int(input("Ingrese el primer numero de 3 digitos: "))
n2 = int(input("Ingrese el segundo numero de 3 digitos: "))
Trad = str(n1 + n2)
for digit in Trad:
    if digit == "0":
        print("-----")
    if digit == "1":
        print(".----")
    if digit == "2":
        print("..--")
    if digit == "3":
        print("...-")
    if digit == "4":
        print("....-")
    if digit == "5":
        print(".....")
    if digit == "6":
        print("-....")
    if digit == "7":
        print("--..")
    if digit ==("8"):
        print("---.")
    if digit ==("9"):
        print("----.")

## 3. Pago Credito Internacional
monto=float(input("ingrese el monto de la compra: "))
cantidad=int(input("ingrese la cantiad de articulos comprados"))
if monto > 250000:
    impuesto=0.017
elif 100000 <= monto <= 250000:
    impuesto=0.025
else:
    impuesto=0.03
if cantidad >=15:
    articulo=0.002
elif 10 <= cantidad <15:
    articulo=0.003
else:
    articulo=0.004
total= round((impuesto+articulo)*monto,3)
print("El monto a pagar por el uso será de $", (total))

## 4. Calidad del aire 
np = float(input("Ingrese el nivel de particulas PM2.5 del aire: "))
if 0 <= np <= 12:
    print("Calidad de aire excelente")

elif 12 < np <= 35.4:
    print("Calidad de aire buena")
    
elif 35.4 < np <= 55.4:
    print("Calidad de aire moderada")

elif 55.4 < np <= 150:
    print("Calidad de aire regular")
    
elif 150 < np <= 250:
    print("Calidad de aire mala")
    
elif np >= 250:
    print("Calidad de aire peligrosa")
    
## 5. Triangulo Rectangulo 
ladoA=float(input("ingrese el primer lado: "))
ladoB=float(input("ingrese el segundo lado: "))
ladoC=float(input("ingrese el tercer lado: "))
if ladoA>=ladoB and ladoA>=ladoC:
    ladomayor=ladoA
elif ladoB>=ladoA and ladoB>=ladoC:
    ladomayor=ladoB
else:
    ladomayor=ladoC
print("el lado mayor es ",(ladomayor))
if ladoA**2+ladoB**2==ladomayor**2:
    print("es un triangulo rectangulo")
elif ladoC**2+ladoB**2==ladomayor**2:
    print("es un triangulo rectangulo")
elif ladoA**2+ladoC**2==ladomayor**2:
    print("es un triangulo rectangulo")
else:
    print("No es un triangulo rectangulo")

## 6. Cajero Automatico 
print("Hola bienvenido a tu cajero automatico :D")
Saldo = 10000
a = True
while a is True:
    OA = input("""Indique que quiere hacer: 
    1. Consultar saldo
    2. Retirar dinero
    3. Salir
    """)
    if OA == "1":
        print(f"""Su saldo es de {Saldo} pesos
        """)
    if OA == "2":
        retiro = float(input(f"Recuerde, su saldo es de {Saldo} pesos, Cuanto desea retirar? "))
        Saldo = Saldo - retiro
        if Saldo < 0:
            print("""Error: no puedes retirar el dinero, no tienes suficiente
            """)
            Saldo = Saldo + retiro
        else:
            print(f"""Su nuevo saldo es de {Saldo}
            
            """)
    if OA == "3":
        a = False
    
    
