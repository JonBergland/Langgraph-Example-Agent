import asyncio
import getpass
import os
from graph.graph import Graph



async def _set_env(var: str):
    with open('config.py') as config_file:
        exec(config_file.read())

    

async def main():
    await _set_env("OPENAI_API_KEY")

    graph = Graph()
    graph.save_image()

    await graph.run_agent("What does is the result of the example method?")


    return 1



if __name__ == "__main__":
    
    asyncio.run(main())