#coding: utf-8
# Wheberton Fialho

pi = 3.14159

def cilindrada(dm_pistao, dm_curso, cilindros):
	multiplicacao = pi * (dm_pistao * dm_pistao) * dm_curso
	
	#MONOCILINDRO OU MULTICILINDRO
	if cilindros == 1:
		print "Resultado e {:.2f} cm3".format((multiplicacao / 1000) / 4)
	else:
		resultado = cilindros == 4 and multiplicacao or (multiplicacao / 4) * cilindros
		print "Resultado e {:.2f} cm3".format(resultado / 1000)
	
if __name__ == '__main__':
	dm_pistao = input("Digite o Diametro do Pistao(mm): ")
	dm_curso = input("Curso Virabrequin(mm): ")
	cilindros = input("Digite quantos cilindros: ")
	cilindrada(dm_pistao, dm_curso, cilindros)
