#Creación de una lista:
lista = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]

#Añadir un elemento al final de la lista:
lista.append(6)

#Insertar un elemento en una posición específica:
lista.insert(2, 'nuevo elemento')

#Eliminar el primer elemento de la lista:
lista.pop(0)

#Eliminar el último elemento de la lista:
lista.pop()

#Eliminar un elemento por su valor:
lista.remove(3)

#Ordenar una lista en orden ascendente:
lista.sort()

#Invierte el orden de los elementos de una lista:
lista.reverse()

#Ordenar una lista en orden descendente:
lista.sort(reverse=True)

#Obtener la longitud de una lista:
len(lista)

#Obtener el índice de un elemento:
lista.index(4)

#agrega elementos de una lista a otra lista:
lista.extend(lista2)

#Elimina todos los elementos de una lista.
lista.clear()
