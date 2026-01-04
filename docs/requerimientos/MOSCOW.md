# Priorización MoSCoW

## ✅ Must Have (MVP - Fase 1)

### Backend
- **HU-001**: Registrar movimientos bancarios
- **HU-002**: Gestionar catálogos (categorías, cuentas)
- **RF-001**: CRUD completo de cuentas
- **RF-002**: CRUD de categorías
- **RF-003**: Transacciones bancarias básicas
- Autenticación de usuarios
- Cálculo de balances

### Frontend
- Login/Registro
- Dashboard con balance total
- Formularios de transacciones
- Lista de movimientos recientes

---

## 🟡 Should Have (V1 - Fase 2)

- **HU-003**: Registrar movimientos de activos
- **HU-004**: Registrar movimientos de pasivos
- **RF-004**: Gestión completa de activos
- **RF-005**: Gestión completa de pasivos
- Gráficos básicos (ingresos vs gastos)
- Filtros por fecha y categoría
- Exportar a CSV

---

## 🟦 Could Have (V2 - Fase 3)

- **HU-000**: Importación masiva CSV
- **HU-006**: Reportes avanzados
- Dashboard con gráficos detallados
- Presupuestos por categoría
- Metas de ahorro
- Notificaciones

---

## ⭕ Won't Have (Futuro)

- Multi-moneda (solo EUR por ahora)
- APIs de precios en tiempo real
- Sincronización bancaria automática
- App móvil nativa
- Multi-tenancy

---

## 🎯 Orden de Desarrollo

1. **Backend Must Have** → Testing → ✓
2. **Frontend Must Have** → Integración → ✓
3. **Backend Should Have** → Testing → ✓
4. **Frontend Should Have** → Integración → ✓
5. **Features Could Have** según prioridad
6. **Dockerización** cuando todo funcione en local
