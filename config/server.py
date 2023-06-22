from .parser import parser

################################
# Server vars
################################

HOST = parser.get('server', 'host', fallback='localhost')
PORT = parser.get('server', 'port', fallback=5855)
INC_SOCKET_BUFFER_LIMIT = parser.get(
    'server', 'inc_socket_buffer_limit', fallback=1024)
