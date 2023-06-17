from .incoming_packets import *
from .outgoing_packets import *
from .packet import packet

incoming_packets = {
   LoginPacket.id: LoginPacket,
   MovementPacket.id: MovementPacket
}

outgoing_packets = [
    
]