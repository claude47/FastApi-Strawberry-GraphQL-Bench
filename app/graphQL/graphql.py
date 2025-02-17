import strawberry
from .schemas import Query, Mutation  

schema = strawberry.Schema(query=Query, mutation=Mutation)
