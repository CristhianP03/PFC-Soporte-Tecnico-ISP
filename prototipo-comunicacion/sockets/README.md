# Prototipo de comunicación entre procesos

Este directorio contiene el prototipo técnico de la entrega E1, que demuestra la comunicación entre procesos utilizando dos mecanismos y un modelo de ordenamiento de eventos.

## Componentes

### 1. Sockets TCP (`sockets/`)

Comunicación directa cliente-servidor mediante TCP sockets.

**Archivos:**
- `servidor.py` — Escucha conexiones TCP y procesa mensajes.
- `cliente.py` — Conecta al servidor y envía/recibe mensajes.

**Ejecución:**
```bash
# Terminal 1
python sockets/servidor.py

# Terminal 2
python sockets/cliente.py
```

### 2. gRPC (`grpc/`)

Comunicación basada en Protocol Buffers con contrato definido en `ticket.proto`.

**Archivos:**
- `ticket.proto` — Definición del servicio y mensajes.
- `servidor_grpc.py` — Implementación del servicio gRPC.
- `cliente_grpc.py` — Cliente que invoca operaciones del servicio.

**Prerrequisitos:**
```bash
pip install grpcio grpcio-tools
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ticket.proto
```

**Ejecución:**
```bash
# Terminal 1
python grpc/servidor_grpc.py

# Terminal 2
python grpc/cliente_grpc.py
```

### 3. Reloj lógico de Lamport (`lamport/`)

Implementación del algoritmo de Lamport para asignar timestamps lógicos a eventos en procesos distribuidos.

**Archivos:**
- `reloj_lamport.py` — Implementación del reloj lógico con integración a sockets y gRPC.

**Ejecución:**
```bash
python lamport/reloj_lamport.py
```

## Flujo del prototipo

1. El servidor TCP recibe una solicitud y la marca con un timestamp de Lamport.
2. El cliente gRPC envía una operación de creación de ticket, también marcada.
3. El reloj de Lamport garantiza el orden causal entre ambos mecanismos de comunicación.
