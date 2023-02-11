import pygame, sys, random, json, random
from operator import itemgetter

pygame.init()
# Color
grey = (34,45,46)
white = (255, 255, 255)

# Font
font_win_mess = pygame.font.Font("Data/Font/upheavtt.ttf", 50)
font_mid = pygame.font.Font("Data/Font/upheavtt.ttf", 39)
font_small = pygame.font.Font("Data/Font/upheavtt.ttf", 25)
font_title = pygame.font.Font("Data/Font/upheavtt.ttf", 75)

# JSON
with open('Data/JSON/scores.json', 'r') as f:
    scores_dic = json.load(f)

with open('Data/JSON/mot.json', 'r') as f:
    mot_dic = json.load(f)