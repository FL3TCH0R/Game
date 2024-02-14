import pygame
import random

Screen_width=600
Screen_height=600

FPS=40

ENEMY_SPAWN_RATE = 2
ENEMY_MIN_SIZE = 4
ENEMY_MAX_SIZE = 15
ENEMY_MIN_SPEED = 2
ENEMY_MAX_SPEED = 10

PLAYER_SPEED=3
PLAYER_SIZE=10
PLAYER_MAX_UP=150

BG_COLOR=pygame.Color("black")
TEXT_COLOR=pygame.Color("white")
ENEMY_COLOR=pygame.Color("gray")
PLAYER_COLOR=pygame.Color("darkgreen")

class Player:
    def __init__(self):
        self.size=PLAYER_SIZE
        self.speed=PLAYER_SPEED
        self.color=PLAYER_COLOR
        self.position=(Screen_width/2, (Screen_height - (Screen_height/10)))

    def draw(self, surface):
        r = self.get_rect()
        pygame.draw.rect(surface, self.color, r)

    def move(self, x, y):
        newX = self.position[0] + x
        newY = self.position[1] + y
        if newX < 0 or newX > Screen_width - PLAYER_SIZE:
            newX=self.position[0]
        if newY < Screen_height - PLAYER_MAX_UP or newY > Screen_height - PLAYER_SIZE:
            newY=self.position[1]
        self.position=(newX, newY)

    def get_rect(self):
        return pygame.Rect(self.position, (self.size, self.size))

    def did_hit(self, rect):
        r =self.get_rect()
        return r.colliderect(rect)

class Enemy:
    def __init__(self):
        self.size=random.randint(ENEMY_MIN_SIZE, ENEMY_MAX_SIZE)
        self.speed= random.randint(ENEMY_MIN_SPEED, ENEMY_MAX_SPEED)
        self.color=ENEMY_COLOR
        self.position=(random.randint(0, Screen_width-self.size), 0 - self.size)

    def draw(self,surface):
        r = self.get_rect()
        pygame.draw.rect(surface, self.color, r)

    def move(self):
        self.position=(self.position[0], self.position[1] + self.speed)

    def is_off_screen(self):
        return self.position[1]>Screen_height

    def get_rect(self):
        return pygame.Rect(self.position, (self.size, self.size))

class World:
    def __init__(self):
        self.reset()

    def reset(self):
        self.player=Player()
        self.enemies=[]
        self.gameOver=False
        self.score=0
        self.enemy_counter=0
        self.moveUp=False
        self.moveDown=False
        self.moveLeft=False
        self.moveRight=False

    def is_game_over(self):
        return self.gameOver

    def update(self):
        self.score += 1

        if self.moveUp:
            self.player.move(0, -PLAYER_SPEED)
        if self.moveDown:
            self.player.move(0, PLAYER_SPEED)
        if self.moveLeft:
            self.player.move(-PLAYER_SPEED, 0)
        if self.moveRight:
            self.player.move(PLAYER_SPEED, 0)

        for e in self.enemies:
            e.move()
            if self.player.did_hit(e.get_rect()):
                self.gameOver=True
            if e.is_off_screen():
                self.enemies.remove(e)

        self.enemy_counter += 1
        if self.enemy_counter > ENEMY_SPAWN_RATE:
            self.enemy_counter=0
            self.enemies.append(Enemy())

    def draw(self, surface):
        self.player.draw(surface)
        for e in self.enemies:
            e.draw(surface)

    def handle_keys(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                self.moveUp = True
            if event.key==pygame.K_DOWN:
                self.moveDown = True
            if event.key==pygame.K_LEFT:
                self.moveLeft = True
            if event.key==pygame.K_RIGHT:
                self.moveRight = True

        if event.type == pygame.KEYUP:
            if event.key==pygame.K_UP:
                self.moveUp = False
            if event.key==pygame.K_DOWN:
                self.moveDown = False
            if event.key==pygame.K_LEFT:
                self.moveLeft = False
            if event.key==pygame.K_RIGHT:
                self.moveRight = False

    

def run():
    pygame.init()

    clock=pygame.time.Clock()
    screen=pygame.display.set_mode((Screen_width, Screen_height))
    pygame.display.set_caption("DODGE")

    surface=pygame.Surface(screen.get_size())
    surface=surface.convert()

    world = World()

    font=pygame.font.SysFont("monospace",42)

    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            elif event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                running=False
            elif event.type==pygame.KEYDOWN and event.key == ord("r"):
                world.reset()
            else:
                world.handle_keys(event)

        clock.tick(FPS)

        if not world.is_game_over():
            world.update()

        surface.fill(BG_COLOR)

        world.draw(surface)

        screen.blit(surface, (0,0))
        text = font.render("Score 0",format(world.score), 1, TEXT_COLOR)
        screen.blit(text, (5,10))
        if world.is_game_over():
            go = font.render("GAME OVER", 1, TEXT_COLOR)
            screen.blit(go, (Screen_width/3, Screen_height/2))
            hr = font.render("Hit R to reset", 1, TEXT_COLOR)
            screen.blit(hr, (Screen_width/3, Screen_height/2 +45))

        pygame.display.update()



if __name__ == '__main__':
    run()
    pygame.quit()

        

            
