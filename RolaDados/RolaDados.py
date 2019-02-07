import random

def RolaDados(tam_dado, qtde_dados):
	dados = []
	soma = 0
	for x in range(qtde_dados):
		vlr_dado = random.randrange(1, tam_dado) 
		dados.append(vlr_dado)
		soma += vlr_dado
	
	print "Valor dos dados {0}".format(dados)	
	print "Soma dos dados {0}".format(soma)
	
if __name__ == "__main__":
	tam_dado = input("Digite o tamanho do dado: ")
	qtde_dados = input("Digite a quantidade dados: ")
	RolaDados(tam_dado, qtde_dados)
	