#!/usr/bin/env python

from random import randrange as rrange

from fltk import *


class ColourSort(Fl_Window):
    def __init__(self):

        super(self.__class__, self).__init__(800, 685, "Colour Sort")
        self.color(fl_rgb_color(34, 34, 34))
        self.begin()

        self.buttons = []
        for y in xrange(18):
            hsl_values = range(y * 20, y * 20 + 20)
            for x in xrange(20):

                but = Fl_Button(x * 35 + 30, y * 35 + 30, 30, 30)

                if x == 0 or x == 19:
                    curr_color = hsl_values.pop(0)
                    boxtype = FL_FLAT_BOX
                else:
                    curr_color = hsl_values.pop(rrange(0, len(hsl_values) - 1))
                    boxtype = FL_DOWN_BOX
                    but.callback(self.swap, (x, y))

                bcolor = fl_rgb_color(*self.hsl_rgb(curr_color, 0.5, 0.5))
                but.color(bcolor)
                but.box(boxtype)
                self.buttons.append([but, (x, y), curr_color])

        check_but = Fl_Button(740, 30, 50, 30, "Check")
        check_but.color(fl_rgb_color(80, 160, 0), fl_rgb_color(80, 160, 0))
        check_but.callback(self.check)

        self.selected = []

        self.end()
        self.show()

    def swap(self, but, pos):
        if len(self.selected) < 2:
            if len(self.selected) == 1:
                if pos[1] == self.selected[0][1][1]:
                    self.selected.append((but, pos))
                else:
                    return
            else:
                self.selected.append((but, pos))
            but.box(FL_EMBOSSED_BOX)

        if len(self.selected) == 2:
            b1, b2 = self.selected[0][0], self.selected[1][0]
            c1, c2 = b1.color(), b2.color()
            b1.color(c2)
            b2.color(c1)
            for but in (b1, b2):
                but.box(FL_DOWN_BOX)

            for i, but in enumerate(self.buttons):
                if but[0] == b1:
                    b1index = i
                if but[0] == b2:
                    b2index = i
            b1hue, b2hue = self.buttons[b1index][2], self.buttons[b2index][2]
            self.buttons[b1index][2] = b2hue
            self.buttons[b2index][2] = b1hue
            self.redraw()
            self.selected = []

    def check(self, wid):
        score = 0
        for but, pos, buthue in self.buttons:
            hue = pos[1] * 20 + pos[0]
            if hue != buthue:
                but.label(str(buthue))
            else:
                but.box(FL_FLAT_BOX)
                score += 1
            but.redraw()
            if pos[0] != 0 and pos[0] != 19:
                but.callback(lambda but, pos: None)

        fl_alert("Score: {0}/324".format(score - 36))

    @staticmethod
    def hsl_rgb(h, s, l):
        C = (1 - abs(2*l - 1)) * s
        H = h / 60.0
        X = C * (1 - abs(H % 2 - 1))

        rgb = [[C, X, 0], [X, C, 0], [0, C, X],
               [0, X, C], [X, 0, C], [C, 0, X]][int(H)]
        return [int(round(255 * (v + (l - 0.5*C)), 0)) for v in rgb]


def main():
    win = ColourSort()

    Fl.scheme("gtk+")
    Fl.run()

if __name__ == "__main__":
    main()
