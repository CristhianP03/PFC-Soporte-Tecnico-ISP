# Dominio y actores

## 1. Dominio

El sistema abarca el ciclo de vida completo de una solicitud de soporte técnico en un ISP:

```
Creación → Clasificación → Asignación → Atención → Resolución → Cierre
```

Cada solicitud (ticket) representa una incidencia reportada por un cliente que requiere intervención técnica o administrativa.

## 2. Actores

| Actor | Rol | Interacciones principales |
|-------|-----|--------------------------|
| **Cliente** | Usuario del servicio de Internet que reporta una incidencia. | Crea solicitudes, consulta estado, recibe notificaciones de resolución. |
| **Técnico** | Profissional asignado para resolver la incidencia. | Recibe asignaciones, actualiza estado, registra acciones realizadas. |
| **Personal administrativo** | Supervisa y coordina el flujo de soporte. | Visualiza métricas, gestiona asignaciones, genera reportes. |

## 3. Ciclo de vida de una solicitud

```
┌─────────┐     ┌──────────────┐     ┌────────────┐     ┌───────────┐     ┌──────────┐
│ Cliente  │────▶│  Solicitud   │────▶│ Asignación │────▶│ Atención  │────▶│ Resuelto │
│ crea     │     │  registrada  │     │ a técnico  │     │ en curso  │     │          │
└─────────┘     └──────────────┘     └────────────┘     └───────────┘     └──────────┘
                                                                  │
                                                                  ▼
                                                           ┌───────────┐
                                                           │  Cerrado  │
                                                           └───────────┘
```

## 4. Fuentes

- **E3:** "quedaron establecidos el dominio, los actores" — requisito explícito de la entrega E1.
- **E2, capítulo 1:** actores identificados (Cliente, Técnico, Personal administrativo) y contexto de negocio aplicado al soporte técnico ISP.
