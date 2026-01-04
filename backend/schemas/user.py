"""User schemas for API validation."""

from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    """Schema for creating a new user."""

    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    name: str = Field(max_length=100)
    apellidos: str = Field(max_length=100)
    password: str = Field(min_length=8, max_length=100)


class UserRead(BaseModel):
    """Schema for reading user data (public response)."""

    id: int
    username: str
    email: str
    name: str
    apellidos: str
    verified: bool
    disabled: bool


class UserUpdate(BaseModel):
    """Schema for updating user data."""

    name: str | None = Field(default=None, max_length=100)
    apellidos: str | None = Field(default=None, max_length=100)
    email: EmailStr | None = None
