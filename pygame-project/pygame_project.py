import pygame
import random

FPS = 60
display_width = 512
display_height = 480
blue_color = (97, 159, 182)
pygame.init()
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Murkwood')
clock = pygame.time.Clock()

bgimage = pygame.image.load('images/background.png').convert_alpha()
heroimage = pygame.image.load('images/hero.png')
goblinimage = pygame.image.load('images/goblin.png')
monsterimage = pygame.image.load('images/monster.png')

class Character:
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def mover(self, event, x, y):
        dir_x = 5
        dir_y = 5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.x -= 5
            elif event.key == pygame.K_RIGHT:
                self.x += 5
            elif event.key == pygame.K_UP:
                self.y += -5
            elif event.key == pygame.K_DOWN:
                self.y -= -5

    def floater(self, x, y):
        if self.x > 512:
            self.x -= 512
        if self.x < 0:
            self.x += 512
        if self.y > 480:
            self.y -= 480
        if self.y < 0:
            self.y += 480

class Goblin(Character):
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    def mover(self, event, x, y, change_dir_countdown):
        if event.type == pygame.KEYDOWN:
            change_dir_countdown -=1
            dir_x = 10
            dir_y = 10
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
                    self.y += -11
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

    def mover(self, event, x, y):
        dir_x = 2
        dir_y = 2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.x -= 2
            elif event.key == pygame.K_RIGHT:
                self.x += 2
            elif event.key == pygame.K_UP:
                self.y += -2
            elif event.key == pygame.K_DOWN:
                self.y -= -2

    def floater(self, x, y):
        if self.x > 482:
            self.x = 482
        if self.x < 0:
            self.x = 0
        if self.y > 450:
            self.y = 450
        if self.y < 0:
            self.y = 0

class Monster(Character):
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def mover(self, event, x, y, achange_dir_countdown):
        if event.type == pygame.KEYDOWN:
            achange_dir_countdown -=1
            dir_x = 10
            dir_y = 10
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
                    self.y += -11
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

        return achange_dir_countdown
pygame.key.set_repeat(50,16)
def main():
    monsterposx = display_width/3
    monsterposy = display_height/3
    goblinposx = display_width/4
    goblinposy = display_height/4
    heroposx = display_width/2
    heroposy = display_height/2
    monster = Monster(monsterposx, monsterposy)
    goblin = Goblin(goblinposx, goblinposy)
    hero = Hero(heroposx, heroposy)
    change_dir_countdown = 5
    achange_dir_countdown = 5
    dir_x = 10
    dir_y = 10

#    lose = pygame.sound.load('sounds/lose.wav')
    # Game initialization

    stop_game = False
    while not stop_game:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                    stop_game = True
            if event.type == pygame.KEYDOWN:
                moving = True
                if moving == True:
                    achange_dir_countdown = monster.mover(event, monster.x, monster.y, change_dir_countdown)
                    change_dir_countdown = goblin.mover(event, goblin.x, goblin.y, change_dir_countdown)
                    monster.floater(monsterposx, monsterposy)
                    hero.mover(event, hero.x, hero.y)
                    hero.floater(heroposx, heroposy)
                    goblin.floater(goblinposx, goblinposy)

            elif event.type == pygame.KEYUP:
                moving = False

        screen.blit(bgimage, (0,0))
        screen.blit(heroimage, (hero.x,hero.y))
        screen.blit(monsterimage, (monster.x,monster.y))
        screen.blit(goblinimage, (goblin.x,goblin.y))

        # Game display
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()
