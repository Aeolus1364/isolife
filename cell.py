import pygame


class Cell(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.image =
        self.rect = pygame.Rect(0, 0, 50, 50)

    def draw(self, surf):
        pygame.draw.rect(surf, (255, 0, 0), self.rect)