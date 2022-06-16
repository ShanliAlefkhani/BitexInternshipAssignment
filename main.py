from fastapi import FastAPI
from pydantic import BaseModel
from redis import Redis
import config
from typing import Union


settings = config.Settings()
redis = Redis(
    host=settings.redis_host,
    port=settings.redis_port,
    password=settings.redis_password,
    db=settings.redis_db,
    charset="utf-8",
    decode_responses=True,
)

item_type = Union[str, int]


class Item(BaseModel):
    key: item_type
    value: item_type


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Bitex"}


@app.get("/get/{key}")
async def get_key(key: item_type):
    return {"message": f"Value of key {key} is {redis.lindex(key, -1)}"}


@app.get("/history/{key}")
async def get_key_history(key: item_type):
    return {"message": f"History of {key} is {redis.lrange(key, 0, -1)}"}


@app.post("/set/")
async def set_value(item: Item):
    redis.rpush(item.key, item.value)
    return {"message": f"Value of {item.key} set to {item.value}"}
