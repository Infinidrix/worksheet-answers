from tkinter import *
from PIL import Image
from multiprocessing import cpu_count
import socket
import os
import time
import math
import chess
import chess.svg

def birthdate(day, month, year):
    magic_year = year + 18
    age_year = 2019 - year - (month//7)
    months = (18 - month)%12
    printed = 'You\'ll turn 18 on ' + str(magic_year) + ' now you are ' + str(months) + ' months and '+ str(age_year)+ ' years.'
    return printed

def title(name, gender):
    prefix = {'Male':'Mr. ', 'Female':'Mrs. '}
    if name[0:2] == 'Mr':
        return name
    return prefix[gender] + name

def adder(num1, num2, num3):
    if num1 == num2 or num2 == num3 or num1 == num3:
        return num1 + num2 + num3
    return None

def sorter(numbers):
    above_fifty = []
    below_fifty = []
    for i in numbers:
        if i < 50:
            below_fifty.append(i)
        else:
            above_fifty.append(i)
    return below_fifty, above_fifty

def histogram(words):
    for i in range(len(words)):
        if words.index(words[i]) == i:
            print(words[i], '#'*words.count(words[i]))
    
def lister(filename):
    img = Image.open(filename)
    listed = list(img.getdata())
    return listed

def factors(values):
	values = int(values)
	dividers = []
	for i in range(1, int(values ** 0.5) + 1):
		if values % i == 0:
			dividers.extend([i, int(values / i)])
	if dividers.count(int(values ** 0.5)) == 2:
		dividers.remove(int(values ** 0.5))
	dividers.sort()
	return dividers


def gcd(values):
	options = factors(min(values))
	options.sort()
	options.reverse()
	for i in options:
		factor = True
		for j in values:
			if j % i != 0:
				factor = False
		if factor:
			return i

def float_adder(num1, num2):
    if isinstance(num1, float) and isinstance(num2, float):
        return num1 + num2
    return None

def px_distance(point1, point2):
    distance = ((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)**(0.5)
    return distance*1.5

def cpu():
    return cpu_count()

def ip():
    return socket.gethostbyname(socket.gethostname())

def win_dimensions():
    return os.get_terminal_size()

def timer(statement):
    start = time.time()
    eval(statement)
    return time.time() - start

def bmi(weight, height):
    return weight/(height)**2

def helper():
    help(math)

def factorial(number):
    if number == 1:
        return 1
    return number*factorial(number-1)

def zero_adder(string, amount):
    return '0'*amount+string

def median(num1, num2, num3):
    seq = [num1, num2, num3]
    seq.sort()
    return seq[1]

def changer(change):
    hundred = change // 100
    change = change % 100
    fifty = change // 50
    change = change % 50
    tens = change // 10
    return hundred, fifty, tens

def pal_check(string):
    for i in range(len(string)):
        if string[i] != string[len(string) - i-1]:
            return False
    return True

def triangle_check(x1,y1,x2,y2,x3,y3):
    dist12=((x1-x2)**2+(y1-y2)**2)**0.5
    dist13=((x1-x3)**2+(y1-y3)**2)**0.5
    dist32=((x3-x2)**2+(y3-y2)**2)**0.5
    dist_list = [dist12,dist13,dist32]
    if max(dist_list) >= sum(dist_list) - max(dist_list):
        return False
    return True

def parallel_check(p,q):
    return (p[0][1] - p[1][1])/(p[0][0]-p[1][0]) == (q[0][1] - q[1][1])/(q[0][0]-q[1][0])

def lower_checker(string):
    for i in string:
        if i.islower():
            return True
    return False

def from_ten(number, base):
    new_num = []
    while number != 0:
        if number % base < 10:
            new_num.append(str(number % base))
        else: new_num.append(chr(55 + (number%base)))
        number = number // base
    new_num.reverse()
    return ''.join(new_num)

def extreme(numbers):
    maximum = numbers[0]
    minimum = numbers[0]
    for i in numbers:
        if maximum < i:
            maximum = i
        if minimum > i:
            minimum = i
    return maximum, minimum

def differ(numbers):
    for i in numbers:
        if numbers.count(i) > 1:
            return False
    return True

def all_possible(seq = ['a','e','i','o','u']):
    if len(seq) == 1:
        return [seq]
    all = []
    perm = [[seq[0]]+i for i in all_possible(seq[1:])]
    for p in range(len(perm)):
        for i in range(len(seq)):
            num_place = [j for j in range(len(seq))]
            for j in range(len(seq)):
                num_place[j] = (j+i)%len(seq)
            all.append([perm[p][j] for j in num_place])
    return all

def printed():
    all = all_possible()
    return ', '.join([''.join(i) for i in all])

def num_permutation(seq):
    str_seq = []
    for i in seq:
        str_seq.append(str(i))
    all = all_possible(str_seq)
    return ', '.join([''.join(i) for i in all])

def circle(x1, y1, r1, x2, y2, r2):
    if r1 > r2:
        larger = r1
        smaller = r2
        big_O = 'C1'
        small_o = 'C2'
    else:
        larger = r2
        smaller = r1
        big_O = 'C2'
        small_o = 'C1'
    distance = ((x2-x1)**2 + (y2 - y1)**2)**(0.5)
    if distance <= larger:
        if distance + smaller <= larger:
            return small_o + ' is in ' + big_O
        else:
            return 'Circumference of ' + big_O + ' and ' + small_o + ' intersect'
    else:
        return "C1 and C2 do not overlap"

def pattern():
    for i in range(5):
        print('* ' * i)
    for i in range(5, 0, -1):
        print('* ' * i)
        
def fact(value):
        if value <= 1:
            return 1
        return value*fact(value-1)

def comb(value):
	difference = value[0] - value[1]
	if difference < 0:
		difference = 0
	return int(fact(value[0]) / (fact(difference)*fact(value[1])))

def pascal(rows):
	for i in range(rows):
		for j in range(rows - i - 1):
			print(' '*3, end='')
		for j in range(i+1):
			print("{:<6d}".format(comb([i, j])), end='')
		print()

def two_power(number):
    return (math.log(number, 2)).is_integer()

def is_perfect(number):
    for i in range(2, int(number**0.5) + 1):
        if math.log(number, i) == 2.0:
            return True
    return False

def find_missing(seq):
    initial = seq[0] - 1
    for i in seq:
        if i != initial + 1:
            return initial + 1
        else:
            initial += 1
    
def sum_of_three(array, summation):
    for i in range(len(array)):
        for j in range(len(array)):
            if i == j:
                continue
            diff = summation - array[i] - array[j]
            if array.count(diff) >= [array[i], array[j], diff].count(diff):
                    return [array[i], array[j], diff]
    return False

def digit_rev(numbers):
    new_num = ''
    num_str = str(numbers)
    for i in num_str:
        new_num = i + new_num
    return new_num

def push_zero(seq):
    for i in seq:
        if i == 0:
            seq.remove(i)
            seq.append(i)
    return seq

def anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    for i in str1:
        if str1.count(i) != str2.count(i):
            return False
    return True

def grading(marks):
    grades = {83:'A', 64: 'B', 53: 'C', 44:'D', 0:'F'}
    for i in marks:
        for j in grades:
            if i >= j:
                break
        print(grades[j])
class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den
        self.reduce()
    def factors(values):
        values = int(values)
        dividers = []
        for i in range(1, int(values ** 0.5) + 1):
            if values % i == 0:
                dividers.extend([i, int(values / i)])
        if dividers.count(int(values ** 0.5)) == 2:
            dividers.remove(int(values ** 0.5))
        dividers.sort()
        return dividers
    def gcd(values):
        options = factors(min(values))
        options.sort()
        options.reverse()
        for i in options:
            factor = True
            for j in values:
                if j % i != 0:
                    factor = False
            if factor:
                return i
    def reduce(self):
        while gcd([self.num, self.den]) != 1:
            divider = gcd([self.num, self.den])
            self.num = self.num//divider
            self.den = self.den//divider
    def show(self):
        return self.num, self.den
    def printed(self):
        print(self.num, '-'*max((len(str(self.num)), len(str(self.den)))), self.den, sep='\n')

def tkinter_chess():
    chess = Tk()
    frames = [Frame(chess) for i in range(8)]
    colors = ['white', 'black']
    for i in range(8):
        for j in range(8):
            Canvas(frames[i], width = 40, height = 40, bg = colors[(i+j)%2]).grid(row=0, column=j)
        frames[i].grid(row = i, column = 0)
def image_chess():
	chess_board = chess.Board()
	img_data = chess.svg.board(board = chess_board)
	image = open('chess.svg', 'w')
	image.write(img_data)
	image.close()
def printer():
    print('Name: Biruk Solomon\nSection: 2\nATR/5471/11')
while True:
    query = input('>>> ')
    printer()
    print(eval(query))
