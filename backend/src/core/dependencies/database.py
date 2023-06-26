from sqlalchemy.ext.asyncio import AsyncSession

from core.database.session import AsyncSessionLocal


async def get_async_db_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
