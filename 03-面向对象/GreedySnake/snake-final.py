import pygame
import random
import copy
    
class Block:
    def __init__(self,blockSize,color):
        self.blockSize = blockSize
        self.xBlock = 0
        self.yBlock = 0
        self.color = color
        
    def GetXYInPixel(self): # 获取屏幕像素坐标
        x = self.xBlock * self.blockSize
        y = self.yBlock * self.blockSize
        return (x, y)

class Food(Block):
    def NewPosition(self,snake):
        while True:
            flag = True
            self.xBlock = random.randint(0,snake.screenSizeInPixel[0]/self.blockSize-1)
            self.yBlock = random.randint(0,snake.screenSizeInPixel[1]/self.blockSize-1)
            #if self == snake.head:
            if self.xBlock == snake.head.xBlock and self.yBlock == snake.head.yBlock:
                flag = False
            else:
                for component in snake.body:
                    #if self == component:
                    if self.xBlock == component.xBlock and self.yBlock == component.yBlock:
                        flag = False
                        break
            if flag:
                break
class Snake:
    def __init__(self,blockSize,initX,initY,screenSizeInPixel,headColor,bodyColor):
        self.head = Block(blockSize,headColor)
        self.head.xBlock = initX
        self.head.xBlock = initY
        self.body = []
        self.bodyColor = bodyColor
        self.direction = "left"
        self.screenSizeInPixel = screenSizeInPixel
    def MoveOneStep(self,food):
        score = 0
        head_copy = copy.copy(self.head)
        if self.direction == 'left' :
            self.head.xBlock -= 1
        elif self.direction == 'right' :
            self.head.xBlock += 1
        elif self.direction == 'up':
            self.head.yBlock -= 1
        elif self.direction == 'down' :
            self.head.yBlock += 1
        if self.IsDead():
            pygame.quit()
            exit()
        head_copy.color=self.bodyColor
        self.body.insert(0,head_copy)
        lastBlock = self.body.pop()
        if self._isEatFood(food):
            score = 1
            food.NewPosition(self)
            self.body.append(lastBlock)   
        return score
        
    def ChangeDirection(self,new_direction):
        if len(self.body) == 0:
            self.direction = new_direction
        else:
            if new_direction == 'left' and self.direction != 'right' :
                self.direction = new_direction
            elif new_direction == 'right' and self.direction != 'left':
                self.direction = new_direction
            elif new_direction == 'up' and self.direction != 'down':
                self.direction = new_direction
            elif new_direction == 'down' and self.direction != 'up':
                self.direction = new_direction
    def IsDead(self):
        x, y = self.head.GetXYInPixel()
        if x<0 or y<0 or x>self.screenSizeInPixel[0] or y>self.screenSizeInPixel[1]:
            return True
        else:
            for component in self.body:
                #if self.head == component:
                if self.head.xBlock==component.xBlock and self.head.yBlock == component.yBlock:
                    return True
        return False
        
    def _isEatFood(self,food):
        if self.head.xBlock==food.xBlock and self.head.yBlock == food.yBlock:
            return True
        else:
            return False

class GreedySnakeGame():
    def __init__(self,WofBlock,HofBlock, blockSize,screen):
        self.sizeInBlock = (WofBlock, HofBlock)
        self.sizeInPixel = (WofBlock * blockSize, HofBlock * blockSize)
        self.blockSize = blockSize
        self.screen = screen
        self.gameSpeed = 7 #游戏速度
        self.snake = None
        self.food = None
        self.level = 1 #游戏关卡
        self.score = 0 #游戏级别

    def InitGame(self,gameSpeed):
        self.gameSpeed = gameSpeed
        snakeInitPosition=(10,10)
        self.snake = Snake(self.blockSize,snakeInitPosition[0],snakeInitPosition[1],self.sizeInPixel,(255,0,0),(180,0,0)) #生成 小蛇 的实例
        self.food = Food(self.blockSize,(0,255,0)) #生成 食物 的实例
        self.food.NewPosition(self.snake)# 根据小蛇位置，随机一个食物位置

    def Run(self,events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:   #如果发生 按键事件，则判断具体按键 是不是 四种方向键
                if event.key == pygame.K_RIGHT:
                    self.snake.ChangeDirection('right')
                elif event.key == pygame.K_LEFT:
                    self.snake.ChangeDirection('left')
                elif event.key == pygame.K_UP:
                    self.snake.ChangeDirection('up')
                elif event.key == pygame.K_DOWN:
                    self.snake.ChangeDirection('down')
        self.score += self.snake.MoveOneStep(self.food)
        self._draw()
        clock.tick(self.gameSpeed)

    def _draw(self):
        pygame.draw.rect(self.screen,(255,255,255), (0, 0, self.sizeInBlock[0]*self.blockSize, self.sizeInBlock[1]*self.blockSize))
        self._drawBlock(self.snake.head)
        for component in self.snake.body:
            self._drawBlock(component)
        self._drawBlock(self.food)
        text = pygame.font.SysFont("宋体",15).render("Score:{}".format(self.score),1,(25,12,255))
        screen.blit(text,(0,0))
        pygame.display.flip()

    def _drawBlock(self,block):
        x,y = block.GetXYInPixel()
        pygame.draw.rect(self.screen,block.color,(x,y,block.blockSize,block.blockSize))

W = 20 # 游戏场地的 宽度（单位为 格子）
H = 20 # 游戏场地的 高度（单位为 格子）
blockSize = 20 # 格子 大小（像素）
screen_size = (W*blockSize,H*blockSize) # 游戏场地的 显示大小（像素）
pygame.init()  # 初始化pygame库
screen = pygame.display.set_mode(screen_size) #初始化显示屏幕

game = GreedySnakeGame(W,H,blockSize,screen) #生成 游戏 的实例
game.InitGame(7) # 游戏初始化
clock = pygame.time.Clock() # 游戏时钟
while True:
    game.Run(pygame.event.get()) # 游戏运行
