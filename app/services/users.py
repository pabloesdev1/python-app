from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from typing import List
from models.User import User


class UserService():

    def __init__(self, db):
        self.db = db


    async def get_users(self) -> List[User]:
        users: List[User] = await self.db.users.find().to_list(1000)
        for user in users: user['_id'] = str(user['_id'])
        return users


    async def get_user(self, id: str) -> User:
        user: User = await self.db.users.find_one({"_id": ObjectId(id)})
        user['_id'] = str(user['_id'])
        return user


    async def register(self, user: User) -> None:
        await self.db.users.insert_one(jsonable_encoder(user))


    async def login(self, user: User) -> None:
        pass
