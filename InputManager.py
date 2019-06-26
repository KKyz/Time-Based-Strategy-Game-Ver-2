import pygame

class InputHandler:
    # state is a dictionary containing the time since last pression for each key.
    # the key in state exists only as long as the key is pressed (partially true).
    def __init__(self, delay):
        self.delay = delay
        self.state = dict()

    def get_key(self, key):
        if pygame.key.get_pressed()[key]:
            if self.state.get(key) != None and pygame.time.get_ticks() - self.state.get(key) < self.delay:
                return False
            self.state[key] = pygame.time.get_ticks()
            return True
        else:
            if self.state.get(key) != None:
                del self.state[key]
            return False

IBO = InputHandler(210)
IDO = InputHandler(125)
