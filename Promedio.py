
#Calcular el promedio de 5 califiucaciones y Mostrar el resultado
	#Utilizando una tarea repetitiva= Mientras v
acum=0
cont=1
nota=0
while cont<=5:
 nota=int(input("Ingresa tu nota ")) 
 acum=acum+nota
 cont=cont+1
promedio=acum/5
print ("El promedio es:  ", promedio)