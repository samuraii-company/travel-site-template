import motor.motor_asyncio
from models import User, Orders


class Database:
    def __init__(self):
        self.connect = motor.motor_asyncio.AsyncIOMotorClient(
            "mongodb://mongodb:27017"
        )
        self.database = self.connect["fast-api"]
        self.users_table = self.database["users"]
        self.orders = self.database["orders"]

    def __del__(self):
        self.connect.close()

    async def get_one(self, id) -> dict:
        data = await self.users_table.find_one({"id": id})
        return data

    async def get_all(self):
        all_users = []
        data = self.users_table.find({})
        async for doc in data:
            all_users.append(User(**doc))
        return all_users
    
    async def get_all_orders(self):
        all_users = []
        data = self.orders.find({})
        async for doc in data:
            all_users.append(Orders(**doc))
        return all_users

    async def insert(self, insert_data):
        document = insert_data
        await self.users_table.insert_one(document)
        return document
    
    async def insert_orders(self, insert_data):
        document = insert_data
        await self.orders.insert_one(document)
        return document

    async def update(self, id, employee) -> bool:
        await self.users_table.update_one(
            {"id": id}, {"$set": {"employee": employee}}
        )
        return True

    async def delete(self, id):
        await self.users_table.delete_one({"id": id})
        return True