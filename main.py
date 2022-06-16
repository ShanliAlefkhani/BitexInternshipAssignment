from fastapi import FastAPI
from pydantic import BaseModel
from redis import Redis
import config


settings = config.Settings()
redis = Redis(
    host=settings.redis_host,
    port=settings.redis_port,
    password=settings.redis_password,
    db=settings.redis_db,
)


class Item(BaseModel):
    key: int
    value: int


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Bitex"}


@app.get("/get/{key}")
async def get_key(key: int):
    return {"message": f"Value of key {key} is {int(redis.lindex(key, -1))}"}


@app.get("/history/{key}")
async def get_key_history(key: int):
    return {"message": f"History of {key} is {[int(x) for x in redis.lrange(key, 0, -1)]}"}


@app.post("/set/")
async def post_key(item: Item):
    redis.rpush(item.key, item.value)
    return {"message": f"Value of {item.key} set to {item.value}"}
