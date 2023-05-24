Algoritmo Promedio
	// Obtener el promedio de 5 calificaciones y mostra el resultado
	// Utilizando una tarea repetitiva - Mientras 
	Definir cont,acum,nota Como Entero
	Definir prom Como Real
	acum <- 0
	cont <- 1
	Mientras cont<=5 Hacer
		Escribir 'Ingresa tu nota ',cont,':'
		Leer nota
		acum <- acum+nota
		cont <- cont+1
	FinMientras
	prom <- acum/5
	Escribir 'Tu promedio es:',prom
FinAlgoritmo
