import net.server as NetworkServer
import asyncio
import ctypes
import inspect
from net.packets import incoming_packets

async def boot():
    await NetworkServer.Server().start()  
    
# asyncio.run(boot())


for k,v in incoming_packets.items():
    print(k,v)
