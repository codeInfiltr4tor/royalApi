from fastapi import Depends, FastAPI, HTTPException, Query
from typing import Annotated
from .database import *
from .routes import product
# import app.models as mm

app = FastAPI();

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

SessionDep = Annotated[Session, Depends(get_session)]

app.include_router(product.router) 

