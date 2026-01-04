"""Pytest configuration and fixtures."""

import os

# Set test database URL BEFORE importing app modules
os.environ["DATABASE_URL"] = "mysql+pymysql://test_user:test_pass@localhost:3307/equity_test"

import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine

from main import app
from database.engine import engine


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    """Create all tables before tests and drop after."""
    SQLModel.metadata.create_all(engine)
    yield
    SQLModel.metadata.drop_all(engine)


@pytest.fixture(scope="function")
def session():
    """Provide a clean database session for each test."""
    with Session(engine) as session:
        yield session
        # Rollback any uncommitted changes
        session.rollback()


@pytest.fixture(scope="function")
def client():
    """Provide a test client for the FastAPI app."""
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def test_user_data():
    """Sample user data for testing."""
    return {
        "username": "testuser",
        "email": "test@example.com",
        "name": "Test",
        "apellidos": "User",
        "password": "testpassword123"
    }
