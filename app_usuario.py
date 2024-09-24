from model import Session
from model.usuario import Usuario
from schemas.usuario import EnderecoDelSchema, EnderecoSchema, apresenta_usuario


def create_endereco(form: EnderecoSchema):
    """ Adiciona um novo endereço ao usuário logado

    Retorna uma representação do usuário associado, junto com o endereço
    """

    try:
        usuario_id = form.id
        session = Session()
        usuario = session.query(Usuario).filter(
            Usuario.id == usuario_id).first()

        if not usuario:
            error_msg = "Usuário não encontrado na base :/"
            return {"message": error_msg}, 404
        elif usuario.cep != "":
            error_msg = "Já existe um endereço cadastrado para esse usuário :/"
            return {"message": error_msg}, 400

        usuario.setEndereco(form.cep, form.logradouro, form.bairro,
                            form.cidade, form.uf, form.complemento)
        session.commit()

        return apresenta_usuario(usuario), 200

    except ValueError as e:
        return {"message": str(e)}, 409

    except Exception as e:
        error_msg = "Não foi possível salvar novo endereço :/"
        return {"message": error_msg}, 400


def search_usuario():
    """Busca no BD pelo usuário logado, com seu endereço

    Retorna uma representação do Usuário, com seu endereço.
    """

    try:
        # Nesse MVP, só temos um usuário na base. Por isso que
        # a busca não usa o id.
        session = Session()
        usuario = session.query(Usuario).first()

        if not usuario:
            error_msg = "Usuário não encontrado na base :/"
            return {"message": error_msg}, 404

        return apresenta_usuario(usuario), 200

    except Exception as e:
        error_msg = "Não foi possível consultar o usuário :/"
        return {"message": error_msg}, 400


def change_endereco(form: EnderecoSchema):
    """ Edita o endereço do usuário logado na base de dados

    Retorna uma representação do usuário com o endereço associado.
    """

    try:
        usuario_id = form.id
        session = Session()
        usuario = session.query(Usuario).filter(
            Usuario.id == usuario_id).first()

        if not usuario:
            error_msg = "Usuário não encontrado na base :/"
            return {"message": error_msg}, 404
        elif usuario.cep == "":
            error_msg = "Não existe um endereço cadastrado para esse usuário :/"
            return {"message": error_msg}, 400

        usuario.setEndereco(form.cep, form.logradouro, form.bairro,
                            form.cidade, form.uf, form.complemento)
        session.commit()

        return apresenta_usuario(usuario), 200

    except ValueError as e:
        return {"message": str(e)}, 409

    except Exception as e:
        error_msg = "Não foi possível editar o endereço :/"
        return {"message": error_msg}, 400


def remove_endereco(form: EnderecoDelSchema):
    """Deleta o endereço do usuário logado na base de dados

    Retorna uma mensagem de confirmação da remoção.
    """

    try:
        usuario_id = form.id
        session = Session()
        usuario = session.query(Usuario).filter(
            Usuario.id == usuario_id).first()

        if not usuario:
            error_msg = "Usuário não encontrado na base :/"
            return {"message": error_msg}, 404

        # Para remover o endereço, setamos os valores existentes para None
        usuario.removeEndereco()
        session.commit()

        return {"message": "Endereço removido!"}, 200

    except ValueError as e:
        return {"message": str(e)}, 409

    except Exception as e:
        error_msg = "Não foi possível remover o endereço :/"
        return {"message": error_msg}, 400
