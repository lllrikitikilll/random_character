import os

from fastapi import FastAPI
from app.characters.router import router as router_character

app = FastAPI()


app.include_router(router_character)
