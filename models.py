from typing import Optional
from pydantic import BaseModel

class Carta(BaseModel):
    id: int
    nome: str
    tipo: str
    raridade: str
    custo: int
    vida: int
    dano: int
    nivel: int
    description: Optional[str] = None

class CartaAtualizar(BaseModel):
    nome: Optional[str] = None
    tipo: Optional[str] = None
    raridade: Optional[str] = None
    custo: Optional[int] = None
    vida: Optional[int] = None
    dano: Optional[int] = None
    nivel: Optional[int] = None
    description: Optional[str] = None