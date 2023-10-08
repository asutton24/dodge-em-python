import pygame
from pygame import *
import random
from typing import List, Any

global black
black = (0, 0, 0)
global white
white = (255, 255, 255)
global red
red = (191,54,54)

class Dot:

    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.scr = s
        self.alive = True


    def drawDot(self):
        if self.alive:
            pygame.draw.rect(self.scr, red, (self.x, self.y, 6, 6))

    def unalive(self):
        self.alive = False

    def collideCheck(self, car):
        if not self.alive:
            return False
        if car.getFacing() % 2 == 0:
            x = car.getX() + 3
            y = car.getY() + 9
            xlen = 24
            ylen = 12
        else:
            x = car.getX() + 9
            y = car.getY() + 3
            xlen = 12
            ylen = 24
        if x < self.x and self.x + 6 < x + xlen and y < self.y and self.y + 6 < y + ylen:
            self.unalive()
            return True
        return False

class Board:

    def __init__(self, s):
        self.scr = s
        self.dots = []
        for k in range(2):
            for j in range(4):
                for i in range(int(4)):
                    self.dots.append(Dot(72 + i * 40, 230*k+72+40*j, self.scr))
                for i in range(int(4)):
                    self.dots.append(Dot(302 + i * 40, 230*k+72+40*j, self.scr))

    def getDots(self):
        return self.dots

    def drawBoard(self):
        pygame.draw.rect(self.scr, red, (40, 40, 20, 420))
        pygame.draw.rect(self.scr, red, (440, 40, 20, 420))
        pygame.draw.rect(self.scr, red, (40, 40, 400, 20))
        pygame.draw.rect(self.scr, red, (40, 440, 400, 20))
        pygame.draw.rect(self.scr,red, (90, 90, 10, 130))
        pygame.draw.rect(self.scr, red, (130, 130, 10, 90))
        pygame.draw.rect(self.scr, red, (170, 170, 10, 50))
        pygame.draw.rect(self.scr, red, (90, 90, 130, 10))
        pygame.draw.rect(self.scr, red, (130, 130, 90, 10))
        pygame.draw.rect(self.scr, red, (170, 170, 50, 10))
        pygame.draw.rect(self.scr, red, (90, 280, 10, 130))
        pygame.draw.rect(self.scr, red, (130, 280, 10, 90))
        pygame.draw.rect(self.scr, red, (170, 280, 10, 40))
        pygame.draw.rect(self.scr, red, (90, 400, 130, 10))
        pygame.draw.rect(self.scr, red, (130, 360, 90, 10))
        pygame.draw.rect(self.scr, red, (170, 320, 50, 10))
        pygame.draw.rect(self.scr, red, (280, 90, 130, 10))
        pygame.draw.rect(self.scr, red, (280, 130, 90, 10))
        pygame.draw.rect(self.scr, red, (280, 170, 50, 10))
        pygame.draw.rect(self.scr, red, (400, 90, 10, 130))
        pygame.draw.rect(self.scr, red, (360, 130, 10, 90))
        pygame.draw.rect(self.scr, red, (320, 170, 10, 50))
        pygame.draw.rect(self.scr, red, (280, 400, 130, 10))
        pygame.draw.rect(self.scr, red, (280, 360, 90, 10))
        pygame.draw.rect(self.scr, red, (280, 320, 50, 10))
        pygame.draw.rect(self.scr, red, (400, 280, 10, 130))
        pygame.draw.rect(self.scr, red, (360, 280, 10, 90))
        pygame.draw.rect(self.scr, red, (320, 280, 10, 50))
        pygame.draw.rect(self.scr, red, (360, 130, 10, 90))
        pygame.draw.rect(self.scr, red, (320, 170, 10, 50))
        pygame.draw.rect(self.scr, red, (320, 170, 10, 10))
        pygame.draw.rect(self.scr, red, (280, 210, 10, 80))
        pygame.draw.rect(self.scr, red, (210, 210, 10, 80))
        pygame.draw.rect(self.scr, red, (210, 210, 80, 10))
        pygame.draw.rect(self.scr, red, (210, 280, 80, 10))
        for i in self.dots:
            i.drawDot()
        #pygame.draw.rect(self.scr, (0,0,255),(410,280, 30, 30))


class Vehicle:

    def __init__(self, s, c, l, f, x, y, e):
        self.lane = l
        self.x = x
        self.y = y
        self.facing = f
        self.scr = s
        self.color = c
        self.enemy = e


    def moveForward(self, speed):
        if self.lane == 3:
            val1 = 410
            val2 = 60
        elif self.lane == 2:
            val1 = 370
            val2 = 100
        elif self.lane == 1:
            val1 = 330
            val2 = 140
        elif self.lane == 0:
            val1 = 290
            val2 = 180
        if self.facing == 0:
            self.x += speed
            if self.x >= val1 and speed > 0:
                self.facing = 1
                self.x = val1
            elif self.x <= val2 and speed < 0:
                self.facing = 3
                self.x = val2
        elif self.facing == 1:
            self.y -= speed
            if self.y <= val2 and speed > 0:
                self.facing = 2
                self.y = val2
            elif self.y >= val1 and speed < 0:
                self.facing = 0
                self.y = val1
        elif self.facing == 2:
            self.x -= speed
            if self.x <= val2 and speed > 0:
                self.facing = 3
                self.x = val2
            elif self.x >= val1 and speed < 0:
                self.facing = 1
                self.x = val1
        else:
            self.y += speed
            if self.y >= val1 and speed > 0:
                self.facing = 0
                self.y = val1
            elif self.y <= val2 and speed < 0:
                self.facing = 2
                self.y = val2

    def changeLane(self, x):
        if 0 <= self.lane + x <= 3:
            self.lane += x

    def getFacing(self):
        return self.facing

    def getLane(self):
        return self.lane

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def moveLane(self, dir):
        if dir == 1:
            self.y += 4
        elif dir == -1:
            self.y -= 4
        elif dir == 2:
            self.x += 4
        elif dir == -2:
            self.x -= 4

    def getDir(self, dir):
        if self.enemy:
            val1 = 220
            val2 = 235
        else:
            val1 = 220
            val2 = 250
        if self.facing == 0:
            if self.x > val1 and self.x < val2:
                if dir == -2 and self.lane != 3:
                    return 1
                elif dir == 2 and self.lane != 0:
                    return -1
        elif self.facing == 1:
            if self.y < val2 and self.y > val1:
                if dir == 1 and self.lane != 3:
                    return 2
                elif dir == -1 and self.lane != 0:
                    return -2
        elif self.facing == 2:
            if self.x < val2 and self.x > val1:
                if dir == 2 and self.lane != 3:
                    return -1
                elif dir == -2 and self.lane != 0:
                    return 1
        elif self.facing == 3:
            if self.y > val1 and self.y < val2:
                if dir == -1 and self.lane != 3:
                    return -2
                elif dir == 1 and self.lane != 0:
                    return 2
        return 0

    def atIntersection(self):
        if self.facing % 2 == 0 and (self.getDir(2) != 0 or self.getDir(-2) != 0):
            return True
        elif self.getDir(1) != 0 or self.getDir(-1) != 0:
            return True
        return False

    def drawPlayer(self):
        if self.facing % 2 == 0:
            pygame.draw.rect(self.scr, self.color, (self.x+3,self.y+9,24,12))
            pygame.draw.rect(self.scr, self.color, (self.x + 6, self.y + 6, 6, 18))
            pygame.draw.rect(self.scr, self.color, (self.x + 18, self.y + 6, 6, 18))
        else:
            pygame.draw.rect(self.scr, self.color, (self.x + 9, self.y + 3, 12, 24))
            pygame.draw.rect(self.scr, self.color, (self.x + 6, self.y + 6, 18, 6))
            pygame.draw.rect(self.scr, self.color, (self.x + 6, self.y + 18, 18, 6))

class Enemies:
    def __init__(self, l, s):
        self.target = 3
        if l == 1:
            self.baseSpeed = -3
            self.cars = [Vehicle(s, (255, 133, 188), 3, 0, 210, 410, True)]
            self.speed = [-3]
            self.turn = [[0, 0]]
        elif l % 2 == 0:
            self.baseSpeed = -4
            self.cars = [Vehicle(s, (255, 133, 188), 3, 0, 210, 410, True)]
            self.speed = [-4]
            self.turn = [[0, 0]]
        else:
            self.baseSpeed = -3
            self.cars = [Vehicle(s, (255, 133, 188), 3, 0, 210, 410, True), Vehicle(s, (255, 133, 188), 3, 2, 250, 60, True)]
            self.speed = [-3, -3]
            self.turn = [[0, 0], [0, 0]]

    def moveEnemies(self):
        for i in range(len(self.cars)):
            self.cars[i].moveForward(self.speed[i])
            if self.turn[i][0] > 0:
                self.cars[i].moveLane(self.turn[i][1])
                self.turn[i][0] -= 1
                if self.turn[i][0] == 0:
                    self.speed[i] = self.baseSpeed


    def turnEnemies(self):
        for i in range(len(self.cars)):
            if self.cars[i].atIntersection() and self.cars[i].getLane() != self.target and self.turn[i][0] == 0:
                laneClear = True
                if self.target > self.cars[i].getLane():
                    x = 1
                    self.cars[i].changeLane(1)
                else:
                    x = -1
                    self.cars[i].changeLane(-1)
                if self.cars[i].getFacing() == 0:
                    self.turn[i] = [10, x]
                elif self.cars[i].getFacing() == 1:
                    self.turn[i] = [10, 2*x]
                elif self.cars[i].getFacing() == 2:
                    self.turn[i] = [10, -1*x]
                elif self.cars[i].getFacing() == 3:
                    self.turn[i] = [10, -2*x]
                self.speed[i] = -1.5

    def collide(self, player):
        for i in self.cars:
            if i.getFacing() % 2 == 0:
                val1 = 24
                val2 = 12
            else:
                val1 = 12
                val2 = 24
            if ((i.getX() <= player.getX() <= i.getX() + val1) or (i.getX() <= player.getX() + val1 <= i.getX() + val1)) and ((i.getY() <= player.getY() <= i.getY() + val2) or (i.getY() <= player.getY() + val2 <= i.getY() + val2)):
                return True
        return False

    def drawEnemies(self):
        for i in self.cars:
            i.drawPlayer()

    def getTarget(self, car):
        self.target = car.getLane()

class Display:
    def __init__(self, len, val, xp, yp, scr, col):
        self.nums = []
        self.l = len
        self.v = val
        self.x = xp
        self.y = yp
        self.val = 0
        self.s = scr
        self.color = col
        for i in range(len):
            self.nums.append(SevenSeg(0, self.x + 30 * i, self.y, self.s, self.color))

    def updateVal(self, val):
        if val < 0:
            val = 0
        self.v = val
        temp = val
        for i in range(len(self.nums) - 1, -1, -1):
            self.nums[i].setVal(temp % 10)
            temp = (int)(temp / 10)

    def draw(self):
        for i in self.nums:
            i.draw()



class SevenSeg:
    def __init__(self, v, xPos, yPos, scr, col):
        self.data = []
        v = str(v)
        self.setVal(v)
        self.x = xPos
        self.y = yPos
        self.s = scr
        self.color = col

    def setVal(self, val):
        val = str(val)
        if val == '1':
            self.data = [False, False, True, False, False, True, False]
        elif val == '2':
            self.data = [True, False, True, True, True, False, True]
        elif val == '3':
            self.data = [True, False, True, True, False, True, True]
        elif val == '4':
            self.data = [False, True, True, True, False, True, False]
        elif val == '5':
            self.data = [True, True, False, True, False, True, True]
        elif val == '6':
            self.data = [True, True, False, True, True, True, True]
        elif val == '7':
            self.data = [True, False, True, False, False, True, False]
        elif val == '8':
            self.data = [True, True, True, True, True, True, True]
        elif val == '9':
            self.data = [True, True, True, True, False, True, True]
        elif val == '0':
            self.data = [True, True, True, False, True, True, True]

    def draw(self):
        if self.data[0]:
            pygame.draw.rect(self.s, self.color, (self.x, self.y, 20, 3))
        if self.data[1]:
            pygame.draw.rect(self.s, self.color, (self.x, self.y, 3, 14))
        if self.data[2]:
            pygame.draw.rect(self.s, self.color, (self.x + 17, self.y, 3, 14))
        if self.data[3]:
            pygame.draw.rect(self.s, self.color, (self.x, self.y + 11, 20, 3))
        if self.data[4]:
            pygame.draw.rect(self.s, self.color, (self.x, self.y + 12, 3, 15))
        if self.data[5]:
            pygame.draw.rect(self.s, self.color, (self.x + 17, self.y + 12, 3, 15))
        if self.data[6]:
            pygame.draw.rect(self.s, self.color, (self.x, self.y + 24, 20, 3))

def main():
    pygame.init()
    screen = pygame.display.set_mode([640,480])
    pygame.display.set_caption('Dodge Em')
    running = True
    idle = True
    gameLoop = True
    game = Board(screen)
    p1 = Vehicle(screen, (232, 128, 63), 3, 0 ,260, 410, False)
    scoreDisp = Display(4, 0, 490, 100, screen, (232, 128, 63))
    livesDisp = Display(1, 0, 490, 150, screen, (232, 128, 63))
    clock = pygame.time.Clock()
    moveClock = 0
    playerSpeed = 3
    turnIter = 0
    turnDir = 0
    score = 0
    while running:
        idle = True
        gameLoop = True
        while idle:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    idle = False
                    gameLoop = False
            clock.tick(60)
            screen.fill(black)
            game.drawBoard()
            p1.moveForward(playerSpeed)
            p1.drawPlayer()
            scoreDisp.draw()
            pygame.display.update()
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_RETURN]:
                idle = False
        p1 = Vehicle(screen, (232, 128, 63), 3, 0, 260, 410, False)
        score = 0
        dotCount = 64
        level = 1
        lives = 2
        extraLife = 200
        playerSpeed = 3
        npc = Enemies(level, screen)
        screen.fill(black)
        game.drawBoard()
        p1.drawPlayer()
        npc.drawEnemies()
        scoreDisp.updateVal(score)
        scoreDisp.draw()
        livesDisp.updateVal(lives)
        livesDisp.draw()
        pygame.display.update()
        pygame.time.delay(1000)
        while gameLoop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    gameLoop = False
                    idle = False
            clock.tick(60)
            p1.moveForward(playerSpeed)
            npc.getTarget(p1)
            npc.turnEnemies()
            npc.moveEnemies()
            screen.fill(black)
            game.drawBoard()
            p1.drawPlayer()
            npc.drawEnemies()
            scoreDisp.draw()
            livesDisp.draw()
            pygame.display.update()
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_z]:
                playerSpeed = 5
            else:
                playerSpeed = 3
            if turnDir != 0:
                playerSpeed = 1.5
                p1.moveLane(turnDir)
                turnIter += 1
                if turnIter == 10:
                    turnDir = 0
                    turnIter = 0
            else:
                if pressed_keys[K_LEFT]:
                    turnDir = p1.getDir(-1)
                    if turnDir != 0:
                        if p1.getFacing() == 1:
                            p1.changeLane(-1)
                        elif p1.getFacing() == 3:
                            p1.changeLane(1)
                elif pressed_keys[K_RIGHT]:
                    turnDir = p1.getDir(1)
                    if turnDir != 0:
                        if p1.getFacing() == 1:
                            p1.changeLane(1)
                        elif p1.getFacing() == 3:
                            p1.changeLane(-1)
                elif pressed_keys[K_UP]:
                    turnDir = p1.getDir(2)
                    if turnDir != 0:
                        if p1.getFacing() == 0:
                            p1.changeLane(-1)
                        elif p1.getFacing() == 2:
                            p1.changeLane(1)
                elif pressed_keys[K_DOWN]:
                    turnDir = p1.getDir(-2)
                    if turnDir != 0:
                        if p1.getFacing() == 0:
                            p1.changeLane(1)
                        elif p1.getFacing() == 2:
                            p1.changeLane(-1)
            for i in game.getDots():
                if i.collideCheck(p1):
                    score += 1
                    scoreDisp.updateVal(score)
                    dotCount -= 1
                    if score == extraLife:
                        lives += 1
                        livesDisp.updateVal(lives)
                    break
            if dotCount == 0:
                score += 8 * level
                level += 1
                dotCount = 64
                screen.fill(black)
                game = Board(screen)
                npc = Enemies(level, screen)
                p1 = Vehicle(screen, (232, 128, 63), 3, 0, 260, 410, False)
                game.drawBoard()
                p1.drawPlayer()
                scoreDisp.updateVal(score)
                scoreDisp.draw()
                livesDisp.draw()
                pygame.display.update()
                pygame.time.delay(1000)
            if npc.collide(p1):
                lives -= 1
                screen.fill(black)
                game.drawBoard()
                scoreDisp.draw()
                livesDisp.updateVal(lives)
                livesDisp.draw()
                npc.drawEnemies()
                pygame.display.update()
                game = Board(screen)
                dotCount = 64
                npc = Enemies(level, screen)
                p1 = Vehicle(screen, (232, 128, 63), 3, 0, 260, 410, False)
                if lives < 0:
                    gameLoop = False
                pygame.time.delay(1000)
                if lives >= 0:
                    screen.fill(black)
                    game.drawBoard()
                    scoreDisp.draw()
                    livesDisp.draw()
                    p1.drawPlayer()
                    npc.drawEnemies()
                    pygame.display.update()
                    pygame.time.delay(1000)


main()