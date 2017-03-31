class Player(object):
    def __init__(self, pygame, **kwargs):
        self.pygame = pygame
        self.kwargs = kwargs
        
        self.ref = self.pygame.image.load(self.kwargs["ref"]) # Player icon
        self.x = self.kwargs["x"]
        self.y = self.kwargs["y"]
        
        self.behaviors = []
        
    def get_keys(self):
        """
        what keys are being pressed?
        """
        keys = self.pygame.key.get_pressed()
        if keys[self.pygame.K_a]:
            self.x -= 1
            
        elif keys[self.pygame.K_d]:
            self.x += 1
        
        if keys[self.pygame.K_w]:
            self.y -= 1
            
        elif keys[self.pygame.K_s]:
            self.y += 1
                    
    def draw(self):
        to_remove = []
        if self.behaviors:
            for behavior in self.behaviors:
                #print("player: " + str(behavior))
                self.ref, self = behavior.update(self.ref, self)
                
                if getattr(behavior, "kill", False):
                    to_remove.append(behavior)
                
        for _ in to_remove:
            self.behaviors.remove(behavior)
            
        self.get_keys()
            
        self.pygame.main_screen.blit(self.ref, (self.x, self.y))