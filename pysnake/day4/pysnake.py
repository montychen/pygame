import sys
import pygame

pygame.init()
pygame.display.set_caption("pysnake")

game_clock = pygame.time.Clock()
game_speed = 60
game_screen_width, game_screen_height = 640, 480
game_screen = pygame.display.set_mode((game_screen_width, game_screen_height))
game_field = game_screen.get_rect()
game_running = True
game_bgcolor = 0, 0, 0
game_linecolor = 33, 33, 33

square_color1 = 33, 255, 33
square_color2 = 245, 155, 66
# square_color2 = 33, 192, 33
# square_x, square_y = 0, 0
# square_size = 20
# square_speed = 1
# square_speed_x, square_speed_y = square_speed, 0
CELL_SIZE = 20 # 一个格子的大小（像素）
square_rect = pygame.Rect(0, 0, CELL_SIZE, CELL_SIZE)
UP, DOWN, LEFT, RIGHT = (0, -CELL_SIZE), (0, CELL_SIZE), (-CELL_SIZE, 0), (CELL_SIZE, 0)
sqare_direction = RIGHT
sqare_can_turn = RIGHT
sqare_speed = 5  # 每秒移动几个格
square_delay = 1000/sqare_speed  # 移动一格需要的时间
sqare_time2move = pygame.time.get_ticks() + square_delay



while game_running:
    # 用户控制 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            if sqare_direction in (LEFT, RIGHT):  # 不允许180度掉头， 只能90度转弯
                if  event.key == pygame.K_UP: sqare_can_turn = UP
                elif event.key == pygame.K_DOWN:  sqare_can_turn = DOWN
            elif sqare_direction in (UP, DOWN):   # 不允许180度掉头， 只能90度转弯
                if event.key == pygame.K_LEFT:  sqare_can_turn = LEFT
                elif event.key == pygame.K_RIGHT: sqare_can_turn = RIGHT
            

    # 更新数据
    # if square_rect.x % CELL_SIZE == 0 and square_rect.y % CELL_SIZE == 0: # 保证在格子内，避免压着线走
    if pygame.time.get_ticks() >= sqare_time2move :
        sqare_time2move = pygame.time.get_ticks() + square_delay  # 更新下一次可以移动的时间
        sqare_direction = sqare_can_turn
        square_rect = square_rect.move(sqare_direction)

    # 不能飞出窗口区域
    print(f"坐标:{square_rect} 速度:{sqare_direction} 范围:{game_field.contains(square_rect)} FPS:{game_clock.get_fps():0.2f} pre tick:{game_clock.get_time()}")
    # if square_rect.left < 0:  square_rect.left = 0
    # elif square_rect.right > game_screen_width: square_rect.right = game_screen_width

    # if square_rect.top < 0: square_rect.top = 0
    # elif square_rect.bottom > game_screen_height: square_rect.bottom = game_screen_height


    # 更新画面
    game_screen.fill(game_bgcolor)

    # 画网格线
    for i in range(CELL_SIZE, game_screen_width, CELL_SIZE): 
        pygame.draw.line(game_screen, game_linecolor, (i, 0), (i, game_screen_height)) # 竖线
    for i in range(CELL_SIZE, game_screen_height, CELL_SIZE): 
        pygame.draw.line(game_screen, game_linecolor, (0, i), (game_screen_width, i))  # 横线

    # pygame.draw.rect(game_screen, square_color, square_rect)
    game_screen.fill(square_color1, square_rect)
    game_screen.fill(square_color2, square_rect.inflate(-4, -4))

    pygame.display.flip()
    game_clock.tick(game_speed)


pygame.quit()
sys.exit(0)