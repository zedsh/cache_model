from fastapi import FastAPI, HTTPException, status
from  sqlalchemy.sql.expression import func, select
from .models import *
from .schemas import *
import random
import string

from .config import settings
from .database import engine
from .exceptions import ResponseError
from .database import async_session_maker
from redis import asyncio as aioredis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/list")
async def read_root() -> UserListSchema:
     async with async_session_maker() as session:
         result = await session.execute(select(User).order_by(User.name))
         return UserListSchema(data=[UserSchema(id=item.id, name=item.name) for item in result.scalars().all()])


@app.get("/list_cached")
@cache()
async def read_root() -> UserListSchema:
    print('no cache!')
    async with async_session_maker() as session:
         result = await session.execute(select(User).order_by(User.name))
         return UserListSchema(data=[UserSchema(id=item.id, name=item.name) for item in result.scalars().all()])


@app.get("/make_fake_data")
async def make_fake_data():
    async with async_session_maker() as session:
        for x in range(1, 1000, 1):
            model = User(name=''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=200)))
            session.add(model)
        await session.commit()
    return {"success": True}


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://redis")
    print('runnn')
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")