from fastapi import APIRouter, Query, Depends, HTTPException, status
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from .database import get_db
from .models import Atleta
from app.schemas.atleta import AtletaListResponse, AtletaCreate
from fastapi_pagination import Page, paginate, add_pagination

router = APIRouter()

@router.get("/atletas", response_model=Page[AtletaListResponse])
def listar_atletas(
    nome: Optional[str] = Query(None),
    cpf: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Atleta)
    if nome:
        query = query.filter(Atleta.nome.ilike(f"%{nome}%"))
    if cpf:
        query = query.filter(Atleta.cpf == cpf)
    return paginate([
        AtletaListResponse(
            nome=a.nome,
            centro_treinamento=a.centro_treinamento.nome,
            categoria=a.categoria.nome
        )
        for a in query.all()
    ])

@router.post("/atletas")
def criar_atleta(atleta: AtletaCreate, db: Session = Depends(get_db)):
    try:
        novo_atleta = Atleta(**atleta.dict())
        db.add(novo_atleta)
        db.commit()
        db.refresh(novo_atleta)
        return novo_atleta
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=303,
            detail=f"Já existe um atleta cadastrado com o cpf: {atleta.cpf}"
        )

# No final do arquivo principal da API (ex: main.py), adicione:
# add_pagination(app)