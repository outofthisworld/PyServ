from .packet import packet

@packet(id=1)
class LoginPacket(object):
    pass

@packet(id=2)
class MovementPacket(object):
    pass