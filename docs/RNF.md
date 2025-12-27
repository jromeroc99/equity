# Requisitos No Funcionales (RNF)

## RNF-001: Integridad de Datos Financieros
- Valores monetarios deben usar **DECIMAL(12,2)** en BD
- Usar tipo `Decimal` en Python para cálculos
- Transacciones deben ser atómicas (rollback en caso de error)

## RNF-002: Seguridad
- Autenticación obligatoria para todos los endpoints
- Validación de permisos (usuarios solo acceden a sus propios datos)
- Hash seguro para contraseñas (bcrypt/argon2)

## RNF-003: Rendimiento
- Consultas de balance < 500ms
- Soportar hasta 10,000 transacciones por usuario
- Importación CSV procesada en background para archivos grandes

## RNF-004: Usabilidad
- Confirmaciones explícitas para acciones destructivas
- Mensajes de error claros y accionables
- Feedback inmediato en operaciones CRUD

## RNF-005: Mantenibilidad
- Type hints completos en Python
- Docstrings en funciones críticas
- Cobertura de tests > 80% en lógica financiera
- Código siguiendo PEP 8

## RNF-006: Escalabilidad
- Estructura preparada para añadir multi-moneda en futuro
- API REST bien documentada (OpenAPI)
- Frontend desacoplado del backend

## RNF-007: Entorno de Desarrollo
- Desarrollo en WSL2 (filesystem Linux)
- MySQL local sin Docker (por ahora)
- Docker solo al final para producción
