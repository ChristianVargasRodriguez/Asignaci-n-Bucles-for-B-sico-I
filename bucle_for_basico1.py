# Básico: imprime todos los números enteros del 0 al 150.

for num in range(151):
    print(num)

print("*" * 50)
# Múltiplos de cinco: imprime todos los múltiplos de 5 entre 5 y 1,000.
for mult_5 in range(5, 1005):
    if (mult_5 % 5 == 0):
        print(mult_5)

print("*" * 50)
# Contar, a la manera del Dojo: imprime números enteros del 1 al 100. Si es divisible por 5,
#  imprime "Coding” en su lugar. Si es divisible por 10, imprime "Coding Dojo".
for contar_dojo in range(1, 101):
    if contar_dojo % 10 == 0:
        print("Coding Dojo")
    elif contar_dojo % 5 == 0:
        print("Coding")
    else:
        print(contar_dojo)

print("*" * 50)
# Whoa. Es un gran idiota: 
# agrega los enteros impares del 0 al 500,000, e imprime la suma final.
impares = []
for impar in range(500000):
    if impar % 2 != 0:
        impares.append(impar)
print(sum(impares))

print("*" * 50)
# Cuenta regresiva de a 4: imprime números positivos 
# comenzando desde el 2018, en cuenta regresiva de 4 en 4.
for regresiva_en_4 in range(2018, 0, -4):
    print(regresiva_en_4)

print("*" * 50)
# Contador flexible: establece tres variables: lowNum, highNum, mult. Comenzando en
# lowNum y pasando por highNum, imprime solo los enteros que sean múltiplos de mult.
# Por ejemplo, si lowNum=2, highNum=9 y mult=3. El bucle debe imprimir 3, 6, 9 (en líneas sucesivas). 

def contar_flexible(lowNum, highNum, mult):
    for resultado in range(lowNum, highNum +1):
        if resultado % mult == 0:
            print(resultado)

contar_flexible(2, 9, 3)