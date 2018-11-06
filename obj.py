import pygame
import res
from const import TILEWS, TILEHS
import operator


class Cell(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = res.cube
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, surf):
        surf.blit(self.image, self.rect)

    def collide(self, point):

        rel_pos = point[0] - self.rect.x, point[1] - self.rect.y

        if self.rect.collidepoint(point):
            return self.mask.get_at(rel_pos)
        else:
            return 0


def isocoord(coord):  # calculates coordinate position based on isometric
    x, y = coord
    xc, yc = 0, 0

    for a in range(x):
        xc += TILEHS
        yc -= TILEWS
        for yc in range(y):
            xc += TILEWS
            yc += TILEHS

    return xc, yc


class Tile(pygame.sprite.Sprite):
    def __init__(self, dim, pos):
        super().__init__()
        self.image = res.tile
        self.rect = self.image.get_rect()
        self.grid_pos = pos
        self.offset = dim

    def draw(self, surf, anchor):
        self.rect.topleft = tuple(map(operator.add, self.offset, anchor))  # adds offset to anchor
        print(self.offset, anchor, self.rect)
        surf.blit(self.image, self.rect)


class Grid:
    def __init__(self, dim, anchor=None):
        self.tiles = []
        self.dim = dim
        if anchor is None:
            self.anchor = [0, 0]
        else:
            self.anchor = anchor

        xc = [0, 0]

        for x in range(dim[0]):
            xc[0] += TILEWS
            xc[1] -= TILEHS
            yc = xc[:]
            for y in range(dim[1]):
                yc[0] += TILEWS
                yc[1] += TILEHS
                self.tiles.append(Tile(yc, (x, y)))
                # print(yc)
                # print(yc, (x, y))

    def draw(self, surf):
        for tile in self.tiles:
            tile.draw(surf, self.anchor)
        print()
