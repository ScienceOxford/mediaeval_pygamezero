tile_size = 64

WIDTH = (tile_size*10)
HEIGHT = (tile_size*10)

pos_x = 0
pos_y = 0

tiles = ['grass1', 'grass1', 'grass1', 'grass1', 'road_ver', 'grass1', 'grass1', 'grass1', 'grass1', 'grass1', 'grass1',
           'grass1', 'grass1', 'grass1', 'grass1', 'road_ver', 'grass1', 'grass1', 'grass1', 'grass1', 'grass1', 'grass1',
           'grass1', 'grass1', 'grass1', 'grass1', 'road_ver', 'grass1', 'grass1', 'grass1', 'grass1', 'grass1', 'grass1',
           'road_hor', 'road_hor', 'road_hor', 'road_hor', 'road_cross', 'road_hor', 'road_hor', 'road_hor', 'road_left', 'grass1', 'grass1',
              'grass1', 'grass1', 'grass1', 'grass1', 'road_ver', 'grass1', 'grass1', 'grass1', 'road_ver', 'grass1', 'grass1',
           'grass1', 'grass1', 'grass1', 'grass1', 'road_ver', 'grass1', 'grass1', 'grass1', 'road_ver', 'grass1', 'grass1',
           'grass1', 'grass1', 'grass1', 'grass1', 'road_ver', 'grass1', 'grass1', 'grass1', 'road_ver', 'grass1', 'grass1',
           'road_hor', 'road_hor', 'road_hor', 'road_hor', 'road_cross', 'road_hor', 'road_hor', 'road_hor', 'road_right', 'grass1', 'grass1',
              'grass1', 'grass1', 'grass1', 'grass1', 'road_ver', 'grass1', 'grass1', 'grass1', 'grass1', 'grass1', 'grass1',
              'grass1', 'grass1', 'grass1', 'grass1', 'road_ver', 'grass1', 'grass1', 'grass1', 'grass1', 'grass1']

def setting():
    global pos_x
    global pos_y
    pos_x += tile_size
    if pos_x <= WIDTH:
        return (pos_x - tile_size, pos_y)
    else:
        pos_x = 0
        pos_y += tile_size