import net.server as NetworkServer
from world import World

async def boot():
    ## Create the server
    serv =  NetworkServer.Server()
    await serv.start()

    ## Create the world
    world = World()
    ## Start the server
    await world.start()
    ## Listen to network events
    world.world_network_event_pipeline.listen(serv.events)
    
# asyncio.run(boot())

