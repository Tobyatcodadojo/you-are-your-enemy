# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
character = input("Press 1..")
dt = 0
num_sprites = 1
dir = [1,0]
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
print (player_pos)
char = pygame.image.load("hungry_monkey_sprites/1.png")
lvl = pygame.image.load("hungry_monkey_sprites/lvl_1.png")
sound = pygame.mixer.Sound("Level 1 theme.mp3")
sound.play(-1)
char_mask = pygame.mask.from_surface(char, threshold=127)
lvl_mask = pygame.mask.from_surface(lvl, threshold=127)
while running:
    #screen.fill((0,0,0))
    #pygame.sprite.collide_mask(char_mask, lvl_mask)
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    

    #pygame.draw.circle(screen, "purple", pygame.Vector2(player_pos.x + 75, player_pos.y - -25), 45)
    #pygame.draw.circle(screen, "purple", pygame.Vector2(player_pos.x - 75, player_pos.y - -25), 45)
    #pygame.draw.circle(screen, "light pink", player_pos, 35)
    #pygame.draw.circle(screen, "light blue", pygame.Vector2(player_pos.x, player_pos.y - -75), 65)
    pygame.draw.circle(screen, "pink", pygame.Vector2(player_pos.x - dir[0], player_pos.y-dir[1]), 40)
    for i in range(num_sprites):
        screen.blit(char, (player_pos.x+i*20, player_pos.y+i*20))
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
        dir[0] = 0
        dir[1] = -250
        screen.fill((0,0,0))
        screen.blit(char, (player_pos.x, player_pos.y))

    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
        dir[0] = 0
        dir[1] = 250
        screen.fill((0,0,0))
        screen.blit(char, (player_pos.x, player_pos.y))
        
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
        dir[0] = 250
        dir[1] = 0
        screen.fill((0,0,0))
        screen.blit(char, (player_pos.x, player_pos.y))

    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
        dir[0] = -250
        dir[1] = 0
        screen.fill((0,0,0))
        screen.blit(char, (player_pos.x, player_pos.y))
    if player_pos.x > 1000:
        player_pos.x = 0
        num_sprites += 1
        print(num_sprites)
    if num_sprites == 10:
        print("You win!")
        pygame.quit()
    pygame.draw.circle(screen, "pink", pygame.Vector2(player_pos.x - dir[0], player_pos.y-dir[1]), 40)
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    #player_pos.y+= 20
    

pygame.quit()