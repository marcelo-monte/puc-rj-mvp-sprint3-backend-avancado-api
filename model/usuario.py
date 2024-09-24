from sqlalchemy import Column, DateTime, Integer, String
from model import Base


class Usuario(Base):
    __tablename__ = "usuario"

    id = Column("pk_usuario", Integer, primary_key=True)
    nome = Column(String(30), nullable=False)
    cpf = Column(String(15), nullable=False)
    cep = Column(String(8), nullable=True)
    logradouro = Column(String(60), nullable=True)
    bairro = Column(String(40), nullable=True)
    cidade = Column(String(60), nullable=True)
    uf = Column(String(2), nullable=True)
    complemento = Column(String(60), nullable=True)

    def __init__(self, nome: str, cpf: DateTime):
        """
        Cria um Usuario (nessa versão, só temos 01 endereço por usuário)

        Arguments:
            nome: o nome do usuário
            cpf: a data de nascimento do usuário
        """
        self.nome = nome
        self.cpf = cpf
        self.removeEndereco()

    def setEndereco(self, cep: str, logradouro: str, bairro: str, cidade: str, uf: str, complemento: str):
        """ Usada tanto para adicionar um endereço como para editar um
            endereço.
        """
        self.cep = cep
        self.logradouro = logradouro
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.complemento = complemento

    def removeEndereco(self):
        """ Usada para remover um endereço.
        """
        self.setEndereco("", "", "", "", "", "")
