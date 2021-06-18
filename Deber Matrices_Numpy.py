#!/usr/bin/env python
# coding: utf-8

# In[7]:



import numpy as np

print("--------------Multiplicacion de Matrices----------------")
print("Nota* El numero de columnas de A tiene que coincider con el numero de filas de B")
print()

# Definir la fila Matriz A
print("=========Matriz A=========")
print()
print("==========================")
filA= input("Introduce el numero de filas: ")

while filA.isalpha():

    filA= input("Introduce nuevamente el numero de filas: ")

print("==========================")
print()
#======================================================================

#Definir la columna Matriz A
print("==========================")

columA= input("Introduce el numero de columnas: ")

while columA.isalpha():

    columA= input("Introduce nuevamente el numero de columnas: ")

print("==========================")

# Convertir datos Matriz A en Type:Int
filA = int(filA)
columAT = columA
columA = int(columA)

print()
#==========================================================================

# Ingreso de Datos
print("===============Ingrese los datos================")

matrizA = np.zeros([filA, columA])

for i in range(filA):
    for j in range(columA):
        dato = int(input("Fila {}, Columna {} : ".format(i+1, j+1)))
        matrizA[i,j] = dato



print("================================================")
#=============================================================================


#Ingresar fila Matriz B

print("=========Matriz B=========")
print()
print("==========================")
filB= input("Introduce el numero de filas: ")
    
while True:
    
    if(filB == columAT):
        break
    filB= input("Introduce nuevamente el numero de filas: ")

print("==========================")
print()
#=================================================================================

#Ingresar columna B

print("==========================")

columB= input("Introduce el numero de columnas: ")

while columB.isalpha():

    columB= input("Introduce nuevamente el numero de columnas: ")

print("==========================")

#=====================================================================

#Transformar los datos Matriz B a type:Int
filB = int(filB)
columB = int(columB)
print()

#====================================================================

#Ingresar datos
print("===============Ingrese los datos================")
matrizB = np.zeros([filB, columB])

for i in range(filB):
    for j in range(columB):
        dato = int(input("Fila {}, Columna {} : ".format(i+1, j+1)))
        matrizB[i,j] = dato

print("================================================")

#=============================================================================


#=============================================================================


#Imprimir      
print("===============Matriz A===========")

print(matrizA)
    
print("==================================")
print()

print("===============Matriz B===========")

print(matrizB)
    
print("==================================")
print()

#Multiplicacion

matrizR = np.dot(matrizA,matrizB)


            
#=============================================================================

print()
print("===============Matriz Resultante===========")

print(matrizR)
    
print("============================================")
print()



# ## 

# In[ ]:




