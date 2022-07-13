import pygame


class Enemy:
    defaultImage = pygame.image.load('objects/alien-space-ship.png')
    winImage = pygame.image.load('objects/enemy_win.png')
    deadImage = pygame.image.load('objects/crash.png')
    moveRate = 0.3

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.deltaX = Enemy.moveRate
        self.deltaY = 0
        self.nextY = (y - (y % 10)) + 10
        self.bounceLeft = False
        self.winner = False
        self.damage = 0
        self.deadTime = 0
        self.hitPoints = 1
        self.image = Enemy.defaultImage

    def move(self, playerX, playerY):
        # Damage check
        if self.damage > 0:
            self.hitPoints -= self.damage
            self.damage = 0

        # Am I alive
        if self.hitPoints <= 0 and self.deadTime == 0:
            self.image = Enemy.deadImage
            self.deadTime = pygame.time.get_ticks()

        # Check Left/Right boundary
        if self.x <= 0:
            if self.bounceLeft:
                if self.y >= self.nextY:
                    self.deltaY = 0
                    self.deltaX = self.moveRate
                    self.bounceLeft = False
                    self.nextY = (self.y - (self.y % 10)) + 10
            else:
                self.bounceLeft = True
                self.deltaX = 0
                self.deltaY = self.moveRate
        if self.x >= 736:
            self.deltaX = -self.moveRate

        # Check if enemy won.
        if ((playerY - 64) <= self.y <= (playerY + 64)) and ((playerX - 64) <= self.x <= (playerX + 64)):
            self.image = Enemy.winImage
            self.deltaX = 0
            self.deltaY = 0
            self.winner = True

        if not self.winner:
            self.x += self.deltaX
            self.y += self.deltaY

        loc = (self.x, self.y)

        return loc
