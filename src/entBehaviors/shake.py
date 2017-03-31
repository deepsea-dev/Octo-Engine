class main(object):
    def __init__(self, ref, entity, args):
        """
        shakes an object
        """
        self.kill = False
        self.ref = ref
        self.entity = entity
        self.args = args
        
        self.horizonal_lock = False
        self.vertical_lock = False
        
        for arg in args:
            if arg.startswith("hz_lock"):
                pass
            
        self.iteration = 0
            
        self.x_diff = 0
        self.relative_x_y = 0
        
        self.postive_direction = False
        
        self.real_x = self.entity.x
        self.real_y = self.entity.y
        
    def update(self, ref, entity):
        self.s = -1 # Current Direction of shake | Current is positive x and y
        self.ref = ref
        self.entity = entity

        while True:
            max_x_y_diff = 50 # Max distance between shaking points
            jump = 10
            
            if not self.postive_direction:
                if self.relative_x_y <= (0 - max_x_y_diff):
                    self.postive_direction = True
                    
                else:
                    self.relative_x_y -= jump
                    
            if self.postive_direction:
                if self.relative_x_y >= max_x_y_diff:
                    self.postive_direction = False
                    
                else:
                    self.relative_x_y += jump
                    
            self.entity.x = self.real_x + self.relative_x_y
            self.entity.y = self.real_y + self.relative_x_y
            self.iteration += 1
            break    
                
        return self.ref, self.entity            