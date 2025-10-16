from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from sqlmodel import Session
from ..database import get_session
from ..models import productCreate, productPublic, Product
# import app.models as mm
from ..crud import product_crud

router = APIRouter(prefix="/products", tags=["Products"])

SessionDep = Annotated[Session, Depends(get_session)]

@router.post("/", response_model=productPublic)
async def create_product(product_data: productCreate, session: SessionDep):
    return product_crud.create_product(session, product)

@router.get("/", response_model=list[productPublic])
def get_products(session: SessionDep):
    return product_crud.get_all_products(session)
