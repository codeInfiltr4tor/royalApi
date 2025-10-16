from sqlmodel import SQLModel, Field
from datetime import datetime

class ProductBase(SQLModel):
    name: str = Field(index=True)
    category: str | None = None
    price: float
    quantity: int

class Product(ProductBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime | None = Field(default_factory=datetime.utcnow)

class ProductCreate(ProductBase):
    pass

class ProductRead(ProductBase):
    id: int
    created_at: datetime

class ProductUpdate(SQLModel):
    name: str | None = None
    category: str | None = None
    price: float | None = None
    quantity: int | None = None
