import pygame
from djitellopy import Tello
import time

# pygame initalization
pygame.init()

size = [1280, 720]

# Set up the drawing window
screen = pygame.display.set_mode(size)

FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()

# setting up controls formatted
controls = []
# +/- control speed, in intervals of 10
# DOESNT USE THIS, CHANGE LATER
controls.append(pygame.K_PLUS) # 0
controls.append(pygame.K_MINUS) # 1

# arrow keys = left right for back
controls.append(pygame.K_LEFT)#2
controls.append(pygame.K_RIGHT)#3
controls.append(pygame.K_UP)#4
controls.append(pygame.K_DOWN)#5

# wasd = turn left right/ up down
controls.append(pygame.K_a)#6
controls.append(pygame.K_d)#7
controls.append(pygame.K_w)#8
controls.append(pygame.K_s)#9

# t = takeoff, l = land
controls.append(pygame.K_t)#10
controls.append(pygame.K_l)#11

# control indicies should be replaced with constants later


# tello initialization
tello = Tello()

tello.connect()
print(tello.get_current_state())
#tello.wait_for_connection(10.0)
#tello.takeoff()

# x is forward / backward
# y is left / right
# z up / down

speed = 50
x_vel = 0
y_vel = 0
z_vel = 0
yaw_vel = 0
flying = False

def update_screen():
    global speed
    global x_vel
    global y_vel
    global z_vel
    global yaw_vel
    global flying

    # stuff every frame
    keys = pygame.key.get_pressed()

    # set speeds in intervals of 10
    if keys[pygame.K_0]:
        speed = 100
    elif keys[pygame.K_1]:
        speed = 10    
    elif keys[pygame.K_2]:
        speed = 20    
    elif keys[pygame.K_3]:
        speed = 30    
    elif keys[pygame.K_4]:
        speed = 40    
    elif keys[pygame.K_5]:
        speed = 50    
    elif keys[pygame.K_6]:
        speed = 60    
    elif keys[pygame.K_7]:
        speed = 70    
    elif keys[pygame.K_8]:
        speed = 80    
    elif keys[pygame.K_9]:
        speed = 90    
    
    
    # left right keys controls y
    if keys[controls[2]]:
        y_vel = -speed
    elif keys[controls[3]]:
        y_vel = speed
    else:
        y_vel = 0
    
    # up down keys controls x
    if keys[controls[4]]:
        x_vel = speed
    elif keys[controls[5]]:
        x_vel = -speed
    else:
        x_vel = 0

    # a d controls yaw
    if keys[controls[6]]:
        yaw_vel = -speed
    elif keys[controls[7]]:
        yaw_vel = speed
    else:
        yaw_vel = 0

    # w s controls z
    if keys[controls[8]]:
        z_vel = speed
    elif keys[controls[9]]:
        z_vel = -speed
    else:
        z_vel = 0

    # t = takeoff, l = land
    if keys[controls[10]]:
        if ~flying:
            tello.takeoff()
            flying = True
    elif keys[controls[11]]:
        if flying:
            tello.land()
            flying = False
    

    #draws background
    screen.fill([255,255,255])

    font = pygame.font.SysFont(None, 24)
    img = font.render(f"X_vel: {x_vel}", True, (0,0,0))
    screen.blit(img, (120 * (1), 20))
    font = pygame.font.SysFont(None, 24)
    img = font.render(f"Y_vel: {y_vel}", True, (0,0,0))
    screen.blit(img, (120 * (2), 20))
    font = pygame.font.SysFont(None, 24)
    img = font.render(f"Z_vel: {z_vel}", True, (0,0,0))
    screen.blit(img, (120 * (3), 20))
    img = font.render(f"yaw_vel: {yaw_vel}", True, (0,0,0))
    screen.blit(img, (120 * (4), 20))
    img = font.render(f"bat: {tello.get_battery()}", True, (0,0,0))
    screen.blit(img, (120 * (5), 20))
    img = font.render(f"flying: {flying}", True, (0,0,0))
    screen.blit(img, (120 * (6), 20))
    img = font.render(f"speed: {speed}", True, (0,0,0))
    screen.blit(img, (120 * (7), 20))

    if flying:
        #if x_vel or y_vel or z_vel or yaw_vel:
        tello.send_rc_control(y_vel, x_vel, z_vel, yaw_vel)

    pygame.display.update()
    fpsClock.tick(FPS)


# Run until the user asks to quit
running = True

while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_END:
            running = False

    #Draw the screen
    update_screen()
    

# quit
pygame.quit()
# in case user didn't land
tello.land()
