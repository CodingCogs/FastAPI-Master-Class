from beanie import init_beanie, PydanticObjectId
# from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import AsyncMongoClient
from typing import Optional, Any
from pydantic_settings import BaseSettings, SettingsConfigDict
from models.events import Event
from models.users import User
from pydantic import BaseModel

class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None
    SECRET_KEY : Optional[str] = None
    async def initialize_database(self):
        client = AsyncMongoClient(self.DATABASE_URL)
        await init_beanie(database=client.planner,
                            document_models=[Event,User])
    async def initialize_test_database(self):
        client = AsyncMongoClient(self.DATABASE_URL)
        await init_beanie(database=client.testdb,
                            document_models=[Event,User])
        
    model_config =SettingsConfigDict(env_file=".env")
    
class Database:
    
    def __init__(self, model):
        self.model = model
    
    async def save(self, document) -> None:
        await document.create()
        return None
    
    async def get(self, id: PydanticObjectId) -> Any:
        doc = await self.model.get(id)
        if doc:
            return doc
        return False
    
    async def get_all(self) -> list[Any]:
        docs = await self.model.find_all().to_list()
        return docs
    
    async def update(self, id: PydanticObjectId, body: BaseModel) -> Any:
        doc_id = id
        des_body = body.dict()
        des_body = {k:v for k,v in des_body.items() if v is not None}
        update_query = {'$set': {
            field: value for field, value in des_body.items()
        }}
        doc = await self.get(doc_id)
        if not doc:
            return False
        await doc.update(update_query)
        return doc
    
    async def delete(self, id: PydanticObjectId,) -> bool:
        doc = await self.get(id)
        if not doc:
            return False
        await doc.delete()
        return True