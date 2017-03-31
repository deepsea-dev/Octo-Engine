"""
Specifically for text seeing as they don't have an .set_alpha attribute
"""
import time

class main(object):
    def __init__(self, ref, entity, args):
        self.kill = False
        self.ref = ref
        self.entity = entity
        
        self.args = args
        for arg in args:
            if arg.startswith("duration"):
                self.add_time = int(arg.split("-")[1]) # Get time for duration calculation
        
            if arg.startswith("colour"):
                self.tuple_arg = tuple(arg.split("-")[1].replace("(", "").replace(")", "").split(","))
                new_tuple = []
                
                for _ in self.tuple_arg:
                    new_tuple.append(int(_))
                    
                self.target_colour = tuple(new_tuple)
                print(self.target_colour)
        
        self.fade_finish = time.time() + self.add_time # estimate for when fade in has ended 
        
        self.init_time = time.time()
        self.fade = True
        
    def change_colour(self, old, target, time_left):
        if target > old:
            difference = target - old
            change = difference / time_left
            return old + change
            
        elif target < old:
            difference = old - target
            change = difference / time_left
            return old - change
            
        
    def update(self, ref, entity):
        self.ref = ref
        self.entity = entity
        
        if not self.fade:
            return
        
        time_left = self.fade_finish - time.time()
        if time_left <= 1:
            self.fade = False
            self.kill = True
            return ref, entity
        
        new_colour = [0,0,0]

        red = self.entity.colour[0]
        green = self.entity.colour[1]
        blue = self.entity.colour[2]
        
        new_colour[0] = self.change_colour(red, self.target_colour[0], time_left)
        new_colour[1] = self.change_colour(green, self.target_colour[1], time_left)
        new_colour[2] = self.change_colour(blue, self.target_colour[2], time_left)
        
        self.entity.colour = new_colour

        return ref, entity