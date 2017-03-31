from . import fade_in, shake, fade_out, colour_fade

class behavior_handler(object):
    def __init__(self, pygame):
        self.pygame = pygame
        
        self.reference = {
            "fade-in": fade_in.main,
            "shake": shake.main,
            "fade-out": fade_out.main,
            "colour-fade": colour_fade.main
        }
        
    def add(self, option, ref, entity, args):
        return self.reference[option](ref, entity, args)
        