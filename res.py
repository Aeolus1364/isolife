import pygame


def load(image):
    img = pygame.image.load("res/{0}".format(image))
    dim = img.get_size()
    dim = (dim[0]*1, dim[1]*1)
    img = pygame.transform.scale(img, dim)
    return img


tile = load("tilec.png")
cube = load("cube.png")