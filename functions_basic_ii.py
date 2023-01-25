# Cuenta regresiva: crea una función que acepte un número como entrada. Devuelve una lista nueva que cuente de uno en uno, desde el número (como elemento 0) hasta 0 (como último elemento). 
# Ejemplo: countdown(5) debería devolver [5,4,3,2,1,0]

def countdown(number):
    lista_regresiva =[]
    for i in range(number, -1, -1):
        lista_regresiva.append(i)
    return lista_regresiva

print(countdown(6))

# Imprimir y devolver: crea una función que reciba una lista con dos números. Imprime el primer valor y devuelve el segundo.
# Ejemplo: imprimir_y_devolver([1,2]) debe imprimir 1 y devolver 2

def imprimir_y_devolver(dosnumeros):
    print(dosnumeros[0])
    return (dosnumeros[1])

print(imprimir_y_devolver([1, 2]))

# Primero más longitud: crea una función que acepte una lista y devuelva la suma del primer valor de la lista, más la longitud de la lista.
# Ejemplo: primero_mas_longitud([1,2,3,4,5]) debe devolver 6 (primer valor: 1 +length: 5)

def primero_mas_longitud(lista_con_n_num):
    return lista_con_n_num[0] + lista_con_n_num[(len(lista_con_n_num)-1)]


print(primero_mas_longitud([1,2,3,4,5]))

# Valores mayores que el segundo: escribe una función que acepte una lista y cree una nueva que contenga solo los valores de la lista original que sean mayores que su segundo valor. Imprime cuántos valores son y luego devuelve la lista nueva. Si la lista tiene menos de 2 elementos, has que la función devuelva False
# Ejemplo: valores_mayores_que_el_segundo([5,2,3,2,1,4]) debe imprimir 3 y devolver [5,3,4]
# Ejemplo: valores_mayores_que_el_segundo([3]) debe devolver False

def valores_mayores_que_el_segundo(lista_cualquiera):
    if len(lista_cualquiera) < 2:
        return False
    lista_a_devolver = []
    for i in range(len(lista_cualquiera)):
        if lista_cualquiera[i] > lista_cualquiera[1]:
            lista_a_devolver.append(lista_cualquiera[i])
    print("Cantidad de valores:", len(lista_a_devolver))
    return lista_a_devolver

print(valores_mayores_que_el_segundo([5,2,3,2,1,4]))
print(valores_mayores_que_el_segundo([3]))

# Esta longitud, ese valor: escribe una función que acepte dos enteros como parámetros: tamaño y valor. La función debe crear y devolver una lista cuya longitud sea igual al tamaño dado, y cuyos valores sean todos el valor dado.
# Ejemplo: length_and_value(4,7) debe devolver [7,7,7,7]
# Ejemplo: length_and_value(6,2) debe devolver [2,2,2,2,2,2]

def length_and_value(largo, valor):
    devuelve = []
    for i in range (largo):
        devuelve.append(valor)
    return devuelve

print(length_and_value(4,7))
print(length_and_value(6,2))