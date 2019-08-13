# coding: utf-8
from flask import  jsonify, abort
from flask_api import  api
from flask_api.product.models import transacao, modelo_transacao
from flask_restplus import Resource
from bson.objectid import ObjectId


@api.route('/read', methods=['GET'])
class ProductView(Resource):


    @api.response(200, 'Success',modelo_transacao)
    @api.response(400, 'Validation Error')
    def get(self):
        lista_transacoes = []
        for row in transacao.find():
            lista_transacoes.append({"Data":row['Data'],
                                      "Hora":row['Hora'],
                                      "_id:":str(ObjectId(row['_id'])),
                                      "ContaInicial":row['ContaInicial'],
                                      "ContaFinal":row['ContaFinal']})



        if lista_transacoes == []:
            return abort(400,'Erro na busca dos objetos/Sem objetos')
        else:
            return jsonify({'result': lista_transacoes})

@api.route('/create', methods=['POST'])
class ProductCreate(Resource):

    @api.response(200, 'Success', modelo_transacao)
    @api.response(400, 'Validation Error')
    @api.expect(modelo_transacao)

    def post(self):

        transacao.insert(api.payload)
        return 'Dado inserido com sucesso'

@api.route('/delete/<id>', methods=['DELETE'])
class ProductDelete(Resource):

    @api.response(200, 'Success', modelo_transacao)
    @api.response(400, 'Validation Error')


    def delete(self, id):

        result = transacao.find_one({'_id': ObjectId(id)})

        if result:
            transacao.remove(result)
            return 'Dado deletado com sucesso'

        else:
            return abort(400,'Erro na busca dos objetos/Sem objetos')





