import numpy as np #para importar numpy


# Crear un array de NumPy de una lista
a = np.array([1, 2, 3, 4, 5])
print(a)  # [1 2 3 4 5]

# Crear un array de NumPy de ceros
b = np.zeros(5)
print(b)  # [0. 0. 0. 0. 0.]

# Crear un array de NumPy de unos
c = np.ones(5)
print(c)  # [1. 1. 1. 1. 1.]



# Acceder al primer elemento del array
print(a[0])  # 1

# Acceder a los elementos desde el segundo al cuarto
print(a[1:4])  # [2 3 4]

# Acceder a los elementos desde el tercero en adelante
print(a[2:])  # [3 4 5]

# Acceder a los elementos de manera inversa
print(a[::-1])  # [5 4 3 2 1]



# Sumar dos arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)  # [5 7 9]

# Multiplicar un array por un escalar
c = np.array([1, 2, 3])
print(c * 2)  # [2 4 6]

# Calcular la media de un array
d = np.array([1, 2, 3, 4, 5])
print(np.mean(d))  # 3.0

# Calcular la desviación estándar de un array
print(np.std(d))  # 1.4142135623730951

import numpy as np



# creación de una matriz 2D
matriz = np.array([[1, 2, 3], [4, 5, 6]])

# imprimir la forma de la matriz
print(matriz.shape)
# Output: 
# array([[1, 2, 3],
#        [4, 5, 6]])

# Acceder al elemento en la fila 1 y columna 2
print(matriz[1, 2])  # salida: 5

#recordar que comienza con 0



# Crear un array de 2x3x4 2 matrizes 3 filas y 4 columnas 
my_3d_array = np.array([[[1, 2, 3, 4],  [5, 6, 7, 8],[9, 10, 11, 12]],[[13, 14, 15, 16],  [17, 18, 19, 20], [21, 22, 23, 24]]])

print(my_3d_array)
#Ouput: 
#array                             
#   fila 0                      ([[[1, 2, 3, 4],
#   fila 1                         [5, 6, 7, 8],       #matriz 0
#   fila 2                         [9, 10, 11, 12]],
#                        
#                        
#   fila 0                      [[13, 14, 15, 16],
#   fila 1                      [17, 18, 19, 20],     #matriz 1
#   fila 2                      [21, 22, 23, 24]]])
                        
                    


# Acceder al elemento en la primera matriz (0), segunda fila (1) y tercera columna (2)
#recordar que se comienza con 0
print(my_3d_array[0, 1, 2])  # salida: 7
