from src.util import logger
from src.core import lexer

logger.greet("-------- Eevee REPL v0.1 --------")

while True:

    text = input("> ")
    result, error = lexer.run("<stdin>", text)

    if error:
        logger.error(error.as_string())
    else:
        logger.log(result)
