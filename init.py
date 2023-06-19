import net.server as NetworkServer
from world import World




async def boot():
    server =  NetworkServer.Server()
    await server.start()  

    world = World()

    WorldEventPipeline(server=server, world=World()).process()
    
    
# asyncio.run(boot())

