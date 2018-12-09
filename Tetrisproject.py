#    15-112: Principles of Programming and Computer Science
#    HW07 Programming: Term Project (Tetris)
#    Name      : Buthaina Al-kuwari
#    AndrewID  : balkuwar

######################################################################
# Refrences:
# https://gist.github.com/silvasur/565419/d9de6a84e7da000797ac681976442073045c74a4
# https://www.youtube.com/watch?v=Ign-VmKmz9g
# https://github.com/matachi/python-tetris/blob/master/main.py
# https://stackoverflow.com/questions/19733226/python-pygame-how-to-make-my-score-text-update-itself-forever
######################################################################

from random import randrange as rand
import pygame, sys

# The configuration
config = {
    'cell_size':    40,
    'cols':     8,
    'rows':     10,
    'delay':    750,
    'maxfps':   30
}


pygame.font.init() #initialize font

#Open scores file for append mode
f = open("scores.txt","a")

#this list is used to store usernames when logged in
lst = []

screen = pygame.display.set_mode((361,630))

colors = [ (255,99,71),
           (255, 0,   0  ),
           (0,   150, 0  ),
           (0,   0,   255),
           (255, 120, 0  ),
           (255, 255, 0  ),
           (180, 0,   255),
           (0,   220, 220)
           ]

def leaderBoard():
    done = True
    
    BackGround = Background('tetris2.jpg', [0,0])
    backButton = pygame.Rect(10, 15, 50, 20)
    
    #This shows the back button on screen
    backText = pygame.font.SysFont('Comic Sans MS', 20)
    backSurface = backText.render('Back', False, (0, 0, 0))

    comingSoon = pygame.font.SysFont('Arial', 40)
    comingSoonT = comingSoon.render('Name       Score', False, (0,0,0))

    names = pygame.font.SysFont("monospace", 35)

    f = open("scores.txt", "r")
    
    line = f.readline()

    #This will print scores on screen
    score1 = pygame.font.SysFont('Arial', 40)
    score1m = score1.render(str(line), False, (0,0,0))
    
    while done:

        screen.blit(BackGround.image, BackGround.rect)

        while line:
            nameo = names.render(line, 1, (0,0,0))
            line = f.readline()
        
            screen.blit(nameo, (5, 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
            #If the back button was clicked, return to main menu
                if backButton.collidepoint(mouse_pos):
                    introPage()

                    
        pygame.draw.rect(screen, [255,255,255], backButton)
        screen.blit(backSurface,(15,17))

        screen.blit(comingSoonT, (100,320))
        screen.blit(score1m, (100,360))
        
        pygame.display.update()
        
def howToPlayPage():
    done = True
    BackGround = Background('tetris2.jpg', [0,0])
    
    BackGround2 = Background('How_toplay.jpeg',[10,150])
    
    backButton = pygame.Rect(10, 15, 50, 20)
    backText = pygame.font.SysFont('Comic Sans MS', 20)
    backSurface = backText.render('Back', False, (0, 0, 0))

    while done:
        
        screen.blit(BackGround.image, BackGround.rect)

        #This shows the instructions page
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

        #clock.tick(30)
        pygame.display.update()

def loginPage():
    login = True
    BackGround = Background('tetris2.jpg', [0,0])


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
    ###To create an input box
    font = pygame.font.Font(None, 32)
    input_box = pygame.Rect(100, 350, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    
    while login:
        screen.blit(BackGround.image, BackGround.rect)
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
                    
                    App = TetrisApp()
                    App.run()
                    
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

        #clock.tick(30)
        pygame.display.update()

        

def introPage():
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


    BackGround = Background('tetris2.jpg', [0,0])

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
        




class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


# Define the shapes of the single parts
tetris_shapes = [
    [[1, 1, 1],
     [0, 1, 0]],
    
        [[0, 0, 5],
     [5, 5, 5]],

    
    [[6, 6, 6, 6]],
    
    [[7, 7],
     [7, 7]]
        
        
]

# This function takes a shape as input parameter and is supposed to rotate
# the shape
def rotateShape(shape):
    if shape == tetris_shapes[2] == [[6,6,6,6]]:
        return [[6], [6], [6], [6]]
    
    if shape == [[6], [6], [6], [6]]:
        return [[6,6,6,6]]
    
    if shape == [[7,7], [7,7]]:
        return [[7,7], [7,7]]

    if shape == [[1,1,1],
                [0,1,0]]:
        
        return [[1, 0],
                [1, 1],
                [1, 0]]
    
    if shape == [[1, 0],
                [1, 1],
                [1, 0]]:
        
        return [[0, 1, 0],
                [1, 1, 1]]

    if shape == [[0, 1, 0],
                [1, 1, 1]]:
        
        return [[0, 1],
                [1, 1],
                [0, 1]]

    if shape == [[0, 1],
                 [1, 1],
                 [0, 1]]:
        return [[1, 1, 1],
                [0, 1, 0]]
        
    if shape == [[0, 0, 5], [5, 5, 5]]:
        
        return [[5, 5], [0, 5], [0, 5]]
    
    if shape == [[5, 5], [0, 5], [0, 5]]:
        
        return [[5, 5, 5],
                [5, 0, 0]]
    
    if shape == [[5, 5, 5],
                 [5, 0, 0]]:
        
        return [[5, 0],
                [5, 0],
                [5, 5]]
    
    if shape == [[5, 0],
                 [5, 0],
                 [5, 5]]:
        
        return [[0, 0, 5],
                [5, 5, 5]]
        

def check_collision(board, shape, offset):
    #This was taken from https://gist.github.com/silvasur/565419/d9de6a84e7da000797ac681976442073045c74a4
    #This function takes the 2d list that represents the board and is supposed to
    #replace a 0 with a number in the board to keep track of shapes
    off_x, off_y = offset
    for cy, row in enumerate(shape):
        for cx, cell in enumerate(row):
            try:
                if cell and board[ cy + off_y ][ cx + off_x ]:
                    return True
            except IndexError:
                return True
    return False


def remove_row(board, row):
    #This function takes the full row and deletes it from the list that represnets the
    #board and replaces it with a new element
    board.pop(row)
    return [[0,0,0,0,0,0,0,0]] + board
    
    
def join_matrixes(mat1, mat2, mat2_off):
#   This part is taken from https://gist.github.com/silvasur/565419/d9de
#   6a84e7da000797ac681976442073045c74a4
    off_x, off_y = mat2_off
    for cy, row in enumerate(mat2):
        for cx, val in enumerate(row):
            mat1[cy+off_y-1 ][cx+off_x] += val
    return mat1

def new_board():
    board = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [1, 1, 1, 1, 1, 1, 1, 1]]
    return board

class TetrisApp(object):
    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(250,25)
        self.width = 40 * 8
        self.height = 40 * 10       
        self.screen = pygame.display.set_mode((361,630))
        pygame.display.set_caption("Tetris")
        
        self.score = 0
        self.init_game()
        pygame.font.init()
    def newBlock(self):
        #This will generate a random shape from the tetris shapes list
        self.block = tetris_shapes[rand(len(tetris_shapes))]
        
        #This will place the shape in the middle of the screen
        self.block_x = int(config['cols']) / 2 
        self.block_y = 0

        #This will call the function check collision which will return
        #true if a collision happened and false otherwise.
        if check_collision(self.board,
                           self.block,
                           (self.block_x, self.block_y)):
            self.gameover = True

            
    #If the game is over this will generate a new board
    def init_game(self):
        self.board = new_board()
        self.newBlock() 

    #This function is used to display messages on screen
    def center_msg(self, msg):
        for i, line in enumerate(msg.splitlines()):
            msg_image =  pygame.font.Font(
                pygame.font.get_default_font(), 30).render(
                      line, False, (255,255,255), (0,0,0))

            msgim_center_x, msgim_center_y = msg_image.get_size()
            msgim_center_x //= 2
            msgim_center_y //= 2
      
            self.screen.blit(msg_image, (
            361 // 2-msgim_center_x,
            620 // 2-msgim_center_y+i*22))

#   This function is the same as the join_matrixes function except that this
#   is used to draw the shapes on the GUI
    def draw_matrix(self, matrix, offset):
                    off_x, off_y  = offset
                    for y, row in enumerate(matrix):
                        for x, val in enumerate(row):
                            if val:
                                pygame.draw.rect( self.screen, colors[val],
                                                  pygame.Rect(
                                                      20+(off_x+x) *
                                              config['cell_size'],
                                        230 + (off_y+y) *
                                          config['cell_size'], 
                                        config['cell_size'],
                                        config['cell_size']),0)
                                
    
    def move(self, delta_x):
            if not self.gameover and not self.paused:
                new_x = self.block_x + delta_x
                if new_x < 0:
                    new_x = 0
                if new_x > config['cols'] - len(self.block[0]):
                    new_x = config['cols'] - len(self.block[0])
                if not check_collision(self.board,
                                self.block,
                                   (new_x, self.block_y)):
                    self.block_x = new_x
    
    def drop(self):
        if not self.gameover and not self.paused:
            self.block_y += 1
            if check_collision(self.board,
                               self.block,
                               (self.block_x, self.block_y)):
                self.board = join_matrixes(
                  self.board,
                  self.block,
                  (self.block_x, self.block_y))
                self.newBlock()
                
                while True:
                    for i, row in enumerate(self.board[:-1]):
                        if 0 not in row:
                            self.score = self.score + 10
                            self.board = remove_row(
                              self.board, i)
                            
                            break
                    else:
                        break
    
    def rotate_stone(self):
        if not self.gameover and not self.paused:
            newBlock = rotateShape(self.block)
            if not check_collision(self.board,
                                   newBlock,
                                   (self.block_x, self.block_y)):
                self.block = newBlock
    
    def toggle_pause(self):
        self.paused = not self.paused
    
    def start_game(self):
        if self.gameover:
            self.init_game()
            self.gameover = False

    def back(self):
        introPage()
    def run(self):
        key_actions = {
            
            'LEFT':     lambda:self.move(-1),
            'RIGHT':    lambda:self.move(+1),
            'DOWN':     self.drop,
            'UP':       self.rotate_stone,
            'p':        self.toggle_pause,
            'SPACE':    self.start_game,
            'b' : self.back
        }

        
        self.gameover = False
        self.paused = False


        pygame.time.set_timer(pygame.USEREVENT+1, config['delay'])
        clock = pygame.time.Clock()
        
        myfont = pygame.font.SysFont("monospace", 35)
        
        BackGround = Background('tetris2.jpg', [0,0])

# I drew this white rectangle to change the color of the score and update the new score
        pygame.draw.rect(self.screen, [255,255,255], pygame.Rect(5,10,120,30))
        
        count = 0
        while 1:

            self.screen.blit(BackGround.image, BackGround.rect)
            
            scoretext = myfont.render("Score = "+str(self.score), 1, (0,0,0))

            self.screen.blit(scoretext, (5, 10))
            

            pygame.draw.rect(self.screen, [255,255,255], pygame.Rect(20,230,320,400))

            #Draw seperators
            for c in range(9):
                pygame.draw.line(screen, [0,0,0], (20+(c*40),230), (20+(c*40),630), 2)

            
            if self.gameover:
                count = count + 1
                
                if count == 1:
                    f.write(str(lst[0])+"    " + str(self.score)+"\n")
                    f.close()
                    
                gameOver = myfont.render("Game over!", 1, (255,0,0))

                gameOver2 = myfont.render("Your score is " + str(self.score), 1, (255,0,0))

                gameOver3 = myfont.render("Press space to play again or", 1, (255,0,0))

                gameOver4 = myfont.render("press B to go to main menu", 1, (255,0,0))

                self.screen.blit(gameOver, (100, 300))
                self.screen.blit(gameOver2, (80, 330))
                self.screen.blit(gameOver3, (20, 360))
                self.screen.blit(gameOver4, (20, 390))
                
            else:
                        if self.paused:
                            self.center_msg("Paused")
                        else:
                            self.draw_matrix(self.board, (0,0))
                            self.draw_matrix(self.block,
                                     (self.block_x,
                                      self.block_y))
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT+1:
                    self.drop()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                elif event.type == pygame.KEYDOWN:
                    for key in key_actions:
                        if event.key == eval("pygame.K_" +key):
                            key_actions[key]()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    
                    
                    
            clock.tick(config['maxfps'])
            
##if __name__ == '__main__':
##    App = TetrisApp()
##    App.run()
introPage()
# project
