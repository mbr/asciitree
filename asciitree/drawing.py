from .util import KeyArgsConstructor

BOX_LIGHT = {
    'UP_AND_RIGHT': u'\u2514',
    'HORIZONTAL': u'\u2500',
    'VERTICAL': u'\u2502',
    'VERTICAL_AND_RIGHT': u'\u251C',
}


BOX_HEAVY = {
    'UP_AND_RIGHT': u'\u2517',
    'HORIZONTAL': u'\u2501',
    'VERTICAL': u'\u2503',
    'VERTICAL_AND_RIGHT': u'\u2523',
}


BOX_DOUBLE = {
    'UP_AND_RIGHT': u'\u255A',
    'HORIZONTAL': u'\u2550',
    'VERTICAL': u'\u2551',
    'VERTICAL_AND_RIGHT': u'\u2560',
}


BOX_ASCII = {
    'UP_AND_RIGHT': u'+',
    'HORIZONTAL': u'-',
    'VERTICAL': u'|',
    'VERTICAL_AND_RIGHT': u'+',
}


BOX_BLANK = {
    'UP_AND_RIGHT': u' ',
    'HORIZONTAL': u' ',
    'VERTICAL': u' ',
    'VERTICAL_AND_RIGHT': u' ',
}


class Draw(KeyArgsConstructor):
    label_format = '{}'

    def node_label(self, text):
        return self.label_format.format(text)

    def child_head(self, label):
        return label

    def child_tail(self, line):
        return line

    def last_child_head(self, label):
        return label

    def last_child_tail(self, line):
        return line


class BoxDraw(Draw):
    gfx = BOX_ASCII
    label_space = 1
    horiz_len = 2
    indent = 1

    def child_head(self, label):
        return (' ' * self.indent
                + self.gfx['VERTICAL_AND_RIGHT']
                + self.gfx['HORIZONTAL'] * self.horiz_len
                + ' ' * self.label_space
                + label)

    def child_tail(self, line):
        return (' ' * self.indent
                + self.gfx['VERTICAL']
                + ' ' * self.horiz_len
                + line)

    def last_child_head(self, label):
        return (' ' * self.indent
                + self.gfx['UP_AND_RIGHT']
                + self.gfx['HORIZONTAL'] * self.horiz_len
                + ' ' * self.label_space
                + label)

    def last_child_tail(self, line):
        return (' ' * self.indent
                + ' ' * len(self.gfx['VERTICAL'])
                + ' ' * self.horiz_len
                + line)
