#!/usr/bin/python

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

print '''~~~ Welcome to Grapher 2.0! ~~~\n
Maximize this window to maximize visibility and readability of the graph!\n
Enter the information of your polynomial in standard form (f(x) = or y =). 
*Note: Grapher will only plot points if they fall exactly on the grid.*
For visibility, limit marker length to one character only!\n'''

while True:
	print 'Graph settings (graph will be centered at (0,0)):'
	width = int(raw_input('\tGraph width: '))
	height = int(raw_input('\tGraph height: '))
	xscl = float(raw_input('\tx scale: '))
	yscl = float(raw_input('\ty scale: '))
	point = raw_input('\tPoint marker (enter for default): ')
	if point == '': point = 'o'
	blank = raw_input('\tBlank space fill (enter for default): ')
	if blank == '': blank = ' '
	print '\n'

	while True:	
		deg = int(raw_input('Degree of equation: '))
		print '\nEquation coefficients:' 
		coef = []
		for n in range(deg,-1,-1):
			coef.append(float(raw_input('\tx^'+str(n)+': ')))

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
		
		xmax = (width/2)*xscl; xmin = (-1*width/2)*xscl
		ymax = (height/2)*yscl; ymin = (-1*height/2)*yscl

		yvals = [] # y-value calculation
		for x in flrange(xmin,xmax+1,xscl):
			xval = coef[0]*x**deg
			for d in range(deg-1,-1,-1):
				xval = xval+(coef[(-1*d)-1]*x**d)
			yvals.append(xval)

		ysvals = [y for y in flrange(ymax,ymin-1,-1*yscl)]
		for val in range(len(yvals)): # Grid filling
			for sval in range(len(ysvals)):
				if yvals[val] == ysvals[sval]:
					grid[sval][val] = point

		print '\n'
		for l in range(len(grid)): 
			print ' '.join(grid[l]), 
			if ysvals[l] % 1 == 0: print ' '+str(int(ysvals[l]))
			else: print ' -' 
		print '\n'

		rep = raw_input('New graph[n]/change settings[s]/quit[q]: ')
		print '\n'
		if rep == 's' or rep == 'q': break
	if rep == 'q': break

print 'Goodbye and thank you for using Grapher 2.0!'