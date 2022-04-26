import pygame,random, time
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def check_word(search,lst):
    while True:
        if lst == []:
            return False
        if len(lst) %2 == 0:
            md = lst[len(lst)//2-1]
            sm = lst[0:len(lst)//2-1]
            lr = lst[len(lst)//2:]
        else:
            md = lst[len(lst)//2+0]
            sm = lst[0:len(lst)//2+0]
            lr = lst[len(lst)//2+1:]
        if search > md:
            lst = lr
        elif search < md:
            lst = sm
        else:
            return True
def text(letter):
    global pos_x, pos_y, guess
    if pos_x < 5:
        text_surface = my_font.render(letter,False,(255,255,255))
        screen.blit(text_surface,(pos_x*70+195,pos_y*70+140))
        guess.append(letter)
        pos_x = pos_x+1
def reset():
    global words, pos_y, pos_x, guess, alphabet, green
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running == False
                end = False
                return ""
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    w = random.choice(words)
                    word = []
                    for i in w:
                        word.append(i.upper())
                    for i in range(5):
                        for a in range(5):
                            pygame.draw.rect(screen,square_colour_grey,pygame.Rect(a*70+185,70*i+150,60,60))
                    if show_word == True:
                        pygame.draw.rect(screen,(0,0,0),pygame.Rect(10,70,700,80))
                        for i in range(len(word)):
                            text_surface = my_font.render(word[i],False,(255,255,255))
                            screen.blit(text_surface,(i*70+195,70))
                    pos_y = 0
                    pos_x = 0
                    guess = []
                    word2 = []
                    for i in alphabet:
                        keyboard(square_colour_lgrey,i)
                    green = ["@","@","@","@","@"]
                    return word
def check(colour,a,i):
    global pos_y, green, guess
    letter = guess[i]
    pygame.draw.rect(screen,colour,pygame.Rect(i*70+185,pos_y*70+150,60,60))
    text_surface = my_font.render(guess[i],False,(255,255,255))
    screen.blit(text_surface,(i*70+195,pos_y*70+140))
    if colour == square_colour_green:
        word2.pop(a)
        word2.insert(a,"@green@")
        guess.pop(i)
        guess.insert(i,"#green#")
    else:
        word2.pop(a)
        word2.insert(a,"@yellow@")
        guess.pop(i)
        guess.insert(i,"#yellow#")
    p = True
    for b in green:
        if letter == b:
            p = False
    if p == False:
        keyboard(square_colour_green,letter)
    else:
        keyboard(colour,letter)
def keyboard(colour,letter):
    if letter == "Q":
        pygame.draw.rect(screen,colour,pygame.Rect(10,570,60,60))
        text_surface = my_font.render("Q",False,(255,255,255))
        screen.blit(text_surface,(20,560))
    elif letter == "W":
        pygame.draw.rect(screen,colour,pygame.Rect(80,570,60,60))
        text_surface = my_font.render("W",False,(255,255,255))
        screen.blit(text_surface,(90,560))
    elif letter == "E":
        pygame.draw.rect(screen,colour,pygame.Rect(150,570,60,60))
        text_surface = my_font.render("E",False,(255,255,255))
        screen.blit(text_surface,(160,560))        
    elif letter == "R":
        pygame.draw.rect(screen,colour,pygame.Rect(220,570,60,60))
        text_surface = my_font.render("R",False,(255,255,255))
        screen.blit(text_surface,(230,560))
    elif letter == "T":
        pygame.draw.rect(screen,colour,pygame.Rect(290,570,60,60))
        text_surface = my_font.render("T",False,(255,255,255))
        screen.blit(text_surface,(300,560))
    elif letter == "Y":
        pygame.draw.rect(screen,colour,pygame.Rect(360,570,60,60))
        text_surface = my_font.render("Y",False,(255,255,255))
        screen.blit(text_surface,(370,560))
    elif letter == "U":
        pygame.draw.rect(screen,colour,pygame.Rect(430,570,60,60))
        text_surface = my_font.render("U",False,(255,255,255))
        screen.blit(text_surface,(440,560))
    elif letter == "I":
        pygame.draw.rect(screen,colour,pygame.Rect(500,570,60,60))
        text_surface = my_font.render("I",False,(255,255,255))
        screen.blit(text_surface,(510,560))
    elif letter == "O":
        pygame.draw.rect(screen,colour,pygame.Rect(570,570,60,60))
        text_surface = my_font.render("O",False,(255,255,255))
        screen.blit(text_surface,(580,560))
    elif letter == "P":
        pygame.draw.rect(screen,colour,pygame.Rect(640,570,60,60))
        text_surface = my_font.render("P",False,(255,255,255))
        screen.blit(text_surface,(650,560))
    elif letter == "A":
        pygame.draw.rect(screen,colour,pygame.Rect(45,640,60,60))
        text_surface = my_font.render("A",False,(255,255,255))
        screen.blit(text_surface,(55,630))
    elif letter == "S":
        pygame.draw.rect(screen,colour,pygame.Rect(115,640,60,60))
        text_surface = my_font.render("S",False,(255,255,255))
        screen.blit(text_surface,(125,630))
    elif letter == "D":
        pygame.draw.rect(screen,colour,pygame.Rect(185,640,60,60))
        text_surface = my_font.render("D",False,(255,255,255))
        screen.blit(text_surface,(195,630))
    elif letter == "F":
        pygame.draw.rect(screen,colour,pygame.Rect(255,640,60,60))
        text_surface = my_font.render("F",False,(255,255,255))
        screen.blit(text_surface,(265,630))
    elif letter == "G":
        pygame.draw.rect(screen,colour,pygame.Rect(325,640,60,60))
        text_surface = my_font.render("G",False,(255,255,255))
        screen.blit(text_surface,(335,630))
    elif letter == "H":
        pygame.draw.rect(screen,colour,pygame.Rect(395,640,60,60))
        text_surface = my_font.render("H",False,(255,255,255))
        screen.blit(text_surface,(405,630))
    elif letter == "J":
        pygame.draw.rect(screen,colour,pygame.Rect(465,640,60,60))
        text_surface = my_font.render("J",False,(255,255,255))
        screen.blit(text_surface,(475,630))
    elif letter == "K":
        pygame.draw.rect(screen,colour,pygame.Rect(535,640,60,60))
        text_surface = my_font.render("K",False,(255,255,255))
        screen.blit(text_surface,(545,630))
    elif letter == "L":
        pygame.draw.rect(screen,colour,pygame.Rect(605,640,60,60))
        text_surface = my_font.render("L",False,(255,255,255))
        screen.blit(text_surface,(615,630))
    elif letter == "Z":
        pygame.draw.rect(screen,colour,pygame.Rect(80,710,60,60))
        text_surface = my_font.render("Z",False,(255,255,255))
        screen.blit(text_surface,(90,700))
    elif letter == "X":
        pygame.draw.rect(screen,colour,pygame.Rect(150,710,60,60))
        text_surface = my_font.render("X",False,(255,255,255))
        screen.blit(text_surface,(160,700))
    elif letter == "C":
        pygame.draw.rect(screen,colour,pygame.Rect(220,710,60,60))
        text_surface = my_font.render("C",False,(255,255,255))
        screen.blit(text_surface,(230,700))
    elif letter == "V":
        pygame.draw.rect(screen,colour,pygame.Rect(290,710,60,60))
        text_surface = my_font.render("V",False,(255,255,255))
        screen.blit(text_surface,(300,700))
    elif letter == "B":
        pygame.draw.rect(screen,colour,pygame.Rect(360,710,60,60))
        text_surface = my_font.render("B",False,(255,255,255))
        screen.blit(text_surface,(370,700))
    elif letter == "N":
        pygame.draw.rect(screen,colour,pygame.Rect(430,710,60,60))
        text_surface = my_font.render("N",False,(255,255,255))
        screen.blit(text_surface,(440,700))
    elif letter == "M":
        pygame.draw.rect(screen,colour,pygame.Rect(500,710,60,60))
        text_surface = my_font.render("M",False,(255,255,255))
        screen.blit(text_surface,(510,700))        
screen_width = 710
screen_height = 780
screen_caption = "WORDLE"
screen_colour = (0,0,0)
square_colour_grey = (60,60,60)
square_colour_yellow = (186,166,81)
square_colour_green = (83,141,78)
square_colour_lgrey = (156,156,156)
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption(screen_caption)
screen.fill((screen_colour))
pygame.draw.rect(screen,square_colour_grey,pygame.Rect(145,10,60,60))
pygame.draw.rect(screen,square_colour_green,pygame.Rect(215,10,60,60))
pygame.draw.rect(screen,square_colour_yellow,pygame.Rect(285,10,60,60))
pygame.draw.rect(screen,square_colour_grey,pygame.Rect(355,10,60,60))
pygame.draw.rect(screen,square_colour_grey,pygame.Rect(425,10,60,60))
pygame.draw.rect(screen,square_colour_yellow,pygame.Rect(495,10,60,60))
for i in range(5):
    for a in range(5):
        pygame.draw.rect(screen,square_colour_grey,pygame.Rect(a*70+185,70*i+150,60,60))
pygame.font.init()
my_font = pygame.font.SysFont("arialblack",50)
for i in range(len(screen_caption)):    
    text_surface = my_font.render(screen_caption[i],False,(255,255,255))
    screen.blit(text_surface,(i*70+155,3))
pygame.display.flip()
for i in alphabet:
    keyboard(square_colour_lgrey,i)
green = ["@","@","@","@","@",]
running = True
show_word = False
pos_x = 0
pos_y = 0
p = 2
word = []
word2 = []
words = []
guess = []
lines = open("Words5.txt","r").readlines()
for i in lines:
    i = i
for a in range (len(i)):
    if i[a] == ",":
        words.append(i[p:a-1])
        p = p+(a-p)+3
w = random.choice(words)
for i in w:
    word.append(i.upper())
while running:
    print(guess)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                text("A")
            elif event.key == pygame.K_b:
                text("B")
            elif event.key == pygame.K_c:
                text("C")
            elif event.key == pygame.K_d:
                text("D")
            elif event.key == pygame.K_e:
                text("E")
            elif event.key == pygame.K_f:
                text("F")
            elif event.key == pygame.K_g:
                text("G")
            elif event.key == pygame.K_h:
                text("H")
            elif event.key == pygame.K_i:
                text("I")
            elif event.key == pygame.K_j:
                text("J")
            elif event.key == pygame.K_k:
                text("K")
            elif event.key == pygame.K_l:
                text("L")
            elif event.key == pygame.K_m:
                text("M")
            elif event.key == pygame.K_n:
                text("N")
            elif event.key == pygame.K_o:
                text("O")
            elif event.key == pygame.K_p:
                text("P")
            elif event.key == pygame.K_q:
                text("Q")
            elif event.key == pygame.K_r:
                text("R")
            elif event.key == pygame.K_s:
                text("S")
            elif event.key == pygame.K_t:
                text("T")
            elif event.key == pygame.K_u:
                text("U")
            elif event.key == pygame.K_v:
                text("V")
            elif event.key == pygame.K_w:
                text("W")
            elif event.key == pygame.K_x:
                text("X")
            elif event.key == pygame.K_y:
                text("Y")
            elif event.key == pygame.K_z:
                text("Z")
            elif event.key == pygame.K_F1:
                if show_word == True:
                    pygame.draw.rect(screen,(0,0,0),pygame.Rect(10,70,700,80))
                    show_word = False
                else:
                    for i in range(len(word)):
                        text_surface = my_font.render(word[i],False,(255,255,255))
                        screen.blit(text_surface,(i*70+195,70))
                    show_word = True
            elif event.key == pygame.K_F2:
                guess2 = ""
                for i in guess:
                    guess2 = guess2+i
                if check_word(guess2.lower(),words) == True:
                    w = guess2.upper()
                    word = []
                    for i in w:
                        word.append(i)
                    if show_word == True:
                        pygame.draw.rect(screen,(0,0,0),pygame.Rect(10,70,700,80))
                        for i in range(len(word)):
                            text_surface = my_font.render(word[i],False,(255,255,255))
                            screen.blit(text_surface,(i*70+195,70))
            elif event.key == pygame.K_F3:
                for i in range(5):
                    if pos_x > 0:
                        pygame.draw.rect(screen,square_colour_grey,pygame.Rect((pos_x-1)*70+185,pos_y*70+150,60,60))
                        pos_x = pos_x-1
                        guess.pop()
                if pos_y > 0:
                    pos_y = pos_y-1
                    for i in range(5):
                        pygame.draw.rect(screen,square_colour_grey,pygame.Rect(((5-i)-1)*70+185,pos_y*70+150,60,60))
            elif event.key == pygame.K_F4:
                for i in alphabet:
                    keyboard(square_colour_lgrey,i)
                green = ["@","@","@","@","@",]
            elif event.key == pygame.K_BACKSPACE:
                if pos_x > 0:
                    pygame.draw.rect(screen,square_colour_grey,pygame.Rect((pos_x-1)*70+185,pos_y*70+150,60,60))
                    pos_x = pos_x-1
                    guess.pop()
            elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                if pos_x == 5:
                    if pos_y < 5:
                        guess2 = ""
                        for i in guess:
                            guess2 = guess2+i
                        if check_word(guess2.lower(),words) == True:
                            for i in guess2:
                                keyboard(square_colour_grey,i)
                            complete = True
                            word2 = word[:]
                            for i in range(len(word2)):
                                if word2[i] == guess[i]:
                                    check(square_colour_green,i,i)
                            for i in range(len(guess)):
                                for a in range(len(word2)):
                                    if word2[a] == guess[i]:
                                        check(square_colour_yellow,a,i)
                            for i in range(len(word2)):
                                if word2[i] == "@green@":
                                    green.pop(i)
                                    green.insert(i,word[i])
                            if word2 == ["@green@","@green@","@green@","@green@","@green@",]:
                                word = reset()
                            else:
                                guess = []
                                pos_y = pos_y+1
                                pos_x = 0
                        else:
                            print("Word not in the list")
                            time.sleep(0.5)
                            print("Cleared")
                    if pos_y > 4:
                        word = reset()
    pygame.display.flip()             
pygame.quit()
