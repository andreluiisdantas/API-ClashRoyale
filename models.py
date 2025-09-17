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