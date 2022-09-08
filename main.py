import asyncio
import simpleobsws
import subprocess

import beatoraja
import config


async def handle(socket, scene: beatoraja.Scene):
    target_scene_name = config.OBS_SCENES.get(scene, None)
    get_scene_request = simpleobsws.Request("GetCurrentProgramScene")
    response = await socket.call(get_scene_request)
    if not response.ok():
        print("Couldn't retrieve current scene!")
        return

    current_scene = response.responseData["currentProgramSceneName"]
    if target_scene_name is None or current_scene == target_scene_name:
        return

    set_scene_request = simpleobsws.Request("SetCurrentProgramScene", {"sceneName": target_scene_name})
    await socket.call(set_scene_request)


async def run():
    url = f"ws://{config.WEBSOCKET_HOST}:{config.WEBSOCKET_PORT}"
    socket = simpleobsws.WebSocketClient(url, config.WEBSOCKET_PASSWORD)
    await socket.connect()
    await socket.wait_until_identified()

    process = subprocess.Popen(config.GAME_PATH, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while True:
        output = process.stdout.readline()
        if output == '' or process.poll() is not None:
            break
        print('beatoraja:', output.decode().strip())
        for search, scene in beatoraja.SCENE_MATCHES.items():
            if search in str(output):
                print('Detected scene', scene)
                await handle(socket, scene)
    await handle(socket, beatoraja.Quit)


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
