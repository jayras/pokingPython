import pygame
import random
from enemy import Enemy
from bullet import Bullet
from player import Player

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('objects/ufo.png')
pygame.display.set_icon(icon)
background = pygame.Surface(screen.get_size())
background = background.convert()

backgroundImage = pygame.image.load('objects/background_800by600.png')
background.blit(backgroundImage, (0, 0))
screen.blit(background, (0, 0))
pygame.display.flip()
scoreDisplay = pygame.font.SysFont("monospace", 60, True)

# Controls
moveLeft = [pygame.K_LEFT, pygame.K_a]
moveRight = [pygame.K_RIGHT, pygame.K_d]
fireKey = [pygame.K_UP, pygame.K_SPACE, pygame.K_w]

# Player
p = Player()
score = 0

def drawPlayer(loc):
    screen.blit(Player.playerImage, loc)


# Enemy
nmy = Enemy(random.randint(0, 736), random.randint(50, 250))
deadDelay = 3000


def drawEnemy(loc: tuple):
    screen.blit(nmy.image, loc)


# Bullets (Holding place)
bullets = []

# Set last fire to -1, so we can fire immediately
lastFire = -1

# Set how often we can fire, ticks are in milliseconds, so 1000 is 1 second
reloadTime = 1000


# Fire the gun
def fire(last):
    checkNow = pygame.time.get_ticks()
    fired = False
    if last < 0 or (last + reloadTime) < checkNow:
        bullets.append(Bullet(p.x + 24, p.y))
        fired = True
    return fired


# Game loop
running = True
while running:
    for event in pygame.event.get():
        # Check for X on window
        if event.type == pygame.QUIT:
            running = False

        # Check for keystroke
        if event.type == pygame.KEYDOWN:
            # Left Key
            if event.key in moveLeft:
                p.moveRate = -0.1
            # Right Key
            if event.key in moveRight:
                p.moveRate = 0.1
            # Fire Key
            if event.key in fireKey:
                if fire(lastFire):
                    lastFire = pygame.time.get_ticks()
        if event.type == pygame.KEYUP:
            # Movement Key
            if event.key in moveLeft or event.key in moveRight:
                p.moveRate = 0

    # Game Screen background
    s = scoreDisplay.render("Score:" + str(score), False, (254, 254, 254))

    screen.blit(background, (0, 0))
    screen.blit(s, (screen.get_width() - (s.get_width() + 20), screen.get_height() - (s.get_height() + 20)))

    # Draw Bullets
    for b in bullets:
        screen.blit(b.image, b.move(nmy))
        if b.hit:
            bullets.remove(b)

    if nmy.hitPoints > 0:
        drawEnemy(nmy.move(p.x, p.y))
    else:
        now = pygame.time.get_ticks()
        if (nmy.deadTime + deadDelay) > now:
            drawEnemy((nmy.x, nmy.y))
        else:
            score += 1
            nmy = Enemy(random.randint(0, 736), random.randint(50, 250))

    if not nmy.winner:
        drawPlayer(p.move())

    # Update game screen
    pygame.display.update()
