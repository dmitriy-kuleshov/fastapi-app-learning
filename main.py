from typing import Union
from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/models/{model_name")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "IDK this is ML model"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "Lenet is an ML model too"}

    return {"model_name": model_name, "message": "WWW"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}
