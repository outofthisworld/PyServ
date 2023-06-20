import net.server as NetworkServer
from world import World
from publishers import WorldNetworkEventPublisher
from loaders import *
import os

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

plugin_loader = PluginLoader()
print('abs path: ' , os.path.join(os.path.dirname(os.path.abspath(__file__)), 'plugins'))
plugin_loader.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'plugins'))
print(plugin_loader.plugins)

