from src.util.position import Position
from src.util.error import IllegalCharError

#######################################
# CONSTANTS
#######################################

DIGITS = "0123456789"

#######################################
# TOKENS
#######################################

TT_INT = "INT"
TT_FLOAT = "FLOAT"
TT_PLUS = "PLUS"
TT_MINUS = "MINUS"
TT_MUL = "MUL"
TT_DIV = "DIV"
TT_MOD = "MOD"
TT_LPAREN = "LPAREN"
TT_RPAREN = "RPAREN"


class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value:
            return f"{self.type}:{self.value}"
        return f"{self.type}"


#######################################
# LEXER
#######################################


class Lexer:
    def __init__(self, filename, text):
        self.filename = filename
        self.text = text
        self.pos = Position(-1, 0, -1, filename, text)
        self.current = None
        self.advance()

    def advance(self):
        self.pos.advance(self.current)
        self.current = (
            self.text[self.pos.idx] if self.pos.idx < len(self.text) else None
        )

    def make_tokens(self):
        tokens = []

        while self.current is not None:
            if self.current in " \t\r":
                self.advance()
            elif self.current == "+":
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current == "-":
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.current == "*":
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.current == "/":
                tokens.append(Token(TT_DIV))
                self.advance()
            elif self.current == "%":
                tokens.append(Token(TT_MOD))
                self.advance()
            elif self.current == "(":
                tokens.append(Token(TT_LPAREN))
                self.advance()
            elif self.current == ")":
                tokens.append(Token(TT_RPAREN))
                self.advance()
            elif self.current in DIGITS:
                tokens.append(self.make_number())
            else:
                pos_start = self.pos.copy()
                char = self.current
                self.advance()
                return [], IllegalCharError(pos_start, self.pos, f"{char}")

        return tokens, None

    def make_number(self):
        num_str = ""
        dot_count = 0

        while self.current is not None and self.current in DIGITS + ".":
            if self.current == ".":
                if dot_count == 1:
                    break
                dot_count += 1
                num_str += "."
            else:
                num_str += self.current

            self.advance()

        if dot_count == 0:
            return Token(TT_INT, int(num_str))
        return Token(TT_FLOAT, float(num_str))


#######################################
# RUN
#######################################


def run(filename, text):
    lexer = Lexer(filename, text)
    tokens, error = lexer.make_tokens()
    return tokens, error
