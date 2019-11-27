# Skeleton for new projects
# CTRL+SHIFT+B to run
#
# KNOWN ISSUES
# -No collision for player up/down
# -FPS tied to game speed
# -No cap on fire speed
# -Holding fire buttons doesn't do anything
import pygame
import random

WIDTH = 360
HEIGHT = 460
FPS = 60

# Define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#Initialise and create window
pygame.init()
pygame.mixer.init() #Handles sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MyGame") #title
clock = pygame.time.Clock()

#Initialise player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # Need this for initialising every sprite
        self.image = pygame.Surface((50,40)) # Creates rectangle
        self.image.fill(BLUE)
        self.rect = self.image.get_rect() # Creates rectangle hitbox based on sprite
        self.rect.centerx = WIDTH / 2 # Spawn location
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

#Update for every tick player edition
    def update(self):
        # self.rect.x += self.speedx
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]: # Processes keypress
            self.speedx = -10
        if keystate[pygame.K_RIGHT]:
            self.speedx = 10
        self.rect.x += self.speedx # Updates based on keypress
        if self.rect.right > WIDTH: # Stops if out of bounds
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if keystate[pygame.K_UP]:
            self.speedy = -10
        if keystate[pygame.K_DOWN]:
            self.speedy = 10
        self.rect.y += self.speedy


    def shoot(self): # No suicide implied, this is shoot function
        bullet = Bullet(self.rect.centerx, self.rect.top) # Spawns top of bullet top of player
        all_sprites.add(bullet)
        bullets.add(bullet)

    def shootleft(self): # Shoot function for each direction
        bullet = BulletLeft(self.rect.centery, self.rect.left) # Left of player
        all_sprites.add(bullet)
        bullets.add(bullet)

    def shootright(self):
        bullet = BulletRight(self.rect.centery, self.rect.right) # Right of player
        all_sprites.add(bullet)
        bullets.add(bullet)

    def shootdown(self):
        bullet = BulletDown(self.rect.centerx, self.rect.bottom) # Bottom of player
        all_sprites.add(bullet)
        bullets.add(bullet)

class Bullet(pygame.sprite.Sprite): # Class for bullet
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20)) # Bb rectangle
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10 # Will travel up

    def update(self): # Update every tick, bullet edition
        self.rect.y += self.speedy
    # Kill if off the top
        if self.rect.bottom < 0:
            self.kill()

class BulletLeft(pygame.sprite.Sprite): # Class for every other bullet direction
    def __init__(self, y, x): # Pretty much reversing x/y and changing speed
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedx = -10

    def update(self):
        self.rect.x += self.speedx
    # Kill if off the top
        if self.rect.bottom < 0:
            self.kill()

class BulletRight(pygame.sprite.Sprite):
    def __init__(self, y, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedx = 10

    def update(self):
        self.rect.x += self.speedx
    # Kill if off the top
        if self.rect.bottom < 0:
            self.kill()

class BulletDown(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = 10

    def update(self):
        self.rect.y += self.speedy
    # Kill if off the top
        if self.rect.bottom < 0:
            self.kill()


all_sprites = pygame.sprite.Group() # Makes referring to everything easier
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

#Game Loop
running = True
while running:
    # Keep running at right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get(): # Check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w: # Binds shooting to WASD, checks for keypresses and calls rught function
                player.shoot()
            if event.key == pygame.K_a:
                player.shootleft()
            if event.key == pygame.K_d:
                player.shootright()
            if event.key == pygame.K_s:
                player.shootdown()

    #Update
    all_sprites.update()
    #Draw/render
    screen.fill(BLACK)
    all_sprites.draw(screen)

    #Flip after drawing everything
    pygame.display.flip()

pygame.quit() # Goodbye world
