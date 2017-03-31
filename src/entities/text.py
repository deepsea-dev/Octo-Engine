import time

class Text(object):
    def __init__(self, pygame, **kwargs):
        self.pygame = pygame
        self.kwargs = kwargs
        
        self.x = self.kwargs["x"]
        self.y = self.kwargs["y"]
        self.text = self.kwargs["text"]
        self.colour = self.kwargs.get("colour", (255, 255, 255))
        self.need_font = self.kwargs.get("font", "monospace")
        self.size = self.kwargs.get("size", 32)
        
        print(self.pygame.font.get_fonts())
        
        #try
        self.ref = self.pygame.font.SysFont(self.need_font, self.size)
            
        #except:
         #   print("font error: " + self.need_font)
          #  return
        
        self.behaviors = []
        
    def draw(self):
        to_remove = []
        if self.behaviors:
            for behavior in self.behaviors:
                #print("text\: " + str(behavior))
                self.ref, self = behavior.update(self.ref, self)
                
                if getattr(behavior, "kill", False):
                    to_remove.append(behavior)
                
        for _ in to_remove:
            self.behaviors.remove(behavior)
        
        label = self.ref.render(self.text, True, self.colour, False)
        self.pygame.main_screen.blit(label, (self.x, self.y))