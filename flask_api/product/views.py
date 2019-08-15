# coding: utf-8
from flask import  jsonify, abort
from flask_api import  api, ns
from flask_api.product.models import transacao, modelo_transacao, modelo_Filtro
from flask_restplus import Resource
from bson.objectid import ObjectId



@ns.route('/')
class ListTransaction(Resource):
    @ns.doc('Consulta de transaçoes')
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
            return jsonify({'Transações': lista_transacoes})

    @ns.doc('Inserindo novas transaçoes')
    @ns.expect(modelo_transacao, validate=True)
    def post(self):

        transacao.insert(api.payload)
        return 'Transação feita com sucesso'

@ns.route('/<_id>')
class Transaction(Resource):

    @ns.doc('Buscando transações via post')
    @ns.response(200, 'Success', modelo_transacao)
    @ns.response(400, 'Bad request')
    @ns.expect(modelo_transacao)
    def put(self, _id ):

        try :
            result = transacao.find_one({'_id': ObjectId(_id)})

            if result:
                transacao.update_one({'_id':ObjectId(_id)}, {"$set": api.payload}, upsert=False)
                return 'Dado(s) atualizado(s) com sucesso!'

        except:
            return 'Erro na atualização de transação/Sem transações'

    @ns.doc('Deletando transação')
    def delete(self, _id):

        result = transacao.find_one({'_id': ObjectId(_id)})

        if result:
            transacao.remove(result)
            return 'Transação deletada com sucesso'

        else:
            return abort(400,'Erro na remoção a transação/Transação Inexistente')





@ns.route('/filter')
class TransactionFilter(Resource):
    @ns.doc('Filtrando transações')
    @ns.response(200, 'Success', modelo_transacao)
    @ns.response(400, 'Bad request')
    @ns.expect(modelo_Filtro, validate=True)
    def post(self):

        lista_transacoes = []
        for row in transacao.find({'$and': [{'Valor':{'$gte':api.payload['Valor']}, 'Hora':{'$gte':api.payload['Hora']}, 'Data':{'$gte':api.payload['Data']} }]}):
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






