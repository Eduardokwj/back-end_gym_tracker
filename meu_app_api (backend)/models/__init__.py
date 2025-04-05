from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

# importando os elementos definidos no modelo
from models.base import Base
from models.exercicio import Exercicio

db_path = "database/"
# Verificar se o diretorio acima existe e se não existe, criar o diretorio
if not os.path.exists(db_path):
    os.makedirs(db_path)

# url de acesso ao banco (essa é uma url de acesso ao sqlite local)
db_url = 'sqlite:///%s/db.sqlite3' % db_path

# cria a engine para conectar ao banco
engine = create_engine(db_url, echo=False)

# Instancia um criador de seção 
Session = sessionmaker(bind=engine)

# se o banco de dados não existe, cria o banco de dados
if not database_exists(engine.url):
    create_database(engine.url)

# cria as tabelas do banco de dados, caso não existam
Base.metadata.create_all(engine)