import pygame,sys




screen = pygame.display.set_mode((800,600))
fbs = pygame.time.Clock()

class p1(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__()
        self.image = pygame.image.load('Assets/enemies/carrot/carrot_w_1.png')
        self.rect = self.image.get_rect(center = (pos))
        self.add(group)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= 3
        if keys[pygame.K_s]:
            self.rect.y += 3
        if keys[pygame.K_a]:
            self.rect.x -= 3
        if keys[pygame.K_d]:
            self.rect.x += 3

class p2(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__()
        self.image = pygame.image.load('Assets/enemies/carrot/carrot_w_1.png')
        self.rect = self.image.get_rect(center = (pos))
        self.add(group)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= 3
        if keys[pygame.K_DOWN]:
            self.rect.y += 3
        if keys[pygame.K_LEFT]:
            self.rect.x -= 3
        if keys[pygame.K_RIGHT]:
            self.rect.x += 3

g1 = pygame.sprite.Group()
sprite1 = p1((100, 100), g1)
sprite2 = p2((300, 300), g1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    fbs.tick(60)

    g1.update()

    g1.draw(screen)

    pygame.display.update()

