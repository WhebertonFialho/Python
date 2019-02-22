import pycep_correios

def consultar(cep):
	endereco = pycep_correios.consultar_cep(cep)
	return endereco