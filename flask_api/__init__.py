# coding: utf-8
from flask import Flask
from flask_pymongo import PyMongo
from flask_restplus import Api



app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'banco'
app.config['MONGO_URI'] = 'mongodb://rendafixa:rendafixa13@ds261277.mlab.com:61277/banco'
api = Api(app,version='1.0', title='APP RENDA FIXA', description='Created by: Emerson Guedes ',
          default ='Functions', default_label='')

mongo = PyMongo(app)



