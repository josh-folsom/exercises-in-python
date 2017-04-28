
import pygame
import random
width = 512
height = 480
blue_color = (97, 159, 182)
pygame.init()
screen = pygame.display.set_mode((512, 480))
pygame.display.set_caption('My Game')
clock = pygame.time.Clock()

bgImage = pygame.image.load('images/background.png').convert_alpha()
heroImage = pygame.image.load('images/hero.png')
goblinImage = pygame.image.load('images/goblin.png')
monsterImage = pygame.image.load('images/monster.png')

class Character:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    def mover(self):

        if event.key == pygame.K_LEFT:
            self.x -= 5
        elif event.key == pygame.K_RIGHT:
            self.x += 5
        elif event.key == pygame.K_UP:
            self.y += -5
        elif event.key == pygame.K_DOWN:
            self.y -= -5

    def floater(self):
        if self.x > 512:
            self.x -= 512
        if self.x < 0:
            self.x += 512
        if self.y > 480:
            self.y -= 480
        if self.y < 0:
            self.y += 480
#


class Monster(Character):
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def mover(self):
        change_dir_countdown -= 1
        if change_dir_countdown == 0:
            change_dir_countdown = 120
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
            self.x -= 5
        elif event.key == pygame.K_RIGHT:
            self.x += 5
        elif event.key == pygame.K_UP:
            self.y += -5
        elif event.key == pygame.K_DOWN:
            self.y -= -5

def main():
    monster_x = 300
    monster_y = 300
    hero_x = 200
    hero_y = 200
    goblin_x = 100
    goblin_y = 100
    change_dir_countdown = 120
    dir_x = 5
    dir_y = 5


    monster = Monster(300,300)

#    lose = pygame.sound.load('sounds/lose.wav')

    # Game initialization

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # mover(Monster)
            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True
        if event.type == pygame.KEYDOWN:

            change_dir_countdown -= 1
            if change_dir_countdown == 0:
                change_dir_countdown = 120
                adjust = random.randint(0,3)
                if adjust == 0:
                    monster_x = monster_x + dir_x
                    monster_y = monster_y + dir_y
                elif adjust == 1:
                    monster_x = monster_x + dir_x
                    monster_y = monster_y - dir_y
                elif adjust == 2:
                    monster_x = monster_x - dir_x
                    monster_y = monster_y + dir_y
                elif adjust == 3:
                    monster_x = monster_x - dir_x
                    monster_y = monster_y - dir_y
            if event.key == pygame.K_LEFT:
                monster_x -= 5
            elif event.key == pygame.K_RIGHT:
                monster_x += 5
            elif event.key == pygame.K_UP:
                monster_y += -5
            elif event.key == pygame.K_DOWN:
                monster_y -= -5
        if event.type == pygame.KEYDOWN:
            monster.floater()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                hero_x -= 5
            elif event.key == pygame.K_RIGHT:
                hero_x += 5
            elif event.key == pygame.K_UP:
                hero_y += -5
            elif event.key == pygame.K_DOWN:
                hero_y -= -5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                goblin_x -= 5
            elif event.key == pygame.K_RIGHT:
                goblin_x += 5
            elif event.key == pygame.K_UP:
                goblin_y += -5
            elif event.key == pygame.K_DOWN:
                goblin_y -= -5
        # if event.type == pygame.KEYDOWN:

        # if monster_x > 512:
        #     monster_x -= 512
        # if monster_x < 0:
        #     monster_x += 512
        # if monster_y > 480:
        #     monster_y -= 480
        # if monster_y < 0:
        #     monster_y += 480

        if hero_x > 512:
            hero_x -= 512
        if hero_x < 0:
            hero_x += 512
        if hero_y > 480:
            hero_y -= 480
        if hero_y < 0:
            hero_y += 480

        if goblin_x > 512:
            goblin_x -= 512
        if goblin_x < 0:
            goblin_x += 512
        if goblin_y > 480:
            goblin_y -= 480
        if goblin_y < 0:
            goblin_y += 480

        screen.blit(bgImage, (0,0))
        screen.blit(goblinImage, (goblin_x,goblin_y))
        screen.blit(heroImage, (hero_x,hero_y))
        screen.blit(monsterImage, (monster_x,monster_y))


        # Game display

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
