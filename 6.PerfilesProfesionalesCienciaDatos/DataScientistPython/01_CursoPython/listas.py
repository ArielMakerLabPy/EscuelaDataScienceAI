to_do = ["Dirigirnos al hotel",
         "Ir a almorzar",
         "Visitar un museo",
         "Volver al hotel"]
print(to_do)

numbers = [1, 2, 3, 4, "cinco"]
print(type(numbers))

print(numbers)
print(len(numbers))

print("Quinto elemento:", numbers[4])
print("Ultimo elemento:", numbers[-1])
print("Rango de elementos:", numbers[1:3])
print("Rango de elementos desde la posición 0:",
      numbers[:4])
print(numbers)
numbers.append(False)
print(numbers)

numbers.insert(3, 3.5)
print(numbers)

print(numbers.index(False))

del numbers[5:]
print(numbers)

a = [1, 2, 3, 4, 5]
b = a
print(a)
print(b)
del a[0]
print(id(a))
print(id(b))

c = a[:]
print(id(a))
print(id(b))
print(id(c))

a.append(6)
print(a)
print(b)
print(c)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)