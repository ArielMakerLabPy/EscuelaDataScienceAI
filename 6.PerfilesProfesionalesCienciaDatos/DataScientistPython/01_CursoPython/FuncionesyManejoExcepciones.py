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
        print('Seleccione')