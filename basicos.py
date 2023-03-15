#variables.


# Definimos la variable 'edad' y le asignamos el valor de 25.
edad = 25

#si es un string(letras) hay que poner "__".
edad_letra = "veinticinco"

# Imprimimos el valor de la variable 'edad'.
print(edad)




#operadores.


# programa para sumar, también se puede múltiplicar y dividir.
sum = 1 + 2
print(sum)

#resta.
resta = 1 - 2
print (resta)

#división.
div = (15/3)
print = (resta)
 
#miltiplicacion.
a = 2
b = 3
c = a * b

print(c)  # Salida: 6.




#input: con el podemos pedir informacion al usuario.

nombre = input("¿Cuál es tu nombre? ")
print("Hola, " + nombre + "!")




#if, elif y else: son estructuras de control de flujo en Python que nos permiten ejecutar diferentes bloques de código en función de ciertas condiciones.


# Pedimos al usuario que ingrese su nombre.
nombre = input("Por favor, ingrese su nombre: ")

# Pedimos al usuario que ingrese su edad.
edad = int(input("Por favor, ingrese su edad: "))

# Imprimimos el nombre ingresado por el usuario en la consola.
print("Hola, " + nombre + "!")

# Utilizamos una estructura de control if-elif-else para evaluar la variable 'edad'.
if edad < 18:
    print("Eres menor de edad.")
elif edad >= 18 and edad < 65:
    print("Eres mayor de edad.")
else:
    print("Eres jubilado.")




#listas: sirven para almacenar datos dentro de variables.
 

#hemos creado una lista.
numeros = [1, 2, 3, 4, 5]
print(numeros)

#ahora veremos algunos metodos.

#se utiliza para obtener la longitud de una lista.
lista = [1, 2, 3, 4, 5]
print(len(lista))  # Salida: 5.

#Indexación: Se puede acceder a los elementos de una lista, con la posicion, la primera posicion es el 0.
lista = [1, 2, 3, 4, 5]
print(lista[0])  # Salida: 1.
print(lista[2])  # Salida: 3.

#Slicing: se ua para obtener el inicio y fin.
lista = [1, 2, 3, 4, 5]
print(lista[1:4])  # Salida: [2, 3, 4].

#append(): Este método se utiliza para agregar un elemento al final de una lista.
lista = [1, 2, 3]
lista.append(4)
print(lista)  # Salida: [1, 2, 3, 4].

#insert(): Eeste metodo se utiliza para insertar un elemento en una posición específica de una lista.
lista = [1, 2, 3]
lista.insert(1, 4)
print(lista)  # Salida: [1, 4, 2, 3].

#pop(): Este metodo se utiliza para eliminar un elemento de una lista.
lista = [1, 2, 3, 4, 5]
lista.pop(2)
print(lista)  # Salida: [1, 2, 4, 5].

#sort(): Este metodo se utiliza para ordenar los elementos de una lista en orden ascendente.
lista = [4, 1, 3, 5, 2]
lista.sort()
print(lista)  # Salida: [1, 2, 3, 4, 5].





#diccionarios: sirven para almacenar datos pero esos datos tienen valores, osea dentro de ellos hay mas datos.

#creamos un diccionario.
diccionario = {
'clave1': 'valor1',
'clave2': 'valor2',
'clave3': 'valor3'}

#si clave1 esta en diccionario
if 'clave1' in diccionario:
   #imprime esto
   print("si esta en la lista")


#creamos una variable, y dentro hay una lista de todos los valores del diccionario
lit_val_dicc = list(diccionario.values())

#imprimimos la lista de los valores del diccionario
print (lit_val_dicc)




#funciones 
nombre = input("¿Cómo te llamas?")
def saludar():
    print("¡Holaaa ", nombre, ", ¿qué tal todo? ¿Cómo vas, guapetón?..")

saludar() #esto hara que imprima un saludo con tu nombre
