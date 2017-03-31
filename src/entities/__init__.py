from . import image, text, sound, player
import json



class entity_handler(object):
    def __init__(self, pygame, behave_handler):
        self.pygame = pygame
        self.behave_handler = behave_handler
        
        self.entities = []
        
    def handle_cmd(self, instruction):
        # We haven't done anything with entity id's yet
        
        if instruction[0].split(":")[1] == "create":
            entity_type = instruction[1].split(":")[1] # Get entity type
            
            kwargs = "".join(instruction[3:]) # Get dict with args for entity
            kwargs = json.loads(kwargs)
            self.add_entity(type_=entity_type, **kwargs) # Lets' create it
        
        elif instruction[0].split(":")[1] == "behavior_add":
            id_ = int(instruction[1].split(":")[1])
            entity = self.entities[id_]
            behavior = self.behave_handler.add(instruction[2], entity.ref, entity, [])
            self.entities[id_].behaviors.append(behavior)
        
    def add_entity(self, type_, **kwargs):
        
        if type_ == "image":
            print(kwargs)
            entity = image.Image(self.pygame, **kwargs)
            
        elif type_ == "text":
            entity = text.Text(self.pygame, **kwargs)
            
        elif type_ == "sound":
            entity = sound.Sound(self.pygame, **kwargs)
            
        elif type_ == "player":
            entity = player.Player(self.pygame, **kwargs)
            
        if "options" in kwargs.keys():
            for option in kwargs["options"]:
                print("option: " + option)
                option_name = option.split(":")[0] # Get the behavior name
                args = option.split(":")[1].split("|") if ":" in option else []
                    
                print(args)
                behavior = self.behave_handler.add(option_name, entity.ref, entity, args)
                    
                entity.behaviors.append(behavior)
            
        self.entities.append(entity)