#!/usr/bin/python

print 'Scorekeeper 1.0'

while True:
    winsc = raw_input('\nScore needed to win (enter to skip): ')
    players = []

    print '\nEnter player names in order (enter to finish)\n'
    while True:
        player = raw_input('Enter player name: ')
        if player == '':
            break
        else:
            players.append(player)

    scores = [0 for player in players]

    if winsc == '':
        print '\nStart playing (to end type "end")\n'
        n = 0

        while True:
            name = players[n]
            score = raw_input(name + "'s turn. Points earned: ")

            if score == 'end':
                break
            else:
                scores[n] = scores[n] + int(score)

            if n == len(players)-1:
                print '\nCurrent scores:'
                for x in range(0, len(players)):
                    print players[x] + "'s score:", scores[x]
                print '\n'

            n = n + 1
            if n == len(players):
                n = 0

        print '\nGame ended!\n'

        for x in range(0, len(players)):
            print players[x] + "'s score:", scores[x]

        if scores.count(max(scores)) == 1:
            print ('\n' + players[scores.index(max(scores))],
                   'wins with a score of:', max(scores))

        else:
            tie, tval = [], max(scores)
            for s in scores:
                if s == tval:
                    tie.append(players[scores.index(max(scores))])
                    players.remove(players[scores.index(max(scores))])
            print ('\nTie between', ', '.join(tie),
                   'with a score of:', max(scores))

    else:
        winsc, n = int(winsc), 0
        print '\nStart playing\n'

        while True:
            name = players[n]
            score = int(raw_input(name + "'s turn. Points earned: "))

            scores[n] = scores[n] + score
            if scores[n] >= winsc:
                break

            if n == len(players) - 1:
                print '\nCurrent scores:'
                for x in range(0, len(players)):
                    print players[x] + ':', scores[x]
                print '\n'

            n = n + 1
            if n == len(players):
                n = 0

        print '\nGame ended!\n'

        print 'Final scores:'
        for x in range(0, len(players)):
            print players[x] + ':', scores[x]

        print ('\n' + players[scores.index(max(scores))],
               'wins with a score of:', max(scores))

    rep = raw_input('\nNew game (y/n)?: ')
    if rep == 'y':
        continue
    break
