# Funciones y manejo de excepciones en python

def greet():
    print('Hola Mundo')
    
greet()


def greet_2(name):
    print('Hola',name)


greet_2('Ariel')
greet_2('Pedro')


def greet_full(name, last_name):
    print('Hola', name, last_name)
    
greet_full('Ariel', 'Martínez')

def greet_full_2(name, last_name='No agregó su apellido'):
    print('Hola', name, last_name)

greet_full_2('Ariel')
greet_full(last_name='Martínez', name='Pedro')

def add(a, b):
    return a+b

def substrate(a,b):
    return a - b

def multiply(a, b):
    return a*b

def divide(a,b):
    return a/b

def calculator():
    while True:
        print('Seleccione una operación')
        print('1. Suma')
        print('2. Resta')
        print('3. Multiplicación')
        print('4. División')
        print('5. Salir')
        
        option = input('Ingrese su opción (1,2,3,4,5): ')
        
        if option =='5':
            print('Saliendo de la calculadora')
            break
            
        if option in ['1','2','3','4']:
            num1 = float(input('Ingrese el primer numero: '))
            num2 = float(input('Ingrese el segundo numero: '))
            
            if option == '1':
                print('La suma es: ', add(num1, num2))
            elif option == '2':
                print('La resta es: ', substrate(num1, num2))
            elif option == '3':
                print('La multiplicación es: ', multiply(num1, num2))
            elif option == '4':
                print('La división es: ', divide(num1, num2))
        else:
            print('Opción no válida, por favor intenta de nuevo')

calculator()


suma = lambda a, b: a + b
print(suma(10, 4))

multiplicacion = lambda a, b: a * b
print(multiplicacion(10, 4))

#Cuadrado de cada numero
numeros = range(11)
cuadrado_numeros = list(map(lambda x: x**2, numeros))
print('Cuadrados', cuadrado_numeros)

#Pares
numeros_pares = list(filter(lambda x: x%2 == 0, numeros))
print('Pares de los numeros hasta 10', numeros_pares)


