from fastapi import FastAPI, Depends, Request
from sqlalchemy.orm import Session
from .settings.database import engine, SessionLocal
from strawberry.fastapi import GraphQLRouter
from .models import *
from .graphQL.graphql import schema

product.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_context(request: Request):
    db = next(get_db())
    return {"db": db, "request": request}

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

graphql_app = GraphQLRouter(schema, context_getter=get_context)
app.include_router(graphql_app, prefix="/graphql")