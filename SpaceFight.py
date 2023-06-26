#sound from zapsplat.com
#images from seekpng.com
#start button similarpng.com
import pygame
import random
from pygame.locals import (
    RLEACCEL,
    K_SPACE,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

myfont = pygame.font.SysFont("Comic Sans MS", 30)

endGameText = myfont.render("", False, (255,255,0))

score = 0

numLasers = 5

brocolliKilled = 0

pygame.mixer.music.load("BackgroundMusic.mp3")

LaserSound = pygame.mixer.Sound("LaserSound.mp3")
ExplosionSound = pygame.mixer.Sound("ExplosionSound.mp3")
#IceCreamSound = pygame.mixer.Sound("IceCreamSound.mp3")

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
enemies_group = pygame.sprite.Group()
friends_group = pygame.sprite.Group()
laser_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("PlayerShip.png").convert()
        self.surf = pygame.transform.scale(self.surf, (40,26))
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.center = (460, 250)
    def getPos(self) :
        return self.rect.center

class Enemy(pygame.sprite.Sprite):
    def __init__(self, xPos, yPos):
        super(Enemy, self).__init__()
        self.speed = random.randint(4, 6)
        self.surf = pygame.image.load("EnemyShip.png").convert()
        self.surf = pygame.transform.scale(self.surf, (30,30))
        self.surf.set_colorkey((0,0,0), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.center = (xPos,yPos)
        
    def update(self):
        self.rect.move_ip(self.speed, 0)

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Laser, self).__init__()
        self.speed = 4
        self.surf = pygame.image.load("BulletPic3.jpg").convert()
        self.surf = pygame.transform.scale(self.surf, (20,10))
        self.surf.set_colorkey((255,255,255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.center = (pos)
        
    def update(self):
        self.rect.move_ip(-self.speed, 0)
            
class Explosion(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Explosion, self).__init__()
        self.speed = 4
        self.surf = pygame.image.load("ExplosionPic2.jpg").convert()
        self.surf = pygame.transform.scale(self.surf, (40,40))
        self.surf.set_colorkey((255,255,255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.center = (pos)
        self.length = 40
        self.count = 0
    def update(self):
        self.count += 1

class Star(pygame.sprite.Sprite):
    def __init__(self, pos, color):
        super(Star, self).__init__()
        self.color = color
        self.surf = pygame.Surface((1,1))
        self.surf.fill((255,255,color))
        self.rect = self.surf.get_rect()
        self.rect.center = (pos)

for x in range(1000) :
    w = random.randint(0,SCREEN_WIDTH)
    h = random.randint(0,SCREEN_HEIGHT)
    c = random.randint(150,200)
    star = Star((w,h),c)
    all_sprites.add(star)

player = Player()
player.groups()
all_sprites.add(player)

makeEnemy = pygame.USEREVENT + 1
pygame.time.set_timer(makeEnemy, 500)

getLaser = pygame.USEREVENT + 8
pygame.time.set_timer(getLaser, 3000)

# INTRO CODE HERE
directions = False
welcome = True
while welcome :
    screen.fill((0, 0, 0))
    for x in range(255) :
        pygame.draw.circle(screen, (0, 0, x), (SCREEN_WIDTH/2,SCREEN_HEIGHT/2), 255 - x)
    image_surf = pygame.image.load("PlayerShip.png").convert()
    image_surf = pygame.transform.scale(image_surf, (240,156))
    image_surf.set_colorkey((0, 0, 0), RLEACCEL)
    image_surf = pygame.transform.rotate(image_surf, 30)
    image_rect = image_surf.get_rect()
    image_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    bul1_surf = pygame.image.load("BulletPic3.jpg").convert()
    bul1_surf = pygame.transform.scale(bul1_surf, (80,40))
    bul1_surf.set_colorkey((255,255,255), RLEACCEL)
    bul1_surf = pygame.transform.rotate(bul1_surf, -55)
    bul1_rect = bul1_surf.get_rect()
    bul1_rect.center = (400, 350)
    flame_surf = pygame.image.load("FlameTrail.png").convert()
    flame_surf = pygame.transform.scale(flame_surf, (100,200))
    flame_surf.set_colorkey((0,0,0), RLEACCEL)
    flame_surf = pygame.transform.rotate(flame_surf, 35)
    flame_rect = flame_surf.get_rect()
    flame_rect.center = (470, 450)
    start_surf = pygame.image.load("StartButton.png").convert()
    start_surf = pygame.transform.scale(start_surf, (200,80))
    start_surf.set_colorkey((0,0,0), RLEACCEL)
    start_rect = start_surf.get_rect()
    start_rect.center = (250, 410)
    dir_surf = pygame.image.load("howPlay.png").convert()
    dir_surf = pygame.transform.scale(dir_surf, (120,30))
    dir_surf.set_colorkey((0,0,0), RLEACCEL)
    dir_surf.set_colorkey((255,255,255), RLEACCEL)
    dir_rect = dir_surf.get_rect()
    dir_rect.center = (250, 470)
    screen.blit(image_surf, image_rect)
    screen.blit(flame_surf, flame_rect)
    screen.blit(bul1_surf, bul1_rect)
    screen.blit(start_surf, start_rect)
    screen.blit(dir_surf, dir_rect)
    introFont = pygame.font.SysFont("inkfree", 80)
    introText = introFont.render("Space Fight", False, (255,255,0))
    introFont2 = pygame.font.SysFont("inkfree", 200)
    introText2 = introFont2.render("2", False, (255,200,0))
    screen.blit(introText2, (200,0))
    screen.blit(introText, (50,40))
    pygame.display.flip()
    for event in pygame.event.get():                
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if start_rect.collidepoint(mouse_pos):
                welcome = False
            if dir_rect.collidepoint(mouse_pos):
                welcome = False
                directions = True
        if event.type == pygame.QUIT:
            pygame.quit()


while directions :
    screen.fill((0, 0, 0))
    for x in range(255) :
        pygame.draw.circle(screen, (0, 0, x), (SCREEN_WIDTH/2,SCREEN_HEIGHT/2), 255 - x)
    start_surf2 = pygame.image.load("StartButton.png").convert()
    start_surf2 = pygame.transform.scale(start_surf2, (200,80))
    start_surf2.set_colorkey((0,0,0), RLEACCEL)
    start_rect2 = start_surf2.get_rect()
    start_rect2.center = (250, 410)
    screen.blit(start_surf2, start_rect2)
    dirFont1 = pygame.font.SysFont("inkfree", 35)
    dirFont2 = pygame.font.SysFont("inkfree", 20)
    dirText1 = dirFont1.render("Goal: ", False, (255,200,0))
    dirText2 = dirFont2.render("Shoot as many red enemy ships as you can (to gain", False, (255,200,0))
    dirText3 = dirFont2.render("points), without getting hit by an enemy ship ", False, (255,200,0))
    dirText4 = dirFont2.render("(which results in death). ", False, (255,200,0))
    dirText5 = dirFont1.render("Directions: ", False, (255,200,0))
    dirText6 = dirFont2.render("Press and release the up/down arrow keys to move.", False, (255,200,0))
    dirText7 = dirFont2.render("Press and release the space bar to shoot.", False, (255,200,0))
    dirText8 = dirFont2.render("Remember: You start with 5 lasers and gain one ", False, (255,200,0))
    dirText9 = dirFont2.render("every 3 seconds. Use them wisely. ", False, (255,200,0))
    screen.blit(dirText1, (40,5))
    screen.blit(dirText2, (40,55))
    screen.blit(dirText3, (40,80))
    screen.blit(dirText4, (40,105))
    screen.blit(dirText5, (40,155))
    screen.blit(dirText6, (40,205))
    screen.blit(dirText7, (40,230))
    screen.blit(dirText8, (40,255))
    screen.blit(dirText9, (40,280))
    pygame.display.flip()
    for event in pygame.event.get():                
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if start_rect2.collidepoint(mouse_pos):
                directions = False
        if event.type == pygame.QUIT:
            pygame.quit()

pygame.mixer.music.play(-1)
running = True
dead = False
counter = 0
x1 = 100
y1 = 100 # (used for end graphics)
while running:
    counter += 1

    for event in pygame.event.get():                
        if event.type == KEYDOWN and not dead:
            if event.key == K_UP:
                player.rect.move_ip(0, -10)
            elif event.key == K_DOWN:
                player.rect.move_ip(0, 10)
            elif event.key == K_SPACE and numLasers > 0:
                laser = Laser(player.rect.center)
                all_sprites.add(laser)
                laser_group.add(laser)   
                pygame.mixer.Sound.play(LaserSound)
                numLasers -= 1
        
        # note: could also use counter to make enemies
        if event.type == makeEnemy:
            numEnemies = 0
            for num in range(0,score + 1,5) :
                if numEnemies < 6 : # limits the increase after 25
                    x = random.randint(0, 10)
                    y = random.randint(0, SCREEN_HEIGHT)
                    enemy = Enemy(x,y)
                    all_sprites.add(enemy)
                    enemies_group.add(enemy)
                    numEnemies += 1

        if event.type == getLaser :
            numLasers += 1            
            
        if event.type == pygame.QUIT:
            running = False

    
    for entity in enemies_group:
        if player.rect.colliderect(entity):
            player.kill()
            myfontEnd = pygame.font.SysFont("impact", 50)
            endGameText = myfontEnd.render("Score: " + str(score), False, (255,255,0))
            over_surf = pygame.image.load("GameOver.png").convert()
            over_surf = pygame.transform.scale(over_surf, (200,150))
            over_surf.set_colorkey((0, 0, 0), RLEACCEL)
            if not dead :
                explosion = Explosion((player.rect.centerx - 25,player.rect.centery - 25))
                explosion.surf = pygame.transform.scale(explosion.surf, (90,90))
                all_sprites.add(explosion)
                explosion_group.add(explosion)
                pygame.mixer.Sound.play(ExplosionSound)
            pygame.mixer.music.stop()
            dead = True

    for entity1 in laser_group:
        for entity2 in enemies_group:
            if entity1.rect.colliderect(entity2):
                entity2.kill()
                score = score + 1
                #EXPLOSION
                explosion = Explosion(entity1.rect.center)
                all_sprites.add(explosion)
                explosion_group.add(explosion)
                pygame.mixer.Sound.play(ExplosionSound)

    text_surface = myfont.render("Score: " + str(score), False, (255,255,0))
    text_surface2 = myfont.render("Lasers: " + str(numLasers), False, (255,255,0))

    for explosion in explosion_group :
        explosion.update()
        if explosion.count == explosion.length :
            explosion.kill()

    # red, green, blue
    screen.fill((0, 0, 0))
    for x in range(255) :
        pygame.draw.circle(screen, (0, 0, x), (SCREEN_WIDTH/2,SCREEN_HEIGHT/2), 255 - x)

    for enemy in enemies_group:
        enemy.update()

    for laser in laser_group:
        laser.update()
    
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    
    if not dead :
        screen.blit(text_surface, (325,450))
        screen.blit(text_surface2, (50,450))
    screen.blit(endGameText, (175,225))
    if dead :
        if counter % 50 == 0 :
            x1 = random.randint(0, 300)
            y1 = random.randint(0, 350)
        screen.blit(over_surf, (x1,y1))
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
