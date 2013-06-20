#!/usr/bin/python

from fltk import *
import lineanalyze as line
import graphcmd


def setopt(widget, align, value, font=None):
    widget.align(align)
    widget.value(value)
    if font is not None:
        widget.labelfont(font)


def update_eqn(widget):
    global eqn

    try:
        if widget == interbutton:
            slope, inter = float(intslope.value()), float(intinter.value())
            eqn = line.Linear('', [slope, inter])
        elif widget == pointbutton:
            y1, x1 = float(pointy1.value()), float(pointx1.value())
            eqn = line.Linear('p', [y1, float(pointslope.value()), x1])
        else:
            a, b = float(gena.value()), float(genb.value())
            eqn = line.Linear('g', [a, b, float(genc.value())])
    except:
        graph.label('Error: Check that coefficients are properly entered.')
        graph.image(None)
        graph.redraw()
        return

    if widget != interbutton:
        intslope.value(str(eqn.slope()))
        intinter.value(str(eqn.yint()))
    if widget != pointbutton:
        coefs = [str(n) for n in eqn.pointform()]
        pointy1.value(coefs[0])
        pointslope.value(coefs[1])
        pointx1.value(coefs[2])
    if widget != genbutton:
        coefs = [str(n) for n in eqn.generalform()]
        gena.value(coefs[0])
        genb.value(coefs[1])
        genc.value(coefs[2])

    if not sim:
        graphcmd.main('c')
    update_setting()
    if 'a' in graphcmd.graphs:
        graphcmd.main('f', 'b', eqn, (0, 0, 200))
    else:
        graphcmd.main('f', 'a', eqn, (200, 0, 0))
    graph.label(None)
    graph.image(Fl_PNG_Image('graph.png'))

    xinttext.value(eqn.xint())
    yinttext.value(eqn.yint())
    slopetext.value(eqn.slope())

    window.redraw()


def update_value(widget):
    try:
        valueoutput.value(eqn.val(widget.value()))
        valueoutput.redraw()
    except NameError:
        pass


def settings_window(widget):
    global setbox, setwindow

    setwindow = Fl_Window(200, 100, 375, 380, 'Linear Analysis: Settings')
    setwindow.color(fl_rgb_color(247, 247, 247))
    setwindow.begin()

    setbox = Fl_Multiline_Input(13, 10, 350, 340)
    with open('config.txt') as config:
        setbox.value(config.read())
    applybutton = Fl_Button(262, 354, 100, 20, 'Apply settings')
    applybutton.color(fl_rgb_color(230, 230, 230))
    applybutton.callback(apply_setting)

    setwindow.end()
    setwindow.show()
    Fl.run()


def apply_setting(widget):
    with open('config.txt', 'w') as config:
        config.write(setbox.value())


def update_setting():
    optdict = {5: 'xmin', 6: 'xmax', 7: 'ymin', 8: 'ymax',
               9: 'xscl', 10: 'yscl', 11: 'point', 12: 'tick',
               13: 'drawaxes', 14: 'axes', 15: 'axescolor',
               16: 'grid', 17: 'backg'}
    newopt = {}
    with open('config.txt') as config:
        lcount = 0
        for configline in config:
            if lcount >= 5:
                exec 'change = ' + configline.split(' : ')[1]
                newopt[optdict[lcount]] = change
            lcount = lcount + 1
    graphcmd.main('s', newopt)

sim = False
graphcmd.main('i', 'graph.png')
update_setting()


window = Fl_Window(200, 100, 800, 700, 'Linear Equation Analysis')
window.color(fl_rgb_color(247, 247, 247))
window.begin()

setbutton = Fl_Button(720, 7, 70, 25, 'Settings')
setbutton.color(fl_rgb_color(230, 230, 230))
setbutton.callback(settings_window)

inttext = Fl_Box(85, 10, 50, 20, 'Slope-intercept form:\t\ty = ')
intslope = Fl_Input(220, 10, 50, 20, 'x')
setopt(intslope, FL_ALIGN_RIGHT, 'm', FL_BOLD + FL_ITALIC)

intinter = Fl_Input(300, 10, 50, 20, '+ ')
setopt(intinter, FL_ALIGN_LEFT, 'b')

pointtext = Fl_Box(80, 40, 50, 20, 'Slope-point form:\t\ty - ')
pointy1 = Fl_Input(205, 40, 50, 20, ' = ')
setopt(pointy1, FL_ALIGN_RIGHT, 'y1')

bracketl = Fl_Box(310, 45, 50, 10, '(')
pointslope = Fl_Input(280, 40, 50, 20, ' x')
setopt(pointslope, FL_ALIGN_RIGHT, 'm', FL_BOLD + FL_ITALIC)

pointx1 = Fl_Input(360, 40, 50, 20, ' - ')
setopt(pointx1, FL_ALIGN_LEFT, 'x1')
bracketr = Fl_Box(390, 45, 50, 10, ')')

gentext = Fl_Box(29, 70, 50, 20, 'General form:')

gena = Fl_Input(150, 70, 50, 20, ' x')
setopt(gena, FL_ALIGN_RIGHT, 'A', FL_BOLD + FL_ITALIC)
genb = Fl_Input(235, 70, 50, 20, ' + ')
setopt(genb, FL_ALIGN_LEFT, 'B')
genc = Fl_Input(320, 70, 50, 20, ' y  + ')
setopt(genc, FL_ALIGN_LEFT, 'C')

gentextend = Fl_Box(360, 70, 50, 20, ' =  0')

interbutton = Fl_Button(450, 7, 200, 25, 'Analyze slope-intercept form')
interbutton.color(fl_rgb_color(230, 230, 230))
pointbutton = Fl_Button(450, 37, 200, 25, 'Analyze slope-point form')
pointbutton.color(fl_rgb_color(230, 230, 230))
genbutton = Fl_Button(450, 67, 200, 25, 'Analyze general form')
genbutton.color(fl_rgb_color(230, 230, 230))
interbutton.callback(update_eqn)
pointbutton.callback(update_eqn)
genbutton.callback(update_eqn)

graph = Fl_Box(25, 125, 550, 550)
graph.box(FL_BORDER_BOX)
graph.color(FL_WHITE)
graph.image(Fl_PNG_Image('graph.png'))

xinttext = Fl_Value_Output(675, 130, 90, 20, 'x-intercept\t')
xinttext.color(FL_WHITE)
yinttext = Fl_Value_Output(675, 160, 90, 20, 'y-intercept\t')
yinttext.color(FL_WHITE)
slopetext = Fl_Value_Output(675, 190, 90, 20, 'Slope\t\t')
slopetext.color(FL_WHITE)
valueinput = Fl_Value_Input(625, 250, 100, 20, 'x = ')
valueinput.value(0)
valueinput.callback(update_value)
valueoutput = Fl_Value_Output(625, 280, 100, 20, 'f(x) = ')
valueoutput.color(FL_WHITE)

window.end()
window.show()
Fl.run()
