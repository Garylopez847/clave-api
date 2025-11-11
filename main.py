from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Clave actual que quieres validar (puedes cambiarla cuando quieras)
CLAVE_ACTUAL = "MMC"

class ClaveRequest(BaseModel):
    clave: str

@app.post("/validar-clave")
def validar_clave(request: ClaveRequest):
    if request.clave == CLAVE_ACTUAL:
        return {"valida": True}
    else:
        raise HTTPException(status_code=401, detail="Clave inválida")