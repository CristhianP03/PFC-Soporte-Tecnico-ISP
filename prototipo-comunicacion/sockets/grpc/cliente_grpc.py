import grpc
import ticket_pb2
import ticket_pb2_grpc


def crear_ticket(stub, asunto, lamport_timestamp=0):
    response = stub.CrearTicket(
        ticket_pb2.TicketRequest(
            asunto=asunto,
            descripcion=f"Solicitud de soporte: {asunto}",
            lamport_timestamp=lamport_timestamp,
        )
    )
    print(
        f"[GRPC-CLIENTE] Ticket creado: {response.ticket_id} | "
        f"Estado: {response.estado} | Lamport: {response.lamport_timestamp}"
    )
    return response


def consultar_ticket(stub, ticket_id):
    response = stub.ConsultarTicket(ticket_pb2.ConsultarRequest(ticket_id=ticket_id))
    print(
        f"[GRPC-CLIENTE] Consulta: {response.ticket_id} | "
        f"Estado: {response.estado} | Lamport: {response.lamport_timestamp}"
    )
    return response


def main():
    channel = grpc.insecure_channel("localhost:50051")
    stub = ticket_pb2_grpc.SoporteServiceStub(channel)

    print("[GRPC-CLIENTE] Creando ticket...")
    resp = crear_ticket(stub, "路由器 no responde", lamport_timestamp=0)

    print("[GRPC-CLIENTE] Consultando ticket...")
    consultar_ticket(stub, resp.ticket_id)


if __name__ == "__main__":
    main()
