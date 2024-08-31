x1 = 5

if x1 > 5:
    print('x es mayor que 5')
elif x1 == 5:
    print('x es igual a 5')
else:
    print('x es menor')

print('Fuera de if')
    
x2 = 15
y2 = 20

if x2>10 and y2>25:
    print('x2 es mayor que 10 y y2 es mayor que 25')

if x2>10 or y2>25:
    print('x2 es mayor que 10 o y2 es mayor que 25')
    
if not x2>10:
    print('x2 no es mayor que 10')
    
is_member = False
age = 15

if is_member:
    if age>=15:
        print('Tienes acceso ya que eres miembro y mayor o igual a 15 años')
    else:
        print('No tienes acceso ya que eres miembro pero menor a 15 años')
else:
    print('No eres miembro y NO TIENES ACCESO')
    
