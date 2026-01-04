"""Equity API - Personal expense control application."""

from fastapi import FastAPI

from routers import auth_router

app = FastAPI(
    title="Equity API",
    description="API para control de gastos personales",
    version="0.1.0",
)

# Include routers
app.include_router(auth_router)


@app.get("/")
def read_root():
    """Health check endpoint."""
    return {"status": "ok", "app": "Equity API"}