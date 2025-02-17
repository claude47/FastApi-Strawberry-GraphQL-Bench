import strawberry
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from ..models.product import Product
from .types import ProductType, CreateProductInput
from .error_handler import ErrorHandler

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

        existing_product = db.query(Product).filter(
            (Product.product_code == input.product_code) | (Product.product_name == input.product_name)
            ).first()

        if existing_product:

            if existing_product.product_code == input.product_code:
                raise ErrorHandler(f"Product code {input.product_code} already exists. ")

            if existing_product.product_name == input.product_name:
                raise ErrorHandler(f"Product name {input.product_name} already exists. ")

        try:
            new_product = Product(
                product_code=input.product_code,
                product_name=input.product_name,
                product_description=input.product_description
            )
            db.add(new_product)
            db.commit()
            db.refresh(new_product)
            return new_product

        except IntegrityError as e:
            db.rollback()
            raise ErrorHandler("There was an error while adding a product. Please try again later.")

        except Exception as e:
            db.rollback()  
            raise ErrorHandler(f"An unexpected error occurred: {str(e)}")
