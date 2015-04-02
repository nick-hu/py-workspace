#!/usr/bin/python

import socket
from sys import path
from fltk import *

path.append('data')
import quizconfig as config

def start_quiz(widget):
    global qnum, qlist, score, healleft, hintleft, cheatleft, conn, teacher

    if qfile.value() == '':
        return
    qlist, c, dat = [], 1, []
    with open('data/' + qfile.value() + '.txt') as qdata:
        for line in qdata:
            line = line.strip()
            if c == 4:
                dat.extend([int(x) for x in line.split()])
            elif c == 5:
                qlist.append((dat[0], dat[1], dat[2], (dat[3], dat[4])))
                c, dat = 0, []
            else:
                dat.append(line)
            c = c + 1

    with open('out.txt', 'w') as out:
        out.write(str(qlist))

    if teachip.value() != '' and 'conn' not in globals():
        connip = teachip.value().split(':')
        connip[1] = int(connip[1])
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect(tuple(connip))
        teachip.value('Connected to teacher')
    teacher = True if 'conn' in globals() else False
    if teacher:
        conn.send('Student started quiz')

    health.value(config.HPMAX)
    health.maximum(config.HPMAX)
    xp.value(0)
    xp.maximum(config.XPMAX)
    prog.value(0)
    result.clear()
    health.label('HP: ' + str(int(health.value())))
    xp.label('XP: ' + str(int(xp.value())))
    prog.label(str(int(prog.value())) + '% complete')

    healleft, hintleft, cheatleft = config.HEAL, config.HINT, config.CHEAT
    heal.label('Heal:\t' + str(healleft))
    hint.label('Hint:\t' + str(hintleft))
    cheat.label('Cheat:\t' + str(cheatleft))
    qnum, score = 1, []
    update_question()


def update_question():
    if prog.value() == 100:
        frac = str(score.count(True)) + '/' + str(len(score))
        percent = int(round((score.count(True) / float(len(score))) * 100))
        corrtext = 'Correct: ' + frac + ' = ' + str(percent) + '%'
        scoretext = round(xp.value() * 10 - (config.HPMAX - health.value()))
        result.textcolor(FL_BLACK)
        result.add('')
        result.add('~ End of Quiz ~')
        result.add('Results:')
        result.add(corrtext)
        result.add('Score: ' + str(int(scoretext)))
        result.redraw()
        if teacher:
            conn.send('Student finished:' + corrtext + '\n' + scoretext)
        return

    with open('data/question.html') as qhtml:
        text = qhtml.readlines()
    text[-3] = '<h6>' + qlist[qnum-1][0] + '</h6>\n'
    with open('data/question.html', 'w') as qhtml:
        qhtml.writelines(text)
    quizwin.load('data/question.html')
    win.redraw()


def submit_answer(widget):
    global qnum

    if prog.value() == 100 or health.value() <= 0:
        return

    correct = eval('ans.value().lower() == qlist[qnum-1][2]')
    score.append(correct)
    xp.value(xp.value() + qlist[qnum-1][3][1])
    result.clear()
    if correct:
        regen = config.REGEN
        health.value(health.value() + int(regen * (qlist[qnum-1][3][0])))
        result.textcolor(fl_rgb_color(50, 130, 50))
        result.add('Correct!')
    else:
        health.value(health.value() - qlist[qnum-1][3][0])
        result.textcolor(fl_rgb_color(220, 75, 60))
        result.add('Incorrect!')
        result.add('The answer was: ' + qlist[qnum-1][2])
    
    if health.value() <= 0:
        health.value(0)
        result.add('\nYou have no more health!')
        result.add('\nHeal or press Start to restart.')
        if teacher:
            conn.send('Student ran out of health!')
    if health.value() > config.HPMAX:
        health.value(config.HPMAX)
    if xp.value() < 0:
        xp.value(0)

    health.label('HP: ' + str(int(health.value())))
    xp.label('XP: ' + str(int(xp.value())))
    prog.value(int(round((float(qnum) / len(qlist)) * 100)))
    prog.label(str(int(prog.value())) + '% complete')

    if teacher:
        status = 'Correct' if correct else 'Incorrect'
        info = {'Health': health.value(), 'XP': xp.value(),
                'Progress': prog.value(), 'Heals left': healleft,
                'Hints left': hintleft, 'Cheats left': cheatleft}
        data = qlist[qnum-1][0]+'\n'+ans.value()+'\n'+status+'\n'+str(info)
        conn.send(data)

    ans.value('')
    qnum = qnum + 1
    update_question()
    win.redraw()


def heal_cb(widget):
    global healleft

    if health.value() == config.HPMAX or prog.value() == 100:
        return
    if 'healleft' not in globals():
        return

    if healleft > 0:
        health.value(health.value() + config.HEALAMOUNT)
        healleft = healleft - 1
        health.label('HP: ' + str(int(health.value())))
        heal.label('Heal:\t' + str(healleft))
        heal.redraw()
        health.redraw()


def hint_cb(widget):
    global hintleft

    if prog.value() == 100 or 'qlist' not in globals():
        return
    if qlist[qnum-1][1] == result.text(2):  # If hint has just been used
        return

    if hintleft > 0:
        result.textcolor(fl_rgb_color(200, 150, 0))
        result.clear()
        result.add('Hint:')
        result.add(qlist[qnum-1][1])  # Display hint in result box
        hintleft = hintleft - 1
        hint.label('Hint:\t' + str(hintleft))
        hint.redraw()
        result.redraw()


def cheat_cb(widget):
    global cheatleft

    if prog.value() == 100 or 'qlist' not in globals():
        return
    if qlist[qnum-1][2] == ans.value():  # If cheat has just been used
        return

    if cheatleft > 0:
        ans.value(qlist[qnum-1][2])  # Put answer in answer box
        cheatleft = cheatleft - 1
        cheat.label('Cheat:\t' + str(cheatleft))
        cheat.redraw()
        ans.redraw()

win = Fl_Window(100, 100, 600, 425, 'Quizzer')
win.color(fl_rgb_color(39, 40, 34))
win.begin()
quizwin = Fl_Help_View(10, 10, 580, 200)

ans = Fl_Input(70, 220, 100, 25, 'Answer: ')
ans.labelcolor(FL_WHITE)
submit = Fl_Button(180, 220, 75, 25, 'Submit')
submit.color(fl_rgb_color(71, 182, 66), fl_rgb_color(71, 182, 66))
submit.callback(submit_answer)
result = Fl_Browser(10, 260, 244, 150)

qfile = Fl_Input(440, 338, 150, 25, 'Quiz file')
qfile.align(FL_ALIGN_TOP)
qfile.labelcolor(FL_WHITE)

teachip = Fl_Input(440, 385, 150, 25, 'Teacher IP')
teachip.align(FL_ALIGN_TOP)
teachip.labelcolor(FL_WHITE)

health = Fl_Progress(390, 220, 200, 25)
health.color(fl_rgb_color(255, 210, 210), fl_rgb_color(210, 0, 0))
xp = Fl_Progress(390, 255, 200, 25)
xp.color(fl_rgb_color(210, 255, 210), fl_rgb_color(0, 170, 60))
prog = Fl_Progress(390, 290, 200, 25)
prog.color(fl_rgb_color(255, 255, 125), fl_rgb_color(235, 195, 25))

heal = Fl_Button(280, 220, 75, 25)
heal.color(fl_rgb_color(250, 175, 225), fl_rgb_color(250, 175, 225))
heal.callback(heal_cb)
hint = Fl_Button(280, 255, 75, 25)
hint.color(fl_rgb_color(255, 215, 50), fl_rgb_color(255, 215, 50))
hint.callback(hint_cb)
cheat = Fl_Button(280, 290, 75, 25)
cheat.color(fl_rgb_color(140, 170, 255), fl_rgb_color(140, 170, 255))
cheat.callback(cheat_cb)

start = Fl_Button(280, 350, 75, 60, 'Start/\nRestart\nQuiz')
start.color(fl_rgb_color(71, 182, 66), fl_rgb_color(71, 182, 66))
start.callback(start_quiz)

win.end()
win.show()
Fl.scheme('gtk+')
Fl.run()

if teacher:  # Send connection end signal to teacher
    conn.send('quit')
    conn.close()
