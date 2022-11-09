def read_tokens():
    with open("Tokens.in") as tokensFile:
        return [line.rstrip('\n') for line in tokensFile]