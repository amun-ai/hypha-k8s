from imjoy_rpc.hypha import connect_to_server
import asyncio

SERVER_URL = "https://ai.imjoy.io"

import docker


async def start_bot():
    client = docker.from_env()
    server = await connect_to_server(
        {"name": "docker-launcher", "server_url": SERVER_URL}
    )
    print(server.config)

    def launch(docker_image, command, context=None):
        return client.containers.run(docker_image, command)


    await server.register_service({
        "name": "docker-launcher",
        "id": "docker-launcher",
        "config": {
            "visibility": "public",
            "require_context": True,
            "run_in_executor": True,
        },
        "launch": launch
    })
    print("Code bot is ready to receive request!",  server.config)

server_url = "https://ai.imjoy.io"
loop = asyncio.get_event_loop()
task = loop.create_task(start_bot())
loop.run_forever()