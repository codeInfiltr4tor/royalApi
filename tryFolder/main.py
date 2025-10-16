from fastapi import FastAPI
from tryFolder.database import create_db_and_tables
from tryFolder.routes import product

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(product.router)
