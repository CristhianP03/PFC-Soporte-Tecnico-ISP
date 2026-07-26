# Estilo arquitectónico

## 1. Propuesta

El sistema de soporte técnico ISP se propone como una **arquitectura distribuida** compuesta por procesos independientes que se comunican mediante mecanismos de interproceso.

En esta primera entrega (E1) **no se definen los microservicios exactos**. Lo que se establece es:

- El estilo arquitectónico general (distribuido).
- Los mecanismos de comunicación entre procesos (sockets TCP y gRPC).
- El modelo de ordenamiento de eventos (reloj lógico de Lamport).

> **Nota:** La definición explícita de microservicios, contenedores y orquestación corresponde a la entrega E2.

## 2. Decisiones arquitectónicas de E1

| Decisión | Descripción | Estado |
|----------|-------------|--------|
| Estilo arquitectónico | Distribuido (procesos independientes) | Definido en E1 |
| Mecanismo de comunicación #1 | Sockets TCP | Prototipado en E1 |
| Mecanismo de comunicación #2 | gRPC | Prototipado en E1 |
| Modelo de ordenamiento | Reloj lógico de Lamport | Implementado en E1 |
| Número de microservicios | No definido explícitamente | Pendiente para E2 |
| Contenedores (Docker) | No definidos | Pendiente para E2 |
| Mensajería (Kafka) | No definida | Pendiente para E2 |

> **Fuente:** Tabla 1.3 del documento E2 (comparativa entre entregas).

## 3. Diagrama de contexto (nivel 1)

Ver [c4-nivel1.svg](diagrams/c4-nivel1.svg) para el diagrama completo.

![Diagrama de Contexto C4 Nivel 1](diagrams/c4-nivel1.svg)

Tres actores interactuan con el sistema:
- **Cliente** — crea solicitudes, recibe notificaciones de estado.
- **Tecnico** — recibe asignaciones, actualiza estado de tickets.
- **Administrador** — gestiona asignaciones, consulta reportes y metricas.

## 4. Mecanismos de comunicación (prototipo E1)

### 4.1. Sockets TCP

Comunicación directa cliente-servidor mediante archivos de socket. Útil para mensajes simples y bajo nivel.

### 4.2. gRPC

Comunicación basada en contratos definidos en Protocol Buffers. Permite tipado fuerte, generación automática de código y soporte para streaming.

### 4.3. Reloj lógico de Lamport

Implementación del algoritmo de Lamport para asignar timestamps lógicos a los eventos del sistema. Permite determinar el orden causal entre eventos en procesos distribuidos sin necesidad de reloj físico sincronizado.

## 5. Fuentes

- **E3:** "propusieron la arquitectura", "el estilo arquitectónico" — pilar obligatorio de E1.
- **E3:** "prototiparon la comunicación entre procesos con sockets y gRPC bajo el modelo lógico de Lamport" — entregable técnico específico de E1.
- **E2, tabla 1.3:** confirma que en E1 el número de microservicios "no [está] definido explícitamente".
