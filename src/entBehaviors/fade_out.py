import time

class main(object):
    """
    Creates a fade out effect for an Image
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
        
        self.fade_out = True
        self.fade_finish = time.time() + self.add_time # estimate for when fade in has ended
        self.fade_out_opacity = 255    
        
        self.init_time = time.time()
        print("init")
        
    def update(self, ref, entity):
        self.ref = ref
        self.entity = entity
        time_left = 1
        
        if time.time() > self.init_time + 1: # Increase every second
            time_left = self.fade_finish - time.time()
            
            if time_left < 1:
                self.fade_out = False
                self.kill = True
        
        self.fade_out_opacity = 255 - (255 / time_left) # hehe
        self.fade_out_opacity = 0 if int(self.fade_out_opacity) == 255 else self.fade_out_opacity # Don't allow image to show in full at first

        if self.fade_out:
            self.ref.set_alpha(self.fade_out_opacity)
            print(str(self.fade_out_opacity))
        
        return self.ref, self.entity