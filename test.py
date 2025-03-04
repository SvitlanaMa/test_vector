import pygame

pygame.init()

FPS = 60
clock = pygame.time.Clock()
#створи вікно гри

wind_w, wind_h = 700, 500
window = pygame.display.set_mode((wind_w, wind_h))
pygame.display.set_caption("test")

class Sprite:
    def __init__(self, x, y, w, h, image):
        self.rect = pygame.Rect(x, y, w, h)
        image = pygame.transform.scale(image, (w, h))
        self.image = image

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Sprite):
    def __init__(self, x, y, w, h, image, speed):
        super().__init__(x, y, w, h, image)
        self.speed = speed
    
    def move(self, a, d):
        keys = pygame.key.get_pressed()
        if keys[d]:
            if self.rect.right < wind_w:
                self.rect.x += self.speed
        if keys[a]:
            if self.rect.x > 0:
                self.rect.x -= self.speed 

    def fire(self):
        bullets.append(Bullet(self.rect.centerx - 13,self.rect.y,25,50, bullet_img, 15))

class Bullet(Sprite):
    def __init__(self, x, y, w, h, image, speed):
        super().__init__(x, y, w, h, image)
        self.speed = speed
    
    def move(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            bullets.remove(self)

bullet_img = pygame.image.load("img/bullet.png")
bullets = []
player = Player(0, 400, 50, 50, pygame.image.load("img/sprite.png"), 5)


game = True
while game:
    window.fill((0, 100, 50))
    for bullet in bullets:
        bullet.draw()
        bullet.move()
    player.draw()
    player.move(pygame.K_a, pygame.K_d)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            player.fire()

    pygame.display.update()
    clock.tick(FPS)