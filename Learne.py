# Importar libreria
from math import *



# variables de cadena
from cgi import print_directory


character_name = "Jhon"
Character_age = "50"
print("there once was a man named " + character_name + ", ")
print("he was " + Character_age + " years old. ")
print("he really liked the name " + character_name +", ")
print("but didn't like being " + Character_age + ".\n" )

#funciones
phrase = "Fabio Academy"
print(phrase.upper().isupper())          # vuelve mayusculas y pregunta si es verdadero o falso
print(phrase.upper())                    # vuelve todo mayusculas
print(phrase[4])                         # muestra la posicion 4 de la phrase
print(len(phrase))                       # cuenta la cantidad de caracteres en la oracion
print(phrase.replace("Fabio", "World"))  # reemplaza la primera palabra por la segunda 
print("Finish\n")

# Working with numbers
print(2.5162)
print(3 + 4)
print(3 / 5)
print(3 * 5)
print(3 * (4 + 2))
print(10 % 3 )    # divide 10 entre 3 y arroja el residuo
print("\n")

# variables numericas
my_num = 5
print(my_num)
print(str(my_num) + " my favorite number")  # convierte el numero en cadena para imprimir cadenas con numeros mas facil
print(pow(3, 2))      # 3 elevado a la 2
print(max(3, 2))      # nos dice que numer es el mayor min() nos dice el minimo
print(round(6.5))     # redondea el numero

# funciones con la libreria de math
print("\n")
print(floor(6.5))     # toma el mas bajo en redondeo
print(ceil(6.5))      # toma el mas alto en redondeo
print(sqrt(128))      # raiz del numero 

print("\n")

# Ejemplo de almacenamiento de datos tipo caracter o cadena
# name = input ("Enter your name: ")
# age = input ("Enter your age: ")
# print("Your name is " + name + " and your age is " + age)  


print("\n")
# Calculadora basica
# num1 = input ("Enter any number 1: ")
# num2 = input ("Enter any numbre 2: ")
# result = float(num1) + float (num2)
# print("el resultado es: " + str(result))    # Usar str para poder imprimir un numero con letras

print("\n")

# listas

# lucky_numbers = [4, 8, 15, 16, 23, 42]
# friends = ["kevin", "karen", "jim", "oscar", "toby", "kelly"]
# friends.extend(lucky_numbers)   #combina las 2 listas
# friends.append("Molly")  # imprime friends y le agrega molly
# friends.insert(1, "add")  #imprime friends y en la posicion 1 coloca add y corre lo demas
# friends.remove("kelly") #elimina el nombre kelly de la lista
# friends.sort() #ordena alfabeticamente la listaa
# lucky_numbers.sort() # ordena de menor a mayor la lista
# lucky_numbers.reverse() # imprime la lista al reves
# friends2 = friends.copy() # copia la lista 1 y la pega en 2

# print(friends[0])
# print(friends[1])
# print(friends[-2])
# print(friends[1:3])
# print(friends.index("kevin"))   # me dice donde esta esenombre en la lista
# print(friends.index("kevin"))   # cuenta cuantas veces esta ese nombre en la lista
# print(friends)

# Funciones

# def sayhi(name,age):
#     print("Hello " + name + ", you are " + str(age))

# sayhi("mike", 35)
# sayhi("fabio", 60)

# def cube(num):
#    return num*num*num

# result = cube(float(input("Enter a number for cube: ")))
# print(result)


# condicionales


def max_num(num1, num2, num3):
    if num1 >= num2 and num1>=num3:
        return num1
    if num2 >= num1 and num2>=num3:
        return num2
    else:
        return num3

num1 = input("Inserte un numero cualquiera: ")
num2 = input("Inserte un numero cualquiera: ")
num3 = input("Inserte un numero cualquiera: ")

print(max_num(num1, num2, num3))