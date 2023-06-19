import net.server as NetworkServer
from world import World




async def boot():
    (serv = await NetworkServer.Server()).start()
    World().event_pipeline.listen(serv.events)
    
# asyncio.run(boot())

