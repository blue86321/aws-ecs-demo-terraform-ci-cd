import socket

from fastapi import FastAPI
from src.database import Base, create_db, engine
# Import all models so that `create_all` can create tables automatically
from src.models import *
from src.routes import items

create_db()
# create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(items.router)


@app.get("/")
def root():
    return {"Hello": f"World, I'm {socket.gethostname()}"}
