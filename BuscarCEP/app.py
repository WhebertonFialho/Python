from API import BuscaCep
from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route('/api/v1/consultarCep', methods=['GET'])
def consultarCep():
	cep = request.args.get('cep', default = '00000000', type=str)
	json = BuscaCep.consultar(cep)
	return jsonify(json)

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='127.0.0.1', port=port)