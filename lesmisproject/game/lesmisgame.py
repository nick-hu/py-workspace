#!/usr/bin/python

import webbrowser as web
import utils

while True:

	print '\033[2J'
	for flagline in range(5):
		print '\t' * 4 + '\033[44m     \033[47m     \033[41m     \033[0m'
	print '\n\t\t\033[31;1mLes Miserables: A text-based adventure game\033[0m'
	print '''\n
	O   \t   O  \t\t\t  O                       O
	T o \t   T  \t\t\t  T|"     "    "    ##  "|V
	^ ^ \t   ^  \t\t\t  ^                 ##    ^ \n\n'''
	print '''
	\t\t===============================
	\t\t          NICHOLAS HU
	\t\t   English 9 Challenge, 1-4
	\t\t=============================== 
	\t\t            v. 1.0             \n\n'''

	ask = 'Play [p] / Instructions [i] / Website [w] / Quit[q]: '
	q = raw_input(utils.color(ask, 33, 1))

	if q == 'i':
		print '\033[2J'
		print utils.color('\nINSTRUCTIONS:', 36, 1)
		print '''
In this game, you will be faced with several scenarios.
For each one, you will have multiple choices.
Type the appropriate letter and enter to select an option.
Each option will lead to another scenario.

Your character also has attributes which will be displayed:
Health points (HP), Experience (XP), and Money - in francs (F).
Each option may also have effects on these attributes.
A small amount of luck/chance is also a factor!
Be careful! 0 HP will result in instant death and
less than 0 F for 3 turns in a row will also lead to death.

Upon death (loss) or victory, your score will be calculated based on
these attributes, primarily XP.'''
		stall = raw_input('\n' * 6 + '(Press enter to return to title)')

	elif q == 'w': web.open('http://lesmisgame.weebly.com/index.html')

	elif q == 'p':
		choices = [('A', 31), ('B', 33), ('C', 32), ('D', 36)] # Choice colors
		index = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
		hp, xp, fr = 75, 0, 5 # Estimate 1 F = $10
		debtcount = 0 # Debt counter (debt for 3 turns = death)
		scid = '1' # Scene ID

		while True:
			print '\033[2J'

			hpdisp = utils.color('\t\tHP: ' + str(hp) + '/100', 31, 1)
			frdisp = utils.color('\t' * 2 + str(fr) + ' F', 33, 1)
			xpdisp = utils.color('\t' * 2 + 'XP: ' + str(xp), 32, 1)
			
			if hp == 0 or debtcount == 3: 
				gamestate = 'l'
				break
			if 'w' in scid: 
				gamestate = 'w'
				break

			print hpdisp + frdisp + xpdisp + '\n\n\n' # Status display
			
			print utils.scenes[scid][0] + '\n\n'
			col = 0
			for opt in utils.scenes[scid][1]: # Options
				let, letcol = choices[col][0], choices[col][1]
				print utils.color(let + '. ' + opt[0] + '\n', letcol, 1)
				col = col + 1

			while True:
				query = raw_input('\nAction [A/B/C/D]: ').upper()
				if query in 'ABCD' and len(query) == 1: break

			act = utils.scenes[scid][1][index[query]][1]
			hp = hp + utils.chance(act[0], act[3])
			fr = fr + utils.chance(act[1], act[4])
			xp = xp + utils.chance(act[2], act[5])
			scid = act[6]

			if fr <= 0: debtcount = debtcount + 1
			else: debtcount = 0
			if hp > 100: hp = 100
			if hp < 0: hp = 0

		score = xp + hp + fr
		print '\033[2J'
		print hpdisp + frdisp + xpdisp + '\n\n\n'

		if gamestate == 'l':
			print '\t' * 4 + '~~~~~~~~~~'
			for l in range(6): 
				if l == 1: print '\t' * 4 + '| R.I.P. |'
				else: print '\t' * 4 + '|        |'			
			print '\t' * 4 + '~~~~~~~~~~'
			print utils.color('\n\n\t\t\t   Game over: YOU LOSE!\n\n', 31)

		else:
			print utils.winscenes[scid]
			print utils.color('\n\n\t\t\t\t~ THE END ~\n\n', 33, 1)

		print utils.color('\t' * 4 + 'Score: ' + str(score), 32)
		stall = raw_input('\n' * 4 + '(Press enter to return to title)')
	
	elif q == 'q': break