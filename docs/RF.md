# Requisitos Funcionales (RF)

## RF-001: Gestión de Cuentas
- **RF-001.1**: Crear cuenta bancaria con nombre, balance inicial y divisa
- **RF-001.2**: Editar información de cuentas existentes
- **RF-001.3**: Eliminar cuenta con confirmación explícita (escribir nombre)
- **RF-001.4**: Eliminar en cascada todas las transacciones al eliminar cuenta

## RF-002: Gestión de Catálogos
- **RF-002.1**: Crear categorías con nombre, icono, color y tipo (regular/transfer/investment)
- **RF-002.2**: Editar categorías existentes
- **RF-002.3**: Eliminar categorías personalizadas
- **RF-002.4**: Crear/editar/eliminar activos (nombre, símbolo, icono, color)
- **RF-002.5**: Crear/editar/eliminar pasivos (nombre, acreedor, icono, color)
- **RF-002.6**: Confirmación explícita antes de eliminar activos/pasivos

## RF-003: Transacciones Bancarias
- **RF-003.1**: Registrar ingreso/gasto con fecha, concepto, importe, cuenta y categoría
- **RF-003.2**: Actualizar balance de cuenta automáticamente
- **RF-003.3**: Añadir notas opcionales

## RF-004: Transacciones de Activos
- **RF-004.1**: Registrar compra/venta con fecha, activo, cantidad y precio unitario
- **RF-004.2**: Calcular total automáticamente (cantidad × precio)
- **RF-004.3**: Calcular balance actual del activo
- **RF-004.4**: Calcular precio promedio de compra ponderado

## RF-005: Transacciones de Pasivos
- **RF-005.1**: Registrar préstamo/pago con fecha, pasivo e importe
- **RF-005.2**: Calcular saldo pendiente automáticamente

## RF-006: Importación CSV
- **RF-006.1**: Descargar plantillas CSV para transacciones, activos y pasivos
- **RF-006.2**: Validar formato CSV (fechas, campos obligatorios, valores numéricos)
- **RF-006.3**: Mostrar resumen de validación con errores detectados
- **RF-006.4**: Crear automáticamente categorías/cuentas/activos/pasivos inexistentes
- **RF-006.5**: Confirmar importación exitosa con resumen de registros procesados
