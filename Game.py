import pygame
from random import randint

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 2000)
bonus_event = pygame.USEREVENT + 1
pygame.time.set_timer(bonus_event, 15000)
w = 700
h = 500
sc = pygame.display.set_mode((w, h))


Black = (0, 0, 0)
White = (255, 255, 255)
Grey = (177, 177, 177)
Dark_Grey = (100, 100, 100)

clock = pygame.time.Clock()
FPS = 30
pygame.mixer.music.load('carm.wav')
menu_font = pygame.font.SysFont('Hack Regular', 36)

h_speed = 10

def closing_window():
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()

def display_update():
    clock.tick(FPS)
    pygame.display.update()

class bonus(pygame.sprite.Sprite):
    def __init__(self, group):
        pygame.sprite.Sprite.__init__(self)
        self.x = randint(20, w)
        self.image = pygame.image.load('Pill.png')
        self.rect = self.image.get_rect(center = (self.x, 20))
        self.speed = randint(10, 20)
        self.add(group)

    def kil(self):
        self.kill()
    def update(self):
        if self.rect.y < h:
            self.rect.y += self.speed
        else:
            self.kil()



bonuses = pygame.sprite.Group()

class bad_boys(pygame.sprite.Sprite):
    def __init__(self, group):
        pygame.sprite.Sprite.__init__(self)
        self.x = (randint(0, w - 25))
        self.image = pygame.image.load('Untitled.png')
        self.rect = self.image.get_rect(center=(self.x, 0))
        self.add(group)
        self.speed = (randint(1, 15))
    def update(self):
        if self.rect.y < h:
            self.rect.y += self.speed
        else:
            self.kill()


enemies = pygame.sprite.Group()

bad_boys(enemies)
class hero(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect(center = (w//2, h-50))
        self.h_speed = 10
    def update(self):
        motion = ''
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            motion = 'up'
        elif keys[pygame.K_DOWN]:
            motion = 'down'
        elif keys[pygame.K_RIGHT]:
            motion = 'right'
        elif keys[pygame.K_LEFT]:
            motion = 'left'

        if self.rect.y >= 0:
            if motion == 'up':
                self.rect.y -= self.h_speed
        if self.rect.x <= (w - 50):
            if motion == 'right':
                self.rect.x += self.h_speed
        if self.rect.y <= (h - 50):
            if motion == 'down':
                self.rect.y += self.h_speed
        if self.rect.x > 0:
            if motion == 'left':
                self.rect.x -= self.h_speed


hero = hero()

class menu():
    def __init__(self):
        self.menu_go = True

    def button(self, x, y, text, text_color=Grey, color=Grey,):
        surf = pygame.Surface((70, 30))
        rect = surf.get_rect(center=(x, y))
        if rect.collidepoint((pygame.mouse.get_pos())):
            color = Dark_Grey
            text_color = Grey
            for i in pygame.event.get():
                if i.type == pygame.MOUSEBUTTONDOWN:
                    if i.button == 1 and text == 'Quit':
                        pygame.quit()
                        exit()
                    elif i.button == 1 and text == 'Start':
                        self.menu_go = False
        surf.fill(color)
        sc.blit(surf, rect)
        f = menu_font.render(text, 1, text_color)
        text_pos = (x - 30, y - 15)
        sc.blit(f, text_pos)


    def main(self):
        while self.menu_go:
            sc.fill(White)
            self.button(w//2+100, h//2+50, 'Quit', Black)
            self.button(w//2-100, h//2+50, 'Start', Black)
            closing_window()
            display_update()

b = bonus(bonuses)
m = menu()
Go = True
def loop():
    pygame.mixer.music.play()
    while 1:

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
            elif i.type == pygame.USEREVENT:
                bad_boys(enemies)
            elif i.type == bonus_event:
                bonus(bonuses)
        if pygame.sprite.spritecollideany(hero, bonuses):
            b.kil()
            hero.h_speed += 5

        if pygame.sprite.spritecollideany(hero, enemies):
            pygame.quit()
            exit()
        else:
            sc.fill(White)
            sc.blit(hero.image, hero.rect)
            bonuses.draw(sc)
            enemies.draw(sc)
            hero.update()
            enemies.update()
            bonuses.update()
            display_update()

while Go:
    closing_window()
    m.main()
    if not m.menu_go:
        loop()







