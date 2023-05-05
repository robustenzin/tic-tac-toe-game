import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Tic Tac Toe')

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up fonts
FONT_SIZE = 60
FONT = pygame.font.Font(None, FONT_SIZE)

# Set up the game board
board = [['', '', ''], ['', '', ''], ['', '', '']]

# Set up players
PLAYER_X = 'X'
PLAYER_O = 'O'
current_player = PLAYER_X

# Set up game state
game_over = False
winner = None

# Function to draw the game board
def draw_board():
    game_window.fill(WHITE)
    pygame.draw.line(game_window, BLACK, (200, 0), (200, 600), 5)
    pygame.draw.line(game_window, BLACK, (400, 0), (400, 600), 5)
    pygame.draw.line(game_window, BLACK, (0, 200), (600, 200), 5)
    pygame.draw.line(game_window, BLACK, (0, 400), (600, 400), 5)
    for row in range(3):
        for column in range(3):
            if board[row][column] == PLAYER_X:
                text = FONT.render(PLAYER_X, True, RED)
                game_window.blit(text, (column * 200 + 70, row * 200 + 60))
            elif board[row][column] == PLAYER_O:
                text = FONT.render(PLAYER_O, True, RED)
                game_window.blit(text, (column * 200 + 70, row * 200 + 60))

# Function to check if there is a winner
def check_winner():
    global game_over, winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            game_over = True
            winner = board[i][0]
            return
        if board[0][i] == board[1][i] == board[2][i] != '':
            game_over = True
            winner = board[0][i]
            return
    if board[0][0] == board[1][1] == board[2][2] != '':
        game_over = True
        winner = board[0][0]
        return
    if board[0][2] == board[1][1] == board[2][0] != '':
        game_over = True
        winner = board[0][2]
        return
    if all(all(row) for row in board):
        game_over = True
        winner = None

# Function to handle events
def handle_events():
    global current_player
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            row = event.pos[1] // 200
            column = event.pos[0] // 200
            if board[row][column] == '':
                board[row][column] = current_player
                if current_player == PLAYER_X:
                    current_player = PLAYER_O
                else:
                    current_player = PLAYER_X

# Game loop
while True:
    handle_events()
    draw_board()
    check_winner()
    if game_over:
        if winner:
            print(f"{winner} wins!")
        else:
            print("It's a tie!")
        pygame.time.wait(3000)
        pygame.quit()
        quit()

    pygame.display.update()

