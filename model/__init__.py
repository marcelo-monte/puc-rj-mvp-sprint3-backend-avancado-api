from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

# importando os elementos definidos no modelo
from model.base import Base
from model.usuario import Usuario

db_path = "database/"
# Verifica se o diretorio não existe
if not os.path.exists(db_path):
    # então cria o diretorio
    os.makedirs(db_path)

# url de acesso ao banco (essa é uma url de acesso ao sqlite local)
db_url = 'sqlite:///%s/db.sqlite3' % db_path

# cria a engine de conexão com o banco
engine = create_engine(db_url, echo=False)

# Instancia um criador de seção com o banco
Session = sessionmaker(bind=engine)

# cria o banco se ele não existir
if not database_exists(engine.url):
    create_database(engine.url)

# cria as tabelas do banco, caso não existam
Base.metadata.create_all(engine)

# Verifica se existe pelo menos um Usuario no banco de dados
session = Session()

# Tenta buscar o primeiro usuário na tabela Usuario
usuario = session.query(Usuario).first()

# Se não houver nenhum usuário, insere um
if not usuario:
    usuario = Usuario(nome="Cicrano da Silva", cpf="222.222.222-22")
    session.add(usuario)
    session.commit()

session.close()
