import os

class Config:
    SECRET_KEY = 'minha_chave_secreta'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tarefas.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
