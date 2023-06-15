import net.server as NetworkServer
import asyncio
import ctypes
import inspect
async def boot():
    await NetworkServer.Server().start()  
    
asyncio.run(boot())
