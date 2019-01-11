import bg
import random

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

castle = (WIDTH//2, HEIGHT//2.2)
barn = (WIDTH// 1.4, HEIGHT//5)
tree = (WIDTH//3, HEIGHT//15)
church = (WIDTH//8, HEIGHT//1.8)

buildings = [castle, barn, tree, church]

wizard = Actor('character_02')
wizard.topleft = 0, 0

fire = Actor('fire_01')
fire.topleft = random.choice(buildings)

speed = 2

def draw():
    background()
    screen.blit('building_02', castle)
    screen.blit('tree_02', tree)
    screen.blit('building_13', barn)
    screen.blit('building_04', church)
    fire.draw()
    wizard.draw()
    
def update():
    '''
    Movement
    '''
    if keyboard.left:
        wizard.x -= speed
        if wizard.x <= 5:
            animate(wizard, pos=(6, wizard.y), duration=0.001)
    if keyboard.right:
        wizard.x += speed
        if wizard.x >= WIDTH-5:
            animate(wizard, pos=(WIDTH-6, wizard.y), duration=0.001)
    if keyboard.up:
        wizard.y -= speed
        if wizard.y <= 5:
            animate(wizard, pos=(wizard.x, 6), duration=0.001)
    if keyboard.down:
        wizard.y += speed
        if wizard.y >= HEIGHT-5:
            animate(wizard, pos=(wizard.x, HEIGHT-6), duration=0.001)
    '''
    Firefighting
    '''
    if wizard.distance_to(fire) <= 50:
        fire.image = 'fire_02'
    if wizard.distance_to(fire) <= 20:
        sounds.fireball.play()
        fire.image = 'fire_01'
        fire.topleft = random.choice(buildings)
