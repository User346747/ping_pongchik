from pygame import *
from random import *
font.init()
font2 = font.Font(None, 36)
win_height = 500
win_width = 700
window = display.set_mode((win_width, win_height))
desk = transform.scale(image.load("desk.png"), (100, 90))
ball = transform.scale(image.load("ball.png"), (100, 90))
display.set_caption("Пинг понг")
background = transform.scale(image.load("field.jpg"), (win_width, win_height))
clock = time.Clock()
FPS = 60
clock.tick(FPS)
game = True
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset (self):
        window.blit(self.image,(self.rect.x, self.rect.y))


class Player1(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__(player_image, player_x, player_y, player_speed,w,h)
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w]:
            self.rect.y -= 5
        if keys_pressed[K_s]:
            self.rect.y += 5


class Player2(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__(player_image, player_x, player_y, player_speed,w,h)
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP]:
            self.rect.y -= 5
        if keys_pressed[K_DOWN]:
            self.rect.y += 5

class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__(player_image, player_x, player_y, player_speed, w, h)


desk1 = Player1('desk.png', 25, win_height - 400, 40,20,180)
ball = Enemy('ball.png', 50, 4, 3, 65, 65)
desk2 = Player2('desk.png', 650, win_height - 200, 4,20,180)
finish = False
speed_x = 3
speed_y = 3


balls = sprite.Group()
desks = sprite.Group()
desks.add(desk1)
desks.add(desk2)
balls.add(ball)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1

    if ball.rect.x > win_width-50 or ball.rect.x < 0:
        finish = True



    collides = sprite.groupcollide(balls, desks, False, False)
    for c in collides:
        speed_x *= -1

    window.blit(background, (0,0))
    ball.update()
    ball.reset()
    desk1.update()
    desk1.reset()
    desk2.update()
    desk2.reset()
    display.update()
    clock.tick(FPS)