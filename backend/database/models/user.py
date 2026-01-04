"""User model for authentication."""

from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    """Base user schema with shared attributes."""

    username: str = Field(unique=True, index=True, max_length=50)
    email: str = Field(unique=True, index=True, max_length=255)
    name: str = Field(max_length=100)
    apellidos: str = Field(max_length=100)


class User(UserBase, table=True):
    """User database model."""

    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str = Field(max_length=255)
    verified: bool = Field(default=False)
    disabled: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class UserCreate(UserBase):
    """Schema for creating a new user."""

    password: str = Field(min_length=8, max_length=100)


class UserRead(UserBase):
    """Schema for reading user data (public response)."""

    id: int
    verified: bool
    disabled: bool


class UserUpdate(SQLModel):
    """Schema for updating user data."""

    name: Optional[str] = Field(default=None, max_length=100)
    apellidos: Optional[str] = Field(default=None, max_length=100)
    email: Optional[str] = Field(default=None, max_length=255)
