import board
import pygame


# game translates the board into a pygame display
class Game:
    # create color constants
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    RED = pygame.Color('red')
    GREEN = pygame.Color('green')

    def __init__(self, width, height, fps, squareSize, snakeCoord, snakeLength):
        # initialize board
        self.board = board.Board(width, height, snakeCoord, snakeLength, None)

        # set square size
        self.squareSize = squareSize

        # set screen size
        self.screenWidth = width * squareSize
        self.screenHeight = height * squareSize

        # set up pygame
        pygame.init()
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        pygame.display.set_caption('Snake')

        # set fps
        self.clock = pygame.time.Clock()
        self.fps = fps

        # store input direction
        self.inputDirection = None

    def draw_snake(self):
        for coord in self.board.snake.get_body():
            x, y = coord
            pygame.draw.rect(self.screen, self.GREEN, (x * self.squareSize, y * self.squareSize, self.squareSize, self.squareSize))

    def draw_apple(self):
        x, y = self.board.apple.get_coord()
        pygame.draw.rect(self.screen, self.RED, (x * self.squareSize, y * self.squareSize, self.squareSize, self.squareSize))

    def draw_score(self, fontSize=20, fontColor=None, font=None):
        if font == None:
            font = pygame.font.SysFont('Arial', fontSize)
        else:
            font = pygame.font.SysFont(font, fontSize)
        if fontColor == None:
            fontColor = self.WHITE
        else:
            fontColor = pygame.Color(fontColor)
        score = font.render('Score: ' + str(self.board.get_score()), True, fontColor)
        self.screen.blit(score, (0, 0))

    def display_game_over(self):
        # game over screen
        self.screen.fill(self.BLACK)
        font = pygame.font.SysFont('Arial', 50)
        gameOver = font.render('Game Over', True, self.WHITE)
        gameOverRect = gameOver.get_rect()
        gameOverRect.center = (self.screenWidth/2, self.screenHeight/2)
        self.screen.blit(gameOver, gameOverRect)
        pygame.display.update()
        pygame.time.wait(1000)

    # handle pygame events
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # quit the game
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.inputDirection = 'right'
                elif event.key == pygame.K_LEFT:
                    self.inputDirection = 'left'
                elif event.key == pygame.K_UP:
                    self.inputDirection = 'up'
                elif event.key == pygame.K_DOWN:
                    self.inputDirection = 'down'

        # check if direction is opposite of current direction
        snakeDirection = self.board.snake.get_direction()
        if self.inputDirection == 'right' and snakeDirection != 'left':
            self.board.snake.change_direction(self.inputDirection)
        elif self.inputDirection == 'left' and snakeDirection != 'right':
            self.board.snake.change_direction(self.inputDirection)
        elif self.inputDirection == 'up' and snakeDirection != 'down':
            self.board.snake.change_direction(self.inputDirection)
        elif self.inputDirection == 'down' and snakeDirection != 'up':
            self.board.snake.change_direction(self.inputDirection)

    def run(self):
        # pause game until user presses a key
        paused = True
        while paused:
            self.handle_events()
            if self.inputDirection != None:
                paused = False
            
            # draw initial board
            self.screen.fill(self.BLACK)
            self.draw_snake()
            self.draw_apple()
            self.draw_score()

            # draw press any key to continue
            font = pygame.font.SysFont('Arial', 50)
            pressKey = font.render('Press any key to continue', True, self.WHITE)
            pressKeyRect = pressKey.get_rect()
            pressKeyRect.midtop = (self.screenWidth/2, self.screenHeight/2)
            self.screen.blit(pressKey, pressKeyRect)

            pygame.display.update()
            self.clock.tick(self.fps)

        # game loop
        while True:
            self.handle_events()
            if self.board.move():
                self.screen.fill(self.BLACK)
                self.draw_apple()
                self.draw_snake()
                self.draw_score() # default arial size 20 font color white
                pygame.display.update()
                self.clock.tick(self.fps)
            else:
                # game over
                self.display_game_over()
                pygame.quit()
                exit()