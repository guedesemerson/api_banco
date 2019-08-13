from flask_api import mongo, api
from flask_restplus import fields
import time

class TimeFormat(fields.Raw):
    def format(self, value):
        return time.strftime(value, "%H:%M")

transacao = mongo.db.transacao
modelo_transacao = api.model('Transação', {"Data": fields.Date(required = True),
          "Hora": TimeFormat(  readonly= True,required = True, description='Hora em HH:MM', default='HH:MM'),
          "ContaInicial": fields.String(required = True, description='Conta do emissor'),
          "ContaFinal": fields.String(required = True,description='Conta do emitente'),
          "Valor": fields.Float( required = True,description='Valor da transação em R$')})











