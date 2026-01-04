# Equity - Control de Gastos Personales

Aplicación para el control de gastos personales con integridad de datos financieros.

## Stack Tecnológico

| Capa | Tecnología |
|------|------------|
| **Backend** | FastAPI + SQLModel |
| **Base de Datos** | MySQL 8.0 |
| **Frontend** | React + Vite + Tailwind CSS |
| **Contenedores** | Docker + Docker Compose |

## Requisitos

- Docker y Docker Compose
- Python 3.12+ con venv (para desarrollo local)

## Inicio Rápido

### Desarrollo

El entorno de desarrollo usa MySQL en Docker y el backend corre localmente con Python/venv para facilitar hot-reload y debugging:

```bash
# 1. Levantar base de datos MySQL
docker compose -f docker-compose.dev.yml up -d

# 2. Verificar que MySQL está listo
docker compose -f docker-compose.dev.yml ps

# 3. Activar entorno virtual e instalar dependencias
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 4. Ejecutar backend
uvicorn main:app --reload

# 5. Parar MySQL cuando termines
docker compose -f docker-compose.dev.yml down
```

La API estará disponible en: http://localhost:8000

**Credenciales MySQL Dev:**
- Host: `localhost:3306`
- Database: `equity_dev`
- User: `equity_user`
- Password: `equity_pass`

### Tests

```bash
# Levantar MySQL efímera para tests (puerto 3307)
docker compose -f docker-compose.test.yml up -d

# Ejecutar tests
cd backend && pytest

# Limpiar (la DB se destruye automáticamente al parar)
docker compose -f docker-compose.test.yml down
```

### Producción

```bash
# Configurar variables de entorno
cp .env.example .env
# Editar .env con valores seguros

# Levantar producción (backend + MySQL containerizados)
docker compose -f docker-compose.prod.yml up -d
```

## Estructura del Proyecto

```
equity/
├── backend/
│   ├── Dockerfile
│   ├── main.py
│   ├── requirements.txt
│   ├── database/
│   └── routers/
├── frontend/
├── docs/
│   └── requerimientos/
├── docker-compose.dev.yml
├── docker-compose.test.yml
├── docker-compose.prod.yml
└── .env.example
```

## Entornos Docker

| Entorno | Archivo | DB | Puerto MySQL | Características |
|---------|---------|-----|--------------|-----------------|
| **Dev** | `docker-compose.dev.yml` | Persistente | 3306 | Solo MySQL, backend local |
| **Test** | `docker-compose.test.yml` | Efímera (tmpfs) | 3307 | Se destruye al parar |
| **Prod** | `docker-compose.prod.yml` | Persistente | No expuesto | Backend + DB containerizados, 4 workers |

## Documentación

- [Requerimientos Funcionales](docs/requerimientos/RF.md)
- [Requerimientos No Funcionales](docs/requerimientos/RNF.md)
- [Priorización MoSCoW](docs/requerimientos/MOSCOW.md)

## Licencia

Ver [LICENSE](LICENSE)