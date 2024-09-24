from flask import redirect

from flask_openapi3 import OpenAPI, Info, Tag

from flask_cors import CORS

from app_usuario import change_endereco, create_endereco, remove_endereco, search_usuario
from schemas.error import ErrorSchema
from schemas.usuario import EnderecoDelSchema, EnderecoDelViewSchema, EnderecoSchema, UsuarioViewSchema

info = Info(title="API de Endereços - MonteBank", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo as tags do OpenAPI
home_tag = Tag(name="Documentação",
               description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
endereco_tag = Tag(
    name="Endereço", description="Operações relacionadas a Endereço de Usuário")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

# Rotas referentes a endereço


@app.post('/endereco', tags=[endereco_tag],
          responses={"200": UsuarioViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_endereco(form: EnderecoSchema):
    """Adiciona um novo endereço ao usuário logado na base de dados

    Retorna uma representação do usuário com o endereço associado.
    """
    return create_endereco(form)


@app.put('/endereco', tags=[endereco_tag],
         responses={"200": UsuarioViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def edit_endereco(form: EnderecoSchema):
    """Edita o endereço do usuário logado na base de dados

    Retorna uma representação do usuário com o endereço associado.
    """
    return change_endereco(form)


@app.get('/usuario', tags=[endereco_tag],
         responses={"200": UsuarioViewSchema, "404": ErrorSchema})
def get_usuario():
    """Busca no BD pelo usuário logado, com seu endereço

    Retorna uma representação do Usuário, com seu endereço.
    """

    return search_usuario()


@app.delete('/endereco', tags=[endereco_tag],
            responses={"200": EnderecoDelViewSchema, "404": ErrorSchema})
def del_endereco(form: EnderecoDelSchema):
    """Deleta o endereço do usuário logado na base de dados

    Retorna uma mensagem de confirmação da remoção.
    """

    return remove_endereco(form)
