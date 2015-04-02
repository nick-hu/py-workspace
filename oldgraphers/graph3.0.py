#!/usr/bin/python

from math import pi, cos, tan, sin, sqrt

def coefinput():
	global deg
	deg = int(raw_input('Degree of polynomial: '))
	print color('\nEquation coefficients:', 1) 
	coef = []
	for n in range(deg,-1,-1):
		coef.append(float(raw_input('\tx^'+str(n)+': ')))
	return coef

def genpoint(coef): # y-value calculation
	global yvals
	yvals = [] 
	for x in flrange(xmin,xmax+1,xscl):
		xval = coef[0]*x**deg
		for d in range(deg-1,-1,-1):
			xval = xval+(coef[(-1*d)-1]*x**d)
		yvals.append(xval)
	return yvals

def plotgrid(grid,yvals):
	global ysvals
	ysvals = [y for y in flrange(ymax,ymin-1,-1*yscl)]
	for val in range(len(yvals)): # Grid filling
		for sval in range(len(ysvals)):
			if yvals[val] == ysvals[sval]:
				grid[sval][val] = color(point, pc)

def dispgrid(grid,coef):
	global point
	print '\n'
	for l in range(len(grid)): 
		print ' '.join(grid[l]), 
		if ysvals[l] % 1 == 0: print ' '+str(int(ysvals[l]))
		elif ysvals[l] % pi == 0 or ysvals[l] % pi == pi: 
			print ' '+str(int(ysvals[l]/pi)), 'pi'
		else: print ' -'
	
	print '\n'
	
def cprint(coef):
	deg = len(coef)-1
	toprint = ''
	toprint += 'f(x) = '
	degco = [(d,len(coef)-1-d) for d in range(deg, -1, -1)]

	for d, c in degco:
		sign = str(coef[c])[0]
		if sign == '-': sign = ''
		else: sign = '+'
		if coef[c-1] == 0 and d+1 == deg: sign = ''
		if d == deg: sign = ''
            
		if coef[c] == 0: continue
			
		if d == 0: 
			toprint += sign + str(coef[c])
			break
		elif d == 1:
			if coef[c] == 1: toprint += sign + 'x '
			else: toprint += sign + str(coef[c]) + 'x '
			continue
		
		elif coef[c] == 1: toprint += sign + 'x^' + str(d)+' '
		else: toprint += sign + str(coef[c]) + 'x^' + str(d)+' '

	return toprint

def flrange(start,end,step): # Float range function
	vals = []
	n = start
	if n < end:
		while n < end:
			vals.append(n)
			n = n+step
	else:
		while n > end:
			vals.append(n)
			n = n+step
	return vals

def color(string, *c):
	ansi = '\033['
	for code in c:
		if len(c) == 1: ansi = ansi + str(code)
		elif code == c[-1]: ansi = ansi + str(code)
		else: ansi = ansi + str(code) + ';'
	return (ansi + 'm%s' + '\033[0m') % string

print '\033[2J\033[H'
print color('~~~ Welcome to Grapher 3.0! ~~~\n', 1, 3)
print color('''Maximize this window to maximize visibility of the graph!
Enter the information of your equation in standard form (f(x) = or y =).
Grapher will only plot points if they fall exactly on the grid.
For visibility, limit marker length to one character only!\n''', 2)

while True:
	print color('Graph settings (graph will be centered at (0,0)):', 1)
	sim = raw_input('\tSingle[enter]/Simultaneous[s]: ')
	width = int(raw_input(color('\tGraph width: ', 31, 2)))
	height = int(raw_input(color('\tGraph height: ', 34, 2)))
	xscl = float(input(color('\tx scale: ', 31, 2)))
	yscl = float(input(color('\ty scale: ', 34, 2)))
	
	colours = {'':30, 'red':31, 'green':32, 'orange':33, 'blue':34,
			'purple':35, 'cyan':36, 'gray':37, 'grey':37}
	
	if sim == '':
		point = raw_input('\tPoint marker (enter for default): ')
		if point == '': point = 'o'
		pc = raw_input('\tPoint colour (enter for default): ')
		if pc in colours: pc = colours[pc]
		else: pc = 30 
	
	blank = raw_input('\tBlank space fill (enter for default): ')
	if blank != '':
		bc = raw_input('\tBlank space colour (enter for default): ')
		bc = colours[bc]
	if blank == '': 
		blank = ' '
		bc = 30
	
	print '\n'
	rep = 'c'

	while True:	
		tp = raw_input(color('Function type', 1) + 
		' (t to view supported types): ')

		if tp == 't':
			print color('''
			===== FUNCTION TYPES =====
			p - Polynomial: y = f(x)
			r - Rational: y = f(x)/g(x)
			rd - Radical: y = sqrt(f(x))
			e - Exponential: y = a^x
			l - Logarithmic: y = logb(x)\n''', 2)
			continue

		if sim == '' or rep == 'c':
			grid = [[] for n in range(height+1)]
			for n in range(height+1):
				if n == height/2: 
					for x in range(width+1):
						if x == width/2: grid[n].append(color('|', 1))
						else: grid[n].append(color('=', 1))
				else:
					for x in range(width+1):
						if x == width/2: grid[n].append(color('|', 1))
						else: grid[n].append(color(blank, bc))

		if sim == 's': 
			point = raw_input('\tPoint marker (enter for default): ')
			if point == '': point = 'o'
			pc = raw_input('\tPoint colour (enter for default): ')
			if pc in colours: pc = colours[pc]
			else: pc = 30 

		xmax = (width/2)*xscl; xmin = (-1*width/2)*xscl
		ymax = (height/2)*yscl; ymin = (-1*height/2)*yscl

		if tp == 'p':
			print '\nPolynomial:\t',
			c = coefinput()		
			p = genpoint(c)
			plotgrid(grid,p)
			dispgrid(grid,c)

		elif tp == 'r':
			print '\nNumerator polynomial:\t',
			c1 = coefinput()
			p1 = genpoint(c1)
			print '\nDenominator polynomial:\t',
			c2 = coefinput()
			p2 = genpoint(c2)

			p3 = []
			for val in range(len(p1)):
				if p2[val] == 0: p3.append(None)
				else: p3.append(p1[val]/p2[val])

			plotgrid(grid,p3)
			dispgrid(grid)

		elif tp == 'rd':
			print '\nRadical polynomial - sqrt(f(x)):\t',
			c = coefinput()
			p = genpoint(c)

			p2 = []
			for val in p:
				if val < 0: p2.append(None)
				else: p2.append(sqrt(val))
			
			plotgrid(grid,p2)
			dispgrid(grid)

		rep = raw_input('New graph[n]/clear grid[c]/settings[s]/quit[q]: ')
		print '\n'
		if rep == 's' or rep == 'q': break
	if rep == 'q': break

print color('~~~ Goodbye and thank you for using Grapher 3.0! ~~~', 1)
