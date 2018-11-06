import pygame
import loader
import obj

pygame.init()


class Client:
    def __init__(self):
        self.cfg = loader.load("settings.cfg")
        self.clock = pygame.time.Clock()
        self.fps = self.cfg["fps"]
        self.resolution = self.cfg["resolution"]
        self.surf = pygame.display.set_mode(self.resolution)
        self.running = True
        self.tracking = False

        self.grid = obj.Grid((50, 50))
        self.test = obj.Cell()

    def loop(self):
        pos = pygame.mouse.get_pos()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # left mouse button
                        self.track_start()
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.track_stop()

            pos_old = pos
            pos = pygame.mouse.get_pos()

            if self.tracking:
                delta = pos[0] - pos_old[0], pos[1] - pos_old[1]
                self.grid.anchor[0] += delta[0]
                self.grid.anchor[1] += delta[1]

            self.surf.fill((255, 255, 255))

            self.grid.draw(self.surf)

            self.test.draw(self.surf)

            pygame.display.update()
            self.clock.tick(self.fps)

    def track_start(self):
        self.tracking = True

    def track_stop(self):
        self.tracking = False


main = Client()
main.loop()