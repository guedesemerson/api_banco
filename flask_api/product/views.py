# coding: utf-8
from flask import  jsonify, abort
from flask_api import  api, ns
from flask_api.product.models import transacao, modelo_transacao, modelo_Filtro
from flask_restplus import Resource
from bson.objectid import ObjectId


@ns.route('/')
class ListProducts(Resource):

    @ns.response(200, 'Success',modelo_transacao)
    @ns.response(400, 'Bad request')
    def get(self):
        lista_transacoes = []
        for row in transacao.find():
            lista_transacoes.append({"Data":row['Data'],
                                     "Hora": row['Hora'],
                                      "_id:":str(ObjectId(row['_id'])),
                                      "Valor":row['Valor'],
                                      "ContaInicial":row['ContaInicial'],
                                      "ContaFinal":row['ContaFinal']})



        if lista_transacoes == []:
            return abort(400,'Erro na busca dos objetos/Sem objetos')
        else:
            return jsonify({'result': lista_transacoes})

    @ns.expect(modelo_transacao)
    def post(self):

        transacao.insert(api.payload)
        return 'Dado inserido com sucesso'

@ns.route('/<_id>')
class Product(Resource):
    @ns.response(200, 'Success', modelo_transacao)
    @ns.response(400, 'Bad request')

    def put(self, _id):
        result = transacao.find_one({'_id': ObjectId(_id)})
        if result:
            return jsonify(result)

        else:
            return abort(400,'Erro na busca dos objetos/Sem objetos')


    def delete(self, _id):

        result = transacao.find_one({'_id': ObjectId(_id)})

        if result:
            transacao.remove(result)
            return 'Dado deletado com sucesso'

        else:
            return abort(400,'Erro na busca dos objetos/Sem objetos')





@ns.route('/filter')
class TransactionFilter(Resource):
    @ns.expect(modelo_Filtro)
    def post(self):

        lista_transacoes = []
        for row in transacao.find(api.payload):
            if row:
                lista_transacoes.append({"Data": row['Data'],
                                         "Hora": row['Hora'],
                                         "_id:": str(ObjectId(row['_id'])),
                                         "Valor": row['Valor'],
                                         "ContaInicial": row['ContaInicial'],
                                         "ContaFinal": row['ContaFinal']})

        if lista_transacoes == []:
            return 'Transações não encontradas com o filtro especificado'


        else:
            return jsonify({'Result': lista_transacoes})






