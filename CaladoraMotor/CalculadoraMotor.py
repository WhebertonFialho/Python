#!/usr/bin/env python
# -*- coding: utf-8 -*-

PI = 3.14159

def CalculaCilindrada(dm_pistao, dm_curso, cilindros):
	raio = dm_pistao / 10
	altura = dm_curso / 10
	area = PI * (raio * raio) * altura
	cilindrada = 0

	#MONOCILINDRO OU MULTICILINDRO
	if cilindros == 1:
		cilindradas = area / 4
	else:
		result = cilindros == 4 and area or (area / 4) * cilindros
		cilindradas = result 
	
	return round(cilindradas, 2)

if __name__ == '__main__':
	dm_pistao = float(input("Digite o Diametro do Pistão(mm): "))
	dm_curso = float(input("Curso Virabrequin(mm): "))
	cilindros = input("Digite quantos cilindros: ")
	cilindradas = CalculaCilindrada(dm_pistao, dm_curso, cilindros)

	print "Cilindradas do Motor: {0}cc".format(cilindradas)
