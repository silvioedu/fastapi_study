from typing import Optional

from pydantic import BaseModel, validator


class Curso(BaseModel):
  id: Optional[int] = None
  titulo: str
  aulas: int
  horas: int

  @validator('titulo')
  def validar_titulo(cls, value):
    palavras = value.split(' ')
    if len(palavras) < 3:
      raise ValueError('O titulo deve ter pelo menos 3 palavras')
    return value  

  @validator('aulas')
  def validar_aulas(cls, value):
    if value < 12:
      raise ValueError('Deve ter pelo menos 12 aulas')
    return value

  @validator('horas')
  def validar_horas(cls, value):
    if value < 10:
      raise ValueError('Deve ter pelo menos 10 horas')
    return value


cursos = [
  Curso(id=1, titulo='Programação para leigos', aulas=42, horas=56),
  Curso(id=2, titulo='Algoritmos e Lógica de programação', aulas=52, horas=66)
]