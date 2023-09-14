################ 1. Hervidor ################ 
from random import randint
rn = randint(18,25)
while rn < 94:
    rn += 2
    print(f"Temperatura = {rn}")
print("El cafe esta en la temperatura optima")

################ 2. Plan de Telefonia Movil ################ 
pc = round(float(input("Ingrese el costo mensual del plan en pesos chilenos: ")),2)
Meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
ca = 0
for sm in Meses:
    if sm == "Marzo" or sm == "Septiembre":
        ca += pc + 1700
    else:
        ca += pc
    
print(f"Su costo anual es de {ca}")

################ 3. Serie ################ 
se = float(input("Ingrese el numero con el que iniciar la serie: "))
F = []
while True:
    F.append(se)
    if se == 1:
        break
        
    elif se % 2 == 0:
        se = se/2
    
    elif se % 2 == 1:
        se = 3*se+1
print(F)

################ 4. Usuarios ################
numeros = ("0123456789")
l4 = True
f = False
wc = ["$","#","%","&","/"]
while l4 is True:
    l41 = True
    while l41 is True:
        u = input("Ingrese su usuario: ")
        e = input("Ingrese su e-mail: ")
        if "@" not in e:
            print("Error: e-mail no valido")
        else:
            l41 = False
            
    e = e.split("@")
    e = e[0]
    if e == u:
        print("Error: El usuario y e-mail son iguales, por favor ingrese otro.")
    else:
        l4 = False

while True:
    Tnum = False
    c = input("""(Recuerde: La contraseña tiene que tener minimo 8 caracteres y no simbolos especiales)
Ingrese su contraseña: """)
    for z in c:
        if z in numeros:
            Tnum = True
    
    if Tnum is True:
        if len(c)<8:
            print("Error: Minimo 8 caracteres ")
        else:
            f = False
            for ws in wc:
                if ws in c:
                    f = True 
            if f == True:
                print("Error: Caracter invalido")
            elif f == False:
                break 
    else:
        print("Error: Minimo tiene que tener un numero")

print("Se ha registrado!!!!  :D")


################ 5. Pantalla ################
s=int(input("""(Recomendado ingresar una escala entre 1 y 5)
Ingrese la escala: """))
loop = True
while loop is True:
    
    #--Imprime los numeros linea por linea--#
    def printing():
        for b_1 in range(0,len(A[0])):
            B = []
            for b_2 in range(0,len(A)):
                B.append(A[b_2][b_1])
            P_B = " "
            for b_3 in range(0,len(B)):
                P_B += ("".join(B[b_3]) + "  ")
            
            print(P_B)

    #--Opciones y Dibujo de numeros--#
    def op():
        if n == 0:
            D[int(len(D)/2)][1] = " "

        elif n == 1:
            for n1_0 in range(0,len(D)):
                D[n1_0][0] = " "
            for n1_1 in range(0,len(D),s+1):
                D[n1_1][1] = s*" "

        elif n == 2:
            for n2_0 in range(1,int(len(D)/2)):
                D[n2_0][0] = " "
            for n2_3 in range(int(len(D)/2),len(D)-1):
                D[n2_3][2] = " "

        elif n == 3:
            for n3_0 in range(0,len(D)):
                D[n3_0][0] = " "

        elif n == 4:
            for n4_0 in range(int(len(D)/2),len(D)-1):
                D[n4_0][0] = " "
            for n4_1 in range(0,len(D),len(D)-1):
                D[n4_1][1] = s*" "

        elif n == 5:
            for n5_0 in range(int(len(D)/2),len(D)-1):
                D[n5_0][0] = " "
            for n5_2 in range(1,int(len(D)/2)):
                D[n5_2][2] = " "

        elif n == 6:
            for n6_2 in range(1,int(len(D)/2)):
                D[n6_2][2] = " "

        elif n == 7:
            for n7_0 in range(0,len(D)):
                D[n7_0][0] = " "
            for n7_1 in range(int(len(D)/2),len(D),s+1):
                D[n7_1][1] = s*" "

        elif n == 9:
            for n9_0 in range(int(len(D)/2),len(D)-1):
                D[n9_0][0] = " "

        else:
            loop = False


    #--Codigo base--#
    k = str(input("""(Escriba "end" para salir del loop)
Ingrese cualquier numero: """))
    if k == "end":
        break
    A = []
    for n in k:
        n=int(n)
        D =   [[" ",s*"-"," "],
               ["|",s*" ","|"],
               [" ",s*"-"," "],
               ["|",s*" ","|"],
               [" ",s*"-"," "]]

        for i in range(1,s):
            D.insert(1,["|",s*" ","|"])
            D.insert(-1,["|",s*" ","|"])

        op()
        A.append(D)
    printing()