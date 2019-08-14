from flask_api import mongo, api
from flask_restplus import fields

transacao = mongo.db.transacao
modelo_transacao = api.model('Transação', {"Data": fields.String(required = True, description='Data em dd/mm/yyyy'),
          "Hora": fields.String(  required = True, description='Hora em HH:MM'),
          "ContaInicial": fields.String(required = True, description='Conta Inicial'),
          "ContaFinal": fields.String(required = True,description='Conta Final'),
          "Valor": fields.Float( required = True,description='Valor da transação em R$')})


modelo_Filtro = api.model('Filtro',{
    "Hora": fields.String(  required = True, description='Hora em HH:MM'),
    "Data": fields.String(required = True, description='Data em dd/mm/yyyy'),
    "Valor": fields.Float( required = True,description='Valor da transação em R$')

})








