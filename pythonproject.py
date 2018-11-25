import pygame

pygame.init()

pygame.font.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
screen = pygame.display.set_mode((361, 650))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

gameExit = True

shapes = [
    [[1,1,1]],

    [[1,1],
     [0,1]],

    [[1,1],
     [1,1]]]


lst = []
freeSpaces = [[0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              ]



class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


##
##def Ishape():
##    count = 0
##    for x in range(3):
##        if freeSpaces[0][x]==0:
##            count += 1
##            if count==3:
##                for i in range(3):
##                    pygame.draw.rect(screen, [255,69,0],(20+40*i, 230, 40, 40))
##                    freeSpaces[0][i] = 1
##
##
##def Lshape():
##    count = 0
##    for x in range(2):
##        if freeSpaces[0][x]==0:
##            count += 1
##            if count==2:
##                for i in range(2):
##                    pygame.draw.rect(screen, [50,205,50],(20+40*i, 230, 40, 40))
##                    freeSpaces[0][i] = 1


def leaderBoard():
    done = True
    BackGround = Background('tetris2.jpg', [0,0])
    backButton = pygame.Rect(10, 15, 50, 20)
    backText = pygame.font.SysFont('Comic Sans MS', 20)
    backSurface = backText.render('Back', False, (0, 0, 0))

    comingSoon = pygame.font.SysFont('Arial', 40)
    comingSoonT = comingSoon.render('Coming Soon!', False, (0,0,0))
    
    while done:
        screen.blit(BackGround.image, BackGround.rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if backButton.collidepoint(mouse_pos):
                    introPage()

                    
        pygame.draw.rect(screen, [255,255,255], backButton)
        screen.blit(backSurface,(15,17))

        screen.blit(comingSoonT, (100,400))
        
        pygame.display.update()
        clock.tick(60)
        
def howToPlayPage():
    done = True
    BackGround = Background('tetris2.jpg', [0,0])
    
    BackGround2 = Background('How_toplay.jpeg',[10,150])
    
    backButton = pygame.Rect(10, 15, 50, 20)
    backText = pygame.font.SysFont('Comic Sans MS', 20)
    backSurface = backText.render('Back', False, (0, 0, 0))

    while done:
        screen.blit(BackGround.image, BackGround.rect)

        #This shows the picture i drew
        screen.blit(BackGround2.image, BackGround2.rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if backButton.collidepoint(mouse_pos):
                    introPage()

                    
        pygame.draw.rect(screen, [255,255,255], backButton)
        screen.blit(backSurface,(15,17))
        
        pygame.display.update()
        clock.tick(60)

def mainGame():
    main = True


    BackGround = Background('tetris2.jpg', [0,0])
    backButton = pygame.Rect(10, 15, 50, 20)
    backText = pygame.font.SysFont('Comic Sans MS', 20)
    backSurface = backText.render('Back', False, (0, 0, 0))

    
    while main:
        screen.blit(BackGround.image, BackGround.rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False
                pygame.quit() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if backButton.collidepoint(mouse_pos):
                    introPage()
                    
        gameSpace = pygame.Rect(20, 230, 320, 400)
        pygame.draw.rect(screen, [255,255,255], gameSpace)
        
        #Draw seperators
        for x in range(9):
            pygame.draw.line(screen, [0,0,0], (20+(x*40),230), (20+(x*40),630), 2)

        
        #This draws the back button
        pygame.draw.rect(screen, [255,255,255], backButton)


        screen.blit(backSurface,(15,17))
        pygame.display.update()

def loginPage():
    login = True
    BackGround = Background('tetris2.jpg', [0,0])
    screen.blit(BackGround.image, BackGround.rect)


    backButton = pygame.Rect(10, 15, 50, 20)
    backText = pygame.font.SysFont('Comic Sans MS', 20)
    backSurface = backText.render('Back', False, (0, 0, 0))


    playButton = pygame.Rect(130,400,100,30)
    playText = pygame.font.SysFont('Arial',20)
    playSurface = playText.render('Play Now!',False,(0,0,0))


    UsernameText = pygame.font.SysFont('Arial',25)
    UsernameSurface = UsernameText.render('Enter Username Below',False,(0,0,0))
        

    ###############################################################
    ###This part is taken from https://stackoverflow.com/questions/46390231/
    ###how-to-create-a-text-input-box-with-pygame
    ###To create a text box
    
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(100, 350, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    
    while login:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                login = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if backButton.collidepoint(mouse_pos):
                    introPage()
                if playButton.collidepoint(mouse_pos):
                    lst.append(text)
                    print lst
                    mainGame()
                ##############
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        # Render the current text.
        if len(text) < 15:
            txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)
                

        pygame.draw.rect(screen, [255,255,255], backButton)
        pygame.draw.rect(screen, [255,255,255], playButton)

        
        screen.blit(backSurface,(15,17))
        screen.blit(playSurface,(140,410))
        screen.blit(UsernameSurface, (100,320))


        pygame.display.update()
        clock.tick(60)

        
def introPage():
    BackGround = Background('tetris2.jpg', [0,0])
    intro = True
#Creates buttons
    button = pygame.Rect(120, 330, 150, 45)
    leaderBoardButton = pygame.Rect(120, 395, 150, 45)
    howToPlay = pygame.Rect(120, 460, 150, 45)

#Texts for Buttons
    myfont = pygame.font.SysFont('Arial', 35)
    textsurface = myfont.render('Play', False, (255, 0, 0))

#Second button text
    text = pygame.font.SysFont('Arial', 30)
    textsurface2 = text.render('Leader Board', False, (255, 0, 0))

#Third button
    text2 = pygame.font.SysFont('Comic Sans MS', 35)
    howToPlayText = text2.render('How To Play', False, (255,0,0))
    while intro:
        screen.blit(BackGround.image, BackGround.rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button.collidepoint(mouse_pos):
                    loginPage()
                if leaderBoardButton.collidepoint(mouse_pos):
                    leaderBoard()

                if howToPlay.collidepoint(mouse_pos):
                    howToPlayPage()

                    
        #Draws rectanges for buttons
        pygame.draw.rect(screen, [255,255,255], button)
        pygame.draw.rect(screen, [255,255,255],howToPlay)
        pygame.draw.rect(screen, [255,255,255], leaderBoardButton)

        screen.blit(textsurface,(170,337))
        screen.blit(textsurface2,(130,405))
        screen.blit(howToPlayText, (125,468))

        
        pygame.display.update()

while gameExit:
    introPage()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = False
            pygame.quit()

    
            
        #if event.type == pygame.KEYDOWN:
            #if event.key == pygame.K_LEFT:
                
            #if event.key == pygame.K_RIGHT:
                







    



###############################################################################
###REFERENCES##
##Background retrived from:
#https://www.the-ebook-reader.com/blackberry-playbook.html
##
