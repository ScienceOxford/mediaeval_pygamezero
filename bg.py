tile_size = 64

WIDTH = (tile_size*9)
HEIGHT = (tile_size*9)

pos_x = 0
pos_y = 0

tiles = ['grass_01', 'grass_01', 'grass_01', 'road_ns_01', 'grass_01', 'grass_01', 'grass_01', 'grass_01', 'grass_01', 'grass_01',
         'grass_01', 'grass_01', 'grass_01', 'road_ns_01', 'grass_01', 'grass_01', 'grass_01', 'grass_01', 'grass_01', 'grass_01',
         'road_ew_01', 'road_ew_01', 'road_ew_01', 'road_nesw_01', 'road_ew_01', 'road_ew_01', 'road_ew_01', 'road_sw_01', 'grass_01', 'grass_01',
         'grass_01', 'grass_01', 'grass_01', 'road_ns_01', 'grass_01', 'grass_01', 'grass_01', 'road_ns_01', 'grass_01', 'grass_01',
         'grass_01', 'grass_01', 'grass_01', 'road_ns_01', 'grass_01', 'grass_01', 'grass_01', 'road_ns_01', 'grass_01', 'grass_01',
         'grass_01', 'grass_01', 'grass_01', 'road_ns_01', 'grass_01', 'grass_01', 'grass_01', 'road_ns_01', 'grass_01', 'grass_01',
         'road_ew_01', 'road_ew_01', 'road_ew_01', 'road_nesw_01', 'road_ew_01', 'road_ew_01', 'road_ew_01', 'road_nw_01', 'grass_01', 'grass_01',
         'grass_01', 'grass_01', 'grass_01', 'road_ns_01', 'grass_01', 'grass_01', 'grass_01', 'grass_01', 'grass_01', 'grass_01',
         'grass_01', 'grass_01', 'grass_01', 'road_ns_01', 'grass_01', 'grass_01', 'grass_01', 'grass_01', 'grass_01']
         
def setting():
    global pos_x
    global pos_y
    pos_x += tile_size
    if pos_x <= WIDTH:
        return (pos_x - tile_size, pos_y)
    else:
        pos_x = 0
        pos_y += tile_size
