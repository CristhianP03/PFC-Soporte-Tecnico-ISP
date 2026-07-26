# Problema y justificación

## 1. Contexto

Los proveedores de servicios de Internet (ISP) gestionan soporte técnico mediante canales informales: correo electrónico, llamadas telefónicas y mensajería instantánea. Esta operación descentralizada genera una serie de problemas recurrentes:

- **Desorganización:** las solicitudes se pierden entre canales, sin un registro único y centralizado.
- **Pérdida de información:** no existe trazabilidad del historial de interacciones entre cliente y técnico.
- **Duplicidad de esfuerzo:** múltiples técnicos pueden atender la misma solicitud sin coordinación.
- **Falta de métricas:** no se pueden medir tiempos de respuesta, resolución o satisfacción del cliente.

## 2. Problema

No existe un sistema formal que centralice la gestión de solicitudes de soporte técnico, permita el seguimiento de cada caso a lo largo de su ciclo de vida y proporcione visibilidad al equipo administrativo sobre el estado general del servicio.

## 3. Justificación de una arquitectura distribuida

La naturaleza del problema justifica una solución distribuida por las siguientes razones:

| Razón | Explicación |
|-------|-------------|
| **Disponibilidad** | Un punto único de fallo no debe dejar fuera todo el sistema de soporte. |
| **Escalabilidad** | El volumen de solicitudes puede crecer de forma desordenada; el sistema debe escalar por componentes independientes. |
| **Aislamiento de cambios** | Cada funcionalidad (autenticación, gestión de tickets, notificaciones) debe poder evolucionar sin afectar a las demás. |

> **Fuente:** Capítulo 1 del documento E2 (sección 1.1), aplicado al dominio de soporte técnico ISP.

## 4. Objetivo

Diseñar e implementar un sistema distribuido de gestión de soporte técnico que:

1. Centralice la recepción, asignación y seguimiento de solicitudes.
2. Permita la comunicación confiable entre los procesos del sistema.
3. Garantice la disponibilidad y escalabilidad del servicio.
4. Proporcione métricas auditable del ciclo de vida de cada solicitud.
