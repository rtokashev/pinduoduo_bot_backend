from sqlalchemy.ext.asyncio import AsyncSession

from database.session import AsyncSessionLocal


async def get_async_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
