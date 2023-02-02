import json
import random
import pygame
import sys
from pygame.locals import *
from operator import itemgetter

pygame.init()
# Load les listes de mots existantes
with open('mot.json', 'r') as f:
    dic_mot = json.load(f)

# Définir les fenetres
size = (800, 400)
screen = pygame.display.set_mode(size)
page_menu = pygame.Surface(size)
page_game = pygame.Surface(size)
page_end = pygame.Surface(size)
page_setlist = pygame.Surface(size)

current_screen = page_menu
# colors
black = (0, 0, 0)
beige = (150, 150, 150)
grey = (44, 47, 50)
white = (255, 255, 255)

# font
font = pygame.font.Font("edosz.ttf", 30)
font_title = pygame.font.Font("edosz.ttf", 45)
font_little = pygame.font.Font("edosz.ttf", 20)
font_scoresboard = pygame.font.Font("edosz.ttf", 15)
# ----MENU-element---- #
# Titre
title = font_title.render("HANGMAN", True, grey)
title_pos = (300, 20)
# checkbox easy
text_lvl_easy = font.render("Easy", True, grey)
checked_image_easy = pygame.image.load("images\checked_box.png")
unchecked_image_easy = pygame.image.load("images/uncheked_box.png")
checked_image_easy = pygame.transform.scale(checked_image_easy, (80, 66))
unchecked_image_easy = pygame.transform.scale(unchecked_image_easy, (80, 66))
checkbox_x_easy = 10
checkbox_y_easy = 70
is_checked_easy = False
# checkbox normal
text_lvl_normal = font.render("Normal", True, grey)
checked_image_normal = pygame.image.load("images\checked_box.png")
unchecked_image_normal = pygame.image.load("images/uncheked_box.png")
checked_image_normal = pygame.transform.scale(checked_image_normal, (80, 66))
unchecked_image_normal = pygame.transform.scale(unchecked_image_normal, (80, 66))
checkbox_x_normal = 10
checkbox_y_normal = 130
is_checked_normal = False
# checkbox hard
text_lvl_hard = font.render("Hard", True, grey)
checked_image_hard = pygame.image.load("images\checked_box.png")
unchecked_image_hard = pygame.image.load("images/uncheked_box.png")
checked_image_hard = pygame.transform.scale(checked_image_hard, (80, 66))
unchecked_image_hard = pygame.transform.scale(unchecked_image_hard, (80, 66))
checkbox_x_hard = 10
checkbox_y_hard = 190
is_checked_hard = False
# Custom
text_lvl_custom = font.render("Custom", True, grey)
checked_image_custom = pygame.image.load("images\checked_box.png")
unchecked_image_custom = pygame.image.load("images/uncheked_box.png")
checked_image_custom = pygame.transform.scale(checked_image_custom, (80, 66))
unchecked_image_custom = pygame.transform.scale(unchecked_image_custom, (80, 66))
checkbox_x_custom = 10
checkbox_y_custom = 250
is_checked_custom = False
# bouton PLAY
play_button = pygame.image.load("images/black_button.png")
play_button_text = font.render("PLAY", True, white)
play_button_x = 300
play_button_y = 280
is_checked_play = False

# ----SETLIST---- #
add_button = pygame.image.load("images/black_button.png")
add_button_text = font.render("ADD", True, white)
add_button_x = 320
add_button_y = 300
instruc_text = font_little.render('Press "ENTER" to validate the Title or the word', True, grey)
instruc_text_2 = font_little.render('And press "ADD" to add the words list and play !', True, grey)
list_show = pygame.image.load("images/scoreboard_box.png")
list_show_pos = (480, 75)
preview = font_little.render("List Preview", True, grey)
preview_pos = (570, 95)
# ----GAME---- #
back_main_button = pygame.image.load("images/black_button.png")
back_main_button_text = font.render("Menu", True, white)
main_button_x = 320
main_button_y = 300

# ----END---- #
text_win = font.render("WINNER !!!", True, grey)
text_lose = font.render("LOOOSER !!!", True, grey)
text_pos_win_lose = (80, 150)
mess_win = font_little.render("Type your name BG: ", True, grey)
mess_lose = font_little.render("Type your name Loser: ", True, grey)
mess_pos_win_lose = (40, 230)
scoresboard = pygame.image.load("images/scoreboard_box.png")
scoresboard_pos = (480, 75)
text_score = font_little.render("Leaderboard", True, grey)
text_score_pos = (570, 95)

# Variables init
run = True
# variables page_menu
is_checked_easy = True

# variables page_game
count = 0
# variables page_setlist
set_variable = False
is_title = False
while run:

    if current_screen == page_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                             
                
                # J'affcihe le scoreboard en classant les scores du plus grands au plus petit.
                is_score_print = False
                if not is_score_print:
                    with open("scores.json", 'r') as f:
                        scores = json.load(f)
                
                    sorted_scores = dict(sorted(scores.items(), key=itemgetter(1), reverse=True))
                    y_pos = 150
                    sorted_scores_str = []
                    for key, value in sorted_scores.items():
                        element = " ".join((str(key), ":", str(value)))
                        sorted_scores_str.append(element)
                    page_menu.fill(beige)
                    page_menu.blit(scoresboard, scoresboard_pos)
                    page_menu.blit(text_score, text_score_pos)
                    for element in sorted_scores_str:
                        text = font_scoresboard.render(element, True, white)
                        page_menu.blit(text, (550, y_pos))
                        y_pos += 25
                    is_score_print = True
                # Je détermine quel checkbox afficher 
                if (checkbox_x_easy < mouse_pos[0] < checkbox_x_easy + checked_image_easy.get_width() and
                        checkbox_y_easy < mouse_pos[1] < checkbox_y_easy + checked_image_easy.get_height()):
                    is_checked_easy = True
                    is_checked_normal = False
                    is_checked_hard = False
                    is_checked_custom = False

                if (checkbox_x_normal < mouse_pos[0] < checkbox_x_normal + checked_image_normal.get_width() and
                        checkbox_y_normal < mouse_pos[1] < checkbox_y_normal + checked_image_normal.get_height()):
                    is_checked_normal = True
                    is_checked_hard = False
                    is_checked_easy = False
                    is_checked_custom = False

                if (checkbox_x_hard < mouse_pos[0] < checkbox_x_hard + checked_image_hard.get_width() and
                        checkbox_y_hard < mouse_pos[1] < checkbox_y_hard + checked_image_hard.get_height()):
                    is_checked_hard = True
                    is_checked_normal = False
                    is_checked_easy = False
                    is_checked_custom = False

                if (checkbox_x_custom < mouse_pos[0] < checkbox_x_custom + checked_image_custom.get_width() and
                        checkbox_y_custom < mouse_pos[1] < checkbox_y_custom + checked_image_custom.get_height()):
                    is_checked_hard = False
                    is_checked_normal = False
                    is_checked_easy = False
                    is_checked_custom = True
                    
                # J'affiche les images correspondantes des checkbox définis au dessus
                if is_checked_easy:
                    page_menu.blit(checked_image_easy, (checkbox_x_easy, checkbox_y_easy))
                else:
                    page_menu.blit(unchecked_image_easy, (checkbox_x_easy, checkbox_y_easy))

                if is_checked_normal:
                    page_menu.blit(checked_image_normal, (checkbox_x_normal, checkbox_y_normal))
                else:
                    page_menu.blit(unchecked_image_normal, (checkbox_x_normal, checkbox_y_normal))

                if is_checked_hard:
                    page_menu.blit(checked_image_hard, (checkbox_x_hard, checkbox_y_hard))
                else:
                    page_menu.blit(unchecked_image_hard, (checkbox_x_hard, checkbox_y_hard))
                
                if is_checked_custom:
                    page_menu.blit(checked_image_custom, (checkbox_x_custom, checkbox_y_custom))
                else:
                    page_menu.blit(unchecked_image_custom, (checkbox_x_custom, checkbox_y_custom))
                page_menu.blit(play_button, (play_button_x, play_button_y))

                if (play_button_x < mouse_pos[0] < play_button_x + play_button.get_width() and
                        play_button_y < mouse_pos[1] < play_button_y + play_button.get_height()):
                    is_checked_play = True
                    if is_checked_custom:
                        current_screen = page_setlist
                    else:
                        current_screen = page_game
                # J'affiche le reste de l'UI
                page_menu.blit(title, title_pos)
                page_menu.blit(text_lvl_easy, (100, 87))
                page_menu.blit(text_lvl_normal, (100, 147))
                page_menu.blit(text_lvl_hard, (100, 207))
                page_menu.blit(text_lvl_custom, (100, 267))
                page_menu.blit(play_button_text, (play_button_x + 50,play_button_y + 25))            
                # Affichage
                screen.blit(page_menu, (0, 0))
                pygame.display.flip()
    if current_screen == page_setlist: # Page qui permet d'ajouter une liste de mot custom
        if not set_variable: # je set mes variables
            list_char_title = []
            list_char_word = []
            list_words = []
        for event in  pygame.event.get():
            set_variable = True
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == KEYDOWN and event.key in range(96, 123):                  
                if is_title: # ajouts des lettres à des sous listes
                    list_char_word.append(chr(event.key))
                    print('char', list_char_word) 
                if not is_title: # ajout des lettres à la liste de titre
                    list_char_title.append(chr(event.key))
                    print('char title', list_char_title)
            if event.type == KEYDOWN and event.key == K_RETURN:
                if is_title: # ajout des mots à la nouvelle liste de mots
                    word = "".join(list_char_word)
                    list_words.append(word)
                    list_char_word = []
                    count_mot = 0

                if not is_title: # créer le titre et la liste de vide pour les mots
                    title_input = "".join(list_char_title)
                    is_title = True

            if event.type == KEYDOWN and event.key == K_BACKSPACE:
                if is_title: # del le dernier char de la liste current_mot
                    list_char_word = list_char_word[:-1]

                if not is_title: # del le dernier élément de la liste titre
                    list_char_title = list_char_title[:-1]

            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if (add_button_x < mouse_pos[0] < add_button_x + add_button.get_width() and
                        add_button_y < mouse_pos[1] < add_button_y + add_button.get_height()):
                    dic_mot[title_input] = list_words
                    with open('mot.json', 'w') as f:
                        json.dump(dic_mot, f)
                    current_screen = page_game

        # UI
        page_setlist.fill(beige)
        # Element
        page_setlist.blit(title, title_pos)
        page_setlist.blit(add_button, (add_button_x, add_button_y))
        page_setlist.blit(add_button_text, (add_button_x + 58, add_button_y + 25))
        page_setlist.blit(instruc_text, (150, 90))
        page_setlist.blit(instruc_text_2, (140, 120))

        # Elements variables de l'affichage
        pre_titre_aff = font_little.render("Your title: ", True, grey)
        titre_aff_txt = "".join(list_char_title)
        titre_aff = font_little.render(titre_aff_txt, True, grey)
        page_setlist.blit(pre_titre_aff, (50, 230))
        page_setlist.blit(titre_aff, (170, 230))

        pre_word_aff = font_little.render("Your words: ", True, grey)
        word_aff_txt = "".join(list_char_word)
        word_aff = font_little.render(word_aff_txt, True, grey)
        page_setlist.blit(pre_word_aff, (400, 230))
        page_setlist.blit(word_aff, (530, 230))

        screen.blit(page_setlist, (0, 0))
        pygame.display.flip()
    if current_screen == page_game: # Page de jeu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            # UI-----------------------------------------
            page_game.fill(beige)
            # UI element---------------------------------
            page_game.blit(title, title_pos)

            if is_checked_play:
                # je sélectionne un mot selon la difficulté
                if is_checked_easy:
                    mot = random.choice(dic_mot["easy"])
                if is_checked_normal:
                    mot = random.choice(dic_mot["normal"])
                if is_checked_hard:
                    mot = random.choice(dic_mot["hard"])
                if is_checked_custom:
                    mot =  random.choice(dic_mot[title_input])

                game_run = True
                lives = 7
                len_mot = len(mot)
                splited_mot = [char for char in mot]
                founded_char = ["_"] * len_mot
                founded_char_aff = " ".join(founded_char)
                wrong_char = []
                win = 0
                not_founded_char = [char for char in mot]
                
                while game_run: # L'algo de recherche du mot
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            game_run = False
                            run = False
                        if event.type == MOUSEBUTTONDOWN:
                            mouse_pos = pygame.mouse.get_pos()
                            if (main_button_x < mouse_pos[0] < main_button_x + back_main_button.get_width() and
                                main_button_y < mouse_pos[1] < main_button_y + back_main_button.get_height()):
                                current_screen = page_menu
                                game_run = False

                        if event.type == KEYDOWN and event.key in range(96, 123):
                            if chr(event.key) in not_founded_char:
                                for i in not_founded_char:
                                    if chr(event.key) == i:
                                        founded_char[not_founded_char.index(chr(event.key))] = chr(event.key)
                                        not_founded_char[not_founded_char.index(chr(event.key))] = "_"
                      
                                        
                            elif chr(event.key) not in wrong_char:
                                wrong_char.append(chr(event.key))
                                lives -= 1
                            else:
                                lives -=1
                        if founded_char == splited_mot:
                            game_run = False
                            current_screen = page_end
                            win += 1
                        
                        # UI-----------------------------------------
                        page_game.fill(beige)
                        # UI element---------------------------------
                        page_game.blit(title, title_pos)
                        page_game.blit(back_main_button, (main_button_x, main_button_y))
                        page_game.blit(back_main_button_text, (main_button_x + 50, main_button_y + 25))
                        used_key = " ,".join(wrong_char)
                        used_key_affichage = font.render(used_key, True, black)
                        page_game.blit(used_key_affichage, (80, 180))

                        found_char_affichage = " ".join(founded_char)
                        text_affichage = font.render(found_char_affichage, True, black)
                        page_game.blit(text_affichage, (120, 150))
                        # J'affiche les différentes photos du pendus en fonction du nombre de vies restantes
                        hangman_pos = (550, 170)
                        if lives == 6:
                            hangman_6 = pygame.image.load("images\hangman_6.png")
                            page_game.blit(hangman_6,hangman_pos)
                        if lives == 5:
                            hangman_5 = pygame.image.load("images\hangman_5.png")
                            page_game.blit(hangman_5,hangman_pos)
                        if lives == 4:
                            hangman_4 = pygame.image.load("images\hangman_4.png")
                            page_game.blit(hangman_4,hangman_pos)
                        if lives == 3:
                            hangman_3 = pygame.image.load("images\hangman_3.png")
                            page_game.blit(hangman_3,hangman_pos)
                        if lives == 2:
                            hangman_2 = pygame.image.load("images\hangman_2.png")
                            page_game.blit(hangman_2,hangman_pos)
                        if lives == 1:
                            hangman_1 = pygame.image.load("images\hangman_1.png")
                            page_game.blit(hangman_1,hangman_pos)
                        if lives == 0:
                            hangman_0 = pygame.image.load("images\hangman_0.png")
                            page_game.blit(hangman_0,hangman_pos)

                            current_screen = page_end
                            page_end.fill(beige)
                            game_run = False
                        # Update de l'affichage
                        screen.blit(page_game, (0, 0))
                        pygame.display.flip()
                        

    if current_screen == page_end: # Page de fin
        for event in pygame.event.get():
            if event.type == pygame.QUIT:        
                run = False
            if event.type == MOUSEBUTTONDOWN:
                
                mouse_pos = pygame.mouse.get_pos()
                if (main_button_x < mouse_pos[0] < main_button_x + back_main_button.get_width() and
                    main_button_y < mouse_pos[1] < main_button_y + back_main_button.get_height()):
                    current_screen = page_menu
        input_name = [" "]
        input_name_aff = " "
        # UI-----------------------------------------
        if count == 1:
            sorted_scores = dict(sorted(scores.items(), key=itemgetter(1), reverse=True))
            y_pos = 150 
            sorted_scores_str = []
            for key, value in sorted_scores.items():
                element = " ".join((str(key), ":", str(value)))
                sorted_scores_str.append(element)
            
            page_end.fill(beige)
            page_end.blit(scoresboard, scoresboard_pos)
            page_end.blit(text_score, text_score_pos)
            for element in sorted_scores_str:
                text = font_scoresboard.render(element, True, (255, 255, 255))
                page_end.blit(text, (550, y_pos))
                y_pos += 25
            page_end.blit(back_main_button, (main_button_x, main_button_y))
            page_end.blit(back_main_button_text, (main_button_x + 50, main_button_y + 25))
            page_end.blit(title, title_pos)
            name = font_little.render(input_name_aff, True, grey)
            page_end.blit(name, (250, 230))
            if win != 0:
                page_end.blit(text_win, text_pos_win_lose)
                page_end.blit(mess_win, mess_pos_win_lose)
            else:
                page_end.blit(text_lose, text_pos_win_lose)
                page_end.blit(mess_lose, mess_pos_win_lose)
            
            input_name_aff = " "
            page_end.blit(name, (250, 230))
            screen.blit(page_end, (0, 0))
            pygame.display.flip()
            count += 1
        if count == 0:
        # UI element---------------------------------
            page_end.fill(beige)
            page_end.blit(title, title_pos)
            page_end.blit(back_main_button, (main_button_x, main_button_y))
            page_end.blit(back_main_button_text, (main_button_x + 50, main_button_y + 25))
            name = font_little.render(input_name_aff, True, grey)
            page_end.blit(name, (250, 230))
            if win != 0:
                page_end.blit(text_win, text_pos_win_lose)
                page_end.blit(mess_win, mess_pos_win_lose)
            else:
                page_end.blit(text_lose, text_pos_win_lose)
                page_end.blit(mess_lose, mess_pos_win_lose)
            page_end.blit(scoresboard, scoresboard_pos)
            page_end.blit(text_score, text_score_pos)
            # Affichage
            screen.blit(page_end, (0, 0))
            pygame.display.flip()
        # Je définis le nom du joueur qui viens de finir sa partie
        input_name = []
        input_name_aff = []
        with open('scores.json', 'r') as f:
            scores = json.load(f)
        running = True
        
        if count == 0: # Je limite les name input à un seul 
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        run = False
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if (main_button_x < mouse_pos[0] < main_button_x + back_main_button.get_width() and
                            main_button_y < mouse_pos[1] < main_button_y + back_main_button.get_height()):
                            running = False
                            current_screen = page_menu # bouton retour au menu
                            
                    if event.type == KEYDOWN and event.key in range(96, 123) or event.type == KEYDOWN and event.key == K_RETURN:
                        if event.key == K_RETURN and win != 0:
                            if input_name_aff in scores:
                                
                                scores[input_name_aff] += 1
                                count += 1                                        
                                running = False
                            else:
                                scores[input_name_aff] = 1
                                count += 1        
                                running = False
                            with open('scores.json', 'w') as f:
                                json.dump(scores, f)
                            pass
                        elif event.key == K_RETURN:
                            if input_name_aff not in scores:
                                scores[input_name_aff] = 0
                                count += 1        
                                with open('scores.json', 'w') as f:
                                    json.dump(scores, f)
                                running = False
                        
                        # UI
                        input_name.append(chr(event.key))
                        input_name_aff = "".join(input_name)
                        name = font_little.render(input_name_aff, True, grey)
                        page_end.blit(name, (260, 230))
                        screen.blit(page_end, (0, 0))
                        pygame.display.update()

                   

pygame.quit()
