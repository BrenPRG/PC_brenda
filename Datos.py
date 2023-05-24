numero=int(input("Ingresa un numero:"))
print(type(numero))

#numero telefonico int
telefono=int(input("Ingresa los numeros de tu telefono:"))
print("Tu numero es:", telefono)
print(type(telefono))

#numero telefonico string
telefono=input("Ingresa los numeros de tu telefono:")
print("Tu numero es:", telefono) #Mostrar lo que escribio el usuario
print(type(telefono)) #que tipo de dato es

correo=input("Ingresa tu correo electronico:")
print("tu correo es:", correo) #Mostrar lo que escribio el usuario
print(type(correo))

alumnoUno=int(input("Ingresa tu edad: \n")) #solicitamos la edad
alumnoDos=int(input("Ingresa tu edad: \n")) #solicitamos la edad
comparacion=alumnoUno>alumnoDos #Comparamos
print(comparacion) #mostrar el resultado de comparacion
print(type(comparacion))

#String - cadena de caracteres
nombre=input("Ingresa tu nombre:")
apellidoP=input("Ingresa tu apellido Paterno:")
apellidoM=input("Ingresa tu apellido Materno:")
print("Tu nombre es:",nombre,"",apellidoP,"",apellidoM)
print(type(nombre))
print(type(apellidoP))
print(type(apellidoM))