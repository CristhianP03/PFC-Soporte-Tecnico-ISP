import grpc
from concurrent import futures
import ticket_pb2
import ticket_pb2_grpc
import uuid


class SoporteServicer(ticket_pb2_grpc.SoporteServiceServicer):
    def __init__(self):
        self.tickets = {}

    def CrearTicket(self, request, context):
        ticket_id = str(uuid.uuid4())[:8]
        lamport = request.lamport_timestamp + 1
        self.tickets[ticket_id] = {
            "asunto": request.asunto,
            "estado": "registrado",
            "lamport": lamport,
        }
        print(f"[GRPC-SERVIDOR] Ticket creado: {ticket_id} | Lamport: {lamport}")
        return ticket_pb2.TicketResponse(
            ticket_id=ticket_id,
            estado="registrado",
            lamport_timestamp=lamport,
            mensaje=f"Ticket '{request.asunto}' creado exitosamente",
        )

    def ConsultarTicket(self, request, context):
        ticket = self.tickets.get(request.ticket_id)
        if ticket:
            return ticket_pb2.TicketResponse(
                ticket_id=request.ticket_id,
                estado=ticket["estado"],
                lamport_timestamp=ticket["lamport"],
                mensaje="Ticket encontrado",
            )
        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details("Ticket no encontrado")
        return ticket_pb2.TicketResponse()


def servir():
    servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ticket_pb2_grpc.add_SoporteServiceServicer_to_server(SoporteServicer(), servidor)
    servidor.add_insecure_port("[::]:50051")
    servidor.start()
    print("[GRPC-SERVIDOR] Servidor gRPC escuchando en puerto 50051")
    servidor.wait_for_termination()


if __name__ == "__main__":
    servir()
