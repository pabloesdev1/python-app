from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from typing import List
from models.Developer import Developer
from models.Skill import Skill


class DeveloperSevice():

    def __init__(self, db):
        self.db = db


    async def get_developers(self) -> List[Developer]:
        developers: List[Developer] = await self.db.developers.find().to_list(1000)
        for developer in developers: developer['_id'] = str(developer['_id'])
        return developers


    async def get_developer(self, id: str) -> Developer:
        developer: Developer = await self.db.developers.find_one({"_id": ObjectId(id)})
        developer['_id'] = str(developer['_id'])
        return developer


    async def get_skills(self, id: str) -> List[Skill]:
        developer: Developer = await self.db.developers.find_one({"_id": ObjectId(id)})
        developer['_id'] = str(developer['_id'])
        return developer['skills']


    async def create_developer(self, developer: Developer) -> None:
        await self.db.developers.insert_one(jsonable_encoder(developer))


    async def update_developer(self, id:str, data: Developer) -> None:
        await self.db.developers.update_one({'_id': ObjectId(id)}, {'$set': jsonable_encoder(data)})


    async def delete_developer(self, id:str) -> None:
        await self.db.developers.delete_one({'_id': ObjectId(id)})