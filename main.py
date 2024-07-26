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
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

fake_items = [{"item_name": "barsa"}, {"item_name": "arsenal"}, {"item_name": "liverpool"},
              {"item_name": "zenit"}, {"item_name": "cska"}, {"item_name": "real"},
              {"item_name": "manchester"}, {"item_name": "tottenham"}, {"item_name": "juventus"},
              {"item_name": "liverpool"}, {"item_name": "out of limit"}
              ]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):  # ограничения для количества элементов массива
    return fake_items[skip: skip + limit]


@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}
