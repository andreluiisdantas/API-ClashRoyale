from fastapi import FastAPI, HTTPException
from typing import List
from models import Carta, CartaAtualizar

app = FastAPI()

db: List[Carta] = []

# Endpoint para ver todas as cartas
@app.get("/", response_model=List[Carta])
def mostrar_cartas():
    return db

# Endpoint para adicionar carta
@app.post("/cartas", response_model=Carta)
async def criar_carta(carta: Carta):

    for item in db:
        if item.nome == carta.nome:
            raise HTTPException(status_code=400, detail="Essa carta ja existe")
        
    db.append(carta)
    return carta

# Endpoint para ver uma carta especifica
@app.get("/cartas/{carta_id}", response_model=Carta)
async def mostrar_especifica(carta_id: int):
    for item in db:
        if item.id == carta_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


# Endpoint para editar uma carta especifica
@app.put("/cartas/{carta_id}", response_model=Carta)
async def editar_especifca(carta_id: int, carta_atualizada: Carta):
    
    for index, item in enumerate(db):
        if item.id == carta_id:
            carta_atualizada.id = item.id
            db[index] = carta_atualizada
            return carta_atualizada
    raise HTTPException(status_code=404, detail="Item não existe")

# Endpoint para editar uma carta especifica
@app.patch("/cartas/{carta_id}", response_model=Carta)
async def editar_campo(carta_id: int, atualizacoes: CartaAtualizar):
    carta_existente = db.get(carta_id)
    if not carta_existente:
        raise HTTPException(status_code=404, detail="Carta não encontrada")
    
    dados_novos = atualizacoes.dict(exclude_unset=True)

    if not dados_novos:
        return carta_existente
    
    carta_atualizada = carta_existente.copy(update=dados_novos)
    
    db[carta_id] = carta_atualizada
    return carta_atualizada
    

# Endpoint para deletar carta especifica
@app.delete("/cartas/{carta_id}", response_model=Carta)
async def deletar_carta(carta_id: int):
    
    for index, item in enumerate(db):
        if item.id == carta_id:
            return db.pop(index)
    raise HTTPException(status_code=404, detail="Item não existe")
