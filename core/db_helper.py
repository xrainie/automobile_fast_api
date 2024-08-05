from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from .config import settings


class DBHelper:
    def __init__(self, db_url: str, echo: bool = False) -> None:
        self.engine = create_async_engine(db_url, echo)
        self.session_factory = async_sessionmaker(
            bind=self.engine, autoflush=False, autocommit=False, expire_on_commit=False
        )


db_helper = DBHelper(settings.db_url, settings.echo)


async def get_db():
    session = db_helper.session_factory()

    try:
        yield session
    finally:
        session.aclose()
