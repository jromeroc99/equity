"""Database engine configuration."""

import os
from typing import Generator

from sqlmodel import Session, SQLModel, create_engine

# Load DATABASE_URL from environment
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://equity_user:equity_pass@localhost:3306/equity_dev"
)

engine = create_engine(DATABASE_URL, echo=False)


def create_db_and_tables() -> None:
    """Create all database tables."""
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    """Dependency that provides a database session."""
    with Session(engine) as session:
        yield session