#######################################
# CONSTANTS
#######################################

DIGITS = "0123456789"

#######################################
# ERRORS
#######################################


class Error:
    def __init__(self, name, message):
        self.name = name
        self.message = message

    def as_string(self):
        return f"{self.name}: {self.message}"


class IllegalCharError(Error):
    def __init__(self, message):
        super().__init__("Illegal character", message)


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
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.line = 1
        self.current = None
        self.advance()

    def advance(self):
        self.pos += 1
        self.current = self.text[self.pos] if self.pos < len(self.text) else None

    def make_tokens(self):
        tokens = []

        while self.current is not None:
            if self.current in " \t\r":
                self.advance()
            elif self.current == "\n":
                self.line += 1
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
                char = self.current
                self.advance()
                return [], IllegalCharError(f"'{char}' at ({self.line}:{self.pos})")

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


def run(text):
    lexer = Lexer(text)
    tokens, error = lexer.make_tokens()
    return tokens, error
