import pygame
import random


def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        x = 0
        y = 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = event.pos
                    if x <= mx <= x + 32 and y <= my <= y + 32:

                        x = random.randrange(0, 640 // 32) * 32
                        y = random.randrange(0, 512 // 32) * 32
            screen.fill("light green")

            #vertical line
            for i in range(32, 640, 32):
                pygame.draw.line(screen, "dark blue", (i,0 ), (i, 512))

            for i in range(32, 512, 32):
                pygame.draw.line(screen, "dark blue", (0,i ), (640, i))




            screen.blit(mole_image, mole_image.get_rect(topleft=(x, y)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
