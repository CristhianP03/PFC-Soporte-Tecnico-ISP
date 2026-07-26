import threading
import time


class RelojLamport:
    """Implementación del reloj lógico de Lamport."""

    def __init__(self):
        self._contador = 0
        self._lock = threading.Lock()

    @property
    def valor(self):
        with self._lock:
            return self._contador

    def incrementar(self):
        """Incrementa el reloj local (evento interno o envío)."""
        with self._lock:
            self._contador += 1
            return self._contador

    def actualizar(self, timestamp_recibido):
        """Actualiza el reloj al recibir un mensaje: max(local, recibido) + 1."""
        with self._lock:
            self._contador = max(self._contador, timestamp_recibido) + 1
            return self._contador

    def __repr__(self):
        return f"RelojLamport({self._contador})"


def simular_eventos():
    """Simula una secuencia de eventos entre dos procesos distribuidos."""

    reloj_a = RelojLamport()
    reloj_b = RelojLamport()

    print("=== Simulacion de reloj logico de Lamport ===\n")

    # Proceso A: evento interno
    ts1 = reloj_a.incrementar()
    print(f"[A] Evento interno          -> Lamport = {ts1}")

    # Proceso A: envia mensaje a B
    ts2 = reloj_a.incrementar()
    print(f"[A] Envia mensaje a B       -> Lamport = {ts2}")

    # Simular latencia de red
    time.sleep(0.1)

    # Proceso B: recibe mensaje de A
    ts3 = reloj_b.actualizar(ts2)
    print(f"[B] Recibe mensaje de A     -> Lamport = {ts3} (max({reloj_b._contador}, {ts2}) + 1)")

    # Proceso B: evento interno
    ts4 = reloj_b.incrementar()
    print(f"[B] Evento interno          -> Lamport = {ts4}")

    # Proceso B: envia respuesta a A
    ts5 = reloj_b.incrementar()
    print(f"[B] Envia respuesta a A     -> Lamport = {ts5}")

    # Simular latencia de red
    time.sleep(0.1)

    # Proceso A: recibe respuesta de B
    ts6 = reloj_a.actualizar(ts5)
    print(f"[A] Recibe respuesta de B   -> Lamport = {ts6} (max({reloj_a._contador}, {ts5}) + 1)")

    print(f"\nEstado final: A={reloj_a}, B={reloj_b}")
    print("\n=== Verificacion de orden causal ===")
    print(f"  Envio de A (ts={ts2}) < Recepcion de B (ts={ts3}): {ts2 < ts3}")
    print(f"  Envio de B (ts={ts5}) < Recepcion de A (ts={ts6}): {ts5 < ts6}")


def integrar_con_socket():
    """Demostración de integración con sockets TCP."""
    import socket
    import json
    import threading

    HOST = "127.0.0.1"
    PORT = 65435

    reloj_servidor = RelojLamport()

    def servidor():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((HOST, PORT))
            s.listen(1)
            conn, _ = s.accept()
            with conn:
                data = conn.recv(4096)
                msg = json.loads(data.decode())
                ts = reloj_servidor.actualizar(msg["lamport"])
                print(f"\n[LAMPORT-SERVIDOR] Recibido Lamport={msg['lamport']} -> Actualizado={ts}")
                respuesta = {"status": "ok", "lamport": ts}
                conn.sendall(json.dumps(respuesta).encode())

    def cliente():
        reloj_cliente = RelojLamport()
        time.sleep(0.2)
        ts = reloj_cliente.incrementar()
        msg = {"asunto": "Test Lamport + Socket", "lamport": ts}
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(json.dumps(msg).encode())
            data = s.recv(4096)
            resp = json.loads(data.decode())
            print(f"[LAMPORT-CLIENTE] Enviado Lamport={ts} -> Respuesta Lamport={resp['lamport']}")

    print("\n=== Integracion Lamport + Socket ===")
    t_serv = threading.Thread(target=servidor, daemon=True)
    t_serv.start()
    cliente()
    t_serv.join(timeout=2)


if __name__ == "__main__":
    simular_eventos()
    integrar_con_socket()
