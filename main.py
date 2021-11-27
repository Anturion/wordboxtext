from fastapi import FastAPI
from src.routes.register import registry_routes
from connection_database.database_connection import Base, engine_azure

Base.metadata.create_all(bind=engine_azure)

app = FastAPI()

app.include_router(registry_routes)
