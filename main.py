import subprocess
from obswebsocket import obsws, requests as obsrequests

import beatoraja
import config


def handle(socket, scene: beatoraja.Scene):
    name = config.OBS_SCENES.get(scene, None)
    if name is None or socket.call(obsrequests.GetCurrentScene()).getName() == name:
        return
    socket.call(obsrequests.SetCurrentScene(name))

def run():
    socket = obsws(config.WEBSOCKET_HOST, config.WEBSOCKET_PORT, config.WEBSOCKET_PASSWORD)
    socket.connect()
    process = subprocess.Popen(config.GAME_PATH, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while True:
        output = process.stdout.readline()
        if output == '' or process.poll() is not None:
            break
        print('beatoraja:', output.decode().strip())
        for search, scene in beatoraja.SCENE_MATCHES.items():
            if search in str(output):
                print('Detected scene', scene)
                handle(socket, scene)
    handle(socket, beatoraja.Quit)

run()
