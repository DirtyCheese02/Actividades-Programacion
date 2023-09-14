## 1. Inversion de lista
A = [1,2,3,4,5,6,7,8,9,10]
for i in range(1,len(A)+1):
    A.append(A[len(A)-i])
    A.pop(len(A)-i-1)
print(A)

## 2. Eliminacion de duplicados
B = [1,2,2,3,2,4,4,3,2,5,0,2,1,5,0]
C = []
for z in B:
    if z not in C:
        C.append(z)
print(C)

## 3. Listas Anidadas y matrices
M = [[5,2,3],
     [4,10,6],
     [7,8,15]]
Suma = 0
for x in range(0,len(M[1])):
    Suma = Suma + M[x][x]
print(Suma)