class Scene:
    pass

class Select(Scene):
    pass

class Decide(Scene):
    pass

class Play(Scene):
    pass

class Result(Scene):
    pass

class Quit(Scene):
    pass
    
SCENE_MATCHES = {
    'bms.player.beatoraja.MainController$SystemSoundManager shuffle': Select,
    'bms.player.beatoraja.SystemSoundManager shuffle': Select,
    'bms.player.beatoraja.play.BMSPlayer create': Play,
    'bms.player.beatoraja.result.MusicResult updateScoreDatabase': Result,
    'bms.player.beatoraja.PlayDataAccessor writeScoreData': Result,
    'alc_cleanup:': Quit,
    'bms.player.beatoraja.MainController dispose': Quit,
}
