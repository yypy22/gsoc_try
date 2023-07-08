import MeCab
import sys

def go_to_tokenize(sin, sout):
    text = sin.read()
    excluded = []
    current = ""
    in_blank = False
    for i in text:
        if i == "[":
            current = ""
            in_blank = True
        elif i == "]":
            current += i
            in_blank = False
            excluded.append(current)
            current = ""
        if in_blank:
            current += i
    ##Alternative would be change setting in mecab dictionary
    ##like dont process []
    for i in range(len(excluded)):
        text = text.replace(excluded[i], "^"+str(i)+"^")
    mecab = MeCab.Tagger("-Owakati")
    token = mecab.parse(text)
    for i in range(len(excluded)):
        token = token.replace("^"+" "+str(i)+" "+"^", excluded[i])
    sout.write(token)

if __name__ == '__main__':
    go_to_tokenize(sys.stdin, sys.stdout)
