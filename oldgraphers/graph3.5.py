#!/usr/bin/python

from math import pi, cos, tan, sin, sqrt
import gutils as gu


colours = {'':30, 'red':31, 'green':32, 'orange':33, 'blue':34,
			'purple':35, 'cyan':36, 'gray':37, 'grey':37}

print gu.color('~~~ Welcome to Grapher 3.5! ~~~\n', 1, 3)
print gu.color(
'''Maximize this window to maximize visibility of the graph!
Enter the information of your equation in standard form (f(x) = or y =).
Grapher will only plot points if they fall exactly on the grid.
For visibility, limit marker length to one character only!\n''', 2)

s = gu.setting()
sim, height, width, blank, bc = s[0], s[1], s[2], s[3], s[4]
rep = ''

while True:
	if rep == 's': 
		s = gu.setting()
		sim, height, width, blank, bc = s[0], s[1], s[2], s[3], s[4]
	
	print '\n'
	rep = 'c'
	coefs = []

	while True:	
		tp = gu.gettp()

		if tp == 't':
			print gu.color('''
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
						if x == width/2: 
							grid[n].append(gu.color('|', 1))
						else: grid[n].append(gu.color('=', 1))
				else:
					for x in range(width+1):
						if x == width/2: 
							grid[n].append(gu.color('|', 1))
						else: grid[n].append(gu.color(blank, bc))

		if sim == 's': 
			point = raw_input('\tPoint marker (enter for default): ')
			if point == '': point = 'o'
			pc = raw_input('\tPoint colour (enter for default): ')
			if pc in colours: pc = colours[pc]
			else: pc = 30
		else: point = None 

		if tp == 'p':
			print '\nPolynomial:\t',
			v = gu.coefgen()
			gu.plotgrid(grid, v, point, pc)

		elif tp == 'r':
			print '\nNumerator polynomial:\t',
			v1 = gu.coefgen()
			print '\nDenominator polynomial:\t',
			v2 = gu.coefgen()

			v3 = []
			for val in range(len(v1)):
				if v2[val] == 0: v3.append(None)
				else: v3.append(v1[val]/v2[val])

			gu.plotgrid(grid, v3, point, pc)

		elif tp == 'rd':
			print '\nRadical polynomial - sqrt(f(x)):\t',
			v = gu.coefgen()

			v2 = []
			for val in v:
				if val < 0: v2.append(None)
				else: v2.append(sqrt(val))
			
			gu.plotgrid(grid, v2, point, pc)

		rep = raw_input(gu.color(
		'New graph[n]/clear grid[c]/settings[s]/quit[q]: '))
		print '\n'
		if rep == 's' or rep == 'q': break
	if rep == 'q': break

print gu.color('Goodbye and thank you for using Grapher 3.5!', 1)
