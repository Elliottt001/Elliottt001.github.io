import sys
import random
import pygame

# 全局定义
SCREEN_X = 600
SCREEN_Y = 600

# 面向对象 # 用python写程序的思维

# 蛇
class Snake(object):
    # 属性：
        # 1.初始化长度
        # 2.蛇头方向
    def __init__(self):
        self.direction = pygame.K_RIGHT
        self.body = []

        for x in range(5):
            self.addnode()
        
    #方法：
        # 1.吃
        # 2.死亡
        # 3.移动
        # 4.方向
    def addnode(self):
        left, top = (0, 0)
        if self.body:
            left, top = (self.body[0].left, self.body[0].top)
        node = pygame.Rect(left, top, 25, 25)
        if self.direction == pygame.K_LEFT:
            node.left -= 25
        elif self.direction == pygame.K_RIGHT:
            node.left += 25
        elif self.direction == pygame.K_UP:
            node.top -= 25
        elif self.direction == pygame.K_DOWN:
            node.top += 25
        self.body.insert(0, node)
    
    # 删除
    def delnode(self):
        self.body.pop()
    
    # 死亡判断
    def isdead(self):
        # 撞墙
        if self.body[0].x not in range(SCREEN_X):
            return True
        if self.body[0].y not in range(SCREEN_Y):
            return True
        # 撞自己
        if self.body[0] in self.body[1:]:
            return True
        return False

    # 移动
    def move(self):
        self.addnode()
        self.delnode()

    # 改变方向
    def changedirection(self, curkey):
        LR = [pygame.K_LEFT, pygame.K_RIGHT]
        UD = [pygame.K_UP, pygame.K_DOWN]
        if curkey in LR + UD:
            if(curkey in LR) and (self.direction in LR):
                return
            if(curkey in UD) and (self.direction in UD):
                return
            self.direction = curkey

# 食物
class Food:
    def __init__(self):
        self.rect = pygame.Rect(-25, 0, 25, 25)
    
    def remove(self):
        self.rect.x = -25

    def set(self):
        if self.rect.x == -25:
            allpos = []
            # 不能靠墙太近 25 ~ SCREEN_X - 25 之间
            for pos in range(25, SCREEN_X - 25, 25):
                allpos.append(pos)
            self.rect.left = random.choice(allpos)
            self.rect.top = random.choice(allpos)
            print(self.rect)

def show_text(screen, pos, text, color, font_bold = False, font_size = 60, font_italic = False):
    # 获取系统字体， 设置文字大小
    cur_font = pygame.font.SysFont("宋体", font_size)
    # 设置是否加粗
    cur_font.set_bode(font_bold)
    # 设置是否斜体
    cur_font.set_italic(font_italic)
    # 设置文字内容
    text_fmt = cur_font.render(text, 1, color)
    # 绘制文字
    screen.blit(text_fmt, pos)

#界面
def main():
    # 初始化
    pygame.init()
    screen_size = (SCREEN_X, SCREEN_Y)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('贪吃蛇') # 窗口标题
    clock = pygame.time.Clock()
    scores = 0
    isdead = False

    snake = Snake()
    food = Food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                snake.changedirection(event.key)
                if event.key == pygame.K_SPACE and isdead:
                    return main()
            
        screen.fill((255, 255, 255))

        # 画蛇身
        if not isdead:
            snake.move()
        for ret in snake.body:
            pygame.draw.rect(screen, (20, 220, 39), rect, 0)

            # 显示死亡文字
        isdead = snake.isdead()

        if isdead:
            show_text(screen, (100, 200), 'YOU DEAD!', (227, 29, 18), False, 100)
            show_text(screen, (150, 260), 'press space to try again...', (0, 0, 22), False, 30)
            
        # 食物处理    吃到 + 50    食物与蛇头   蛇的长度 + 1方块
        if food.rect == snake.body[0]:
            scores += 50
            food.remove()
            snake.addnode()
        
        food.set()
        pygame.draw.rect(screen, (136, 0, 24), food.rect, 0)

        # 显示分数文字
        show_text(screen, (50, 500), 'Scores : ' + str(scores), (223, 223, 223))

        pygame.display.update()  # 更新
        clock.tick(10)

main()
