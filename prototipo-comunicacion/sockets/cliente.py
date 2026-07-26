import socket
import json

HOST = "127.0.0.1"
PORT = 65432


def enviar_solicitud(asunto, lamport_tick=0):
    mensaje = {
        "asunto": asunto,
        "descripcion": f"Solicitud de soporte: {asunto}",
        "lamport": lamport_tick,
    }
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(json.dumps(mensaje).encode("utf-8"))
        data = s.recv(4096)
        respuesta = json.loads(data.decode("utf-8"))
        print(f"[CLIENTE] Respuesta: {respuesta}")
        return respuesta


if __name__ == "__main__":
    print("[CLIENTE] Enviando solicitud por socket TCP...")
    enviar_solicitud("No hay conexion a Internet")
