from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  models import Base


class Exercicio(Base):
    __tablename__ = 'exercicio'

    id = Column("pk_exercicio", Integer, primary_key=True)
    exercicio = Column(String(140), unique=True)
    series = Column(Integer)
    peso = Column(Float)
    repeticoes = Column(Integer)
    data = Column(DateTime, default=datetime.now())


    def __init__(self, exercicio:str, series:int, repeticoes: int, peso:float,
                 data:Union[DateTime,None]=None):
        """
        Cria um Exercicio na tabela
        
        Arguments:
            exercicio: exercicio que será feito
            series: quantidade de séries que serão feitas
            repetições: quantidade de repetições em cada série
            peso: peso utilizado em cada série
            data: data quando o exercicio foi inserido na base de dados
        """
        self.exercicio = exercicio
        self.series = series
        self.repeticoes = repeticoes
        self.peso = peso

        # se a data nao for informada, sera a data da inserção no banco de dados
        if data:
            self.data=data