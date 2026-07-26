# PFC — Soporte Técnico ISP

Sistema distribuido de gestión de soporte técnico para proveedores de servicios de Internet (ISP).

## Entregas

| Entrega | Descripción | Estado |
|---------|-------------|--------|
| **E1** | Problema fundamentado, arquitectura propuesta, prototipo de comunicación (sockets, gRPC, Lamport) | En progreso |
| E2 | Microservicios, Docker Compose, Kafka, API Gateway | Pendiente |
| E3 | CockroachDB, Spark, ADRs de fragmentación | Pendiente |

## Estructura del repositorio

```
proyecto-pfc/
├── README.md
├── pom.xml                          # proyecto Java (microservicios, E2+)
├── docs/
│   ├── problema-y-justificacion.md
│   ├── dominio-y-actores.md
│   ├── requisitos-no-funcionales.md
│   ├── estilo-arquitectonico.md
│   └── diagrams/
├── prototipo-comunicacion/          # prototipo técnico E1
│   ├── README.md
│   ├── sockets/
│   ├── grpc/
│   └── lamport/
├── entrega1/
│   └── (snapshot PDF de la entrega)
└── src/                             # código Java del sistema (E2+)
```

## Prototipo de comunicación (E1)

El directorio `prototipo-comunicacion/` contiene tres componentes:

- **sockets/** — Comunicación cliente-servidor mediante TCP sockets.
- **grpc/** — Servicio gRPC con definición de contrato `ticket.proto`.
- **lamport/** — Reloj lógico de Lamport para ordenar eventos causalmente entre los dos mecanismos de comunicación.

Ver [prototipo-comunicacion/README.md](prototipo-comunicacion/README.md) para instrucciones de ejecución.

## Tecnologías

- **E1:** Python (prototipo de comunicación)
- **E2+:** Java 21, Maven, Spring Boot, Docker, Kafka, API Gateway
