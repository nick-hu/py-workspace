#!/usr/bin/python

from math import pi, cos, tan, sin, sqrt

def coefinput():
	global deg
	deg = int(raw_input('Degree of polynomial: '))
	print '\nEquation coefficients:' 
	coef = []
	for n in range(deg,-1,-1):
		coef.append(float(raw_input('\tx^'+str(n)+': ')))
	return coef

def genpoint(coef): # y-value calculation
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
				grid[sval][val] = point

def dispgrid(grid):
	print '\n'
	for l in range(len(grid)): 
		print ' '.join(grid[l]), 
		if ysvals[l] % 1 == 0: print ' '+str(int(ysvals[l]))
		elif ysvals[l] % pi == 0 or ysvals[l] % pi == pi: 
			print ' '+str(int(ysvals[l]/pi)), 'pi'
		else: print ' -'
	print '\n'

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

print '''~~~ Welcome to Grapher 2.5! ~~~\n
Maximize this window to maximize visibility and readability of the graph!\n
Enter the information of your equation in standard form (f(x) = or y =). 
*Note: Grapher will only plot points if they fall exactly on the grid.*
For visibility, limit marker length to one character only!\n'''

while True:
	print 'Graph settings (graph will be centered at (0,0)):'
	sim = raw_input('\tSingle[enter]/Simultaneous[s]: ')
	width = int(raw_input('\tGraph width: '))
	height = int(raw_input('\tGraph height: '))
	xscl = float(input('\tx scale: '))
	yscl = float(input('\ty scale: '))
	if sim == '':
		point = raw_input('\tPoint marker (enter for default): ')
		if point == '': point = 'o'
	blank = raw_input('\tBlank space fill (enter for default): ')
	if blank == '': blank = ' '
	print '\n'
	rep = 'c'

	while True:	
		tp = raw_input('Function type (t to view supported types): ')

		if tp == 't':
			print '''
			===== FUNCTION TYPES =====
			p - Polynomial: y = f(x)
			r - Rational: y = f(x)/g(x)
			rd - Radical: y = sqrt(f(x))
			e - Exponential: y = a^x
			l - Logarithmic: y = logb(x)\n'''
			continue

		if sim == '' or rep == 'c':
			grid = [[] for n in range(height+1)]
			for n in range(height+1):
				if n == height/2: 
					for x in range(width+1):
						if x == width/2: grid[n].append('|')
						else: grid[n].append('=')
				else:
					for x in range(width+1):
						if x == width/2: grid[n].append('|')
						else: grid[n].append(blank)

		if sim == 's': 
			point = raw_input('Point marker (enter for default): ')
			if point == '': point = 'o'

		xmax = (width/2)*xscl; xmin = (-1*width/2)*xscl
		ymax = (height/2)*yscl; ymin = (-1*height/2)*yscl

		if tp == 'p':
			print '\nPolynomial:\t',
			c = coefinput()		
			p = genpoint(c)
			plotgrid(grid,p)
			dispgrid(grid)

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

			dispgrid(grid)

		rep = raw_input('New graph[n]/clear grid[c]/settings[s]/quit[q]: ')
		print '\n'
		if rep == 's' or rep == 'q': break
	if rep == 'q': break

print 'Goodbye and thank you for using Grapher 2.5!'