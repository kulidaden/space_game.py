import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        super(Bullet, self).__init__()
        self.screen = screen
        i = 2
        # with open('highscore.txt','r') as hs:
        #     highscore = hs.readline().strip()
        #     while i>6:
        #         if int(highscore)%500==0:
        #             i+=1
        self.rect = pygame.Rect(0, 0, i, 12)
        self.color = 0, 204, 255
        self.speed = 5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
