#создай игру "Лабиринт"!
from pygame import *
init()
text = font.SysFont('Arial', 50) 

windows = display.set_mode((700,500))
display.set_caption('Лабиринт')
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        windows.blit(self.image, (self.rect.x, self.rect.y))
    
#Музыка
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')
mixer.music.load('jungles.ogg')
mixer.music.set_volume(0.30)
mixer.music.play()

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 3:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 440:
            self.rect.y += self.speed
        if keys_pressed[K_LEFT] and self.rect.x > -2:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 640:
            self.rect.x += self.speed

class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__(player_image, player_x, player_y, player_speed, size_x, size_y)
        self.direction = 'left'
    def update(self):
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        if self.rect.x <= 450:
            self.direction = 'right'
        if self.rect.x >= 650:
            self.direction = 'left'

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        windows.blit(self.image, (self.rect.x, self.rect.y))
  
wall_1 = Wall(196,212,0,60,375,150,15)#горизонталь
wall_2 = Wall(196,212,0,60,465,250,15)
wall_3 = Wall(196,212,0,292,265,18,200)#вертикаль
wall_4 = Wall(196,212,0,192,145,18,230)
wall_5 = Wall(196,212,0,300,265,150,15)
wall_6 = Wall(196,212,0,210,145,120,15)
wall_7 = Wall(196,212,0,322,-50,18,210)
wall_8 = Wall(196,212,0,422,-50,18,210)
wall_9 = Wall(196,212,0,430,145,120,15)
wall_10 = Wall(196,212,0,400,265,150,15)
wall_11 = Wall(196,212,0,530,145,120,15)
wall_12 = Wall(196,212,0,632,145,18,60)

win = text.render('ТЫ ПОБЕДИЛ!', True, (255, 215 ,0))
game_over = text.render('ТЫ  ПРОИГРАЛ!', True, (255, 0, 0))

player = Player('hero.png',20,400,5,65,65)
enemy = Enemy('cyborg.png',600,300,3,65,65)
treasure = GameSprite('treasure.png',600,400,0,65,65)

background = transform.scale(image.load('background.jpg'), (700, 500))
finish = False


game = True
while game:
    key_pressed = key.get_pressed()
    if key_pressed[K_r]:
        player.rect.x = 20
        player.rect.y = 400
        finish = False
    if finish != True:
        windows.blit(background,(0, 0))
        player.reset()
        player.update()
        enemy.reset()
        enemy.update()
        treasure.reset()
        wall_1.draw_wall()
        wall_2.draw_wall()
        wall_3.draw_wall()
        wall_4.draw_wall()
        wall_5.draw_wall()
        wall_6.draw_wall()
        wall_7.draw_wall()
        wall_8.draw_wall()
        wall_9.draw_wall()
        wall_10.draw_wall()
        wall_11.draw_wall()
        wall_12.draw_wall()
        if sprite.collide_rect(player, treasure):
            finish  = True
            money.play()
            windows.blit(win, (220, 200))
        if sprite.collide_rect(player, enemy):
            finish = True
            kick.play()
            windows.blit(game_over, (220, 200))
        if sprite.collide_rect(player, wall_1) or sprite.collide_rect(player, wall_2) or sprite.collide_rect(player, wall_3) or sprite.collide_rect(player, wall_4) or sprite.collide_rect(player, wall_5) or sprite.collide_rect(player, wall_6) or sprite.collide_rect(player, wall_7) or sprite.collide_rect(player, wall_8) or sprite.collide_rect(player, wall_9) or sprite.collide_rect(player, wall_10) or sprite.collide_rect(player, wall_11) or sprite.collide_rect(player, wall_12):
            player.rect.x = 20
            player.rect.y = 400 
            kick.play()    
    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(60)
    display.update()        
