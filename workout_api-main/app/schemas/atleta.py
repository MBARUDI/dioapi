from pydantic import BaseModel

class AtletaListResponse(BaseModel):
    nome: str
    centro_treinamento: str
    categoria: str