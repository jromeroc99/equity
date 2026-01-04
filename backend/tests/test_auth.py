"""Tests for authentication endpoints."""

import pytest
from sqlmodel import Session, select

from database.models import User


class TestRegister:
    """Tests for POST /auth/register."""

    def test_register_success(self, client, test_user_data, session):
        """Test successful user registration."""
        response = client.post("/auth/register", json=test_user_data)

        assert response.status_code == 201
        data = response.json()
        assert data["username"] == test_user_data["username"]
        assert data["email"] == test_user_data["email"]
        assert data["name"] == test_user_data["name"]
        assert data["apellidos"] == test_user_data["apellidos"]
        assert data["verified"] is False
        assert data["disabled"] is False
        assert "password" not in data
        assert "hashed_password" not in data

        # Cleanup
        user = session.exec(select(User).where(User.username == test_user_data["username"])).first()
        if user:
            session.delete(user)
            session.commit()

    def test_register_duplicate_username(self, client, test_user_data, session):
        """Test registration fails with duplicate username."""
        # Create first user
        response1 = client.post("/auth/register", json=test_user_data)
        assert response1.status_code == 201

        # Try to create second user with same username
        response2 = client.post("/auth/register", json=test_user_data)
        assert response2.status_code == 400
        assert "Username already registered" in response2.json()["detail"]

        # Cleanup
        user = session.exec(select(User).where(User.username == test_user_data["username"])).first()
        if user:
            session.delete(user)
            session.commit()

    def test_register_duplicate_email(self, client, test_user_data, session):
        """Test registration fails with duplicate email."""
        # Create first user
        response1 = client.post("/auth/register", json=test_user_data)
        assert response1.status_code == 201

        # Try to create second user with same email but different username
        user_data2 = test_user_data.copy()
        user_data2["username"] = "differentuser"
        response2 = client.post("/auth/register", json=user_data2)
        assert response2.status_code == 400
        assert "Email already registered" in response2.json()["detail"]

        # Cleanup
        user = session.exec(select(User).where(User.username == test_user_data["username"])).first()
        if user:
            session.delete(user)
            session.commit()

    def test_register_invalid_password_too_short(self, client, test_user_data):
        """Test registration fails with short password."""
        user_data = test_user_data.copy()
        user_data["password"] = "short"
        response = client.post("/auth/register", json=user_data)
        assert response.status_code == 422  # Validation error


class TestLogin:
    """Tests for POST /auth/login."""

    def test_login_success(self, client, test_user_data, session):
        """Test successful login returns JWT token."""
        # Register user first
        client.post("/auth/register", json=test_user_data)

        # Login
        response = client.post(
            "/auth/login",
            data={
                "username": test_user_data["username"],
                "password": test_user_data["password"],
            },
        )

        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"

        # Cleanup
        user = session.exec(select(User).where(User.username == test_user_data["username"])).first()
        if user:
            session.delete(user)
            session.commit()

    def test_login_wrong_password(self, client, test_user_data, session):
        """Test login fails with wrong password."""
        # Register user first
        client.post("/auth/register", json=test_user_data)

        # Login with wrong password
        response = client.post(
            "/auth/login",
            data={
                "username": test_user_data["username"],
                "password": "wrongpassword",
            },
        )

        assert response.status_code == 401
        assert "Incorrect username or password" in response.json()["detail"]

        # Cleanup
        user = session.exec(select(User).where(User.username == test_user_data["username"])).first()
        if user:
            session.delete(user)
            session.commit()

    def test_login_nonexistent_user(self, client):
        """Test login fails with nonexistent user."""
        response = client.post(
            "/auth/login",
            data={
                "username": "nonexistent",
                "password": "password123",
            },
        )

        assert response.status_code == 401


class TestMe:
    """Tests for GET /auth/me."""

    def test_me_authenticated(self, client, test_user_data, session):
        """Test getting current user with valid token."""
        # Register and login
        client.post("/auth/register", json=test_user_data)
        login_response = client.post(
            "/auth/login",
            data={
                "username": test_user_data["username"],
                "password": test_user_data["password"],
            },
        )
        token = login_response.json()["access_token"]

        # Get current user
        response = client.get(
            "/auth/me",
            headers={"Authorization": f"Bearer {token}"},
        )

        assert response.status_code == 200
        data = response.json()
        assert data["username"] == test_user_data["username"]
        assert data["email"] == test_user_data["email"]

        # Cleanup
        user = session.exec(select(User).where(User.username == test_user_data["username"])).first()
        if user:
            session.delete(user)
            session.commit()

    def test_me_unauthenticated(self, client):
        """Test getting current user without token fails."""
        response = client.get("/auth/me")
        assert response.status_code == 401

    def test_me_invalid_token(self, client):
        """Test getting current user with invalid token fails."""
        response = client.get(
            "/auth/me",
            headers={"Authorization": "Bearer invalidtoken"},
        )
        assert response.status_code == 401
