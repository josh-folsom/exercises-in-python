import pygame
import random
import time
import sys, os

# this is the area that has the information to initialize the Game
# i set the initial infomration needed for variables to be here as well
FPS = 30
display_width = 512
display_height = 480
pygame.init()
sound1 = pygame.mixer.Sound('sounds/music.wav')
sound2 = pygame.mixer.Sound('sounds/win.wav')
sound3 = pygame.mixer.Sound('sounds/lose.wav')
pygame.mixer.Sound.play(sound1)
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Murkwood')
clock = pygame.time.Clock()
red = (200,0,0)
white = (255,255,255)
black = (0,0,0)
green = (0,128,0)
blue_color = (0,0,255)
collision = False
pause = False

# this is all the sprite images and backrounds
bgimage = pygame.image.load('images/background.png').convert_alpha()
heroimage = pygame.image.load('images/hero.png')
goblinimage = pygame.image.load('images/goblin.png')
goblinimage2 = pygame.image.load('images/goblin.png')
goblinimage3 = pygame.image.load('images/goblin.png')
monsterimage = pygame.image.load('images/monster.png')

# classes begin here
class Character:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
# this is the general class functions that any sprite would inherit by default
    def mover(self, event, x, y):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.x -= 4
            elif event.key == pygame.K_RIGHT:
                self.x += 4
            elif event.key == pygame.K_UP:
                self.y += -4
            elif event.key == pygame.K_DOWN:
                self.y -= -4
#general class function to let the sprite wrap around from one side of the screen
    def floater(self, x, y):
        if self.x > 512:
            self.x -= 512
        if self.x < 0:
            self.x += 512
        if self.y > 480:
            self.y -= 480
        if self.y < 0:
            self.y += 480
# class with a specialized movement to generate random movements
class Goblin(Character):
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    def mover(self, event, x, y, change_dir_countdown):
        if event.type == pygame.KEYDOWN:
            change_dir_countdown -=1
            dir_x = random.randint(5,10)
            dir_y = random.randint(5,10)
            if change_dir_countdown == 0:
                change_dir_countdown = 5
                adjust = random.randint(0,3)
                if adjust == 0:
                    self.x = self.x + dir_x
                    self.y = self.y + dir_y
                elif adjust == 1:
                    self.x = self.x + dir_x
                    self.y = self.y - dir_y
                elif adjust == 2:
                    self.x = self.x - dir_x
                    self.y = self.y + dir_y
                elif adjust == 3:
                    self.x = self.x - dir_x
                    self.y = self.y - dir_y
                if event.key == pygame.K_LEFT:
                    kleft = random.randint(0,3)
                    if kleft == 0:
                        self.x = self.x + dir_x
                        self.y = self.y + dir_y
                    elif kleft == 1:
                        self.x = self.x + dir_x
                        self.y = self.y - dir_y
                    elif kleft == 2:
                        self.x = self.x - dir_x
                        self.y = self.y + dir_y
                    elif kleft == 3:
                        self.x = self.x - dir_x
                        self.y = self.y - dir_y
                elif event.key == pygame.K_RIGHT:
                    kright = random.randint(0,3)
                    if kright == 0:
                        self.x = self.x + dir_x
                        self.y = self.y + dir_y
                    elif kright == 1:
                        self.x = self.x + dir_x
                        self.y = self.y - dir_y
                    elif kright == 2:
                        self.x = self.x - dir_x
                        self.y = self.y + dir_y
                    elif kright == 3:
                        self.x = self.x - dir_x
                        self.y = self.y - dir_y
                elif event.key == pygame.K_UP:
                    kup = random.randint(0,3)
                    if kup == 0:
                        self.x = self.x + dir_x
                        self.y = self.y + dir_y
                    elif kup == 1:
                        self.x = self.x + dir_x
                        self.y = self.y - dir_y
                    elif kup == 2:
                        self.x = self.x - dir_x
                        self.y = self.y + dir_y
                    elif kup == 3:
                        self.x = self.x - dir_x
                        self.y = self.y - dir_y
                elif event.key == pygame.K_DOWN:
                    kdown = random.randint(0,3)
                    if kdown == 0:
                        self.x = self.x + dir_x
                        self.y = self.y + dir_y
                    elif kdown == 1:
                        self.x = self.x + dir_x
                        self.y = self.y - dir_y
                    elif kdown == 2:
                        self.x = self.x - dir_x
                        self.y = self.y + dir_y
                    elif kdown == 3:
                        self.x = self.x - dir_x
                        self.y = self.y - dir_y
        return change_dir_countdown

class Hero(Character):
    def __init__ (self, x, y):
        self.x = x
        self.y = y
# specialized move funciton to provide slower movements that are not random
    def mover(self, event, x, y):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.x -= 3
            elif event.key == pygame.K_RIGHT:
                self.x += 3
            elif event.key == pygame.K_UP:
                self.y -= 3
            elif event.key == pygame.K_DOWN:
                self.y += 3
# class with a specialized float that won't let him wrap from side to side
    def floater(self, x, y):
        if self.x > 482:
            self.x = 482
        if self.x < 0:
            self.x = 0
        if self.y > 450:
            self.y = 450
        if self.y < 0:
            self.y = 0
# class with specialied move feature and wrap feature, fastest class as well
class Monster(Character):
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def mover(self, event, x, y, achange_dir_countdown):
        if event.type == pygame.KEYDOWN:
            achange_dir_countdown -=1
            dir_x = random.randint(15,25)
            dir_y = random.randint(15,25)
            if achange_dir_countdown == 0:
                achange_dir_countdown = 5
                adjust = random.randint(0,3)
                if adjust == 0:
                    self.x = self.x + dir_x
                    self.y = self.y + dir_y
                elif adjust == 1:
                    self.x = self.x + dir_x
                    self.y = self.y - dir_y
                elif adjust == 2:
                    self.x = self.x - dir_x
                    self.y = self.y + dir_y
                elif adjust == 3:
                    self.x = self.x - dir_x
                    self.y = self.y - dir_y
                if event.key == pygame.K_LEFT:
                    kleft = random.randint(0,3)
                    if kleft == 0:
                        self.x = self.x + dir_x
                        self.y = self.y + dir_y
                    elif kleft == 1:
                        self.x = self.x + dir_x
                        self.y = self.y - dir_y
                    elif kleft == 2:
                        self.x = self.x - dir_x
                        self.y = self.y + dir_y
                    elif kleft == 3:
                        self.x = self.x - dir_x
                        self.y = self.y - dir_y
                elif event.key == pygame.K_RIGHT:
                    kright = random.randint(0,3)
                    if kright == 0:
                        self.x = self.x + dir_x
                        self.y = self.y + dir_y
                    elif kright == 1:
                        self.x = self.x + dir_x
                        self.y = self.y - dir_y
                    elif kright == 2:
                        self.x = self.x - dir_x
                        self.y = self.y + dir_y
                    elif kright == 3:
                        self.x = self.x - dir_x
                        self.y = self.y - dir_y
                elif event.key == pygame.K_UP:
                    kup = random.randint(0,3)
                    if kup == 0:
                        self.x = self.x + dir_x
                        self.y = self.y + dir_y
                    elif kup == 1:
                        self.x = self.x + dir_x
                        self.y = self.y - dir_y
                    elif kup == 2:
                        self.x = self.x - dir_x
                        self.y = self.y + dir_y
                    elif kup == 3:
                        self.x = self.x - dir_x
                        self.y = self.y - dir_y

                elif event.key == pygame.K_DOWN:
                    kdown = random.randint(0,3)
                    if kdown == 0:
                        self.x = self.x + dir_x
                        self.y = self.y + dir_y
                    elif kdown == 1:
                        self.x = self.x + dir_x
                        self.y = self.y - dir_y
                    elif kdown == 2:
                        self.x = self.x - dir_x
                        self.y = self.y + dir_y
                    elif kdown == 3:
                        self.x = self.x - dir_x
                        self.y = self.y - dir_y
# this return is like the retuen in goblin, mandatory from coundown counter method
        return achange_dir_countdown

# this is a pygame feature that allows the button to be held down for constant movement
pygame.key.set_repeat(50,16)

# the beginning of the main program and where I generate all my random numbers for x and y
# randomization.
def main():
    randomnumX1 = random.randint(0, 480)
    randomnumY1 = random.randint(0, 450)
    randomnumX2 = random.randint(0, 480)
    randomnumY2 = random.randint(0, 450)
    randomnumX3 = random.randint(0, 480)
    randomnumY3 = random.randint(0, 450)
    randomnumX4 = random.randint(0, 480)
    randomnumY4 = random.randint(0, 450)
    randomnumX5 = random.randint(0, 480)
    randomnumY5 = random.randint(0, 450)
# the above randoms are assigned to the sprites below accordingly
    monsterposx = randomnumX1
    monsterposy = randomnumY1
    goblinposx = randomnumX2
    goblinposy = randomnumY2
    goblin2posx = randomnumX4
    goblin2posy = randomnumY4
    goblin3posx = randomnumX5
    goblin3posy = randomnumY5
    heroposx = randomnumX3
    heroposy = randomnumY3
# here i generate my characters and provide x,y coords from above
    goblin = Goblin(goblinposx, goblinposy)
    goblin2 = Goblin(goblin2posx, goblin2posy)
    goblin3 = Goblin(goblin3posx, goblin3posy)
    hero = Hero(heroposx, heroposy)
    monster = Monster(monsterposx, monsterposy)
# this is a feature of the randomization countdown, sets initial count
    change_dir_countdown = 5
    achange_dir_countdown = 5
# sets font for in game text notifications.  25 is the size.
    font = pygame.font.SysFont(None, 25)
# this is the function used create text messages easily.
    def text_objects(text, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()
# this is the function that is used to actually write them to the screen
    def message_to_screen(msg, color, y_displace=0):
        textSurf, textRect = text_objects(msg, color)
        textRect.center = (display_width / 2), (display_height / 2)+y_displace
        screen.blit(textSurf, textRect)


    # Game initialization
# begin of game loop
    stop_game = False
    while not stop_game:
        while stop_game == True:
            message_to_screen("Game Over", red, -20)
            pygame.display.update()
# the vast majority of my game goes inside this loop below.
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                    stop_game = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    stop_game = True
# i decided to add a pause feature, this is how i did it below.
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_p:
                    pause = True
                    message_to_screen("PAUSED", white, -20)
                    message_to_screen("press P to unpause", white, 20)
                    pygame.display.update()
                    while pause == True:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYUP:
                                if event.key == pygame.K_p:
                                    pause = False

# this is the majority of my sprites added to the game and all the functions they
# need to move and float/wrap around the board.  lots of repitition because of 5
# differet sprites.
            if event.type == pygame.KEYDOWN:
                moving = True
                if moving == True:
                    screen.blit(heroimage, (hero.x,hero.y))
                    screen.blit(monsterimage, (monster.x,monster.y))
                    screen.blit(goblinimage, (goblin.x,goblin.y))
                    screen.blit(goblinimage2, (goblin2.x,goblin2.y))
                    screen.blit(goblinimage3, (goblin3.x,goblin3.y))
                    achange_dir_countdown = monster.mover(event, monster.x, monster.y, change_dir_countdown)
                    change_dir_countdown = goblin.mover(event, goblin.x, goblin.y, change_dir_countdown)
                    change_dir_countdown = goblin2.mover(event, goblin2.x, goblin2.y, change_dir_countdown)
                    change_dir_countdown = goblin3.mover(event, goblin3.x, goblin3.y, change_dir_countdown)
                    monster.floater(monster.x, monster.y)
                    hero.mover(event, hero.x, hero.y)
                    hero.floater(hero.x, hero.y)
                    goblin.floater(goblin.x, goblin.y)
                    goblin2.floater(goblin2.x, goblin2.y)
                    goblin3.floater(goblin3.x, goblin3.y)

            elif event.type == pygame.KEYUP:
                moving = False
# this is how you remove an image from teh screen if they are considered dead
        objectsonscreen = []
        objectsonscreen.append(bgimage)
        screen.blit(bgimage, (0,0))
        screen.blit(heroimage, (hero.x,hero.y))
        screen.blit(monsterimage, (monster.x,monster.y))
        screen.blit(goblinimage, (goblin.x,goblin.y))
        screen.blit(goblinimage2, (goblin2.x,goblin2.y))
        screen.blit(goblinimage3, (goblin3.x,goblin3.y))
                # Game display
# i don't know if you need so many updates, but i tried to add a few to make the
# screen refresh more frequently to give the appearance of less choppy animation
        pygame.display.update()
# this is the collision statment between the first goblin and the hero.  and how to remove
# the hero when he dies is underneath.  including sound effects and messages to the screen
        if goblin.x > hero.x and goblin.x < hero.x + 30 or goblin.x + 30 > hero.x and goblin.x + 30 < hero.x + 30 or goblin.x < hero.x and goblin.x > hero.x - 30 or goblin.x - 30 < hero.x and goblin.x - 30 > hero.x - 30:
            if goblin.y > hero.y and goblin.y < hero.y + 30 or goblin.y + 30 > hero.y and goblin.y + 30 < hero.x + 30 or goblin.y < hero.y and goblin.y > hero.y - 30 or goblin.y - 30 < hero.y and goblin.y - 30 > hero.x - 30:
                if goblin.y + 30 > hero.y and goblin.y + 30 < hero.y + 30 or goblin.y - 30 < hero.y and goblin.y - 30 > hero.y - 30:
                    objectsonscreen.append(hero)
                    screen.blit(bgimage, (0,0))
                    pygame.display.update()
                    objectsonscreen = [bgimage, monsterimage, goblinimage]
                    screen.blit(bgimage, (0,0))
                    screen.blit(monsterimage, (monster.x,monster.y))
                    screen.blit(goblinimage, (goblin.x,goblin.y))
                    screen.blit(goblinimage2, (goblin2.x,goblin2.y))
                    pygame.display.update()
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(sound3)
                    message_to_screen("You were killed by a GOBLIN!", red, -20)
                    message_to_screen("Press ENTER to play again or ESCAPE to quit", white, 20)
                    pygame.display.update()
                    time.sleep(3)
# this is the collision statment between the second goblin and the hero.  and how to remove
# the hero when he dies is underneath.  including sound effects and messages to the screen

        if goblin2.x > hero.x and goblin2.x < hero.x + 30 or goblin2.x + 30 > hero.x and goblin2.x + 30 < hero.x + 30 or goblin2.x < hero.x and goblin2.x > hero.x - 30 or goblin2.x - 30 < hero.x and goblin2.x - 30 > hero.x - 30:
            if goblin2.y > hero.y and goblin2.y < hero.y + 30 or goblin2.y + 30 > hero.y and goblin2.y + 30 < hero.x + 30 or goblin2.y < hero.y and goblin2.y > hero.y - 30 or goblin2.y - 30 < hero.y and goblin2.y - 30 > hero.x - 30:
                if goblin2.y + 30 > hero.y and goblin2.y + 30 < hero.y + 30 or goblin2.y - 30 < hero.y and goblin2.y - 30 > hero.y - 30:
                    objectsonscreen.append(hero)
                    screen.blit(bgimage, (0,0))
                    pygame.display.update()
                    objectsonscreen = [bgimage, monsterimage, goblinimage]
                    screen.blit(bgimage, (0,0))
                    screen.blit(monsterimage, (monster.x,monster.y))
                    screen.blit(goblinimage, (goblin.x,goblin.y))
                    screen.blit(goblinimage2, (goblin2.x,goblin2.y))
                    pygame.display.update()
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(sound3)
                    message_to_screen("You were killed by a GOBLIN!", red, -20)
                    message_to_screen("Press ENTER to play again or ESCAPE to quit", white, 20)
                    pygame.display.update()
                    time.sleep(3)
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            stop_game = True
                        elif event.key == pygame.K_RETURN:
                            stop_game = False
                            return main()
# this is the collision statment between the third goblin and the hero.  and how to remove
# the hero when he dies is underneath.  including sound effects and messages to the screen


        if goblin3.x > hero.x and goblin3.x < hero.x + 30 or goblin3.x + 30 > hero.x and goblin3.x + 30 < hero.x + 30 or goblin3.x < hero.x and goblin3.x > hero.x - 30 or goblin3.x - 30 < hero.x and goblin3.x - 30 > hero.x - 30:
            if goblin3.y > hero.y and goblin3.y < hero.y + 30 or goblin3.y + 30 > hero.y and goblin3.y + 30 < hero.x + 30 or goblin3.y < hero.y and goblin3.y > hero.y - 30 or goblin3.y - 30 < hero.y and goblin3.y - 30 > hero.x - 30:
                if goblin3.y + 30 > hero.y and goblin3.y + 30 < hero.y + 30 or goblin3.y - 30 < hero.y and goblin3.y - 30 > hero.y - 30:
                    objectsonscreen.append(hero)
                    screen.blit(bgimage, (0,0))
                    pygame.display.update()
                    objectsonscreen = [bgimage, monsterimage, goblinimage]
                    screen.blit(bgimage, (0,0))
                    screen.blit(monsterimage, (monster.x,monster.y))
                    screen.blit(goblinimage, (goblin.x,goblin.y))
                    screen.blit(goblinimage2, (goblin2.x,goblin2.y))
                    screen.blit(goblinimage3, (goblin3.x,goblin3.y))
                    pygame.display.update()
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(sound3)
                    message_to_screen("You were killed by a GOBLIN!", red, -20)
                    message_to_screen("Press ENTER to play again or ESCAPE to quit", white, 20)
                    pygame.display.update()
                    time.sleep(3)

# this is the collision statment between the monster and the hero.  and how to remove
# the hero when he dies is underneath.  including sound effects and messages to the screen
        if monster.x > hero.x and monster.x < hero.x + 30 or monster.x + 30 > hero.x and monster.x + 30 < hero.x + 30 or monster.x < hero.x and monster.x > hero.x - 30 or monster.x - 30 < hero.x and monster.x - 30 > hero.x - 30:
            if monster.y > hero.y and monster.y < hero.y + 30 or monster.y + 30 > hero.y and monster.y + 30 < hero.x + 30 or monster.y < hero.y and monster.y > hero.y - 30 or monster.y - 30 < hero.y and monster.y - 30 > hero.x - 30:
                if monster.y + 30 > hero.y and monster.y + 30 < hero.y + 30 or monster.y - 30 < hero.y and monster.y - 30 > hero.y - 30:
                    objectsonscreen.append(monster)
                    screen.blit(bgimage, (0,0))
                    pygame.display.update()
                    objectsonscreen = [bgimage, heroimage, goblinimage]
                    screen.blit(bgimage, (0,0))
                    screen.blit(heroimage, (hero.x,hero.y))
                    screen.blit(goblinimage, (goblin.x,goblin.y))
                    screen.blit(goblinimage2, (goblin2.x,goblin2.y))
                    screen.blit(goblinimage3, (goblin3.x,goblin3.y))
                    pygame.display.update()
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(sound2)
                    message_to_screen("You Win!", blue_color, -20)
                    message_to_screen("Press ENTER to play again or ESCAPE to quit", white, 20)
                    pygame.display.update()
                    time.sleep(3)
# thisis how i setup the press ESCAPE to quit feature
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            stop_game = True
                        elif event.key == pygame.K_RETURN:
                            stop_game = False
                            return main()
        clock.tick(FPS)
    pygame.display.update()
    time.sleep(1)
    pygame.quit()
    quit()

if __name__ == '__main__':
    main()
