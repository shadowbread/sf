import pygame
pygame.init()

width = 1600 / 1.5
height = 900 / 1.5
fps = 50

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

def coil(kef):
    global screen
    step = 80
    pygame.draw.rect(screen, "yellow", (100 + (step * kef), 425, 75, 100))

def game():
    global screen
    pygame.draw.rect(screen, "white", (20, 400, 100, 150))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        coil(1)
    if keys[pygame.K_w]:
        coil(2)
    if keys[pygame.K_e]:
        coil(3)

while True:
    screen.fill("black")
    game()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    #clock.tick(fps)
