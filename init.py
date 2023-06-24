import asyncio
import os
import net.server 
import world
import sub
import inspect
import functools

async def boot():
    ## Create the server
    serv =  net.server.Server()
    await serv.start()

    ## Create the world
    game_world = world.World()
    ## Start the server
    await game_world.start()
    ## Listen to network events

    sub.WorldNetworkEventSubscriber(
        world=world
    ).listen(serv.events)
    
# asyncio.run(boot())
