
import pygame
pygame.init()

black = (0,0,0)
white = (255,255,255)
gray = (197,197,197)
yellow = (255,255,128)
green = (128,255,128)
purple = (128,0,128)
blue =(0,0,255)
red = (255,0,0)
pink = (255,170,255)
Dark_Green = (0,64,0)
light_blue =(82,200,220)
light_yellow = (255,0,128)

# display_output = [1000,600]
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Bouncing Balls")
Bounce = True
clock= pygame.time.Clock()


ball_pos_x = 50
ball_pos_y = 50

ball_pos1_x = 5
ball_pos1_y = 5

spd_dir_x = 50
spd_dir_y = 50
spd_dir1_x = 50
spd_dir1_y =50

while Bounce == True:
    for evnt in pygame.event.get():
        if evnt.type == pygame.QUIT:
            Bounce == False
            pygame.quit()

    screen.fill(black)
    pygame.draw.circle(screen,green, [ball_pos_x, ball_pos_y],30)
    pygame.draw.circle(screen, green, [ball_pos_x+5, ball_pos_y+5], 10)
    pygame.draw.circle(screen, green, [ball_pos1_x, ball_pos1_y], 30)
    pygame.draw.circle(screen, green, [ball_pos1_x + 5, ball_pos1_y + 5], 10)
    ball_pos_x = spd_dir_x
    ball_pos_y = spd_dir_y
    ball_pos1_x = spd_dir1_x
    ball_pos1_y = spd_dir1_y

    if ball_pos_y > 550 or ball_pos_y < 10:
        spd_dir_y =spd_dir_y * -1
    if ball_pos_x > 950 or ball_pos_x < 10:
        spd_dir_x = spd_dir_x * -1

    if ball_pos1_y > 550 or ball_pos1_y < 10:
        spd_dir1_y =spd_dir1_y * -1
    if ball_pos1_x > 950 or ball_pos1_x < 10:
        spd_dir1_x = spd_dir1_x * -1

    clock.tick(60)

    pygame.display.flip()
    pygame.quit()

