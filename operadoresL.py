#SOLICITAR UNA EDAD y que el usuario pueda ingresar el dato por teclado
#Si la edad que ingresa es mayor o igual a 18
#debemos mostrar por pantalla un mensaje "Eres mayor de edad"

print("""
         Bienvendido a mi programa que indica si eres un niño, adolecsente, adulto, de la era edad
         """)

edad=int(input("Ingresa tu edad:"))

if edad>=0 and edad<=12:
   print("Eres un niño")

if edad>=13 and edad<=17:
   print("Eres un adolecsente")

if edad>=18 and edad<=64:
   print("Eres un adulto")

if edad>=65:
   print("Eres de la 3ra edad")

