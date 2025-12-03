from fastapi import FastAPI, Depends, HTTPException
from typing import List

from models import Product
import database as db
from security import get_role_from_token, require_admin

app = FastAPI(title="Product Service", version="1.0")


# ------------------------------
#   DEPENDENCIA DE SEGURIDAD
# ------------------------------
def get_current_role(role: str = Depends(get_role_from_token)):
    return role


# ------------------------------
#           ENDPOINTS
# ------------------------------

@app.get("/products", response_model=List[Product])
def get_products(role: str = Depends(get_current_role)):
    return db.get_all_products()


@app.get("/products/{id}", response_model=Product)
def get_product(id: int, role: str = Depends(get_current_role)):
    prod = db.get_product(id)
    if not prod:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return prod


@app.post("/products", response_model=Product)
def create_product(
    product: Product,
    role: str = Depends(get_current_role)
):
    require_admin(role)  # 🔐 Verificación de ADMIN
    return db.create_product(product.dict())


@app.put("/products/{id}", response_model=Product)
def update_product(
    id: int,
    product: Product,
    role: str = Depends(get_current_role)
):
    require_admin(role)
    updated = db.update_product(id, product.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return updated


@app.delete("/products/{id}")
def delete_product(
    id: int,
    role: str = Depends(get_current_role)
):
    require_admin(role)
    deleted = db.delete_product(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"message": "Producto eliminado correctamente"}
