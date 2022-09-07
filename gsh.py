def findQuote(char, quote, inQuotes, esc):
    '''not meant for usage by the user'''
    if char == quote and not esc:
        return not inQuotes
def Tokenize(string):
    '''not meant for usage by the user'''
    Quotes = 3
    Esc = False
    Token = ""
    Tokens = {}
    for char in list(string):
        if findQuote(char, "'", False, Esc or Quotes == 3):
            if Quotes == 3:
                Quotes = 1
                if Token != "":
                    Tokens[len(Tokens) + 1] = [Token, False]
            else:
                Quotes = 3
                Tokens[len(Tokens) + 1] = [f"'{Token}'", True]
            Token = ""
        elif findQuote(char, '"', False, Esc or Quotes == 1):
            if Quotes == 3:
                Quotes = 2
                if Token != "":
                    Tokens[len(Tokens) + 1] = [Token, False]
            else:
                Quotes = 3
                Tokens[len(Tokens) + 1] = [f'"{Token}"', True]
            Token = ""
        elif char.isspace() and Quotes == 3 and not Esc:
            if Token != "":
                Tokens[len(Tokens) + 1] = [Token, False]
            Token = ""
        elif (char != "\\") or (char == "\\" and Esc):
            Token  += char
        if Esc or (char == "\\" and not Esc):
            Esc = not Esc
    if Quotes != 3:
        return ""
    else:
        if Token != "":
            Tokens[len(Tokens) + 1] = [Token, False]
        return Tokens

def main():
    cont = True
    while cont:
        try:
            print(Tokenize(input("gsh> ")))
        except EOFError:
            print("^D")
            cont = False

if __name__ == "__main__":
    main()
