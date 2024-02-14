import pygame

pygame.font.init()

pygame.font.get_init()

display_surface = pygame.display.set_mode((500,500))

pygame.display.set_caption('Dodge')

font1=pygame.font.SysFont('freesanbold.ttf',70)
font2=pygame.font.SysFont('chalkduster.ttf',40)

text1=font1.render('Dodge',True, (0,255,0))
text2=font2.render('Press ENTER to start', True, (0,255,0))

textRect1 = text1.get_rect()
textRect2=text2.get_rect()

textRect1.center=(250,50)
textRect2.center=(250,300)

img=pygame.image.load("C:\\Users\\fletc\\OneDrive\\Documents\\Art\\WIN_20240131_14_23_25_Pro.jpg").convert()
DEFAULT_IMAGE_SIZE=(300,170)
img = pygame.transform.scale(img, DEFAULT_IMAGE_SIZE)

while True:

    display_surface.fill((0,0,0))

    display_surface.blit(text1, textRect1)
    display_surface.blit(text2, textRect2)
    display_surface.blit(img, (105,110))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            pass
        if event.key == pygame.K_KP_ENTER:
            from game import *

        pygame.display.update()
