import motor.motor_asyncio

async def connection():
    client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
    db = client['apivelopers']
    return db