import strawberry

@strawberry.type
class ProductType:
    id: int
    product_code: str
    product_name: str
    product_description: str


@strawberry.input
class CreateProductInput:
    product_code: str
    product_name: str
    product_description: str