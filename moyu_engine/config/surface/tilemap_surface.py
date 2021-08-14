
import sys
import pygame
from pygame.locals import *

import constants as C
import graphics as G
import font as F

import components.tilemap_manager
import components.tilebutton
import components.window_move

def graphics():
    C.tilemap_surface.fill((0,0,0))
    components.tilemap_manager.tilemap_loarder()