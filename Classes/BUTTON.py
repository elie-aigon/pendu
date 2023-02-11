from Settings import *

class BUTTON:
    def __init__(self, surface, font , color,pos_x, pos_y, width, height, text, background, command):
        self.x = pos_x
        self.y = pos_y
        self.width = width
        self.height = height
        self.text = text
        self.font = font
        self.color = color
        self.screen = surface
        self.text_button = self.font.render(self.text, True, self.color)
        self.button_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.background = pygame.image.load(background).convert_alpha()
        self.background = pygame.transform.scale(self.background, (width, height))
        self.command = command

    def draw_button(self):
        self.screen.blit(self.background, self.button_rect)
        self.screen.blit(self.text_button, (self.x + (self.width // 2) - (self.text_button.get_width() // 2), self.y + (self.height // 2) - (self.text_button.get_height() // 2) - 3))
    
    def is_clicked(self, pos):
        if self.button_rect.collidepoint(pos):
            self.command()