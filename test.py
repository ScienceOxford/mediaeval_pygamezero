import game

TILE_SIZE = game.tile_size
WIDTH = game.WIDTH
HEIGHT = game.HEIGHT

def background():
    for tile in game.tiles:
        pos = game.setting()
        if pos is not None:
            screen.blit(tile, pos)
    game.pos_x = 0
    game.pos_y = 0

# YOUR CODE BELOW HERE

wizard = Actor('wizard')
wizard.bottomleft = 0, HEIGHT

def draw():
    background()
    screen.blit('castle', (WIDTH//2, HEIGHT//2))
    wizard.draw()

def update():
    if keyboard.left:
        wizard.x -= 1
#        if wizard.x <= 5:
#            animate(wizard, pos=(6, wizard.y), duration=0.001)
    if keyboard.right:
        wizard.x += 1
#        if wizard.x >= WIDTH:
#            animate(wizard, pos=(WIDTH-6, wizard.y), duration=0.001)
    if keyboard.up:
        wizard.y -= 1
#        if wizard.y <= HEIGHT:
#            animate(wizard, pos=(wizard.x, HEIGHT+6), duration=0.001)
    if keyboard.down:
        wizard.y += 1
