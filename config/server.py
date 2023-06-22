"""Server config"""
from . import config

HOST = config.get('server', 'host', fallback='localhost')
PORT = config.get('server', 'port', fallback=5855)
INC_SOCKET_BUFFER_LIMIT = config.get(
    'server', 'inc_socket_buffer_limit', fallback=1024)
