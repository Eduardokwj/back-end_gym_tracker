from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote
from flask import send_from_directory

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from models import Session, Exercicio
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="Gym Tracker", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definição de tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
exercicio_tag = Tag(name="Exercicio", description="Adição, visualização e remoção de exercícios na base")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, onde é possível escolher a documentação."""
    return redirect('/openapi')


@app.post('/exercicio', tags=[exercicio_tag],
          responses={"200": ExercicioViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_exercicio(form: ExercicioSchema):
    """ Adiciona um exercício ao banco de dados """
    
    exercicio = Exercicio(
        exercicio=form.exercicio,
        series=form.series,
        repeticoes=form.repeticoes,
        peso=form.peso
    )
    
    logger.debug(f"Adicionando o exercício: '{exercicio.exercicio}'")

    try:
        with Session() as session:
            session.add(exercicio)
            session.commit()
            logger.debug("Exercício adicionado")
            return apresenta_exercicio(exercicio), 200
    
    except IntegrityError:
        error_msg = "Exercício já se encontra na base :/"
        logger.warning(f"Erro ao adicionar exercício '{exercicio.exercicio}': {error_msg}")
        return {"message": error_msg}, 409

    except Exception as e:
        error_msg = "Não foi possível adicionar o novo exercício :/"
        logger.error(f"Erro inesperado ao adicionar '{exercicio.exercicio}': {e}")
        return {"message": error_msg}, 400

@app.get('/exercicios', tags=[exercicio_tag],
         responses={"200": ListagemExercicioSchema, "404": ErrorSchema})
def get_exercicios():
    """ Retorna todos os exercícios cadastrados no banco de dados """
    logger.debug("Coletando todos os exercícios")

    with Session() as session:
        exercicios = session.query(Exercicio).all()

    if not exercicios:
        return {"exercícios": []}, 200
    
    logger.debug(f"{len(exercicios)} exercícios cadastrados")
    return apresenta_exercicios(exercicios), 200

@app.get('/exercicio', tags=[exercicio_tag],
         responses={"200": ExercicioViewSchema, "404": ErrorSchema})
def get_exercicio(query: BuscaExercicioSchema):
    """Busca um exercício pelo nome"""
    
    exercicio_nome = query.exercicio
    logger.debug(f"Buscando exercício: '{exercicio_nome}'")

    with Session() as session:
        exercicio = session.query(Exercicio).filter(Exercicio.exercicio == exercicio_nome).first()

    if not exercicio:
        error_msg = "Exercício não encontrado na base de dados :/"
        logger.warning(f"Erro ao encontrar exercício '{exercicio_nome}': {error_msg}")
        return {"message": error_msg}, 404

    logger.debug(f"Exercício encontrado: '{exercicio_nome}'")
    return apresenta_exercicio(exercicio), 200

@app.delete('/exercicio', tags=[exercicio_tag],
            responses={"200": ExercicioDelSchema, "404": ErrorSchema})
def deleta_exercicio(query: BuscaExercicioSchema):
    """Deleta um exercício pelo nome"""

    exercicio_nome = unquote(query.exercicio)
    logger.debug(f"Tentando deletar exercício: '{exercicio_nome}'")

    with Session() as session:
        count = session.query(Exercicio).filter(Exercicio.exercicio == exercicio_nome).delete()
        session.commit()

    if count:
        logger.debug(f"Exercício '{exercicio_nome}' deletado com sucesso")
        return {"message": "Exercício removido", "id": exercicio_nome}
    
    error_msg = "Exercício não encontrado na base :/"
    logger.warning(f"Erro ao deletar '{exercicio_nome}': {error_msg}")
    return {"message": error_msg}, 404
