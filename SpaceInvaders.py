"""
Space Invasion: To The Red Planet
(an arcade game using pygame library)
"""

import pygame, sys, random

#Initialise the pygame library
pygame.init()

#Colour definitions
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

#Manage screen updation time
clock = pygame.time.Clock()

#Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])

#Set the name of the window
pygame.display.set_caption('Space Invasion')

#Set positions of graphics
background_position = [0, 0]

#Load and set up graphics.
background_image0 = pygame.image.load("vortex.png").convert()
background_image1 = pygame.image.load("redplanet_level1.png").convert()
background_image2 = pygame.image.load("redplanet_level2.png").convert()
background_image3 = pygame.image.load("redplanet_level3.png").convert()

#Load the sounds
bgm = pygame.mixer.Sound("space walk.ogg")
click_sound = pygame.mixer.Sound("laser5.ogg")
explosion_sound = pygame.mixer.Sound("rumble.ogg")
explosion_sound_two = pygame.mixer.Sound("chunky explosion.ogg")

#Initialise common font type and size
myfont = pygame.font.SysFont("monospace", 20)

class Enemyship(pygame.sprite.Sprite):
    """
    This class represents the enemy spaceship.
    """
    def __init__(self):
        #Call the parent class (Sprite) constructor
        super().__init__()
        #Load image of enemy spaceship
        self.image = pygame.image.load("rsz_enemyship.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        #Move enemyship down one pixel
        self.rect.y += 1

class Player(pygame.sprite.Sprite):
    """
    This class represents the player and can be fully utilised in multiplayer gaming.
    """
    def __init__(self):
        #Call the parent class (Sprite) constructor
        super().__init__()
        # Load image of player
        self.image = pygame.image.load("rsz_ship1.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
    
    def update(self):
        #Get the current mouse position
        pos = pygame.mouse.get_pos()
        #Set the player object to the mouse location
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        #Restrict the player's movement within display area
        if pos[0] > 750:
            self.rect.x = 750
        if pos[0] < 0:
            self.rect.x = 0
        self.rect.y = pos[1]
        if pos[1] > 550:
            self.rect.y = 550
        if pos[1] < 0:
            self.rect.y = 0

class Bullet(pygame.sprite.Sprite):
    """
    This class represents the bullet.
    """
    def __init__(self):
        #Call the parent class (Sprite) constructor
        super().__init__()
        #Create bullet
        self.image = pygame.Surface([4, 20])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

    def update(self):
        #Move/Fire the bullet
        self.rect.y -= 3

class Missile(pygame.sprite.Sprite):
    """
    This class represents the missile.
    """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        #Load image of missile
        self.image = pygame.image.load("rsz_missile05.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        #Move the missile
        self.rect.y += 5

"""
switch_screen function displays screen with buttons as options to choosing activity.
Parameter disp indicates the button labels (Start Game/ Continue Game/ Restart Game).
The game's name is also displayed.
"""
def switch_screen(disp):
    pygame.mouse.set_visible(True)
    done = False
    while not done:
        pos = pygame.mouse.get_pos()
        #Run event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                #The loop will break and the control will return to normal flow
                if pos[0]>300 and pos[0]<500 and pos[1]>120 and pos[1]<170:
                    done = True
                #Quit the pygame engine
                if pos[0]>300 and pos[0]<500 and pos[1]>440 and pos[1]<490:
                    pygame.quit()
                    #sys.exit() halts all working after quit or else pygame.error: display Surface quit pops up
                    sys.exit()

        #Blit background image on screen
        screen.blit(background_image0, background_position)

        #Buttons will become red when mouse pointer is on them
        #Button label for starting/continuing/restarting game
        if disp == 1:
            text = "Start Game"
        elif disp == 2:
            text = "Continue Game"
        elif disp == 3:
            text = "Restart Game"
        if pos[0]>300 and pos[0]<500 and pos[1]>120 and pos[1]<170:
            pygame.draw.rect(screen, RED,(300, 120, 200, 50), 7)
            screen.blit(myfont.render(text, 1, RED), (340, 135))
        else:
            pygame.draw.rect(screen, WHITE,(300, 120, 200, 50), 7)
            screen.blit(myfont.render(text, 1, WHITE,), (340, 135))
        #Button for Quit Game
        if pos[0]>300 and pos[0]<500 and pos[1]>440 and pos[1]<490:
            pygame.draw.rect(screen, RED,(300, 440, 200, 50), 7)
            screen.blit(myfont.render("Quit Game", 1, RED), (345, 455))
        else:
            pygame.draw.rect(screen, WHITE,(300, 440, 200, 50), 7)
            screen.blit(myfont.render("Quit Game", 1, WHITE,), (345, 455))

        #Blit game name on screen
        screen.blit(pygame.font.SysFont("monospace", 40).render("Space Invasion: To The Red Planet", 1, RED,), (7, 275))
        #Update display
        pygame.display.flip()
        #Set 60 frames per second
        clock.tick(60)

    pygame.mouse.set_visible(False)

"""
game_end_screen function displays final score when the game ends.
Parameter disp indicates one of the two cases- game over due to collision or successful completion of all levels.
The player's final score is also displayed.
"""
def game_end_screen(disp, score):
    pygame.mouse.set_visible(True)
    done = False
    while not done:
        #Run event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                done = True
        #Blit background image on screen
        screen.blit(background_image0, background_position)
        #Display score
        if disp == 1:
            screen.blit(myfont.render("Game Over. Score: {0}".format(score), 20, WHITE,), (290, 240))
        elif disp == 2:
            screen.blit(myfont.render("You won! Score: {0}".format(score), 20, WHITE,), (290, 240))
        screen.blit(myfont.render("Click anywhere to continue.", 20, RED,), (245, 310))
        #Update display
        pygame.display.flip()
        #Set 60 frames per second
        clock.tick(60)
    pygame.mouse.set_visible(False)

"""
For using the various objects derived from sprite class, group lists are created
"""
#Create a list of enemyships
enemy_list = pygame.sprite.Group()
#Function is defined for re-creating enemyships for new levels
def create_enemies(enemy_list):
    j = 0
    i = 0
    for count in range(1, 51):
        enemyship = Enemyship()
        enemyship.rect.x = i*10
        i+=8
        enemyship.rect.y = j*10
        if count%10==0:
            i = 0
            j+=7
        enemy_list.add(enemyship)
#Create a list of player(s), 1 in this case
player_list = pygame.sprite.Group()
player = Player()
player_list.add(player)
#Create a list of bullets
bullet_list = pygame.sprite.Group()
#Create a list of missiles
missile_list = pygame.sprite.Group()

#Start the background music
bgm.play()

"""
Game Logic
"""
#initialise score related variables
score = 0

#define counters for keeping track of time in the game loop
counter_one = 0
counter_two = 0

#Initialising with level 1
level = 1

#When deactivate_shield equal zero, the player won't die on colliding with enemyships or missiles
deactivate_shield = 0

#Call function to create enemyships
create_enemies(enemy_list)

#Start with Start button and Quit button screen
switch_screen(1)

# This hides the mouse cursor
pygame.mouse.set_visible(False)

while True:
    #Run event handling loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            switch_screen(2)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #Bullets are fired when user/ player presses down the mouse button
            click_sound.play()
            #Change bullet type according to score
            if score <= 400:
                #single bullet fire
                bullet = Bullet()
                bullet.rect.x = player.rect.x + 33
                bullet.rect.y = player.rect.y
                bullet_list.add(bullet)
            elif score > 400 and score <=1010 :
                #double bullet fire
                bullet1 = Bullet()
                bullet1.rect.x = player.rect.x + 1
                bullet1.rect.y = player.rect.y
                bullet_list.add(bullet1)
                bullet2 = Bullet()
                bullet2.rect.x = player.rect.x + 63
                bullet2.rect.y = player.rect.y
                bullet_list.add(bullet2)
            elif score > 1010:
                #triple bullet fire
                bullet1 = Bullet()
                bullet1.rect.x = player.rect.x + 12
                bullet1.rect.y = player.rect.y
                bullet_list.add(bullet1)
                bullet2 = Bullet()
                bullet2.rect.x = player.rect.x + 45
                bullet2.rect.y = player.rect.y
                bullet_list.add(bullet2)
                bullet3 = Bullet()
                bullet3.rect.x = player.rect.x + 78
                bullet3.rect.y = player.rect.y
                bullet_list.add(bullet3)    

    #Initialise counters
    #counter_one keeps track of time for updation of enemyships (shifting down)
    counter_one += 1
    #counter_two keeps track of time for deactivating shield
    counter_two += 1

    #Copy background image to screen
    if level == 1:
        screen.blit(background_image1, background_position)
    elif level == 2:
        screen.blit(background_image2, background_position)
    elif level == 3:
        screen.blit(background_image3, background_position)

    #Check hits made by bullets
    for bullet in bullet_list:
        #See if it hit an enemyship
        enemy_hit_list = pygame.sprite.spritecollide(bullet, enemy_list, True)
        #For each enemyship hit, remove the bullet and enemy, and add to the score
        for enemy in enemy_hit_list:
            explosion_sound.play()
            bullet_list.remove(bullet)
            enemy_list.remove(enemy)
            score += 10
        #Remove the bullet if it flies up off the screen
        if bullet.rect.y < -5:
            bullet_list.remove(bullet)

    #Deactivate shield
    if counter_two == 200:
        deactivate_shield = 1;

    #Check if shield is deactivated
    if deactivate_shield == 1:
        screen.blit(myfont.render("Shield Deactivated", 1, WHITE), (550, 10))
        #Detect collision with enemyships and if it happens, set level and score to zero
        collision_list = pygame.sprite.spritecollide(player, enemy_list, True)
        for enemy in collision_list:
            collision_list.remove(enemy)
            explosion_sound_two.play()
            game_end_screen(1, score)
            switch_screen(3)
            enemy_list.empty()
            bullet_list.empty()
            level = 0
            score = 0
            continue
        #Detect collision with missiles and if it happens, set level and score to zero
        collision_list = pygame.sprite.spritecollide(player, missile_list, True)
        for missile in collision_list:
            collision_list.remove(missile)
            explosion_sound_two.play()
            game_end_screen(1, score)
            switch_screen(3)
            enemy_list.empty()
            bullet_list.empty()
            missile_list.empty()
            level = 0
            score = 0
            continue
    else:
        #The shield is active
        screen.blit(myfont.render("Shield Active", 1, WHITE), (600, 10))

    #Loop for detecting if an enemyship has reached the bottom of the screen
    for ship in enemy_list:
        if ship.rect.y > 550:
            game_end_screen(1, score)
            switch_screen(3)
            enemy_list.empty()
            bullet_list.empty()
            level = 0
            score = 0
            continue

    #Generate random missiles using player(x cooordinate) and enemyship(y coordinate) positions and add to list
    for ship in enemy_list:
        x = random.randrange(2000)
        if x == 4:
            missile = Missile()
            missile.rect.x = player.rect.x
            missile.rect.y = ship.rect.y
            missile_list.add(missile)

    #Remove the missile from list if it flies out of the sceen
    for missile in missile_list:
        if missile.rect.y > 550:
            missile_list.remove(missile)

    #Change ships according to score
    if score <= 400:
        player.image = pygame.image.load("rsz_ship1.png").convert()
        player.image.set_colorkey(BLACK)
    if score > 400:
        player.image = pygame.image.load("rsz_ship2.png").convert()
        player.image.set_colorkey(BLACK)
    if score > 1010:
        player.image = pygame.image.load("rsz_ship3.png").convert()
        player.image.set_colorkey(BLACK)

    """
    End of level is indicated by emptying of enemy_list.
    Empty bullet and missile lists and create new enemyships.
    On completion of each level, level is incremented by 1.
    level 0 is for special cases of 'Continue Game' and 'Restart Game'.
    On completion of level 3, screen is switched to one with 'Restart Game' button.
    """
    if level == 0:
        level = 1
        counter_two = 0
        deactivate_shield = 0;
        bullet_list.empty()
        missile_list.empty()
        create_enemies(enemy_list)
    elif len(enemy_list) == 0 and level == 1:
        level = 2
        counter_two = 0
        deactivate_shield = 0;
        bullet_list.empty()
        missile_list.empty()
        create_enemies(enemy_list)
    elif len(enemy_list) == 0 and level == 2:
        level = 3
        counter_two = 0
        deactivate_shield = 0;
        bullet_list.empty()
        missile_list.empty()
        create_enemies(enemy_list)
    elif len(enemy_list) == 0 and level == 3:
        game_end_screen(2, score)
        switch_screen(3)
        level = 0
        score = 0
        continue

    #Update all sprites
    player_list.update()
    bullet_list.update()
    missile_list.update()
    if counter_one >= 7 and level == 1:
        enemy_list.update()
        counter_one = 0
    if counter_one >= 3 and level == 2:
        enemy_list.update()
        counter_one = 0
    if counter_one >= 2 and level == 3:
        enemy_list.update()
        counter_one = 0

    #Draw all sprites
    enemy_list.draw(screen)
    bullet_list.draw(screen)
    missile_list.draw(screen)
    player_list.draw(screen)

    #When shield is active, a shield (circle) is drawn around the player ship
    if deactivate_shield == 0:
        pos = (player.rect.x+35, player.rect.y+40)
        pygame.draw.circle(screen, WHITE, pos, 50, 1)

    #Display score
    screen.blit(myfont.render("Score: {0} Level: {1}".format(score, level), 1, WHITE), (5, 10))

    #Update display
    pygame.display.flip()

    #Set to 60 frames per second
    clock.tick(60)

#Code not reachable but used as marker
pygame.quit()
