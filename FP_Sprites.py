import pygame

class SpriteSheet():
    def __init__(self,image):
        self.sheet = image
    def p1_display(self,row,column, width,height,scale,color):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0,0), ((column*width), (row*height), width, height))
        image = pygame.transform.scale(image,(width*scale,height*scale))
        image.set_colorkey(color)
        return image
def get_player1_animations(sprite_sheet):
    idle_down = sprite_sheet.p1_display(1, 0, 384, 512, .15, (134, 192, 48))
    idle_up = sprite_sheet.p1_display(2, 0, 384, 512, .15, (134, 192, 48))
    idle_right = sprite_sheet.p1_display(0, 0, 384, 512, .15, (134, 192, 48))
    idle_left = pygame.transform.flip((sprite_sheet.p1_display(0, 0, 384, 512, .15, (134, 192, 48))), True, False)
    frame_down1 = sprite_sheet.p1_display(1, 1, 384, 512, .15, (134, 192, 48))
    frame_down2 = sprite_sheet.p1_display(1, 2, 384, 512, .15, (134, 192, 48))
    frame_up1 = sprite_sheet.p1_display(2, 1, 384, 512, .15, (134, 192, 48))
    frame_up2 = sprite_sheet.p1_display(2, 2, 384, 512, .15, (134, 192, 48))
    frame_right1 = sprite_sheet.p1_display(0, 1, 384, 512, .15, (134, 192, 48))
    frame_right2 = sprite_sheet.p1_display(0, 2, 384, 512, .15, (134, 192, 48))
    frame_left1 = pygame.transform.flip(frame_right1, True, False)
    frame_left2 = pygame.transform.flip(frame_right2, True, False)

    return {
        "idle down": [idle_down],
        "idle up": [idle_up],
        "idle right": [idle_right],
        "idle left": [idle_left],
        "down": [frame_down1, frame_down1, idle_down, frame_down2, frame_down2, idle_down],
        "up": [frame_up1, frame_up1, idle_up, frame_up2, frame_up2, idle_up],
        "left": [frame_left1, frame_left1, idle_left, frame_left2, frame_left2, idle_left],
        "right": [frame_right1, frame_right1, idle_right, frame_right2, frame_right2, idle_right]
    }

        
