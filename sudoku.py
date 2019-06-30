from tkinter import *
from math import factorial
from itertools import permutations
import copy
import sys
from random import choice


def beginning(grid):
	for x in range(9):
		for y in range(9):
			tell.configure(text='let me know {}'.format(grid[x][y].get()))
			if not grid[x][y].get().isdigit:
				tell.configure(text='box[{}][{}] is not text. It is {}'.format(x,y,grid[x][y].get()))
				grid[x][y].configure(bg='red')


def begin(grid):
	box = []
	for y in range(9):
		smallbox = []
		for x in range(9):
			smallbox.append(grid[x][y].get())
		box.append(smallbox)
	player(box, grid)


def player(box, grid):
	check = checker(box)
	if check:
		trial(box, grid)
	else:
		tell.configure(text='There is a problem with the sudoku.')


def checker(box):
	check2 = horicheck(box)
	check1 = vertcheck(box)
	check3=boxcheck(box)
	return check1 and check2 and check3

			
def horicheck(box):
	check = True
	for j in range(len(box)):
		for i in box[j]:
			if i != '':
				if box[j].count(i)>1 or int(i)>9 or int(i)<0:
					check=False
	return check
	
def vertcheck(box):
	box2=[[] for i in range(9)]
	for i in box:
		[box2[j].append(i[j]) for j in range(9)]
	return horicheck(box2)
def vtoh(box):
	box2=[[] for i in range(9)]
	for i in box:
		[box2[j].append(i[j]) for j in range(9)]
	return box2
	
def btoh(box):
	box2=[[] for i in range(9)]
	for i in box:
		x=0
		for j in range(9):
			while len(box2[(j//3)+x]) == 9: x+=3
			box2[(j//3)+x].append(i[j])
	return box2

def boxcheck(box):
	box2=[[] for i in range(9)]
	for i in box:
		x=0
		for j in range(9):
			while len(box2[(j//3)+x]) == 9: x+=3
			box2[(j//3)+x].append(i[j])
	return horicheck(box2)
	
def trial(box, grid):
	state, candidate, pos = findlowest(box, [], [])
	possibilities = []
	possibilities = lister(candidate, possibilities)
	loc = {len(possibilities):str(state)+str(pos)}
	blacklisted = []
	while True:
		box2, possibilities, loc, blacklisted, finished = first_pass(box, possibilities, loc, blacklisted, grid)
		if finished:
			break
		combo = []
		for i in loc:
			combo.append(loc[i])
		state, candidate, pos = findlowest(box2, combo, blacklisted)
		possibilities = lister(candidate, possibilities)
		loc[len(possibilities)] = str(state)+str(pos)

def findlowest(box, combo, blacklisted):
	boxb = btoh(box)
	boxv = vtoh(box)
	mini = 10
	state = ''
	for i in range(9):
		if boxv[i].count('') < mini and boxv[i].count('') > 0 and blacklisted.count(combo+['v'+str(i)]) == 0:
			state = 'v'
			pos = i
			lowest = boxv[i]
			mini = boxv[i].count('')
		if box[i].count('') < mini and box[i].count('') > 0 and blacklisted.count(combo+['h'+str(i)]) == 0:
			state = 'h'
			pos=i
			lowest = box[i]
			mini = box[i].count('')
		if boxb[i].count('') < mini and boxb[i].count('') > 0 and blacklisted.count(combo+['b'+str(i)]) == 0:
			state = 'b'
			lowest = boxb[i]
			pos=i
			mini = boxb[i].count('')
	return state, lowest, pos


def lister(candidate, possibilities):
	l=[1,2,3,4,5,6,7,8,9]
	blank = candidate.count('')
	for i in candidate:
		if i != '': l.remove(int(i))
	cand = ''.join(map(str,l))
	poss = [''.join(p) for p in permutations(cand)]
	for i in poss:
		candidates = copy.deepcopy(candidate)
		j = list(i)
		while candidates.count('')>0: candidates[candidates.index('')] = j.pop(0)
		possibilities.append(candidates)
	return possibilities 


def first_pass(box, possibilities, loc, blacklisted, grid):
	finished = False
	while True:
		state = []
		pos = []
		candidate = []
		places = []
		combo = []
		amount = len(possibilities)
		for i in loc:
			state.append(loc[i][0])
			pos.append(loc[i][1])
			try:
				candidate.append(possibilities[i-1])
			except IndexError:
				print(loc)
				sys.exit()
			places.append(i)
			combo.append(loc[i])
		box2 = boxing(candidate, state, pos, box)
		if not checker(box2):

			if amount == 1:
				print('error.')
				sys.exit()
			if len(places) > 1:
				possibilities.pop(places[-1] - 1)
				if places[-1]-places[-2] == 1:
					m = 0
					for i in range(1, len(places)):
						if not places[-i] - places[-i-1] == 1: break
						m += 1
					#if places[-1] - places[0] == len(places)+1 and len(places) > 2: i += 1
					m += 1
					for n in range(1, m):
						if n == m-1:
							loc[places[-n-1]-1] = loc[places[-n-1]]
							del(loc[places[-n-1]])
							blacklisted.append(combo[:-n])
						possibilities.pop(places[-n-1]-1)
						del(loc[places[-n]])
				else:

					loc[places[-1]-1] = loc[places[-1]]
					del (loc[places[-1]])
			else:
				if len(possibilities) > 1:
					possibilities.pop(places[-1] - 1)
					loc[places[-1] - 1] = loc[places[-1]]
					del (loc[places[-1]])


		else:
			check = True
			for i in box2:
				if i.count('') > 0:
					check = False
			if check:
				finish(box2, grid)
				finished = True
				return box2, possibilities, loc, blacklisted, finished
			else:
				return box2, possibilities, loc, blacklisted, finished


def boxing(candidate, state, pos, boxs):
	box = copy.deepcopy(boxs)
	for i in range(len(state)):
		if state[i] == 'h':
			box[int(pos[i])] = candidate[i]
		if state[i] == 'v':
			boxv = vtoh(box)
			boxv[int(pos[i])] = candidate[i]
			box = vtoh(boxv)
		if state[i] == 'b':
			boxb = btoh(box)
			boxb[int(pos[i])] = candidate[i]
			box = btoh(boxb)
	return box


def finish(box2, grid):
	box2 = vtoh(box2)
	for i in range(len(box2)):
		for j in range(len(box2[i])):
			grid[i][j].delete(0, END)
			grid[i][j].insert(0, box2[i][j])
			
	
	
room=Tk()
box=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
playground=Frame()
for x in range(9):
	for y in range(9):
		box[x][y]=Entry(playground,font=('Verdana',10),width=3)
		box[x][y].grid(row=y, column=x)
done=Button(text="Solve it", command = lambda grid=box: begin(grid))
tell=Label(text='Sudoku Solver')
playground.grid(row=1, column=0)
done.grid(row=2, column=0)
tell.grid(row=0, column=0)
mainloop()
