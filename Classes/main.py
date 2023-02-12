from BUTTON import BUTTON
from SCOREBOARD import SCOREBOARD
from CHECKBOX import CHECKBOX
from Settings import *

class MAIN():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Hangman")
        self.screen = pygame.display.set_mode((1300, 800))
        self.title = font_title.render("Hangman", True, white)
        self.scoreboard = SCOREBOARD(self.screen, (910, 100))
        self.quit_button = BUTTON(self.screen, font_mid, grey, 60, 700, 150, 80, "QUIT", "Data/Images/red/red_normal.png", lambda: self.quit())
        self.win = BUTTON(self.screen, font_win_mess, white, 300, 200, 400, 300, "YOU WIN !", "Data/Images/win_mess.png", lambda: self.restart())
        self.lose = BUTTON(self.screen, font_win_mess, white, 300, 200, 400, 300, "YOU LOSE ...", "Data/Images/win_mess.png", lambda: self.restart())
        self.add_word_button = BUTTON(self.screen, font_mid, grey, 450, 700, 300, 80, "ADD WORD", "Data/images/yellow/yellow_normal.png", lambda: self.add_word_set())
        self.menu_button = BUTTON(self.screen, font_mid, grey, 1020, 700, 150, 80, "Menu", "Data/images/green_button/gree_normal.png", lambda: self.restart())       
        # checkbox state
        self.easy = True
        self.normal = False
        self.hard = False

        self.checked_box_easy = CHECKBOX(self.screen, font_mid, white, 80, 300, 100, 90, "EASY", "Data/images/unchecked_box.png", lambda: self.easy_clicked())
        self.checked_box_normal = CHECKBOX(self.screen, font_mid, white, 80, 420, 100, 90, "Normal", "Data/images/unchecked_box.png", lambda: self.normal_clicked())
        self.checked_box_hard = CHECKBOX(self.screen, font_mid, white, 80, 540, 100, 90, "hard", "Data/images/unchecked_box.png", lambda: self.hard_clicked())
        
        # game state
        self.add_word = False
        self.game_set = False
        self.game_win = False
        self.name_set = False
        self.game_lose = False
        self.score_update = False
        self.name = []

    # Navigate between game state
    def add_word_set(self):
        self.name_set = True
        self.add_word = True
        self.word_list = []

    def restart(self):
        self.game_set = False
        self.game_win = False
        self.game_lose = False
        self.name_set = False
        self.score_update = False
        self.add_word = False
        self.name = []

    def quit(self):
        pygame.quit()
        sys.exit()

    # Checkbox
    def easy_clicked(self):
        self.easy = True
        self.normal = False
        self.hard = False
    def normal_clicked(self):
        self.normal = True
        self.easy = False
        self.hard = False
    def hard_clicked(self):
        self.hard = True
        self.easy = False
        self.normal = False

    # UI
    def draw_elements(self):
        self.screen.blit(self.title, (650 - self.title.get_width() // 2, 20))
        
        self.quit_button.draw_button()
        self.menu_button.draw_button()
        if self.add_word:
            self.new_word = font_win_mess.render("".join(self.word_list), True, white)
            self.screen.blit(self.new_word, (250, 350))
            self.instructions = font_mid.render("Type The word you want to add and press 'enter' : ", True, white)
            self.instructions_2 = font_mid.render("Then Go back to Main menu to play with your new words ! ", True, white)
            self.screen.blit(self.instructions, (40, 120))
            self.screen.blit(self.instructions_2, (30, 600))
            self.hangman_add_word_frame = pygame.image.load("Data/images/hangman_0.png")
            self.hangman_add_word_frame = pygame.transform.scale(self.hangman_add_word_frame, (400, 310))
            self.screen.blit(self.hangman_add_word_frame, (850, 250))
        if not self.name_set:
            self.instructions = font_mid.render("Type your name : ", True, white)
            self.name_aff = font_mid.render("".join(self.name), True, white)
            self.screen.blit(self.name_aff, (380, 120))
            self.start_instruc = font_small.render("Click the difficulty and Press 'ENTER' to start", True, white)
            self.screen.blit(self.start_instruc, (30, 210))
            # checkbox
            self.checked_box_easy.draw_button(self.easy)
            self.checked_box_normal.draw_button(self.normal)
            self.checked_box_hard.draw_button(self.hard)
            self.add_word_button.draw_button()
            self.scoreboard.draw_scoreboard()
            self.screen.blit(self.instructions, (30, 120))
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
            self.scoreboard.draw_scoreboard()
            self.screen.blit(self.instructions, (30, 120))
        if self.game_win:
            self.win.draw_button()
            self.instruc_win = font_small.render("Click me to restart", True, grey)
            self.screen.blit(self.instruc_win, (370, 233))
            self.scoreboard.draw_scoreboard()
        elif self.game_lose:
            self.lose.draw_button()
            self.instruc_win = font_small.render("Click me to restart", True, grey)
            self.screen.blit(self.instruc_win, (370, 233))
            self.scoreboard.draw_scoreboard()

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
                if self.easy:
                    self.scoreboard.update_score("".join(self.name), self.lives)
                if self.normal:
                    self.scoreboard.update_score("".join(self.name), self.lives * 2)
                if self.hard:
                    self.scoreboard.update_score("".join(self.name), self.lives * 3)
                self.score_update = True
        elif self.lives == 0:
            self.game_set = True
            self.game_lose = True
            if not self.score_update:
                self.scoreboard.update_score("".join(self.name), -1)
                self.score_update = True

    def gen_game_components(self):
        self.word = random.choice(mot_dic)
        self.word_list = list(self.word)
        self.not_founded_char = list(self.word)
        self.wrong_char = []
        self.guessed_char = ["_"] * len(self.word)
        if self.easy:
            self.lives = 10
        if self.normal:
            self.lives = 7
        if self.hard:
            self.lives = 5
    
    def add_word_fonction(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.word_list = self.word_list[:-1]
            if event.key in range(96, 123):
                self.word_list.append(chr(event.key)) 
            if event.key == pygame.K_RETURN:
                if "".join(self.word_list) not in mot_dic:
                    mot_dic.append("".join(self.word_list))
                    with open('Data/JSON/mot.json', 'w') as f:
                        json.dump(mot_dic, f)
                self.word_list = []
                
    def while_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    self.quit_button.is_clicked(pygame.mouse.get_pos())
                    self.menu_button.is_clicked(pygame.mouse.get_pos())
          
                    if not self.name_set:
                        self.checked_box_easy.is_clicked(pygame.mouse.get_pos())
                        self.checked_box_normal.is_clicked(pygame.mouse.get_pos())
                        self.checked_box_hard.is_clicked(pygame.mouse.get_pos())
                        self.add_word_button.is_clicked(pygame.mouse.get_pos())
                    if self.game_win:
                        self.win.is_clicked(pygame.mouse.get_pos())
                    if self.game_lose:
                        self.lose.is_clicked(pygame.mouse.get_pos())
                if self.add_word:
                    self.add_word_fonction(event)
                
                if not self.name_set:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            self.name = self.name[:-1]
                        if event.key == pygame.K_RETURN:
                            self.name_set = True
                            self.game_set = True
                            self.gen_game_components()
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
            self.screen.fill(grey)
            self.draw_elements()
            pygame.display.update()

main = MAIN()
main.while_loop()