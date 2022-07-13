import pygame


class Bullet:
    bulletRate = 5
    bulletImage = pygame.image.load('objects/bullet.png')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hit = False
        self.rate = -Bullet.bulletRate
        self.image = Bullet.bulletImage

    def move(self, enemy):
        # Check to see if we hit anything
        if (self.x + 32) >= enemy.x and self.x <= (enemy.x + 64) and (
                self.y <= (enemy.y + 64) and (self.y + 32) >= enemy.y):
            enemy.damage += 1
            self.hit = True
            self.rate = 0

        # Check to see if we hit the top of the window.
        if self.y <= 0:
            self.rate = 0
            self.hit = True

        self.y += self.rate

        loc = (self.x, self.y)
        return loc
