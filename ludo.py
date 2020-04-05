import pygame
import sys
from board import *
from token_piece import Token
from player import Player
import random

BLUE = (0,88,150)
GREEN = (28,140,45)
YELLOW = (231,255,9)
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)

pygame.init()

window_height = 900
window_width = 900
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Ludo")
clock = pygame.time.Clock()
game_window.fill(WHITE)

is_player_turn = True

def intro():
	for event in pygame.event.get():
		print(event)
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
			
	game_window.fill(WHITE)
	font = pygame.font.SysFont("comicsansms", 250)
	text = font.render("Ludo", True, (0, 128, 0))
	game_window.blit(text,
        (450 - text.get_width() // 2, 450 - text.get_height() // 2))
	pygame.display.update()
	pygame.time.wait(500)

	game_window.fill(WHITE)
	pygame.display.update()
	assert window_width == window_height == 900
	draw_board(game_window)

def get_roll(): # Simple dice function
	return random.randint(1, 6)

def create_token(token, x): # Adds a new token to the starting pos (x == token number)
	token.status = "board"
	draw_token(game_window, token, x)

def move_token(token, roll, x): # Moves token
	pygame.event.get()
	if token.currPos + roll > 56 :
		token.currPos = 55
	else:
		token.currPos += roll
	draw_token(game_window, token, x)
	if token.currPos == 56:
		token.status = "home"
	# print(token)
	# print()
	pygame.time.wait(500)


def main():
	intro()

	players = [("Player 1", BLUE), ("Player 2", GREEN)]

	load_board_state(game_window)

	# Builds the token lists
	green_tokens = [Token(GREEN, number=i) for i in range(4)]
	blue_tokens = [Token(BLUE, number=i) for i in range(4)]
	red_tokens = [Token(RED, number=i) for i in range(4)]
	yellow_tokens = [Token(YELLOW, number=i) for i in range(4)]

	# Two players for testing purposes
	player1 = Player("Player 1", GREEN, green_tokens)
	player2 = Player("Player 2", BLUE, blue_tokens)
	player3 = Player("Player 3", RED, red_tokens)
	player4 = Player("Player 4", YELLOW, yellow_tokens)
	players = [player1, player2]

	pygame.time.wait(500)

	game_over = False
	while not game_over:
		pygame.event.get()
		for player in players: # Changes player turn
			roll = 6
			x = 0 # Token number (index)
			while roll == 6: # Current player's turn while roll is 6
				print("{}'s turn".format(player.name))
				print(input("Press enter to roll the dice "))
				roll = get_roll()
				print("Roll: {}".format(roll))

				numYardTokens = len([t for t in player.tokens if t.status == "yard"]) # Gets number of tokens in yard
				numBoardTokens = len([t for t in player.tokens if t.status == "board"]) # Gets number of tokens on board

				if numYardTokens > 0 and roll == 6:
					if numBoardTokens > 0: # If the player rolls a 6 and has tokens in the yard they can choose to add a token to the board
						addToken = input("Would you like to add a token? [y/n] ")
						if addToken == "y":
							player.tokens[numBoardTokens].status == "board"
							create_token(player.tokens[numBoardTokens], str(numBoardTokens))
						else:
							x = int(input("Enter token number: ")) if numBoardTokens > 1 else 0
							clear_token(game_window, player.tokens[x])
							move_token(player.tokens[x], roll, str(x))
					else: # If the player rolls a 6 and has no tokens one is automatically added
						player.tokens[0].status == "board"
						create_token(player.tokens[0], str(0))
				
				elif numBoardTokens > 0:
					if numBoardTokens > 1: x = int(input("Enter token number: ")) # If player has multiple tokens they must choose which one is to be moved
					elif numBoardTokens > 0: x = 0 # If player has 1 token, it is moved automatically
					clear_token(game_window, player.tokens[x])
					move_token(player.tokens[x], roll, str(x))
				
				if player.tokens[x].status == "home": # If a token reaches the finish, the game ends (temporary)
					game_over = True
					break

			if game_over == True:
				break # Needed to fix bug no. 3 (see below)
		

	pygame.time.wait(2000)
	pygame.image.save(game_window, "board.tga")
	game_over = True

if __name__ == '__main__':
	main()

""" Bugs:

1. Multiple tokens on same space not supported
2. (FIXED) White circle if token pos is cleared on coloured square
3. (FIXED) If player other than last player wins, other players still get one more turn
	
"""	