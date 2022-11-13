#######################################
# POSITION
#######################################


class Position:
    def __init__(self, idx, ln, col, filename, filetext):
        self.idx = idx
        self.ln = ln
        self.col = col
        self.filename = filename
        self.filetext = filetext

    def advance(self, current):
        self.idx += 1
        self.col += 1

        if current == "\n":
            self.ln += 1
            self.col = 0

        return self

    def copy(self):
        return Position(self.idx, self.ln, self.col, self.filename, self.filetext)
