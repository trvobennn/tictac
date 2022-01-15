import pygame
pygame.init()
pygame.font.init()
# initialize board and various state variables
text = pygame.font.SysFont('arial',30,False,False)
running = True
playing = True
move_y = None
move_x = None
board_state = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0,
             5: 0, 6: 0, 7: 0, 8: 0}
cursor_state = {0: [110,100], 1: [230,100], 2: [350,100], 3: [110,210], 4: [230,210],
                5: [350,210], 6: [110,310], 7: [230,310], 8: [350,310]}
window = pygame.display.set_mode((600,400))
curs_ind = 0
turn = 1
# sprites for 'pieces'
piece_group = pygame.sprite.Group()
class Piece1(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((50,50))
        self.image.fill((220,80,50))
        self.rect = self.image.get_rect(bottomleft=(pos[0],pos[1]))
class Piece2(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((50, 80, 220))
        self.rect = self.image.get_rect(bottomleft=(pos[0],pos[1]))
# if board modified, insert proper piece
def draw_pieces():
    for i in board_state:
        if board_state[i] == 1:
            p_1 = Piece1((cursor_state[i][0], cursor_state[i][1]))
            piece_group.add(p_1)
        if board_state[i] == 2:
            p_2 = Piece2((cursor_state[i][0], cursor_state[i][1]))
            piece_group.add(p_2)
        else:
            continue
# draw board lines
def draw_board():
    game_surface = pygame.Surface((600,400))
    game_surface.fill((30,30,30))
    window.blit(game_surface,(0,0))
    l1 = pygame.draw.line(window, (190,190,190),(80,40),(80,340))
    l2 = pygame.draw.line(window, (190, 190, 190), (200, 40), (200, 340))
    l3 = pygame.draw.line(window, (190, 190, 190), (320, 40), (320, 340))
    l4 = pygame.draw.line(window, (190, 190, 190), (440, 40), (440, 340))
    l5 = pygame.draw.line(window, (190, 190, 190), (80, 130), (440, 130))
    l6 = pygame.draw.line(window, (190, 190, 190), (80, 240), (440, 240))
# take user input
def input():
    global move_x, move_y, turn, playing
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if playing:
                if event.key == pygame.K_w:
                    move_y = 'up'
                if event.key == pygame.K_s:
                    move_y = 'down'
                if event.key == pygame.K_a:
                    move_x = 'left'
                if event.key == pygame.K_d:
                    move_x = 'right'
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    if board_state[curs_ind] == 0:
                        if turn == 1 or turn % 2 == 1:
                            board_state[curs_ind] = 1
                            turn += 1
                        elif turn % 2 == 0:
                            board_state[curs_ind] = 2
                            turn += 1
            if not playing:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    turn = 1
                    for i in range(0,len(board_state)):
                        board_state[i] = 0
                    piece_group.empty()
                    playing = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                move_y = None
            if event.key == pygame.K_a or event.key == pygame.K_d:
                move_x = None

def win_cond():
    global playing
    p1_win = text.render('Player 1 wins! Space/retrn to restart.', True, False, (160,160,160))
    p2_win = text.render('Player 2 wins! Space/retrn to restart.', True, False, (160,160,160))
    # horizontal
    if board_state[0] == 1 and board_state[1] == 1 and board_state[2] == 1 \
            or board_state[3] == 1 and board_state[4] == 1 and board_state[5] == 1\
            or board_state[6] == 1 and board_state[7] == 1 and board_state[8] == 1:
        window.blit(p1_win,(90,330))
        playing = False
    if board_state[0] == 2 and board_state[1] == 2 and board_state[2] == 2 \
            or board_state[3] == 2 and board_state[4] == 2 and board_state[5] == 2\
            or board_state[6] == 2 and board_state[7] == 2 and board_state[8] == 2:
        window.blit(p2_win,(90,330))
        playing = False
    # vertical
    if board_state[0] == 1 and board_state[3] == 1 and board_state[6] == 1 \
            or board_state[1] == 1 and board_state[4] == 1 and board_state[7] == 1\
            or board_state[2] == 1 and board_state[5] == 1 and board_state[8] == 1:
        window.blit(p1_win,(90,330))
        playing = False
    if board_state[0] == 2 and board_state[3] == 2 and board_state[6] == 2 \
            or board_state[1] == 2 and board_state[4] == 2 and board_state[7] == 2\
            or board_state[2] == 2 and board_state[5] == 2 and board_state[8] == 2:
        window.blit(p2_win,(90,330))
        playing = False
    # diag
    if board_state[0] == 1 and board_state[4] == 1 and board_state[8] == 1 \
            or board_state[2] == 1 and board_state[4] == 1 and board_state[6] == 1:
        window.blit(p1_win,(90,330))
        playing = False
    if board_state[0] == 2 and board_state[4] == 2 and board_state[8] == 2 \
            or board_state[2] == 2 and board_state[4] == 2 and board_state[6] == 2:
        window.blit(p2_win,(90,330))
        playing = False
def game_loop():
    global curs_ind, move_y, move_x
    cursor_pos = cursor_state[curs_ind][0], cursor_state[curs_ind][1]
    cursor = pygame.Surface((60, 20))
    cursor.fill((190, 190, 190))
    window.blit(cursor,cursor_pos)

    if move_x == 'right':
        curs_ind = (curs_ind + 1) % len(board_state)
        move_x = None
    if move_x == 'left':
        curs_ind = (curs_ind - 1) % len(board_state)
        move_x = None
    if move_y == 'up':
        curs_ind = (curs_ind - 3) % len(board_state)
        move_y = None
    if move_y == 'down':
        curs_ind = (curs_ind + 3) % len(board_state)
        move_y = None

def update():
    draw_pieces()
    draw_board()
    win_cond()
    game_loop()
    piece_group.draw(window)
    pygame.display.update()

def loop():

    clock = pygame.time.Clock()
    while True:
        window.fill((0, 0, 0))
        clock.tick(40)
        input()
        #print(curs_ind)
        update()

while running:
    loop()

