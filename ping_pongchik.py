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
    def update(self):
        global skip
        if self.rect.y <= 500:
            self.rect.y += self.speed
        if self.rect.y >= 480:
            self.rect.y -=520
            self.rect.x = randint(5,700)
            skip += 1

desk1 = Player1('desk.png', 25, win_height - 400, 40,20,180)

desk2 = Player2('desk.png', 650, win_height - 200, 4,20,180)


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


    window.blit(background, (0,0))

    desk1.update()
    desk1.reset()
    desk2.update()
    desk2.reset()
    display.update()
    clock.tick(FPS)