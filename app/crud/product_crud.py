from sqlmodel import Session, select
from ..models import Product, productCreate, productPublic

def create_product(session: Session, product_data: productCreate) -> productPublic:
    product = Product.model_validate(product_data)
    session.add(product)
    session.commit()
    session.refresh(product)
    return product

def get_all_products(session: Session):
    return session.exec(select(Product)).all()

def get_product_by_id(session: Session, product_id):
    return session.get(Product, product_id)

def update_product(session: Session, product_id, update_data):
    db_product = session.get(Product, product_id)
    if not db_product:
        return None
    db_product.sqlmodel_update(update_data.model_dump(exclude_unset=True))
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product

def delete_product(session: Session, product_id):
    product = session.get(Product, product_id)
    if not product:
        return None
    session.delete(product)
    session.commit()
    return True
