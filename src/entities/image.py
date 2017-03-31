import time

class Image(object):
    def __init__(self, pygame, **kwargs):
        self.pygame = pygame
        
        self.kwargs = kwargs
        
        self.x = self.kwargs["x"]
        self.y = self.kwargs["y"]
        self.ref = pygame.image.load(self.kwargs["ref"])
    
        self.behaviors = []
    
    def draw(self):
        to_remove = []
        if self.behaviors:
            for behavior in self.behaviors:
                #print("image: " + str(behavior))
                self.ref, self = behavior.update(self.ref, self)
                
                if getattr(behavior, "kill", False):
                    to_remove.append(behavior)
                
        for _ in to_remove:
            self.behaviors.remove(behavior)
        
        self.pygame.main_screen.blit(self.ref, (self.x, self.y))       
        
    