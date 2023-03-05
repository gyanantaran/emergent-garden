
PARTICLE_DEFAULT_SPAWN_NUM = 100

PARTICLE_DEFAULT_UPDATE_TIME = 0.4
WALL_HEAT = 1
WALL_BOUNDARY = 10

PARTICLE_POWER_OF_DISTANCE = 2
PARTICLE_CLOSENESS_LIMIT = 0

FRAME_RATE = 30


# ALMOST NEVER CHANGES:
SCREEN_DIM = (500, 500)

BACK_BLACK = (0, 0, 0)

PARTICLE_DEFAULT_RADIUS = 2

PARTICLE_COLOR_RED = (0xff, 0x00, 0x00)
PARTICLE_COLOR_YELLOW = (0xff, 0xA0, 0x00)
PARTICLE_COLOR_GREEN = (0x00, 0xff, 0x00)
PARTICLE_COLOR_BLUE = (0x00, 0x00, 0xff)

# THE SPAWNING MARGINS
margin_x, margin_y = (0.5, 0.5)
center_x, center_y = (0.5, 0.5)
PARTICLE_DEFAULT_SPAWN_FRAME = (
    (
        int((center_x - margin_x) * SCREEN_DIM[0]),
        int((center_x + margin_x) * SCREEN_DIM[0])
    ),
    (
        int((center_y - margin_y) * SCREEN_DIM[1]),
        int((center_y + margin_y) * SCREEN_DIM[1])
    )
)
