def findQuote(char, quote, esc):
    '''not meant for usage by the user'''
    return char == quote and not esc
def Tokenize(string:str, vars:dict) -> list:
    '''not meant for usage by the user'''
    Quotes = 3
    Esc = False
    Token = ""
    Tokens = []
    ind = 0
    var = ""
    string = f"{string} "
    while not ind >= len(string) - 1:
        if findQuote(string[ind], "$", Esc or Quotes == 1):
            ind += 1
            if string[ind].isalpha():
                while string[ind].isalpha():
                    var += string[ind]
                    ind += 1
                try:
                    Token += vars[var]
                except Exception:
                    print(f"Error: variable {var} does not exist")
                    return ""
                var = ""
            else:
                Token += "$"
        if findQuote(string[ind], "'", Esc or Quotes == 2):
            if Quotes == 3:
                Quotes = 1
                if Token != "":
                    Tokens.append(Token)
            else:
                Quotes = 3
                Tokens.append(Token)
            Token = ""
        elif findQuote(string[ind], '"', Esc or Quotes == 1):
            if Quotes == 3:
                Quotes = 2
                if Token != "":
                    Tokens.append(Token)
            else:
                Quotes = 3
                Tokens.append(Token)
            Token = ""
        elif string[ind].isspace() and Quotes == 3 and not Esc:
            if Token != "":
                Tokens.append(Token)
            Token = ""
        elif Esc and string[ind].lower() == "n":
            Token += "\n"
        elif (string[ind] != "\\") or (string[ind] == "\\" and Esc):
            Token  += string[ind]
        if Esc or (string[ind] == "\\" and not Esc):
            Esc = not Esc
        ind += 1
    if Quotes != 3:
        print("Error: quote left open")
        return ""
    else:
        if Token != "":
            Tokens.append(Token)
        return Tokens

def main():
    cont = True
    while cont:
        try:
            print(Tokenize(input("gsh> "), {"foo": "bar", "bar": "baz", "baz": "foo"}))
        except EOFError:
            print("^D")
            cont = False

if __name__ == "__main__":
    main()
