import asyncio
import os
import net.server 
import world
import publishers
import loaders 

async def boot():
    ## Create the server
    serv =  net.server.Server()
    await serv.start()

    ## Create the world
    world = world.World()
    ## Start the server
    await world.start()
    ## Listen to network events

    publishers.WorldNetworkEventPublisher(
        world=world
    ).listen(serv.events)
    
# asyncio.run(boot())


async def go():
    plugin_loader = loaders.py_plugin_loader.PluginLoader()
    result = await plugin_loader.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'plugins'))
    for module in result:
        print(module)
        module.boot()
asyncio.run(go())
