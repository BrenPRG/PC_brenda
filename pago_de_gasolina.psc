Algoritmo pago_de_gasolina
	// precio_gasolina
	// litros_gasolina
	// pago
	Definir p_g,pago Como Real
	Definir litro Como Entero
	Escribir 'Ingresa el precio de la gasolina:'
	Leer p_g
	Escribir 'Ingresa los litros de gasolina despachados:'
	Leer litro
	pago <- p_g*litro
	Escribir 'El pago por la gasolina es:',pago
FinAlgoritmo
