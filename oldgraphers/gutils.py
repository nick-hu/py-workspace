#!/usr/bin/python

from math import pi, cos, tan, sin, sqrt

print '\033[2J', '\033[H'

colours = {'':30, 'red':31, 'green':32, 'orange':33, 'blue':34,
			'purple':35, 'cyan':36, 'gray':37, 'grey':37}

class Graph():	
	def __init__(self, grid, gdata, coef, tp):
		self.grid = grid

		self.sim = gdata[0]
		self.width, self.height = gdata[1], gdata[2]
		self.xscl, self.yscl = gdata[3], gdata[4]
		self.pm, self.pc = gdata[5], gdata[6]
		self.bm, self.bc = gdata[7], gdata[8]
		self.xmax = (gdata[1]/2) * gdata[3]
		self.xmin = (-1 * gdata[1]/2) * gdata[3]
		self.ymax = (gdata[2]/2) * gdata[4]
		self.ymax = (-1 * gdata[2]/2) * gdata[4]

		self.coef = coef
		self.tp = tp

	def genvals(self):
		'''Generates y-values.'''

		if self.sim != 's': coefs = []
		print sim, coefs
		coefs.append((coef, pc, tp))
		
		yvals = [] 
		for x in flrange(xmin,xmax+1,xscl):
			xval = coef[0]*x**deg
			for d in range(deg-1,-1,-1):
				xval = xval+(coef[(-1*d)-1]*x**d)
			yvals.append(xval)
		
		return yvals
	
	def memcoef(self):
		coefs.append((self.coef, self.pc, self.tp))
		
	def plotgrid(self, yvals):
		'''Plots points on grid and prints grid to screen.'''

		if point == None: point = 
		
		ysvals = [y for y in flrange(
			self.ymax, self.ymin-1,-1 * self.yscl)]
		for val in range(len(yvals)):
			for sval in range(len(ysvals)):
				if yvals[val] == ysvals[sval]:
					self.grid[sval][val] = color(self.pm, self.pc)

		print '\n'
		for l in range(len(grid)): 
			print ' '.join(grid[l]), 
			if ysvals[l] % 1 == 0: print ' '+str(int(ysvals[l]))
			else: print ' -'
		
		print '\n'
		if sim != 's': coefs = []
		
		for c, p, tp in coefs:
			denom = False
			if tp == 'p' or denom == True: 
				print color(cprint(c), p)
				denom = False
			elif tp == 'r' and denom == False:
				print color(cprint(c), p) + '/'
				denom = True
			elif tp == 'rd': print color('sqrt(' + cprint(c) + ')', p)
		
		print '\n'
		
	


def setting():
	'''Provides graph settings.'''

	gdata = []
	''' Contents: sim, width, height, xscl, yscl,
		pmark, pcolour, bmark, bcolour'''
	
	print color('Graph settings (centered at (0,0)):', 1)
	inappend('\tSingle[enter]/Simultaneous[s]: ', gdata)
	if gdata[-1] != 's': gdata[-1] = ''
	
	inappend(color('\tGraph width: ', 31, 2), gdata, 'int')
	inappend(color('\tGraph height: ', 34, 2), gdata, 'int')
	inappend(color('\tx scale: ', 31, 2), gdata, 'float', True)
	inappend(color('\ty scale: ', 34, 2), gdata, 'float', True)
	
	if gdata[0] == '':
		inappend('\tPoint marker (enter for default): ', gdata)
		if gdata[-1] == '': gdata[-1] = 'o'

		inappend('\tPoint colour (enter for default): ', gdata)
		if gdata[-1] in colours: gdata[-1] = colours[gdata[-1]]
		else: gdata[-1] = 30

	else: gdata.extend([None, None])

	inappend('\tBlank space fill (enter for default): ', gdata)
	if gdata[-1] != '':
		inappend('\tBlank space colour (enter for default): ', gdata)
		if gdata[-1] in colours: gdata[-1] = colours[gdata[-1]]
		else: gdata[-1] = 30

	else: gdata.extend([' ', 30])

	print '\033[2J', '\033[H'
	
	return gdata

def inappend(prompt, data, tpe = '', evalu = False):
	'''Facilitates large amount of input to data structures.'''

	if evalu: data.append(float(input(prompt)))
	else:
		if tpe == 'int': data.append(int(raw_input(prompt)))
		elif tpe == 'float': data.append(float(raw_input(prompt)))
		else: data.append(raw_input(prompt))

	return data

def coefinput():
	'''Gathers coefficient input.'''
	
	deg = int(raw_input('Degree of polynomial: '))
	print color('\nEquation coefficients:', 1) 
	coef = []
	for n in range(deg,-1,-1):
		coef.append(float(raw_input('\tx^'+str(n)+': ')))
		
	return coef
	
def point
	
def cprint(coef):
	'''Equation printer.'''
	
	toprint = 'f(x) = '
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

def flrange(start, end, step):
	'''Range-like function for floats.'''
	
	vals = []
	if (start < end and step <= 0) or (start > end and step >= 0):
		return vals
	
	n = start
	if n < end:
		while n < end:
			vals.append(n)
			n = n + step
	else:
		while n > end:
			vals.append(n)
			n = n + step
	
	return vals

def color(string, *c):
	'''String colouring with ANSI escape sequences.'''
	
	ansi = '\033['
	for code in c:
		if len(c) == 1: ansi = ansi + str(code)
		elif code == c[-1]: ansi = ansi + str(code)
		else: ansi = ansi + str(code) + ';'
	
	return (ansi + 'm%s' + '\033[0m') % string

testgrid = []
testgraph = Graph(testgrid, setting(), coefinput(), 'p')
