import bg

TILE_SIZE = bg.tile_size
WIDTH = bg.WIDTH
HEIGHT = bg.HEIGHT

print(WIDTH)
print(HEIGHT)

def background():
    for tile in bg.tiles:
        pos = bg.setting()
        if pos is not None:
            screen.blit(tile, pos)
    bg.pos_x = 0
    bg.pos_y = 0


def draw():
    background()
