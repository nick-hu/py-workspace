#!/usr/bin/python

HEAL = 1 
HEALAMOUNT =  10
HINT = 3 
CHEAT = 1 

HPMAX = 100 
REGEN = 10 
XPMAX = 1000 

if __name__ == '__main__':
    with open('quizconfig.py', 'r+') as qconfig:
        old = qconfig.readlines()
        print 'Current settings:\n' + '=' * 17
        print 'Heals:', HEAL, '\nHeal amount:', HEALAMOUNT
        print 'Hints:', HINT, '\nCheats:', CHEAT
        print 'Maximum HP:', HPMAX, '\nRegeneration factor:', REGEN
        print 'Maximum XP:', XPMAX, '\n\n'

        print 'New settings:\n' + '=' * 13
        newheal = raw_input('Heals: ')
        old[2] = 'HEAL = ' + newheal + '\n'
        newhealamount = raw_input('Heal amount: ')
        old[3] = 'HEALAMOUNT = ' + newhealamount + '\n'
        newhint = raw_input('Hints: ')
        old[4] = 'HINT = ' + newhint + '\n'
        newcheat = raw_input('Cheats: ')
        old[5] = 'CHEAT = ' + newcheat + '\n'
        newhp = raw_input('Maximum HP: ')
        old[7] = 'HPMAX = ' + newhp + '\n'
        newregen = raw_input('Regeneration factor: ')
        old[8] = 'REGEN = ' + newregen + '\n'
        newxp = raw_input('Maximum XP: ')
        old[9] = 'XPMAX = ' + newxp + '\n'

        qconfig.seek(0)
        qconfig.writelines(old)

    raw_input('\nSettings saved, press return to exit')
