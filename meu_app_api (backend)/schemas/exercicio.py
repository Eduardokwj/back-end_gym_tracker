from pydantic import BaseModel
from typing import Optional, List
from models.exercicio import Exercicio

class ExercicioSchema (BaseModel):
    """ Define como um novo exercicio a ser inserido no banco deve ser inserido
    """

    exercicio: str
    series: int
    repeticoes: int
    peso: float

class BuscaExercicioSchema (BaseModel):
    """ Define como deve ser feita a busca no programa
    """

    exercicio: str


class ListagemExercicioSchema(BaseModel):
    """ Define como a listagem de exercicios deve retornar
    """
    exercicios:List[ExercicioSchema]

def apresenta_exercicios(exercicios: List[Exercicio]):
    """ Retorna uma representação do exercicio seguindo o Schema definido
    """
    result = []
    for exercicio in exercicios:
        result.append({
            "exercicio" : exercicio.exercicio,
            "series" : exercicio.series,
            "repeticoes" : exercicio.repeticoes,
            "peso" : exercicio.peso,
        })

    return {"exercicios": result}

class ExercicioViewSchema(BaseModel):
    """ Define como um exercicio retornará.
    """
    id: int
    exercicio: str
    series: int
    repeticoes : int
    peso: float


class ExercicioDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_exercicio(exercicio: Exercicio):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "id": exercicio.id,
        "exercicio": exercicio.exercicio,
        "series": exercicio.series,
        "repeticoes": exercicio.repeticoes,
        "peso": exercicio.peso,
        "data": exercicio.data
    }

