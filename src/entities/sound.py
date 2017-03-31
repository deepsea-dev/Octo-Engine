import time

class Sound(object):
    def __init__(self, pygame, **kwargs):
        self.pygame = pygame
        self.kwargs = kwargs
        
        self.sound = self.pygame.mixer.Sound(self.kwargs["ref"])
        
        self.init_time = time.time() + 8
        
    def draw(self): # not REALLY
        if time.time() > self.init_time and time.time() < self.init_time + 2:
            self.sound.play()