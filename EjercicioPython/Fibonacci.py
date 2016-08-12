#!/usr/bin/python3

num1 = 0;
num2 = 1;
num3 = 0;
detener = int(raw_input("Numero en el que se debe detener: "));

num1, num2 = 0, 1;
def sumar(n1, n2):
	return n1 + n2
	
#cadena = str(num1) + " " + str(num2);
cadena = "Resultado: "
while sumar(num1, num2) <= detener:
	num3 = sumar(num1, num2)
	num1 = num2
	num2 = num3
	cadena += " " + str(num3)

print cadena;
