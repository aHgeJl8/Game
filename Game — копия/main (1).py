import pygame


pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

font = pygame.font.SysFont("Kristen ITC", 50)
font2 = pygame.font.SysFont("Kristen ITC", 30)

img = pygame.image.load("kosmos.jpg")
new_size = (800, 600)
new_img = pygame.transform.scale(img, new_size)

hero_img = pygame.image.load("doodle_jump.png")
size_hero = (75, 50)
new_hero_img = pygame.transform.scale(hero_img, size_hero)

hero_img_right = pygame.image.load('doodle_jump _right.png')
size_hero_right = (75, 50)
new_hero_img_right = pygame.transform.scale(hero_img_right, size_hero_right)

monster = pygame.image.load("monster.png")
size_monster = (75, 50)
monster = pygame.transform.scale(monster, size_monster)

x,y = 200, 0
x1,y1 = 140, 80
x2,y2 = 140, 120
x3, y3 = 400, 300

speed = 0.5
bullet = pygame.image.load("goroh.png")
bullet = pygame.transform.scale(bullet, (15, 15))

zvuk = pygame.mixer.Sound("shagi.mp3")

perevorot = new_hero_img

storona = 'left'


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            y3 += 30

    screen.blit(new_img, (0, 0))

    screen.blit(perevorot, (x3, y3))

    screen.blit(monster, (200, 200))

    text = font.render("Welcome to game!!", True, (0, 0, 100))
    screen.blit(text, (x, y))
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y3 = y3 - speed
        zvuk.play()
    if keys[pygame.K_s]:
        y3 = y3 + speed
        zvuk.play()
    if keys[pygame.K_a]:
        x3 = x3 - speed
        storona = 'left'
        perevorot = new_hero_img
        zvuk.play()
    if keys[pygame.K_d]:
        x3 = x3 + speed
        storona = 'right'
        perevorot = new_hero_img_right
        zvuk.play()
    if keys[pygame.K_SPACE]:
        screen.blit(bullet, (x3, y3))
        x4 = x3
        y4 = y3

        if storona == 'right':
            for i in range(800 - int(x4)):
                screen.blit(text, (x, y))
                screen.blit(new_img, (0, 0))
                screen.blit(perevorot, (x3, y3))
                screen.blit(bullet, (x4 + 30, y3 + 18))
                screen.blit(monster, (200, 200))
                x4 += 1
                pygame.display.update()
                pass
        else:
            for i in range(int(x4)):
                screen.blit(text, (x, y))
                screen.blit(new_img, (0, 0))
                screen.blit(perevorot, (x3, y3))
                screen.blit(bullet, (x4 + 30, y3 + 18))
                screen.blit(monster, (200, 200))
                x4 -= 1
                pygame.display.update()
                pass
            
            pygame.display.update()


    if not keys[pygame.K_w] and not keys[pygame.K_s] and not keys[pygame.K_a] and not keys[pygame.K_d]:
        zvuk.stop()







    pygame.display.update()