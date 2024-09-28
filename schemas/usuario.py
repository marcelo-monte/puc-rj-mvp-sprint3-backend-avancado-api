from pydantic import BaseModel, validator

from model.usuario import Usuario


class UsuarioViewSchema(BaseModel):
    """ Define como um Usuário será retornado.
    """
    id: int = 1
    nome: str = "Fulano da Silva"
    cpf: str = "111.111.111-11"
    cep: str = "22451-900"
    logradouro: str = "Rua Marquês de São Vicente"
    bairro: str = "Gávea"
    cidade: str = "Rio de Janeiro"
    uf: str = "RJ"
    complemento: str = "225"


class EnderecoDelSchema(BaseModel):
    """ Define os parâmetros para remover um endereço (pelo id do usuário).
    """
    id: int = 1

    @validator('id', pre=True, always=True)
    def valida_id(cls, valor):
        if not valor or valor == "":
            valor = 0
        return valor


class EnderecoDelViewSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str


class EnderecoSchema(BaseModel):
    """ Define como um Endereço a ser inserido/editado deve ser representado
    """
    # id do usuário, já que o endereço é salvo no mesmo registro.
    id: int = 1
    cep: str = "50670-901"
    logradouro: str = "Avenida Professor Moraes Rego"
    bairro: str = "Iputinga"
    cidade: str = "Recife"
    uf: str = "PE"
    complemento: str = "s/n"

    @validator('id', pre=True, always=True)
    def valida_id(cls, valor):
        if not valor or valor == "":
            valor = 0
        return valor


def apresenta_usuario(usuario: Usuario):
    """ Retorna uma representação do Usuario seguindo o schema definido em
        UsuarioViewSchema.
    """
    return {
        "id": usuario.id,
        "nome": usuario.nome,
        "cpf": usuario.cpf,
        "cep": usuario.cep,
        "logradouro": usuario.logradouro,
        "bairro": usuario.bairro,
        "cidade": usuario.cidade,
        "uf": usuario.uf,
        "complemento": usuario.complemento
    }
