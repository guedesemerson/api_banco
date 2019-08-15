from flask_api import mongo, api
from flask_restplus import fields

transacao = mongo.db.transacao
modelo_transacao = api.model('Transação', {"Data": fields.DateTime(dt_format='rfc822',required = True, description='Data em dd-mm-yyyy'),
          "Hora": fields.DateTime( dt_format='rfc822', required = True, description='Hora em hh:mm'),
          "ContaInicial": fields.String(required = True, description='Conta Inicial'),
          "ContaFinal": fields.String(required = True,description='Conta Final'),
          "Valor": fields.Float( required = True,description='Valor da transação em R$', min=0)})


modelo_Filtro = api.model('Filtro',{
    "Hora": fields.DateTime( dt_format='rfc822', required = True, description='Hora em hh:mm'),
    "Data": fields.DateTime(dt_format='rfc822',required = True, description='Data em dd-mm-yyyy'),
    "Valor": fields.Float( required = True,description='Valor da transação em R$', min=0)})








