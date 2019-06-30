import random
import copy
import unittest
import os

class Box:
	def __init__(self, size=4):
		"""Creates a 2048 box with specified size(default 4)"""
		self.empty = []
		self.fields = [[Field(x, y) for x in range(size)] for y in range(size)]

	def swipe(self, d):
		"""Decides what the key assignments mean and sends data to the move method"""
		if d == 'w':
			[self.move(0, -1, fields) for line in self.fields for fields in line]
		elif d == 's':
			reverse_list = copy.deepcopy(self.fields)
			reverse_list.reverse()
			[self.move(0, 1, fields) for line in reverse_list for fields in line]
		elif d == 'a':
			aside = copy.deepcopy(self.fields)
			aside = [[line[x] for line in aside] for x in range(len(aside))]
			[self.move(-1, 0, fields) for line in aside for fields in line]
		elif d == 'd':
			aside_rev = copy.deepcopy(self.fields)
			aside_rev = [[line[x] for line in aside_rev] for x in range(len(aside_rev))]
			aside_rev.reverse()
			[self.move(1, 0, fields) for line in aside_rev for fields in line]
		else:
			raise SyntaxError('Unknown movement key pressed.')

	def move(self, x, y, fields):
		"""Moves a single cell in a specified direction following the rules of 2048"""
		move_to = self.fields[fields.y][fields.x]
		if fields.value != 0:
			while 1:
				out_of_bounds = False
				if fields.y + y < 0 or fields.x + x < 0:
					out_of_bounds = True
				if not out_of_bounds:
					try:
						move_to = self.fields[fields.y + y][fields.x + x]
					except IndexError:
						out_of_bounds = True
				if out_of_bounds:
					if y == 0:
						x -= abs(x) // x
					else:
						y -= abs(y) // y
					break
				if move_to.value == 0:
					if y == 0:
						x += abs(x)//x
					else:
						y += abs(y)//y
				elif move_to.value == fields.value:
					if move_to.add_value == 0:
						move_to.add_value = fields.value
						self.fields[fields.y][fields.x].value = 0
						break
					else:
						if y == 0:
							x -= abs(x) // x
						else:
							y -= abs(y) // y
						break
				else:
					if y == 0:
						x -= abs(x) // x
					else:
						y -= abs(y) // y
					break
			move_to = self.fields[fields.y + y][fields.x + x]
			if fields.value != 0 and (move_to.x != fields.x or move_to.y != fields.y):
				move_to.value = fields.value
				self.fields[fields.y][fields.x].value = 0

	def compute(self):
		"""Adds up the joined tiles after each swipe"""
		for element in self.fields:
			for tile in element:
				if tile.add_value != 0 and tile.value != 0:
					tile.value += tile.add_value
					tile.add_value = 0

	def spaces(self):
		"""Checks for empty cells and returns the list of empty cell objects (empty list if no empty)"""
		self.empty = [fields for line in self.fields for fields in line if fields.value == 0]

	def high_tile(self):
		"""Returns the highest tile value"""
		all_values = [tile.value for line in self.fields for tile in line]
		all_values.sort()
		return all_values[-1]

	def end_check(self):
		"""Checks if the game is over, if so if the player has won or not"""
		top = self.high_tile()
		self.spaces()
		if top == 2048:
			return [True, True]
		else:
			if not self.empty:
				return [True, False]
			return [False, False]

	def spawn(self):
		"""Generates either 2 or 4 on a random empty tile"""
		self.spaces()
		spawned = (random.choice([2, 2, 4]), random.choice(self.empty))
		spawned[1].value = spawned[0]

	def prints(self):
		"""Prints the box neatly on a console"""
		[print([fields.value for fields in line]) for line in self.fields]
		print('')


class Field:
	"""A single cell/tile in the 2048 box."""
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.value = 0
		self.add_value = 0


def main():
	table = Box()
	game_over = table.end_check()
	table.spawn()
	table.prints()
	while not game_over[0]:
		print('Use WASD keys to control direction.')
		input_check = False
		while not input_check:
			d = input('> ')
			if d == 'w' or d == 'a' or d == 's' or d == 'd':
				input_check = True
				table.swipe(d.lower())
			else:
				print('Please only use the WASD keys.')
		table.compute()
		game_over = table.end_check()
		
		if game_over[0]:
			break
		os.system('cls')
		table.spawn()
		table.prints()
	if game_over[1]:
		print('Congratulations! you have reached the 2048 tile.')
	else:
		print('You have lost with the highest tile being ', table.high_tile())

main()