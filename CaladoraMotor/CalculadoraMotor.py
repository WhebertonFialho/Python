#coding: utf-8
# Wheberton Fialho

pi = 3.14159

def CalculaCilindrada(dm_pistao, dm_curso, cilindros):
	multiplicacao = pi * (dm_pistao * dm_pistao) * dm_curso
	cilindrada = 0

	#MONOCILINDRO OU MULTICILINDRO
	if cilindros == 1:
		cilindradas = (multiplicacao / 1000) / 4
	else:
		resultado = cilindros == 4 and multiplicacao or (multiplicacao / 4) * cilindros
		cilindradas = round(resultado / 1000, 2)
	
	return cilindradas

def CalculaTaxaMotor():
	pass

def CalculaVolumeMotor():
	pass

if __name__ == '__main__':
	dm_pistao = input("Digite o Diametro do Pistao(mm): ")
	dm_curso = input("Curso Virabrequin(mm): ")
	cilindros = input("Digite quantos cilindros: ")
	cilindradas = CalculaCilindrada(dm_pistao, dm_curso, cilindros)

	print "Cilindradas: {0}cc".format(cilindradas)
