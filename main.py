import pygame
import loader
import cell

pygame.init()


class Client:
    def __init__(self):
        self.cfg = loader.load("settings.cfg")
        self.clock = pygame.time.Clock()
        self.fps = self.cfg["fps"]
        self.surf = pygame.display.set_mode(self.cfg["resolution"])
        self.running = True
        self.test = cell.Cell()

    def loop(self):
        while self.running:
            delta = 0, 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # left mouse button
                        pos_start = event.pos
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        pos_end = event.pos
                        delta = pos_end[0] - pos_start[0], pos_end[1] - pos_start[1]

            self.surf.fill((255, 255, 255))
            self.test.draw(self.surf)
            self.test.rect.x += delta[0]
            self.test.rect.y += delta[1]
            pygame.display.update()
            self.clock.tick(self.fps)


main = Client()
main.loop()