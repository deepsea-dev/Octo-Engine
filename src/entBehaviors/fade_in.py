import time

class main(object):
    """
    Creates a fade in effect for an Image
    or Surface
    """
    def __init__(self, ref, entity, args):
        self.kill = False
        self.ref = ref
        self.entity = entity
        
        self.args = args
        for arg in args:
            if arg.startswith("duration"):
                self.add_time = int(arg.split("-")[1]) # Get time for duration calculation
        
        self.fade_in = True
        self.fade_finish = time.time() + self.add_time # estimate for when fade in has ended
        self.fade_in_opacity = 0       
        
        self.init_time = time.time()
        
    def update(self, ref, entity):
        self.ref = ref
        self.entity = entity
        time_left = 1
        
        if time.time() > self.init_time + 1: # Increase every second
            time_left = self.fade_finish - time.time()
            
            if time_left < 1:
                self.fade_in = False
                self.kill = True
        
        self.fade_in_opacity = 255 / time_left
        self.fade_in_opacity = 0 if int(self.fade_in_opacity) == 255 else self.fade_in_opacity # Don't allow image to show in full at first

        if self.fade_in:
            self.ref.set_alpha(self.fade_in_opacity)
        
        return self.ref, self.entity