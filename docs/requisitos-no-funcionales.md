# Requisitos no funcionales

Los siguientes requisitos no funcionales (RNF) se derivan de la justificación de una arquitectura distribuida para el sistema de soporte técnico ISP.

## 1. Disponibilidad

El sistema debe permanecer operativo ante la falla de un componente individual. La caída de un proceso no debe interrumpir el servicio completo de soporte.

**Criterio verificable:** Si un proceso se detiene, los demás continúan respondiendo.

## 2. Escalabilidad

El sistema debe permitir el crecimiento del volumen de solicitudes sin degradación significativa del rendimiento. Cada componente debe poder escalar de forma independiente.

**Criterio verificable:** El agregado de instancias de un componente no requiere modificaciones en los demás.

## 3. Mantenibilidad

Cada componente del sistema debe ser modificable sin afectar a los demás. Los cambios en un módulo (por ejemplo, la lógica de autenticación) no deben forzar cambios en otros módulos.

**Criterio verificable:** Una modificación funcional en un componente no genera cambios en componentes dependientes.

## 4. Comunicación confiable

Los procesos del sistema deben comunicarse de forma ordenada y consistente. Los eventos deben respetar el orden causal entre componentes.

**Criterio verificable:** El reloj lógico de Lamport mantiene el orden causal de eventos entre sockets y gRPC.

## 5. Trazabilidad

Cada acción sobre una solicitud debe quedar registrada con un identificador temporal que permita reconstruir la secuencia de eventos.

**Criterio verificable:** Es posible reconstruir el historial completo de una solicitud a partir de los registros del sistema.

## 6. Fuentes

- **E3:** "los requisitos no funcionales" — uno de los 4 pilares obligatorios de la entrega E1.
- **E2, capítulo 1:** justificación distribuida (disponibilidad, escalabilidad, aislamiento de cambios) como base para los RNF.
