#funciones 

def suma(a, b): #suma es el nombre(parámetro) de la función y a, b son los argumentos.
    return a + b #esto es el cuerpo y podemos añadir aqui lo que ara si llamamos a la función.
 
 #aqui lo llamamos, es importante el orden.
     
resultado = suma(2, 3) # suma es el nombre de la funcion, 2 y 3 son los argumentos. 

print (resultado) #si lo imprimimos daria "5".

 

#argumentos de palabra clave.



def saludar(nombre, mensaje):
    print(f"{mensaje}, {nombre}!")

saludar(nombre="Juan", mensaje="Hola")#aqui se especifica el nombre del parámetro junto con el argumento, aqui no importa el nombre.



#argumentos de variable, lo que hacen es acepat un número variable de argumentos(cuantos se necesiten).



#argumentos de variable de posición, guarda los argumentos en forma de tupla.



#se usa un * en el argumento.
def sumar(*números):
    total = 0 #aqui se ira almacenando los números.
        #con (for) se crea una variable llamada número.
    for número in números: #aqui lo que hace es revisar todos los argumentos (*número) y lo guarda en número.
        total += número #aqui suma +1 a cada numero que va a ir mirando el bucle.
         
    return total # se termina el bucle.

resultado = sumar( 1, 2, 3, 4, 5) 
print(resultado)
#l resultado es 15.
 


#argumentos de variable de palabra clave.
#guarda los argumentos en forma de dicionarios.

 

def imprimir_detalles(**kwargs): #se utiliza **kwargs en el argumentos.
    for clave, valor in kwargs.items():#aqui con .items se da el formato y la clave se guarda en la variable clave y el valor en la variable valor. 
        print(f"{clave}: {valor}") #aqui simplemente lo imprimimos.

#y si añadimos estos argumentos.          
imprimir_detalles(nombre="Juan", edad=30, ciudad="Madrid")

#nos devuelve esto. 

# nombre: Juan
# edad: 30
# ciudad: Madrid

