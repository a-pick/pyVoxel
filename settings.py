from numba import njit
import numpy as np
import glm
import math

# resolution settings
WIN_RES = glm.vec2(1920, 1080)

# camera settings
ASPECT_RATIO = WIN_RES.x / WIN_RES.y
FOV_DEG = 50
V_FOV = glm.radians(FOV_DEG)  # vertical fov
H_FOV = 2 * math.atan(math.tan(V_FOV * 0.5) * ASPECT_RATIO)  # horizontal fov
NEAR = 0.1  # near clipping plane
FAR = 2000.0  # far clipping plane
PITCH_MAX = glm.radians(89)

# player
PLAYER_SPEED = 0.005
PLAYER_ROT_SPEED = 0.003
PLAYER_POS = glm.vec3(0, 0, 1)
MOUSE_SENSITIVITY = 0.002

# colors
BG_COLOR = glm.vec3(0, 0, 0)
