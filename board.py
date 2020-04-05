import pygame

BLUE = (0,88,150)
GREEN = (28,140,45)
YELLOW = (231,255,9)
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 900

YARD = 360
YARD_HOLE = 45

blue_path = [[90, 390], [150, 390], [210, 390], [270, 390], [330, 390],
		[390, 330], [390, 270], [390, 210], [390, 150], [390, 90], [390, 30],
		[450, 30],
		[510, 30], [510, 90], [510, 150], [510, 210], [510, 270],
		[510, 330],
		[570, 390], [630, 390], [690, 390], [750, 390], [810, 390], [870, 390],
		[870, 450],
		[870, 510], [810, 510], [750, 510], [690, 510], [630, 510], [570, 510],
		[510, 570], [510, 630], [510, 690], [510, 750], [510, 810], [510, 870],
		[450, 870],
		[390, 870], [390, 810], [390, 750], [390, 690], [390, 630], [390, 570],
		[330, 510], [270, 510], [210, 510], [150, 510], [90, 510], [30, 510],
		[30, 450], [90, 450], [150, 450], [210, 450], [270, 450], [330, 450], [390, 450]]

RED_path = [[510, 90], [510, 150], [510, 210], [510, 270],
		[510, 330],
		[570, 390], [630, 390], [690, 390], [750, 390], [810, 390], [870, 390],
		[870, 450],
		[870, 510], [810, 510], [750, 510], [690, 510], [630, 510], [570, 510],
		[510, 570], [510, 630], [510, 690], [510, 750], [510, 810], [510, 870],
		[450, 870],
		[390, 870], [390, 810], [390, 750], [390, 690], [390, 630], [390, 570],
		[330, 510], [270, 510], [210, 510], [150, 510], [90, 510], [30, 510],
		[30, 450],
		[30, 390], [90, 390], [150, 390], [210, 390], [270, 390], [330, 390],
		[390, 330], [390, 270], [390, 210], [390, 150], [390, 90],[390, 30],
		[450, 30], [450, 90], [450, 150], [450, 210], [450, 270], [450, 330], [450, 390]]

green_path = [[810, 510], [750, 510], [690, 510], [630, 510], [570, 510],
		[510, 570], [510, 630], [510, 690], [510, 750], [510, 810], [510, 870],
		[450, 870],
		[390, 870], [390, 810], [390, 750], [390, 690], [390, 630], [390, 570],
		[330, 510], [270, 510], [210, 510], [150, 510], [90, 510], [30, 510],
		[30, 450],
		[30, 390], [90, 390], [150, 390], [210, 390], [270, 390], [330, 390],
		[390, 330], [390, 270], [390, 210], [390, 150], [390, 90], [390, 30],
		[450, 30],
		[510, 30], [510, 90], [510, 150], [510, 210], [510, 270],
		[510, 330],
		[570, 390], [630, 390], [690, 390], [750, 390], [810, 390], [870, 390],
		[870, 450], [810, 450], [750, 450], [690, 450], [630, 450], [570, 450], [510, 450]]

yellow_path = [[390, 810], [390, 750], [390, 690], [390, 630], [390, 570],
		[330, 510], [270, 510], [210, 510], [150, 510], [90, 510], [30, 510],
		[30, 450],
		[30, 390], [90, 390], [150, 390], [210, 390], [270, 390], [330, 390],
		[390, 330], [390, 270], [390, 210], [390, 150], [390, 90], [390, 30],
		[450, 30],
		[510, 30], [510, 90], [510, 150], [510, 210], [510, 270],
		[510, 330],
		[570, 390], [630, 390], [690, 390], [750, 390], [810, 390], [870, 390],
		[870, 450],
		[870, 510], [810, 510], [750, 510], [690, 510], [630, 510], [570, 510],
		[510, 570], [510, 630], [510, 690], [510, 750], [510, 810], [510, 870],
		[450, 870], [450, 810], [450, 750], [450, 690], [450, 630], [450, 570], [450, 510]]

assert len(blue_path) == len(RED_path) == len(green_path) == len(yellow_path)
assert WINDOW_WIDTH == WINDOW_HEIGHT == 900

def draw_board(game_window):
	# Blue
	pygame.draw.rect(game_window, BLUE, [0, 0, 360, 360]) # Draw the "yard" rectangle
	pygame.draw.polygon(game_window, BLUE, [[360, 360], [360, 540], [450, 450]]) # Draw the "home" triangle
	pygame.draw.circle(game_window, WHITE, [90, 90], YARD_HOLE)
	pygame.draw.circle(game_window, WHITE, [270, 90], YARD_HOLE)
	pygame.draw.circle(game_window, WHITE, [90, 270], YARD_HOLE)
	pygame.draw.circle(game_window, WHITE, [270, 270], YARD_HOLE)
	# Tokens
	pygame.draw.circle(game_window, BLUE, [90, 90], 30)
	pygame.draw.circle(game_window, BLUE, [270, 90], 30)
	pygame.draw.circle(game_window, BLUE, [90, 270], 30)
	pygame.draw.circle(game_window, BLUE, [270, 270], 30)

	# Yellow
	pygame.draw.rect(game_window, YELLOW, [0,540,360,360])
	pygame.draw.polygon(game_window, YELLOW, [[360, 540], [540, 540], [450, 450]])
	pygame.draw.circle(game_window, WHITE, [90, 810], YARD_HOLE)
	pygame.draw.circle(game_window, WHITE, [90, 630], YARD_HOLE)
	pygame.draw.circle(game_window, WHITE, [270, 810], YARD_HOLE)
	pygame.draw.circle(game_window, WHITE, [270, 630], YARD_HOLE)
	# Tokens
	pygame.draw.circle(game_window, YELLOW, [90, 810], 30)
	pygame.draw.circle(game_window, YELLOW, [90, 630], 30)
	pygame.draw.circle(game_window, YELLOW, [270, 810], 30)
	pygame.draw.circle(game_window, YELLOW, [270, 630], 30)

	# RED
	pygame.draw.rect(game_window, RED, [540, 0, 360, 360])
	pygame.draw.polygon(game_window, RED, [[360, 360], [540, 360], [450, 450]])
	pygame.draw.circle(game_window, WHITE, [630, 90], YARD_HOLE)
	pygame.draw.circle(game_window, WHITE, [810, 90], YARD_HOLE)
	pygame.draw.circle(game_window, WHITE, [810, 270], YARD_HOLE)
	pygame.draw.circle(game_window, WHITE, [630, 270], YARD_HOLE)
	# Tokens
	pygame.draw.circle(game_window, RED, [630, 90], 30)
	pygame.draw.circle(game_window, RED, [810, 90], 30)
	pygame.draw.circle(game_window, RED, [810, 270], 30)
	pygame.draw.circle(game_window, RED, [630, 270], 30)

	# Green
	pygame.draw.rect(game_window, GREEN, [540, 540, 360, 360])
	pygame.draw.polygon(game_window, GREEN, [[540, 540], [540, 360], [450, 450]])
	pygame.draw.circle(game_window, WHITE, [810, 810], YARD_HOLE)
	pygame.draw.circle(game_window, WHITE, [630, 810], YARD_HOLE)
	pygame.draw.circle(game_window, WHITE, [630, 630], YARD_HOLE)
	pygame.draw.circle(game_window, WHITE, [810, 630], YARD_HOLE)
	# Tokens
	pygame.draw.circle(game_window, GREEN, [810, 810], 30)
	pygame.draw.circle(game_window, GREEN, [630, 810], 30)
	pygame.draw.circle(game_window, GREEN, [630, 630], 30)
	pygame.draw.circle(game_window, GREEN, [810, 630], 30)

	#Boxes (long)
	pygame.draw.rect(game_window, RED, [420, 60, 60, 360])
	pygame.draw.rect(game_window, YELLOW, [420, 540, 60, 300])
	pygame.draw.rect(game_window, BLUE, [60, 420, 360, 60])
	pygame.draw.rect(game_window, GREEN, [540, 420, 300, 60])
	
	#Boxes (short)
	pygame.draw.rect(game_window, BLUE, [60, 360, 60, 60])
	pygame.draw.rect(game_window, GREEN, [780, 480, 60, 60])
	pygame.draw.rect(game_window, YELLOW, [360, 780, 60, 60])
	pygame.draw.rect(game_window, RED, [480, 60, 60, 60])

	# Squares (vertical lines)
	line1 = YARD
	while line1 <= WINDOW_WIDTH-YARD:
		pygame.draw.line(game_window, BLACK, [line1, 0], [line1, YARD], 2)
		pygame.draw.line(game_window, BLACK, [line1, WINDOW_HEIGHT-YARD], [line1, WINDOW_HEIGHT], 2)
		pygame.draw.line(game_window, BLACK, [0, line1], [YARD, line1], 2)
		pygame.draw.line(game_window, BLACK, [WINDOW_WIDTH-YARD, line1], [WINDOW_WIDTH, line1], 2)
		line1 += 60 # Line spacing
	
	# Squares (horizontal lines)
	line2 = 0
	while line2 <= YARD:
		pygame.draw.line(game_window, BLACK, [YARD, line2], [WINDOW_WIDTH - YARD, line2], 2)
		pygame.draw.line(game_window, BLACK, [YARD, WINDOW_HEIGHT-line2], [WINDOW_WIDTH-YARD, WINDOW_HEIGHT-line2], 2)
		pygame.draw.line(game_window, BLACK, [line2, YARD], [line2, WINDOW_HEIGHT-YARD], 2)
		pygame.draw.line(game_window, BLACK, [WINDOW_WIDTH-line2, YARD], [WINDOW_WIDTH-line2, WINDOW_HEIGHT-YARD], 2)
		line2 += 60

	pygame.display.update()
	pygame.image.save(game_window, "board.tga")

def get_path(colour): # Get the path depending on colour
	if colour == BLUE:
		return blue_path
	elif colour == RED:
		return RED_path
	elif colour == GREEN:
		return green_path
	else:
		return yellow_path

def clear_token(game_window, token):
	img = pygame.image.load("board.tga")
	game_window.blit(img,(0,0))
	pygame.display.update()

	path = get_path(token.colour)
	if path[token.currPos] in [[90, 390], [90, 450], [150, 450], [210, 450], [270, 450], [330, 450], [390, 450]]:
		pygame.draw.circle(game_window, BLUE, path[token.currPos], 19)
	elif path[token.currPos] in [[510, 90], [450, 90], [450, 150], [450, 210], [450, 270], [450, 330], [450, 390]]:
		pygame.draw.circle(game_window, RED, path[token.currPos], 19)
	elif path[token.currPos] in [[810, 510], [810, 450], [750, 450], [690, 450], [630, 450], [570, 450], [510, 450]]:
		pygame.draw.circle(game_window, GREEN, path[token.currPos], 19)
	elif path[token.currPos] in [[390, 810], [450, 810], [450, 750], [450, 690], [450, 630], [450, 570], [450, 510]]:
		pygame.draw.circle(game_window, YELLOW, path[token.currPos], 19)
	else:
		pygame.draw.circle(game_window, WHITE, path[token.currPos], 19)

	pygame.image.save(game_window, "board.tga")
	pygame.display.update()

def draw_token(game_window, token, x):
	img = pygame.image.load("board.tga")
	game_window.blit(img,(0,0))
	pygame.display.update()

	path = get_path(token.colour)
	pygame.draw.circle(game_window, BLACK, path[token.currPos], 18)
	pygame.draw.circle(game_window, token.colour, path[token.currPos], 15)

	font = pygame.font.SysFont("comicsansms", 25)
	text = font.render(x, True, BLACK)
	game_window.blit(text, [path[token.currPos][0]-4, path[token.currPos][1]-7])

	pygame.image.save(game_window, "board.tga")
	pygame.display.update()

def load_board_state(game_window):
	img = pygame.image.load("board.tga")
	game_window.blit(img,(0,0))
	pygame.display.update()