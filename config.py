
import beatoraja

# REPLACE WITH YOUR OBS WEBSOCKETS SETTINGS (dont need to if you use default settings)
WEBSOCKET_HOST = '127.0.0.1'
WEBSOCKET_PORT = 4444
WEBSOCKET_PASSWORD = 'password'

# REPLACE WITH THE PATH TO THE SCRIPT YOU USE TO LAUNCH THE GAME
GAME_PATH = r'E:\Games\PC\BMS\Players\beatoraja0.8.1\config.bat'

# REPLACE THE TEXTS ON THE RIGHT WITH YOUR OBS SCENE NAMES
OBS_SCENES = {
    beatoraja.Select: 'BMS Select',
    beatoraja.Play: 'BMS Play',
    beatoraja.Result: 'BMS Result',
    beatoraja.Quit: 'Chatting',
}
