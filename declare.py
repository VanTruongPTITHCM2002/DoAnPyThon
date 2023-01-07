import pygame
import math

WIDTH = 1280
HEIGHT = 720
RADIUS_VALUE = 20
listVetex = []
adjaGraphVoHuong = []
adjaGraph = []
textColor = "Black"
workingZoneColor = "Gray"
optionZoneColor = "SaddleBrown"
textZoneColor = "Snow3"
# Menu
nomalMenuColor = "GhostWhite"
activeMenuColor = "DeepSkyBlue1"
# vetex
nomalVetexColor = "Green1"
chooseVetexColor = "Red1"
moveVetextColor = "Dark Cyan"
# line
nomalLineColor = "Orange1"
moveLineColor = "VioletRed"
# Hỗ trợ save
isSaved = True
# True = có hướng, false = vô hướng
FlagHuongDoThi = True
textColor = "Black"
RADIUS_VALUE = 20
INF = math.inf
delay = 300
pygame.init()
def fontsize(size):
    font = pygame.font.SysFont("Corbel", size)
    return font

font_default = pygame.font.SysFont('Corbel', 16)
labels = []