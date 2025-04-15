import pygame
import time
import FP_Sprites2


#setting up what the screen looks like
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

#setting up the player
sprite_sheet_image = pygame.image.load('Bomberman_spritesheet.png').convert_alpha()
sprite_sheet = FP_Sprites2.SpriteSheet(sprite_sheet_image)
animations = FP_Sprites2.get_player1_animations(sprite_sheet)


#setting up controller
pygame.joystick.init()
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Detected joystick: {joystick.get_name()}")
else:
    joystick = 0
    print("No joystick detected.")
print("Joysticks found: ",pygame.joystick.get_count())


#setting up P1 moving set up 
TILE_SIZE = 24   #tile size
move_speed = 2.5   #speed of P1
P1X, P1Y = 1, 1   #Position of P1 (this is also the starting position)
P1_pixelX, P1_pixelY = P1X * TILE_SIZE, P1Y * TILE_SIZE   #specific pixel position
target_x, target_y = P1_pixelX, P1_pixelY   #target grid position the character is moving to
moving = False  #if P1 is moving or not
current_direction = "down"   #current direction character is facing


#P1 frames and animation settings
current_frame = 0   #which animation frame is currently showing
frame_timer = 0   #timer to track how long the current frame has been showing
frame_delay = 60   #time to wait before switching to the next frame







# running the game
run = True
while run:
    dt = clock.tick(60)
    screen.fill((80, 80, 80))
    
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    # Default direction values
    x_axis = 0
    y_axis = 0

    # Read joystick input if available
    if joystick:
        x_axis = joystick.get_axis(0)  # Left stick horizontal
        y_axis = joystick.get_axis(1)  # Left stick vertical

    # handle movement input
    if not moving:
        if keys[pygame.K_a] or x_axis < -.5:
            target_x = (P1X - 1) * TILE_SIZE
            P1X -= 1
            current_direction = "left"
            moving = True
        elif keys[pygame.K_d] or x_axis >.5:
            target_x = (P1X + 1) * TILE_SIZE
            P1X += 1
            current_direction = "right"
            moving = True
        elif keys[pygame.K_w] or y_axis < -.5:
            target_y = (P1Y - 1) * TILE_SIZE
            P1Y -= 1
            current_direction = "up"
            moving = True
        elif keys[pygame.K_s] or y_axis > .5:
            target_y = (P1Y + 1) * TILE_SIZE
            P1Y += 1
            current_direction = "down"
            moving = True

    # move toward target pixel by pixel
    if moving:
        dx = target_x - P1_pixelX
        dy = target_y - P1_pixelY

        if dx != 0:
            P1_pixelX += move_speed if dx > 0 else -move_speed
            if abs(P1_pixelX - target_x) < move_speed:
                P1_pixelX = target_x
        if dy != 0:
            P1_pixelY += move_speed if dy > 0 else -move_speed
            if abs(P1_pixelY - target_y) < move_speed:
                P1_pixelY = target_y

        # check if done moving
        if P1_pixelX == target_x and P1_pixelY == target_y:
            moving = False

    # determine animation key
    if moving or (keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d]):
        anim_key = current_direction
    else:
        anim_key = f"idle {current_direction}"

    # ensure anim_key exists and is not empty
    if anim_key not in animations or not animations[anim_key]:
        anim_key = "idle down"

    # secondary safety fallback
    if anim_key not in animations or not animations[anim_key]:
        raise Exception(f"Missing fallback animation: '{anim_key}'")

    anim_frames = animations[anim_key]
    num_frames = len(anim_frames)

    # update animation frame safely
    frame_timer += dt
    if frame_timer >= frame_delay:
        frame_timer = 0
        current_frame = (current_frame + 1) % num_frames

    # draw player
    frame = anim_frames[current_frame % num_frames]
    screen.blit(frame, (P1_pixelX, P1_pixelY))

    pygame.display.update()

print ("exited game")
pygame.quit()
