import pygame

class GameObj(object):
    # the game object takes the coordinates, the dimensions and the color as its initialization parameters
    def __init__(self, x, y, w, h, color):
        # coordinates is the x and y value at which the object will be drawn in pygame
        self.coordinates = [x, y]
        # dimension is the height and width of the object
        self.dimensions = [w, h]
        # color is the color of the object
        self.color = pygame.color.Color(color)
