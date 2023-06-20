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

    WorldNetworkEventPublisher(
        world=world
    ).listen(serv.events)
    
# asyncio.run(boot())

