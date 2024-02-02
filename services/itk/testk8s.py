from imjoy_rpc.hypha import connect_to_server
import asyncio

SERVER_URL = "https://hypha.imjoy.io"

import kubernetes
from kubernetes import client, config, watch

async def start_bot():
    config.load_incluster_config()
    server = await connect_to_server(
        {"name":"kubernetes-launcher", "server_url": SERVER_URL}
        )
    print(server.config)

    def get_pods():
        v1 = client.CoreV1Api()
        print("Listing pods with their IPs:")
        ret = v1.list_pod_for_all_namespaces(watch=False)
        for i in ret.items:
            print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
        return ret

    async def launch(docker_image, command, context=None):
        return client.containers.run(docker_image, command)

    await server.register_service({
        "name": "kubernetes-launcher",
        "id": "kubernetes-launcher",
        "config": {
            "visibility": "public",
            "require_context": True,
            "run_in_executor": True,
        },
        "launch": launch
    })
    print("Code bot is ready to receive request!", server.config)

server_url = "https://hypha.imjoy.io"
loop = asyncio.get_event_loop()
task = loop.create_task(start_bot())
loop.run_forever()