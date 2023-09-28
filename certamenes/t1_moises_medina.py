from random import randint

programa = True
while programa is True:

    numeros_correctos = []
    for x in range(1,8):
        while True:
            n_aleatorio = randint(1,7)
            if n_aleatorio not in numeros_correctos:
                numeros_correctos.append(n_aleatorio)
                break
    
    def check(b):
        estado_check = False
        if b > 20 or b < 0:
            print("El numero tiene que estar entre 0 y 20")
        elif b in numeros_elegidos:
            print("Eliga un numero no repetido")
        else:
            estado_check = True
            return estado_check


    print(numeros_correctos)
    n = 1
    numeros_elegidos = []
    for y in range(0,7):
        while True:
            estado_check = False
            if n == 7:
                numero = int(input("Comodin: "))
            else:
                numero = int(input(f"Numero {n}: "))
                
            estado_check = check(numero)
            if estado_check is True:
                numeros_elegidos.append(numero)
                n += 1
                break


    comodin = numeros_elegidos[-1]
    numeros_elegidos.pop(-1)
    cont_0 = 0

    for z in numeros_elegidos:                               ### for z es el index no el elemento como tal haciendo que elimine solo la mitad de la lista :O 
        if z in numeros_correctos:
            numeros_elegidos.remove(z)
            numeros_elegidos.insert(0,0)
            cont_0 += 1
            numeros_correctos.remove(z)
    
    for z in range(0,cont_0):
        numeros_elegidos.remove(0)
    print(numeros_elegidos)

    if comodin in numeros_correctos:
        ec = True
        numeros_correctos.remove(comodin)
    elif len(numeros_correctos) == 1:
        ec = False
        if comodin < numeros_correctos[0]:
            mayor_menor = "mayor"
        else:
            mayor_menor = "menor"
    else:
        ec = False

    
    if len(numeros_correctos) == 1 and ec == False:
        comodin = int(input(f"""Felicidades!!!, Acertaste en todas excepto en el comodin, tiene permitido cambiarlo.
(Pista: el numero es {mayor_menor} a {comodin})
Comodin: """))
        if comodin == numeros_correctos[0]:
            numeros_correctos.remove(comodin)

    elif len(numeros_correctos) > 1 and ec == False:
        numeros_elegidos.sort()
        print(f"""Se equivoco en los numeros {numeros_elegidos} y en el comodin {comodin}, tiene permitido cambiar el menor numero sin contar el comodin.
en este caso el numero {numeros_elegidos[0]}""")



    if len(numeros_correctos) == 0:
        print("Has ganado la loteria!!!!, su premio es de 50.000.000$")
        programa = False
