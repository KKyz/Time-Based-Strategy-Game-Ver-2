from math import sin,cos
import pygame

WHITE = (250, 250, 250)
BLACK = (5, 5, 5)

class WaveText:
 
    def __init__(self, text, pos=(0, 0), frequency=5, speed=-0.3, radius=4, spread_x=1.5,
                 font=pygame.font.Font(pygame.font.get_default_font(), 40)):
        """
       A basic wavy text widget.
       :param text: The string to render
       :param pos: Top left corner of the text. Note that because of the circles it will move outside of it
       :param frequency: How often a new wave is stared
       :param speed: the speed of each wave (~difference of position with the next letter)
       :param radius: radius on which letters move
       :param spread_x: to have an ellipse stretched in the x axis set this to > 1 and < 1 for the y axis.
       :param font:
       """
        self.speed = speed
        self.frequency = frequency
        self.radius = radius
        self.pos = pos
        self.spread_x = spread_x
 
        self.t = 0
 
        self.text = text
        self.font = font
        self.char_surfs = [font.render(c, True, WHITE) for c in self.text]
 
 
    def update(self):
        self.t += 1
 
    def draw(self, screen):
        x0, y0 = self.pos
 
        for i, char in enumerate(self.char_surfs):
            dx = self.radius * cos(self.t / self.frequency + self.speed * i) * self.spread_x
            dy = self.radius * sin(self.t / self.frequency + self.speed * i)
            screen.blit(char, (x0 + dx, y0 + dy))
            x0 += char.get_width()