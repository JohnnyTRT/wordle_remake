import pygame
from sys import exit
import random
import time

def check(word, secret):
    partial_indexes = []
    correct_indexes = []
    for i in range(5):
        if word[i] in secret:
            if word[i] == secret[i]:
                correct_indexes.append(int(i))
            else:
                partial_indexes.append(int(i))
            secret = secret.replace(word[i], ".", 1)
    final = [partial_indexes, correct_indexes]
    return final

pygame.init()
screen = pygame.display.set_mode((620, 1100))
pygame.display.set_caption("Wordle")
clock = pygame.time.Clock()
wordle_font = pygame.font.Font("graphics/Wordle_Font.ttf", 35)
base_font = pygame.font.Font("graphics/FranklinGothic.ttf", 75)

#secret word block
words = [
    "CHAIR", "TABLE", "HOUSE", "TRAIN", "MUSIC", "BRAIN", "LIGHT", "HEART", "SMALL", "LARGE",
    "APPLE", "BREAD", "WATCH", "TIMER", "PHONE", "STAGE", "DANCE", "PIZZA", "CLOUD", "WATER",
    "MONEY", "BANKS", "PRIZE", "BADGE", "GLOVE", "SHOES", "SOCKS", "CHAOS", "GHOST", "BIRTH",
    "LAUGH", "JOKES", "BEACH", "PARKS", "THORN", "FROST", "FLAME", "TRUTH", "SWORD", "MAGIC",
    "SPELL", "WITCH", "MOUSE", "BEAST", "PILOT", "BLAZE", "CROWN", "JEWEL", "STONE", "SUNNY",
    "LIGHT", "DARKS", "STORM", "OCEAN", "SANDY", "BREEZ", "JASPY", "CRISP", "THICK", "SHARP",
    "BLUNT", "SMOKE", "ASHES", "SPICY", "SALTY", "SWEET", "BITER", "TANGY", "BUTER", "CREAM",
    "RIPEN", "FRESH", "MELON", "CRISP", "SHARP", "BLUNT", "CRISP", "BREEZ", "JASPY", "CROWN",
    "KINGDOM", "ANGEL", "WITCH", "MOUSE", "SWEET", "BREAD", "TRAIN", "ALIGN", "CENTER", "RIGHT",
    "EXTRA", "GUEST", "STAND", "BOOTH", "STAGE", "STORY", "NEWER", "OLDER", "ROUND", "BOUND",
    "BLESS", "SIXTY", "STAFF", "ESSEX", "BIRCH", "THREE", "TIGER", "QUICK", "WORLD", "THROW",
    "CRUSH", "PLANT", "GRAND", "LEMON", "DOUBT", "BRUSH", "HONEY", "FROST", "MANGO", "GUESS",
    "BEARD", "BEAST", "PRIME", "MOUNT", "STEEP", "QUIET", "STEAK", "BLOOM", "BLOOM", "DRESS",
    "SALAD", "CHILI", "SQUAD", "GOOSE", "BUTER", "BACON", "TIMER", "TOMBS", "DARKS", "HAPPY",
    "SADLY", "GLORY", "MOUSE", "JOKER", "LOSER", "STINK", "CRIME", "PLUMB", "TROTH", "WHELM",
    "ALONE", "WORST", "STEAL", "WISPY", "NORSE", "SUMMY", "SNEEZE", "SOLEMN", "SPICE", "CRUST",
    "SPURS", "DAILY", "LUCID", "YOGIS", "TWICE", "SPREE", "STOCK", "SMILE", "ROUND", "GADY",
    "FRUIT", "SWING", "SMILE", "MOODS", "BELLY", "MOIST", "GOALS", "DREAM", "SORRY", "HOURS",
    "MINDE", "WAVES", "TAKEE", "FLUTE", "RIVER", "STORE", "EASTS", "WIDTH", "SCORE", "REACH",
    "WORKS", "UNDER", "ORGAN", "MOVER", "WOMAN", "UPEND", "UTERO", "WELLS", "WORKE", "WRING",
    "PLUMP", "TWICE", "FIRST", "THIRD", "REACH", "UNDER", "UTERO", "WOMAN", "WORKE", "WRING",
    "TAUNT", "PASTE", "HAPPY", "ENDEP", "RIDER", "STAGE", "BLINK", "TELLS", "ARROW", "SOUPS",
    "SPINE", "STOVE", "TRACK", "CHART", "DOZEN", "OCCUR", "MOUTH", "SCARY", "PAGER", "BREED",
    "STRET", "DOGES", "SPOIL", "PHOEN", "MOTHS", "USHER", "BROKE", "POVER", "MOURN", "SUGAR",
    "MOTOR", "GLARE", "SCENT", "TRIMM", "LATTE", "SLEEP", "BRAVE", "EASIL", "BUDGE", "CYNIC",
    "TIGHT", "CLARK", "CRASH", "SMART", "THINK", "QUART", "IVORY", "AUGER", "QUICK", "STOCK",
    "STAMP", "PRIME", "GREAT", "MOUNT", "FIRST", "SIXTY", "TIRED", "WITTY", "LAUGH", "OLIVE"
]
random.seed()
secret_word = words[random.randint(0, len(words) - 1)]

#surfaces
background = pygame.Surface((621, 1104))
background.fill("grey9")


new_surface = pygame.Surface((621, 1))
new_surface.fill("White")

new_surface2 = pygame.Surface((621, 1))
new_surface2.fill("Grey")

wordle_text = wordle_font.render("Wordle", True, "White")

box_surface = pygame.Surface((70, 70))
box_surface.fill("grey23")

boxcolor = box_surface

yellow_box = pygame.Surface((70, 70))
yellow_box.fill("gold3")
green_box = pygame.Surface((70, 70))
green_box.fill("chartreuse4")

box_surface2 = pygame.Surface((66, 66))
box_surface2.fill("grey9")


#word positioning

user_text = ""

locked1 = ""
locked2 = ""
locked3 = ""
locked4 = ""
locked5 = ""
locked6 = ""

line = 1
row = 258

normal = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
correct = []
win = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if win == 0:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                    user_text = user_text[0:-1]
                elif len(user_text) < 5:
                    if event.unicode.isalpha() == True:
                        user_text += event.unicode.upper()
                elif event.key == pygame.K_RETURN:
                    if len(user_text) == 5:
                        newcheck = check(user_text, secret_word)
                        for i in range(len(newcheck[0])):
                            if line == 2:
                                newcheck[0][i] += 5
                            elif line == 3:
                                newcheck[0][i] += 10
                            elif line == 4:
                                newcheck[0][i] += 15
                            elif line == 5:
                                newcheck[0][i] += 20
                            elif line == 6:
                                newcheck[0][i] += 25
                            else:
                                pass
                            correct.append(newcheck[0][i])
                            try:
                                normal.remove(newcheck[0][i])
                            except ValueError:
                                pass
                        for w in range(len(newcheck[1])):
                            if line == 2:
                                newcheck[1][w] += 5
                            elif line == 3:
                                newcheck[1][w] += 10
                            elif line == 4:
                                newcheck[1][w] += 15
                            elif line == 5:
                                newcheck[1][w] += 20
                            elif line == 6:
                                newcheck[1][w] += 25
                            else:
                                pass
                            try:
                                correct.remove(newcheck[1][w])
                            except ValueError:
                                pass
                            try:
                                normal.remove(newcheck[1][w])
                            except ValueError:
                                pass
                        if line == 1:
                            locked1 = user_text
                        elif line == 2:
                            locked2 = user_text
                        elif line == 3:
                            locked3 = user_text
                        elif line == 4:
                            locked4 = user_text
                        elif line == 5:
                            locked5 = user_text
                        elif line == 6:
                            locked6 = user_text
                            time.sleep(5)
                            pygame.quit()
                            exit()
                        else:
                            pass
                        if user_text == secret_word.upper():
                            win = 1
                        user_text = ""
                        row += 75
                        line += 1
                else:
                    pass
    
    screen.blit(background, (0,0))
    screen.blit(wordle_text, (250, 40))
    screen.blit(new_surface, (0,20))
    screen.blit(new_surface2, (0,90))

    if 0 in normal:
        screen.blit(boxcolor, (125, 250))
        screen.blit(box_surface2, (127, 252))
    elif 0 in correct:
        screen.blit(yellow_box, (125, 250))
    else:
        screen.blit(green_box, (125, 250))

    if 1 in normal:
        screen.blit(boxcolor, (200, 250))
        screen.blit(box_surface2, (202, 252))
    elif 1 in correct:
        screen.blit(yellow_box, (200, 250))
    else:
        screen.blit(green_box, (200, 250))
   
    if 2 in normal:
        screen.blit(boxcolor, (275, 250))
        screen.blit(box_surface2, (277, 252))
    elif 2 in correct:
        screen.blit(yellow_box, (275, 250))
    else:
        screen.blit(green_box, (275, 250))
       
    if 3 in normal:
        screen.blit(boxcolor, (350, 250))
        screen.blit(box_surface2, (352, 252))
    elif 3 in correct:
        screen.blit(yellow_box, (350, 250))
    else:
        screen.blit(green_box, (350, 250))  
   
    if 4 in normal:
        screen.blit(boxcolor, (425, 250))
        screen.blit(box_surface2, (427, 252))
    elif 4 in correct:
        screen.blit(yellow_box, (425, 250))
    else:
        screen.blit(green_box, (425, 250))  
   
    if 5 in normal:
        screen.blit(boxcolor, (125, 325))
        screen.blit(box_surface2, (127, 327))
    elif 5 in correct:
        screen.blit(yellow_box, (125, 325))
    else:
        screen.blit(green_box, (125, 325))

    if 6 in normal:
        screen.blit(boxcolor, (200, 325))
        screen.blit(box_surface2, (202, 327))
    elif 6 in correct:
        screen.blit(yellow_box, (200, 325))
    else:
        screen.blit(green_box, (200, 325))
   
    if 7 in normal:
        screen.blit(boxcolor, (275, 325))
        screen.blit(box_surface2, (277, 327))
    elif 7 in correct:
        screen.blit(yellow_box, (275, 325))
    else:
        screen.blit(green_box, (275, 325))

    if 8 in normal:
        screen.blit(boxcolor, (350, 325))
        screen.blit(box_surface2, (352, 327))
    elif 8 in correct:
        screen.blit(yellow_box, (350, 325))
    else:
        screen.blit(green_box, (350, 325))
   
    if 9 in normal:
        screen.blit(boxcolor, (425, 325))
        screen.blit(box_surface2, (427, 327))
    elif 9 in correct:
        screen.blit(yellow_box, (425, 325))
    else:
        screen.blit(green_box, (425, 325))
   
    if 10 in normal:
        screen.blit(boxcolor, (125, 400))
        screen.blit(box_surface2, (127, 402))
    elif 10 in correct:
        screen.blit(yellow_box, (125, 400))
    else:
        screen.blit(green_box, (125, 400))

    if 11 in normal:
        screen.blit(boxcolor, (200, 400))
        screen.blit(box_surface2, (202, 402))
    elif 11 in correct:
        screen.blit(yellow_box, (200, 400))
    else:
        screen.blit(green_box, (200, 400))

    if 12 in normal:
        screen.blit(boxcolor, (275, 400))
        screen.blit(box_surface2, (277, 402))
    elif 12 in correct:
        screen.blit(yellow_box, (275, 400))
    else:
        screen.blit(green_box, (275, 400))
   
    if 13 in normal:
        screen.blit(boxcolor, (350, 400))
        screen.blit(box_surface2, (352, 402))
    elif 13 in correct:
        screen.blit(yellow_box, (350, 400))
    else:
        screen.blit(green_box, (350, 400))
   
    if 14 in normal:
        screen.blit(boxcolor, (425, 400))
        screen.blit(box_surface2, (427, 402))
    elif 14 in correct:
        screen.blit(yellow_box, (425, 400))
    else:
        screen.blit(green_box, (425, 400))

    if 15 in normal:
        screen.blit(boxcolor, (125, 475))
        screen.blit(box_surface2, (127, 477))
    elif 15 in correct:
        screen.blit(yellow_box, (125, 475))
    else:
        screen.blit(green_box, (125, 475))

    if 16 in normal:
        screen.blit(boxcolor, (200, 475))
        screen.blit(box_surface2, (202, 477))
    elif 16 in correct:
        screen.blit(yellow_box, (200, 475))
    else:
        screen.blit(green_box, (200, 475))

    if 17 in normal:
        screen.blit(boxcolor, (275, 475))
        screen.blit(box_surface2, (277, 477))
    elif 17 in correct:
        screen.blit(yellow_box, (275, 475))
    else:
        screen.blit(green_box, (275, 475))
   
    if 18 in normal:
        screen.blit(boxcolor, (350, 475))
        screen.blit(box_surface2, (352, 477))
    elif 18 in correct:
        screen.blit(yellow_box, (350, 475))
    else:
        screen.blit(green_box, (350, 475))
   
    if 19 in normal:
        screen.blit(boxcolor, (425, 475))
        screen.blit(box_surface2, (427, 477))
    elif 19 in correct:
        screen.blit(yellow_box, (425, 475))
    else:
        screen.blit(green_box, (425, 475))

    if 20 in normal:
        screen.blit(boxcolor, (125, 550))
        screen.blit(box_surface2, (127, 552))
    elif 20 in correct:
        screen.blit(yellow_box, (125, 550))
    else:
        screen.blit(green_box, (125, 550))
   
    if 21 in normal:
        screen.blit(boxcolor, (200, 550))
        screen.blit(box_surface2, (202, 552))
    elif 21 in correct:
        screen.blit(yellow_box, (200, 550))
    else:
        screen.blit(green_box, (200, 550))
   
    if 22 in normal:
        screen.blit(boxcolor, (275, 550))
        screen.blit(box_surface2, (277, 552))
    elif 22 in correct:
        screen.blit(yellow_box, (275, 550))
    else:
        screen.blit(green_box, (275, 550))

    if 23 in normal:
        screen.blit(boxcolor, (350, 550))
        screen.blit(box_surface2, (352, 552))
    elif 23 in correct:
        screen.blit(yellow_box, (350, 550))
    else:
        screen.blit(green_box, (350, 550))
   
    if 24 in normal:
        screen.blit(boxcolor, (425, 550))
        screen.blit(box_surface2, (427, 552))
    elif 24 in correct:
        screen.blit(yellow_box, (425, 550))
    else:
        screen.blit(green_box, (425, 550))
   
    if 25 in normal:
        screen.blit(boxcolor, (125, 625))
        screen.blit(box_surface2, (127, 627))
    elif 25 in correct:
        screen.blit(yellow_box, (125, 625))
    else:
        screen.blit(green_box, (125, 625))

    if 26 in normal:
        screen.blit(boxcolor, (200, 625))
        screen.blit(box_surface2, (202, 627))
    elif 26 in correct:
        screen.blit(yellow_box, (200, 625))
    else:
        screen.blit(green_box, (200, 625))
   
    if 27 in normal:
        screen.blit(boxcolor, (275, 625))
        screen.blit(box_surface2, (277, 627))
    elif 27 in correct:
        screen.blit(yellow_box, (275, 625))
    else:
        screen.blit(green_box, (275, 625))
   
    if 28 in normal:
        screen.blit(boxcolor, (350, 625))
        screen.blit(box_surface2, (352, 627))
    elif 28 in correct:
        screen.blit(yellow_box, (350, 625))
    else:
        screen.blit(green_box, (350, 625))

    if 29 in normal:
        screen.blit(boxcolor, (425, 625))
        screen.blit(box_surface2, (427, 627))
    elif 29 in correct:
        screen.blit(yellow_box, (425, 625))
    else:
        screen.blit(green_box, (425, 625))

    column1 = 136
    for i in range(len(locked1)):
        textScreen1 = base_font.render(locked1[i], True, "White")
        screen.blit(textScreen1, (column1, 258))
        column1 += 75
    
    column2 = 136
    for i in range(len(locked2)):
        textScreen2 = base_font.render(locked2[i], True, "White")
        screen.blit(textScreen2, (column2, 333))
        column2 += 75
    
    column3 = 136
    for i in range(len(locked3)):
        textScreen3 = base_font.render(locked3[i], True, "White")
        screen.blit(textScreen3, (column3, 408))
        column3 += 75

    column4 = 136
    for i in range(len(locked4)):
        textScreen4 = base_font.render(locked4[i], True, "White")
        screen.blit(textScreen4, (column4, 483))
        column4 += 75

    column5 = 136
    for i in range(len(locked5)):
        textScreen5 = base_font.render(locked5[i], True, "White")
        screen.blit(textScreen5, (column5, 558))
        column5 += 75

    column6 = 136
    for i in range(len(locked6)):
        textScreen6 = base_font.render(locked6[i], True, "White")
        screen.blit(textScreen6, (column6, 633))
        column6 += 75

    column = 136

    for i in range(len(user_text)):
        textScreen = base_font.render(user_text[i], True, "White")
        screen.blit(textScreen, (column, row))
        column += 75


    pygame.display.update()
    clock.tick(60) 