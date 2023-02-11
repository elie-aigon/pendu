from BUTTON import BUTTON
from SCOREBOARD import SCOREBOARD
from CHECKBOX import CHECKBOX
from Settings import *

class MAIN():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Hangman")
        self.screen = pygame.display.set_mode((1300, 800))
        self.title = font_title.render("Handgman", True, white)
        self.scoreboard = SCOREBOARD(self.screen, (910, 100))
        self.quit_button = BUTTON(self.screen, font_mid, grey, 20, 700, 150, 80, "QUIT", "Data/Images/red/red_normal.png", lambda: self.quit())
        self.win = BUTTON(self.screen, font_win_mess, white, 300, 200, 400, 300, "YOU WIN !", "Data/Images/win_mess.png", lambda: self.restart())
        self.lose = BUTTON(self.screen, font_win_mess, white, 300, 200, 400, 300, "YOU LOSE ...", "Data/Images/win_mess.png", lambda: self.restart())
       
        # checkbox state
        self.easy = True
        self.normal = False
        self.hard = False

        self.checked_box_easy = CHECKBOX(self.screen, font_mid, white, 80, 300, 100, 90, "EASY", "Data/images/unchecked_box.png")
        self.checked_box_normal = CHECKBOX(self.screen, font_mid, white, 80, 420, 100, 90, "Normal", "Data/images/unchecked_box.png")
        self.checked_box_hard = CHECKBOX(self.screen, font_mid, white, 80, 540, 100, 90, "hard", "Data/images/unchecked_box.png")
        # game state
        self.game_set = False
        self.game_win = False
        self.name_set = False
        self.game_lose = False
        self.score_update = False
        self.name = []
        
    def restart(self):
        self.game_set = False
        self.game_win = False
        self.game_lose = False
        self.name_set = False
        self.score_update = False
        self.name = []

    def quit(self):
        pygame.quit()
        sys.exit()

    def checked_box_org(self):
        if self.easy:
            self.normal = False
            self.hard = False
        if self.normal:
            self.easy = False
            self.hard = False
        if self.hard:
            self.normal = False
            self.easy = False

    def draw_elements(self):
        self.screen.blit(self.title, (650 - self.title.get_width() // 2, 20))
        self.scoreboard.draw_scoreboard()
        self.quit_button.draw_button()

        if not self.name_set:
            self.instructions = font_mid.render("Type your name : ", True, white)
            self.name_aff = font_mid.render("".join(self.name), True, white)
            self.screen.blit(self.name_aff, (380, 120))
            # checkbox
            self.checked_box_org()
            self.checked_box_easy.draw_button(self.easy)
            self.checked_box_normal.draw_button(self.normal)
            self.checked_box_hard.draw_button(self.hard)
        elif self.game_set:
            self.instructions = font_mid.render("Type characters to try to guess the word : ", True, white)
            self.guessed_char_aff = font_mid.render(" ".join(self.guessed_char), True, white)
            self.screen.blit(self.guessed_char_aff, (80, 250))
            self.wrong_instruc = font_mid.render("Wrong char : ", True, white)
            self.screen.blit(self.wrong_instruc, (50, 400))
            self.wrong_char_aff = font_mid.render(", ".join(self.wrong_char), True, white)
            self.screen.blit(self.wrong_char_aff, (80, 450))
            self.lives_aff = font_mid.render("Lives : " +str(self.lives), True, white)
            self.screen.blit(self.lives_aff, (0, 0))
            self.draw_hangman(self.lives)
        
        self.screen.blit(self.instructions, (30, 120))
        if self.game_win:
            self.win.draw_button()
            self.instruc_win = font_small.render("Click me to restart", True, grey)
            self.screen.blit(self.instruc_win, (370, 233))
        elif self.game_lose:
            self.lose.draw_button()
            self.instruc_win = font_small.render("Click me to restart", True, grey)
            self.screen.blit(self.instruc_win, (370, 233))

    def draw_hangman(self, lives):
        if lives == 7:
            pass
        if lives == 0:
            self.hangman = pygame.image.load("Data/images/hangman_0.png")
            self.hangman = pygame.transform.scale(self.hangman, (400, 310))
            self.screen.blit(self.hangman, (500, 250))
        if lives == 1:
            self.hangman = pygame.image.load("Data/images/hangman_1.png")
            self.hangman = pygame.transform.scale(self.hangman, (400, 310))
            self.screen.blit(self.hangman, (500, 250))
        if lives == 2:
            self.hangman = pygame.image.load("Data/images/hangman_2.png")
            self.hangman = pygame.transform.scale(self.hangman, (400, 310))
            self.screen.blit(self.hangman, (500, 250))
        if lives == 3:
            self.hangman = pygame.image.load("Data/images/hangman_3.png")
            self.hangman = pygame.transform.scale(self.hangman, (400, 310))
            self.screen.blit(self.hangman, (500, 250))
        if lives == 4:
            self.hangman = pygame.image.load("Data/images/hangman_4.png")
            self.hangman = pygame.transform.scale(self.hangman, (400, 310))
            self.screen.blit(self.hangman, (500, 250))
        if lives == 5:
            self.hangman = pygame.image.load("Data/images/hangman_5.png")
            self.hangman = pygame.transform.scale(self.hangman, (400, 310))
            self.screen.blit(self.hangman, (500, 250))
        if lives == 6:
            self.hangman = pygame.image.load("Data/images/hangman_6.png")
            self.hangman = pygame.transform.scale(self.hangman, (400, 310))
            self.screen.blit(self.hangman, (500, 250))

    def detect_win(self):
        if self.guessed_char == self.word_list:
            self.game_set = True
            self.game_win = True
            if not self.score_update:
                self.scoreboard.update_score("".join(self.name), self.lives)
                self.score_update = True
        elif self.lives == 0:
            self.game_set = True
            self.game_lose = True
            if not self.score_update:
                self.scoreboard.update_score("".join(self.name), -1)
                self.score_update = True

    def gen_game_components(self, list_name):
        self.word = random.choice(mot_dic[list_name])
        self.word_list = list(self.word)
        self.not_founded_char = list(self.word)
        self.wrong_char = []
        self.guessed_char = ["_"] * len(self.word)
        self.lives = 7

    def while_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    self.quit_button.is_clicked(pygame.mouse.get_pos())
                    if not self.name_set:
                        self.checked_box_easy.is_clicked(self.easy,pygame.mouse.get_pos())
                        self.checked_box_normal.is_clicked(self.normal, pygame.mouse.get_pos())
                        self.checked_box_hard.is_clicked(self.hard, pygame.mouse.get_pos())
                    if self.game_win:
                        self.win.is_clicked(pygame.mouse.get_pos())
                    if self.game_lose:
                        self.lose.is_clicked(pygame.mouse.get_pos())
                if not self.name_set:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            self.name = self.name[:-1]
                        if event.key == pygame.K_RETURN:
                            self.name_set = True
                            self.game_set = True
                            self.gen_game_components("easy")
                        if event.key in range(96, 123):
                            self.name.append(chr(event.key))
                elif self.game_set:
                    if not self.score_update:
                        if event.type == pygame.KEYDOWN:
                            if event.key in range(96, 123):
                                if chr(event.key) in self.not_founded_char:
                                    for i in self.not_founded_char:
                                        if chr(event.key) == i:
                                            self.guessed_char[self.not_founded_char.index(chr(event.key))] = chr(event.key)
                                            self.not_founded_char[self.not_founded_char.index(chr(event.key))] = "_"
                                else:                               
                                    if chr(event.key) not in self.wrong_char:
                                        self.wrong_char.append(chr(event.key))
                                        if self.lives >= 0:
                                            self.lives -= 1
                                self.detect_win()
                    else:
                        pass  
            self.screen.fill(grey)
            self.draw_elements()
            pygame.display.update()

main = MAIN()
main.while_loop()