#!/usr/bin/python

from fltk import *
import lineanalyze as line
import graphcmd


def update_eqn(widget):
    global eqn

    try:
        if widget in [finterbutton, fpointbutton, fgenbutton]:
            if widget == finterbutton:
                slope, inter = fintslope.value(), fintinter.value()
                eqn = line.Linear('', [slope, inter])
            elif widget == fpointbutton:
                y1, x1 = fpointy1.value(), fpointx1.value()
                eqn = line.Linear('p', [y1, fpointslope.value(), x1])
            else:
                a, b, c = fgena.value(), fgenb.value(), fgenc.value()
                eqn = line.Linear('g', [a, b, c])
        else:
            if widget == ginterbutton:
                slope, inter = gintslope.value(), gintinter.value()
                eqn = line.Linear('', [slope, inter])
            elif widget == gpointbutton:
                y1, x1 = gpointy1.value(), gpointx1.value()
                eqn = line.Linear('p', [y1, gpointslope.value(), x1])
            else:
                a, b, c = ggena.value(), ggenb.value(), ggenc.value()
                eqn = line.Linear('g', [a, b, c])
    except:
        graph.label('Error: Check that coefficients are properly entered.')
        graph.image(None)
        graph.redraw()
        return

    if widget in [finterbutton, fpointbutton, fgenbutton]:
        fxinttext.value(eqn.xint())
        fyinttext.value(eqn.yint())
        fslopetext.value(eqn.slope())
        if widget != finterbutton:
            fintslope.value(str(eqn.slope()))
            fintinter.value(str(eqn.yint()))
        if widget != fpointbutton:
            coefs = [str(n) for n in eqn.pointform()]
            fpointy1.value(coefs[0])
            fpointslope.value(coefs[1])
            fpointx1.value(coefs[2])
        if widget != fgenbutton:
            coefs = [str(n) for n in eqn.generalform()]
            fgena.value(coefs[0])
            fgenb.value(coefs[1])
            fgenc.value(coefs[2])
    else:
        gxinttext.value(eqn.xint())
        gyinttext.value(eqn.yint())
        gslopetext.value(eqn.slope())
        if widget != ginterbutton:
            gintslope.value(str(eqn.slope()))
            gintinter.value(str(eqn.yint()))
        if widget != gpointbutton:
            coefs = [str(n) for n in eqn.pointform()]
            gpointy1.value(coefs[0])
            gpointslope.value(coefs[1])
            gpointx1.value(coefs[2])
        if widget != ggenbutton:
            coefs = [str(n) for n in eqn.generalform()]
            ggena.value(coefs[0])
            ggenb.value(coefs[1])
            ggenc.value(coefs[2])

    update_setting()
    if widget in [finterbutton, fpointbutton, fgenbutton]:
        graphcmd.graphs['f'] = (eqn, flinecolor)
    else:
        graphcmd.graphs['g'] = (eqn, glinecolor)
    graphcmd.main('s', graphcmd.opt)
    graph.label(None)
    graph.image(Fl_PNG_Image('graph.png'))

    if len(graphcmd.graphs) == 2:
        eqna, eqnb = graphcmd.graphs['f'][0], graphcmd.graphs['g'][0]
        solution.value(str(line.LinearSystem(eqna, eqnb).xint()))

    window.redraw()


def update_value(widget):
    if 'f' in graphcmd.graphs:
        fvalueoutput.value(graphcmd.graphs['f'][0].val(widget.value()))
        fvalueoutput.redraw()
    if 'g' in graphcmd.graphs:
        gvalueoutput.value(graphcmd.graphs['g'][0].val(widget.value()))
        gvalueoutput.redraw()


def clear_func(widget):
    global eqns

    try:
        if widget == clearf:
            del graphcmd.graphs['f']
            graphcmd.main('s', graphcmd.opt)
            for widget in [fxinttext, fyinttext, fslopetext, fvalueoutput]:
                widget.value(0)
        else:
            del graphcmd.graphs['g']
            graphcmd.main('s', graphcmd.opt)
            for widget in [gxinttext, gyinttext, gslopetext, gvalueoutput]:
                widget.value(0)
    except KeyError:
        pass
    graph.image(Fl_PNG_Image('graph.png'))
    window.redraw()


def settings_window(widget):
    global setbox, setwindow

    setwindow = Fl_Window(200, 100, 400, 380, 'Linear Analysis: Settings')
    setwindow.color(fl_rgb_color(247, 247, 247))
    setwindow.begin()

    setbox = Fl_Multiline_Input(13, 10, 375, 340)
    with open('config.txt') as config:
        setbox.value(config.read())
    applybutton = Fl_Button(287, 354, 100, 20, 'Apply settings')
    applybutton.color(fl_rgb_color(230, 230, 230))
    applybutton.callback(apply_setting)

    setwindow.end()
    setwindow.show()
    Fl.run()


def apply_setting(widget):
    with open('config.txt', 'w') as config:
        config.write(setbox.value())


def update_setting():
    global flinecolor, glinecolor

    optdict = {7: 'xmin', 8: 'xmax', 9: 'ymin', 10: 'ymax',
               11: 'xscl', 12: 'yscl', 13: 'point', 14: 'tick',
               15: 'drawaxes', 16: 'axes', 17: 'axescolor',
               18: 'grid', 19: 'backg'}
    newopt = {}
    with open('config.txt') as config:
        lcount = 0
        for configline in config:
            if lcount == 5:
                colortup = configline.split(' : ')[1]
                exec('flinecolor = ' + colortup, globals())
            elif lcount == 6:
                colortup = configline.split(' : ')[1]
                exec('glinecolor = ' + colortup, globals())
            elif lcount >= 7:
                exec('change = ' + configline.split(' : ')[1])
                newopt[optdict[lcount]] = change
            lcount = lcount + 1
    graphcmd.main('s', newopt)


def setopt(widget, align, value, font=None):
    widget.align(align)
    widget.value(value)
    if font is not None:
        widget.labelfont(font)


graphcmd.main('i', 'graph.png')
update_setting()


window = Fl_Window(50, 50, 1250, 671, 'Linear Equation Analysis')
window.color(fl_rgb_color(247, 247, 247))
window.begin()

setbutton = Fl_Button(1160, 635, 80, 25, 'Settings')
setbutton.color(fl_rgb_color(230, 230, 230))
setbutton.callback(settings_window)

fxtext = Fl_Box(589, 20, 0, 0, 'f(x)')
fxtext.labelfont(FL_BOLD)

finttext = Fl_Box(637, 40, 50, 20, 'Slope-intercept form:\ty = ')
fintslope = Fl_Input(759, 40, 50, 20, 'x')
setopt(fintslope, FL_ALIGN_RIGHT, 'm', FL_BOLD + FL_ITALIC)

fintinter = Fl_Input(839, 40, 50, 20, '+ ')
setopt(fintinter, FL_ALIGN_LEFT, 'b')

fpointtext = Fl_Box(632, 69, 50, 20, 'Slope-point form:\ty - ')
fpointy1 = Fl_Input(759, 69, 50, 20, ' = ')
setopt(fpointy1, FL_ALIGN_RIGHT, 'y1')

fbracketl = Fl_Box(869, 73, 50, 10, '(')
fpointslope = Fl_Input(839, 69, 50, 20, ' x')
setopt(fpointslope, FL_ALIGN_RIGHT, 'm', FL_BOLD + FL_ITALIC)

fpointx1 = Fl_Input(919, 69, 50, 20, ' - ')
setopt(fpointx1, FL_ALIGN_LEFT, 'x1')
fbracketr = Fl_Box(949, 73, 50, 10, ')')

fgentext = Fl_Box(597, 98, 50, 20, 'General form:')
fgena = Fl_Input(759, 98, 50, 20, 'x')
setopt(fgena, FL_ALIGN_RIGHT, 'A', FL_BOLD + FL_ITALIC)
fgenb = Fl_Input(839, 98, 50, 20, '+ ')
setopt(fgenb, FL_ALIGN_LEFT, 'B')
fgenc = Fl_Input(919, 98, 50, 20, 'y + ')
setopt(fgenc, FL_ALIGN_LEFT, 'C')
fgentextend = Fl_Box(960, 98, 50, 20, ' =  0')

gxtext = Fl_Box(590, 140, 0, 0, 'g(x)')
gxtext.labelfont(FL_BOLD)

ginttext = Fl_Box(637, 160, 50, 20, 'Slope-intercept form:\ty = ')
gintslope = Fl_Input(759, 160, 50, 20, 'x')
setopt(gintslope, FL_ALIGN_RIGHT, 'm', FL_BOLD + FL_ITALIC)

gintinter = Fl_Input(839, 160, 50, 20, '+ ')
setopt(gintinter, FL_ALIGN_LEFT, 'b')

gpointtext = Fl_Box(632, 189, 50, 20, 'Slope-point form:\ty - ')
gpointy1 = Fl_Input(759, 189, 50, 20, ' = ')
setopt(gpointy1, FL_ALIGN_RIGHT, 'y1')

gbracketl = Fl_Box(869, 193, 50, 10, '(')
gpointslope = Fl_Input(839, 189, 50, 20, ' x')
setopt(gpointslope, FL_ALIGN_RIGHT, 'm', FL_BOLD + FL_ITALIC)

gpointx1 = Fl_Input(919, 189, 50, 20, ' - ')
setopt(gpointx1, FL_ALIGN_LEFT, 'x1')
gbracketr = Fl_Box(949, 193, 50, 10, ')')

ggentext = Fl_Box(597, 218, 50, 20, 'General form:')
ggena = Fl_Input(759, 218, 50, 20, 'x')
setopt(ggena, FL_ALIGN_RIGHT, 'A', FL_BOLD + FL_ITALIC)
ggenb = Fl_Input(839, 218, 50, 20, '+ ')
setopt(ggenb, FL_ALIGN_LEFT, 'B')
ggenc = Fl_Input(919, 218, 50, 20, 'y + ')
setopt(ggenc, FL_ALIGN_LEFT, 'C')
ggentextend = Fl_Box(960, 218, 50, 20, ' =  0')

finterbutton = Fl_Button(1015, 35, 225, 25, 'Analyze slope-intercept form')
finterbutton.color(fl_rgb_color(230, 230, 230))
fpointbutton = Fl_Button(1015, 65, 225, 25, 'Analyze slope-point form')
fpointbutton.color(fl_rgb_color(230, 230, 230))
fgenbutton = Fl_Button(1015, 95, 225, 25, 'Analyze general form')
fgenbutton.color(fl_rgb_color(230, 230, 230))
finterbutton.callback(update_eqn)
fpointbutton.callback(update_eqn)
fgenbutton.callback(update_eqn)

ginterbutton = Fl_Button(1015, 155, 225, 25, 'Analyze slope-intercept form')
ginterbutton.color(fl_rgb_color(230, 230, 230))
gpointbutton = Fl_Button(1015, 185, 225, 25, 'Analyze slope-point form')
gpointbutton.color(fl_rgb_color(230, 230, 230))
ggenbutton = Fl_Button(1015, 215, 225, 25, 'Analyze general form')
ggenbutton.color(fl_rgb_color(230, 230, 230))
ginterbutton.callback(update_eqn)
gpointbutton.callback(update_eqn)
ggenbutton.callback(update_eqn)

graph = Fl_Box(9, 9, 550, 550)
graph.box(FL_BORDER_BOX)
graph.color(FL_WHITE)
graph.image(Fl_PNG_Image('graph.png'))


fxinttext = Fl_Value_Output(159, 570, 90, 20, 'f(x) x-intercept\t')
fxinttext.color(FL_WHITE)
fyinttext = Fl_Value_Output(159, 600, 90, 20, 'f(x) y-intercept\t')
fyinttext.color(FL_WHITE)
fslopetext = Fl_Value_Output(159, 630, 90, 20, 'f(x) Slope\t\t')
fslopetext.color(FL_WHITE)
valueinput = Fl_Value_Input(625, 300, 100, 20, 'x = ')
valueinput.value(0)
valueinput.callback(update_value)
fvalueoutput = Fl_Value_Output(625, 330, 100, 20, 'f(x) = ')
fvalueoutput.color(FL_WHITE)

gxinttext = Fl_Value_Output(450, 570, 90, 20, 'g(x) x-intercept\t')
gxinttext.color(FL_WHITE)
gyinttext = Fl_Value_Output(450, 600, 90, 20, 'g(x) y-intercept\t')
gyinttext.color(FL_WHITE)
gslopetext = Fl_Value_Output(450, 630, 90, 20, 'g(x) Slope\t\t')
gslopetext.color(FL_WHITE)
gvalueoutput = Fl_Value_Output(625, 360, 100, 20, 'g(x) = ')
gvalueoutput.color(FL_WHITE)

solution = Fl_Output(775, 330, 150, 20, 'Solution of f(x) = g(x)')
solution.cursor_color(FL_WHITE)
setopt(solution, FL_ALIGN_TOP, '')
clearf = Fl_Button(975, 312, 100, 25, 'Clear f(x)')
clearf.color(fl_rgb_color(230, 230, 230))
clearf.callback(clear_func)
clearg = Fl_Button(975, 342, 100, 25, 'Clear g(x)')
clearg.color(fl_rgb_color(230, 230, 230))
clearg.callback(clear_func)


window.end()
window.show()
Fl.scheme('gtk+')
Fl.run()
