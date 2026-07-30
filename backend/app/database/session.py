from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from typing import AsyncGenerator
from app.config.settings import settings

# Create async engine with asyncpg
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,  # Useful for debugging SQL statements in dev environments
)

# Async session factory
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency that yields an async database session for route handlers.
    Closes the connection context when the handler finishes execution.
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
