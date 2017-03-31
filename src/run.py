# Imports
import pygame
import os
import entities
import entBehaviors
import time
from threading import Timer, Thread

pygame.font.init()
pygame.mixer.init()

# Utility function for paths
def convert_system_path(path):
    return os.path.join(*path.split("/"))

# Main Class for Object handling
class Main(object):
    def __init__(self):
        
        self.behavior_handler = entBehaviors.behavior_handler(pygame)
        self.entity_handler = entities.entity_handler(pygame, self.behavior_handler)
        
        self.width, self.height = 1060, 720 # TODO: Get resolution from config
        self.screen = pygame.display.set_mode((self.width, self.height))#, pygame.FULLSCREEN)
        
        setattr(pygame, "main_screen", self.screen)
        
        
        self.last_executed = 0 # Instruction last executed from level
        self.run_loop()
        
    def cycle_screen(self):
        """
        Update Screen elements from a list
        """
            
        self.screen.fill(0) # Clears the screen
        
        for entity in self.entity_handler.entities:
            entity.draw()
            
        pygame.display.flip() # Drawing Screen
        
    def process_level(self, load=False, single_cmd=False): # Creating a separate class for this would be ideal.
        if load:
            print(convert_system_path("levels/level_1"))
            self.current_level = open(convert_system_path("levels/level_1"), "r")
            
        """
        Let's move this to a separate class later on when the game is
        completely functional
        """
        if single_cmd:
            instruction_ = single_cmd + "\n"
            print("got single command")
            print(single_cmd)
        
        to_run = [single_cmd] if single_cmd else self.current_level.readlines()
        print("running: " + str(to_run))
        for instruction_ in to_run:
            instruction = instruction_.split()[0]
            args = instruction_.split()[1:]
            
            if instruction == "sleep":
                self.event_timer = Timer(int(args[0]), self.process_level, [False, " ".join(args[1:])])
                self.event_timer.setDaemon(False)
                self.event_timer.start()
                
                while self.event_timer.isAlive():
                    pass
                
                continue # Process next instruction
            
            if instruction.startswith("entity:"):
                self.entity_handler.handle_cmd(instruction_.split())
                
            if instruction.startswith("clear:"):
                if instruction.split(":")[1] == "all":
                    print("Clearing screen")
                    
                self.entity_handler.entities = []
        
    def run_loop(self):
        self.level_thread = Thread(target=self.process_level, args=(True,))
        self.level_thread.start()
        
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit

            # Do Current Level PROCESSING_INSTRUCTION
            
            self.cycle_screen()
            
_main_ = Main() # Run Class
