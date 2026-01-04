# Requisitos Funcionales (RF)

## RF-001: Gestión de Cuentas
- **RF-001.1**: Crear cuenta bancaria con nombre, balance inicial y divisa
- **RF-001.2**: Editar información de cuentas existentes
- **RF-001.3**: Eliminar cuenta con confirmación explícita (escribir nombre)
- **RF-001.4**: Eliminar en cascada todas las transacciones al eliminar cuenta

## RF-002: Gestión de Catálogos
- **RF-002.1**: Crear categorías con nombre, icono, color y tipo (normal, inversión, deuda, transferencia entre cuentas)
- **RF-002.2**: Editar categorías existentes
- **RF-002.3**: Eliminar categorías personalizadas
- **RF-002.4**: Crear/editar/eliminar activos (nombre, ticker, participaciones, precio medio de compra, icono, color)
- **RF-002.5**: Crear/editar/eliminar pasivos (nombre, acreedor,tipo_sistema,capital_pendiente,tin_actual,meses_restantes, icono, color)
- **RF-002.6**: Confirmación explícita antes de eliminar activos/pasivos

## RF-003: Transacciones Bancarias (core de la app)
- **RF-003.1**: Registrar ingreso/gasto con fecha, concepto, importe, cuenta y categoría
- **RF-003.2**: Actualizar balance de cuenta automáticamente
- **RF-003.3**: Añadir notas opcionales
- **RF-003.4**: Añadir activo/ pasivo directamente desde un movimiento bancario

## RF-004: Transacciones de Activos
- **RF-004.1**: Registrar compra/venta con fecha, activo, cantidad, precio unitario, divisa
- **RF-004.2**: Calcular total automáticamente (cantidad × precio) y actualizar precio medio de compra y actualizar tabla de activos


## RF-005: Transacciones de Pasivos
- **RF-005.1**: Registrar préstamo/pago con fecha, pasivo e importe
- **RF-005.2**: Calcular saldo pendiente automáticamente

## RF-006: Importación CSV
- **RF-006.1**: Descargar plantillas CSV para transacciones, activos y pasivos
- **RF-006.2**: Validar formato CSV (fechas, campos obligatorios, valores numéricos)
- **RF-006.3**: Mostrar resumen de validación con errores detectados
- **RF-006.4**: Crear automáticamente categorías/cuentas/activos/pasivos inexistentes
- **RF-006.5**: Confirmar importación exitosa con resumen de registros procesados
