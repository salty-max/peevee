from src import lexer, logger

logger.greet("-------- Eevee REPL v0.1 --------")

while True:

    text = input("> ")
    result, error = lexer.run(text)

    if error:
        logger.error(error.as_string())
    else:
        logger.log(result)
