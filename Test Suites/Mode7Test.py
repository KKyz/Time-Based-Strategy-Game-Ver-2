import pygame as pg
import traceback
from math import sin, cos, pi
 
vec = pg.math.Vector2
 
 
 
class Game:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((800, 600))
        self.screen_rect = self.screen.get_rect()
        self.fake_screen = pg.Surface((200, 150))
        self.fake_screen_rect = self.fake_screen.get_rect()
        self.fps = 30      
        self.all_sprites = pg.sprite.Group()
       
        try:
            self.map_img = pg.image.load('mariocircuit-3.png')
            self.map = Mode7(self, self.map_img)
        except:
            self.map = Mode7(self)
   
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
 
   
    def update(self, dt):
        self.fake_screen = pg.Surface((200, 150))
        self.fake_screen.fill(pg.Color('black'))
        self.all_sprites.update(dt)
       
 
   
    def draw(self):
        self.fake_screen = pg.transform.scale(self.fake_screen, self.screen_rect.size)
        self.screen.blit(self.fake_screen, (0,0))
        pg.display.update()
       
       
    def run(self):
        self.running = True
        while self.running:
            delta_time = self.clock.tick(self.fps) / 1000
            pg.display.set_caption(f'FPS: {self.clock.get_fps()}')
            self.events()        
            self.update(delta_time)
            self.draw()
       
        pg.quit()
       
       
       
class Mode7(pg.sprite.Sprite):
    def __init__(self, game, sprite=None, size=(1024, 1024)):
        super().__init__(game.all_sprites)
        self.game = game
        # if no sprite is provided, draw an image with horizontal and vertical lines
        if sprite:
            self.image = sprite
            self.size = sprite.get_size()
        else:
            self.image = pg.Surface(size)
            self.image.fill(pg.Color('black'))
           
            tilesize = 32
            for x in range(0, size[0], tilesize):
                pg.draw.line(self.image, pg.Color('darkturquoise'),
                                 (x, 0), (x, size[1]), 4)
            for y in range(0, size[1], tilesize):
                pg.draw.line(self.image, pg.Color('blueviolet'),
                                 (0, y), (size[0], y), 4)
        self.rect = self.image.get_rect()
       
        # position of the player on the map
        self.world_x = 1000
        self.world_y = 1000
        # viewing angle of the player
        self.angle = 0.1
        # settings for the near and far plane
        self.near = 0.005
        self.far = 0.03
        # field of view
        self.fov_half = pi / 4
        # movement speed
        self.speed = 0.5
       
   
    def update(self, dt):
        # references to the "fake" screen (the one that gets rendered onto the screen)
        screen = self.game.fake_screen
        screen_rect = self.game.fake_screen_rect
       
        # create the frustum corner points
        far_x1 = self.world_x + cos(self.angle - self.fov_half) * self.far
        far_y1 = self.world_y + sin(self.angle - self.fov_half) * self.far
       
        near_x1 = self.world_x + cos(self.angle - self.fov_half) * self.near
        near_y1 = self.world_y + sin(self.angle - self.fov_half) * self.near
       
        far_x2 = self.world_x + cos(self.angle + self.fov_half) * self.far
        far_y2 = self.world_y + sin(self.angle + self.fov_half) * self.far
       
        near_x2 = self.world_x + cos(self.angle + self.fov_half) * self.near
        near_y2 = self.world_y + sin(self.angle + self.fov_half) * self.near
       
        # loop over every pixel on the image, beginning furthest away towards the
        # camera point
        for y in range(screen_rect.h // 2):
            # take a sample point for depth linearly related to rows on the screen
            sample_depth = y / (screen_rect.h / 2) + 0.0000001 # this prevents div by 0 errors
            # not sure how this is handled in the c++ code
           
            # Use sample point in non-linear (1/x) way to enable perspective
            # and grab start and end points for lines across the screen
            start_x = (far_x1 - near_x1) / sample_depth + near_x1
            start_y = (far_y1 - near_y1) / sample_depth + near_y1
            end_x = (far_x2 - near_x2) / sample_depth + near_x2
            end_y = (far_y2 - near_y2) / sample_depth + near_y2
           
            # Linearly interpolate lines across the screen
            for x in range(screen_rect.w):
                sample_width = x / screen_rect.w
                sample_x = (end_x - start_x) * sample_width + start_x
                sample_y = (end_y - start_y) * sample_width + start_y
               
                # Wrap sample coordinates to give "infinite" periodicity on maps
                sample_x = sample_x % 1
                sample_y = sample_y % 1
               
                # sample a color from the image
                # translate x and y to screen proportions first because they are fractions of 1
                col = self.image.get_at((int(sample_x * screen_rect.w),
                                         int(sample_y * screen_rect.w)))
                # set the pixel values of the fake screen image
                # get_at and set_at are super slow, gonna try pixel arrays instead
                screen.set_at((x, int(y + (screen_rect.h / 2))),
                                        col)
       
# =============================================================================
#         pg.draw.line(screen, pg.Color('white'), (0, screen_rect.h / 2),
#                      (screen_rect.w, screen_rect.h / 2))
# =============================================================================
       
        # player movement
       
        keys = pg.key.get_pressed()
       
        # rotate the camera
        if keys[pg.K_a]:
            self.angle -= 1 * dt
        elif keys[pg.K_d]:
            self.angle += 1 * dt
        # move forward or backwards
        if keys[pg.K_w]:
            self.world_x += cos(self.angle) * self.speed * dt
            self.world_y += sin(self.angle) * self.speed * dt
        elif keys[pg.K_s]:
            self.world_x -= cos(self.angle) * self.speed * dt
            self.world_y -= sin(self.angle) * self.speed * dt
        # control the rendering parameters
        if keys[pg.K_LEFT]:
            self.near -= 0.1 * dt
        elif keys[pg.K_RIGHT]:
            self.near += 0.1 * dt
        if keys[pg.K_UP]:
            self.far += 0.1 * dt
        elif keys[pg.K_DOWN]:
            self.far -= 0.1 * dt
            self.far = max(self.far, 0.01)
        if keys[pg.K_q]:
            self.fov_half -= 0.1 * dt
        elif keys[pg.K_e]:
            self.fov_half += 0.1 * dt
 
 
 
       
if __name__ == '__main__':
    try:
        g = Game()
        g.run()
    except:
        traceback.print_exc()
        pg.quit()