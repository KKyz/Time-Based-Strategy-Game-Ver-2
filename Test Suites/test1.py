import pygame
import random

TILESIZE = 32
GRID_W, GRID_H = (20, 15)
LOOKUP = None

class Actor(pygame.sprite.Sprite):
    def __init__(self, grid_pos):
        super().__init__()
        self.image = pygame.Surface((TILESIZE // 2, TILESIZE // 2))
        self.rect = self.image.get_rect()
        self.pos = pygame.Vector2()
        self.update_pos(grid_pos)
        self.image.fill(pygame.Color('dodgerblue'))
        self.timeout = 1000

    def update_pos(self, grid_pos):
        self.grid_pos = grid_pos
        self.rect.center = get_grid_rect(grid_pos).center
        self.pos = pygame.Vector2(self.rect.topleft)

    def move_random(self):
        d = random.choice([-1, 1])
        x, y = self.grid_pos
        if random.randint(0, 2):
            x += d
        else:
            y += d
        self.update_pos((x, y))

    def update(self, events, dt):
        self.timeout -= dt
        if self.timeout <= 0:
            self.timeout = 1000
            self.move_random()

def get_grid_rect(pos):
    x, y = pos
    return LOOKUP[y][x]

def create_grid():
    surf = pygame.Surface((TILESIZE * GRID_W, TILESIZE * GRID_H))
    surf.set_colorkey((2, 2, 2))
    surf.fill((2, 2, 2))
    grid = []
    for y in range(GRID_H):
        line = []
        for x in range(GRID_W):
            r = pygame.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE)
            line.append(r)
            pygame.draw.rect(surf, pygame.Color('grey'), r, 1)
        grid.append(line)

    return grid, surf

def main():
    screen = pygame.display.set_mode((TILESIZE * GRID_W, TILESIZE * GRID_H))
    dt, clock = 0, pygame.time.Clock()
    grid, grid_surf = create_grid()
    global LOOKUP 
    LOOKUP = grid
    sprites = pygame.sprite.Group(Actor((9, 6)))
    while True:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                return
        sprites.update(events, dt)
        screen.fill((30, 30, 30))
        screen.blit(grid_surf, (0, 0))
        sprites.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)

if __name__ == '__main__':
    main()