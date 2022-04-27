import pygame, time, Settings, Wordle4, Wordle5, Wordle6
def Main():
    one = "SETTINGS"
    two = "4 LETTERS"
    three = "5 LETTERS"
    four = "6 LETTERS"
    screen_width = 710
    screen_height = 780
    screen_caption = "WORDLE"
    square_colour_grey = (60,60,60)
    square_colour_yellow = (186,166,81)
    square_colour_green = (83,141,78)
    square_colour_lgrey = (156,156,156)
    screen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption(screen_caption)
    pygame.draw.rect(screen,square_colour_grey,pygame.Rect(145,10,60,60))
    pygame.draw.rect(screen,square_colour_green,pygame.Rect(215,10,60,60))
    pygame.draw.rect(screen,square_colour_yellow,pygame.Rect(285,10,60,60))
    pygame.draw.rect(screen,square_colour_grey,pygame.Rect(355,10,60,60))
    pygame.draw.rect(screen,square_colour_grey,pygame.Rect(425,10,60,60))
    pygame.draw.rect(screen,square_colour_yellow,pygame.Rect(495,10,60,60))
    pygame.font.init()
    my_font = pygame.font.SysFont("arialblack",50)
    def reset():
        pygame.draw.rect(screen,(0,0,0),pygame.Rect(0,70,800,800))
        for i in range(len(screen_caption)):
            text_surface = my_font.render(screen_caption[i],False,(255,255,255))
            screen.blit(text_surface,(i*70+155,3))
        for i in range(8):
            pygame.draw.rect(screen,square_colour_grey,pygame.Rect(75+i*70,150,60,60))
        for i in range(9):
            pygame.draw.rect(screen,square_colour_grey,pygame.Rect(43.5+i*70,290,60,60))
        for i in range(9):
            pygame.draw.rect(screen,square_colour_grey,pygame.Rect(43.5+i*70,430,60,60))
        for i in range(9):
            pygame.draw.rect(screen,square_colour_grey,pygame.Rect(43.5+i*70,570,60,60))
        for i in range(len(one)):
            text_surface = my_font.render(one[i],False,(255,255,255))
            screen.blit(text_surface,(i*70+85,140))
        for i in range(len(two)):
            text_surface = my_font.render(two[i],False,(255,255,255))
            screen.blit(text_surface,(i*70+53.5,280))
        for i in range(len(three)):
            text_surface = my_font.render(three[i],False,(255,255,255))
            screen.blit(text_surface,(i*70+53.5,420))
        for i in range(len(four)):
            text_surface = my_font.render(four[i],False,(255,255,255))
            screen.blit(text_surface,(i*70+53.5,560))
        pygame.display.flip()
    reset()
    running = True
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                mouse_x = pygame.mouse.get_pos()[0]
                mouse_y = pygame.mouse.get_pos()[1]
                if mouse_x > 70 and mouse_x < 625 and mouse_y > 150 and mouse_y < 210:
                    for i in range(8):
                        pygame.draw.rect(screen,square_colour_yellow,pygame.Rect(75+i*70,150,60,60)) 
                    for i in range(len(one)):
                        text_surface = my_font.render(one[i],False,(255,255,255))
                        screen.blit(text_surface,(i*70+85,140))
                    mouse_position = "ONE"
                elif mouse_x > 40 and mouse_x < 665 and mouse_y > 290 and mouse_y < 350:
                    for i in range(9):
                        pygame.draw.rect(screen,square_colour_yellow,pygame.Rect(43.5+i*70,290,60,60))                
                    for i in range(len(two)):
                        text_surface = my_font.render(two[i],False,(255,255,255))
                        screen.blit(text_surface,(i*70+53.5,280))
                    mouse_position = "TWO"
                elif mouse_x > 40 and mouse_x < 665 and mouse_y > 430 and mouse_y < 490:
                    for i in range(9):
                        pygame.draw.rect(screen,square_colour_yellow,pygame.Rect(43.5+i*70,430,60,60))
                    for i in range(len(three)):
                        text_surface = my_font.render(three[i],False,(255,255,255))
                        screen.blit(text_surface,(i*70+53.5,420))
                    mouse_position = "THREE"
                elif mouse_x > 40 and mouse_x < 665 and mouse_y > 570 and mouse_y < 630:
                    for i in range(9):
                        pygame.draw.rect(screen,square_colour_yellow,pygame.Rect(43.5+i*70,570,60,60))
                    for i in range(len(four)):
                        text_surface = my_font.render(four[i],False,(255,255,255))
                        screen.blit(text_surface,(i*70+53.5,560))
                    mouse_position = "FOUR"
                else:
                    reset()
                    mouse_position = "##"
                pygame.display.flip()
            elif event.type == pygame.MOUSEBUTTONUP:
                if mouse_position != "##":
                    if mouse_position == "ONE":
                        for i in range(8):
                            pygame.draw.rect(screen,square_colour_green,pygame.Rect(75+i*70,150,60,60))   
                        for i in range(len(one)):
                            text_surface = my_font.render(one[i],False,(255,255,255))
                            screen.blit(text_surface,(i*70+85,140))
                        pygame.display.flip()
                        time.sleep(0.2)
                        running = Settings.Settings()
                        if running == True:
                            reset()
                    elif mouse_position == "TWO":
                        for i in range(9):
                            pygame.draw.rect(screen,square_colour_green,pygame.Rect(43.5+i*70,290,60,60))
                        for i in range(len(two)):
                            text_surface = my_font.render(two[i],False,(255,255,255))
                            screen.blit(text_surface,(i*70+53.5,280))
                        pygame.display.flip()
                        time.sleep(0.2)
                        running = Wordle4.Wordle4()
                        if running == True:
                            reset()
                    elif mouse_position == "THREE":
                        for i in range(9):
                            pygame.draw.rect(screen,square_colour_green,pygame.Rect(43.5+i*70,430,60,60))
                        for i in range(len(three)):
                            text_surface = my_font.render(three[i],False,(255,255,255))
                            screen.blit(text_surface,(i*70+53.5,420))
                        pygame.display.flip()
                        time.sleep(0.2)
                        running = Wordle5.Wordle5()
                        if running == True:
                            reset()
                    elif mouse_position == "FOUR":
                        for i in range(9):
                            pygame.draw.rect(screen,square_colour_green,pygame.Rect(43.5+i*70,570,60,60))
                        for i in range(len(four)):
                            text_surface = my_font.render(four[i],False,(255,255,255))
                            screen.blit(text_surface,(i*70+53.5,560))
                        pygame.display.flip()
                        time.sleep(0.2)
                        running = Wordle6.Wordle6()
                        if running == True:
                            reset()
    pygame.quit()
