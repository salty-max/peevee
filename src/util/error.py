#######################################
# ERRORS
#######################################


class Error:
    def __init__(self, pos_start, pos_end, name, message):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.name = name
        self.message = message

    def as_string(self):
        return f"{self.name}: {self.message}\nin {self.pos_start.filename} ({self.pos_start.ln + 1}:{self.pos_end.col})"


class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, message):
        super().__init__(pos_start, pos_end, "Illegal character", message)
