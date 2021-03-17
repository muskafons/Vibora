cars = ['audi', 'bmw', 'subaru', 'toyota']

print(cars[0] == 'audi')

print('\n\n\n')

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

if 'bmwd' in cars:
    print('Ey YOU DOACTAR')


print('\n\n\n')

# ---------------------------------------
a = 25
b = 25

print('\n\n\n')

if a == b:
    print("Thats true suckers!!!")
else:
    print('Suck me these')


c = 23.444
d = 34.5555

if(a <= b) and (c < d):
    print('REAL MOTHERFUCKING G')

print('\n\n\n')

# ---------------------------------------
age = 45

if(age < 18):
    print('No vota la perra')
elif(age >= 18 and age <= 30):
    print('DONT SUCK my balls')
elif (age > 30):
    print('Niggaz and Blacks')
else:
    print('nuggas')

print('\n\n\n')
# ---------------------------------------
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")

if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")

if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

print('\n\n\n')
# ---------------------------------------
alien_color = 'yellow'

if(alien_color == 'red'):
    print("WIN SOME 5 points idiota")
elif(alien_color == 'green'):
    print("WIN SOME 8 points idiota")
elif(alien_color == 'yellow'):
    print("WIN SOME 16 points idiota")
else:
    print('NO ALIEN Hijo de puta')

print('\n\n\n')
# ---------------------------------------
frutas = ('guayaba', 'cocoa', 'banana', 'pera', 'mora')

if('pepsi' in frutas):
    print('i like the cocoa')
else:
    print('dont suckit')

print('\n\n\n')
# ---------------------------------------
requested_toppings = ['tropical']


if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
        print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

print('\n\n\n')
# ---------------------------------------
available_toppings = ['mushrooms', 'olives',
                      'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")

print('\n\n\n')
# ---------------------------------------

names = ('carlos', 'admin', 'tenas', 'remt', 'raza')

if(names):
    for name in names:
        if (name == 'admin'):
            print('Hello admin, would you like to see a status report?')
        else:
            print('hello', name, 'thank you for logging in again')
else:
    print('There is nothing')

print('\n\n\n')
# ---------------------------------------

currentNames = ['carl', 'raul', 'royce', 'bente']
newNames = ['zipla', 'fuma', 'reeer', 'royce', 'alan']

print(currentNames)

for newName in newNames:
    if newName in currentNames:
        print(newName, 'Ya es usado')
    else:
        print(newName, 'WELCOME BITCHES')
        currentNames.append(newName)

print(currentNames)

print('\n\n\n')
# ---------------------------------------

numeros = list(range(1, 11))
numerosTH = []

for numero in numeros:
    if(numero == 1):
        numerosTH.append('1st')
    elif(numero == 2):
        numerosTH.append('2nd')
    elif(numero == 3):
        numerosTH.append('3rd')
    else:
        numerosTH.append(f'{numero}th')

print(numerosTH)
