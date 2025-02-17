import strawberry
from typing import List
from sqlalchemy.orm import Session
from ..models.product import Product
from .types import ProductType, CreateProductInput


@strawberry.type
class Query:
    @strawberry.field
    def get_products(self, info) -> List[ProductType]:
        db: Session = info.context["db"]
        products = db.query(Product).all()
        return products

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_product(self, info, input: CreateProductInput) -> ProductType:
        db: Session = info.context["db"]

        # existing_product = db.query(Product).filter(Product.product_code)

        new_product = Product(
            product_code=input.product_code,
            product_name=input.product_name,
            product_description=input.product_description
        )
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        return new_product
