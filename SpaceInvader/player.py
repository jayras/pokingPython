import pygame


class Player:
    playerImage = pygame.image.load('objects/space-invaders.png')

    def __init__(self):
        self.x = 370
        self.y = 450
        self.moveRate = 0

    def move(self):
        self.x += self.moveRate

        # Right Boundary
        if self.x <= 0:
            self.x = 0

        # Left boundary (800 - size of ship (64) )
        if self.x >= 736:
            self.x = 736

        loc = (self.x, self.y)
        return loc
