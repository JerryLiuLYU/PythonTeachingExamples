import pygame
import random

pygame.init()

#建立画布
blocksize = 20
W = blocksize*20
H = blocksize*20

screen_size = (W,H)
screen = pygame.display.set_mode(screen_size)

#方块坐标
def point(x,y):
    x=x*blocksize
    y=y*blocksize
    return [x,y]

#画方块
def draw(point,color):
    x=point[0]
    y=point[1]
    pygame.draw.rect(screen,color,(x,y,blocksize,blocksize))

#判断是否吃到食物
def eatFood(snake,food):
    if snake[0]==food[0] and snake[1] == food [1]:
        return True
    else:
        return False

#判断是否碰撞
def collide(head,body):
    if head[0]<0 or head[1]<0 or head[0]>W or head[1]>H:
        return True
    else:
        for component in body:
            if head == component:
                return True
    return False

#生成食物
def getFood(head,body):
    while True:
        flag = True
        food =point(random.randint(0,W/blocksize-1),random.randint(0,H/blocksize-1))
        if food == head:
            continue
        for component in body:
            if food == component:
                flag = False
                break
        if flag:
            break
    return food

#蛇的颜色，大小
head = point(random.randint(W/blocksize/2,W/blocksize-1),random.randint(0,H/blocksize-1))
head_color = (0,100,0)
body = []
body_color = (50,205,50)
food = getFood(head,body)
food_color = (220,20,60)
#确定初始方向
direction ='left'
new_direction = direction

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
    #方向按键
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                new_direction= 'right'
            elif event.key == pygame.K_LEFT:
                new_direction = 'left'
            elif event.key == pygame.K_UP:
                new_direction = 'up'
            elif event.key == pygame.K_DOWN:
                new_direction = 'down'
#改变方向
    if len(body) == 0:
        direction = new_direction
    else:
        if new_direction == 'left' and direction != 'right' :
            direction = new_direction
        elif new_direction == 'right' and direction != 'left':
            direction = new_direction
        elif new_direction == 'up' and direction != 'down':
            direction = new_direction
        elif new_direction == 'down' and direction != 'up':
            direction = new_direction
    head_copy = list(head)
    if direction == 'left' :
        head[0] -= blocksize
    elif direction == 'right' :
        head[0] += blocksize
    elif direction == 'up':
        head[1] -= blocksize
    elif direction == 'down' :
        head[1] += blocksize
#判断碰撞
    if collide(head,body):
        pygame.quit()
        exit()
    body.insert(0,head_copy)
#判断是否吃到食物
    if eatFood(head,food):
        food=getFood(head,body)     
    else:
        body.pop()
#刷新窗体
    pygame.draw.rect(screen,(255,255,255), (0, 0, W, H))
    draw(head,head_color)
    for component in body:
        draw(component,body_color)
    draw(food,food_color)
    pygame.display.flip()
    clock.tick(7)
