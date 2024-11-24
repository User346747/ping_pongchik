from pygame import *
from random import *
font.init()
font2 = font.Font(None, 36)
win_height = 500
win_width = 700
window = display.set_mode((win_width, win_height))
display.set_caption("Пинг понг")
white = [200,200,255]
window.fill(white)
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


class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__(player_image, player_x, player_y, player_speed,w,h)
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w]:
            self.rect.y -= 5
        if keys_pressed[K_s]:
            self.rect.y += 5


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
