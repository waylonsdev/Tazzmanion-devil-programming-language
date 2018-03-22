from sys import *

def open_file(filename):
    data = open(filename, "r").read()
    return data

def lex(filecontents):
    filecontents = list(filecontents)
    print(filecontents)

def run():
    data = open_file(argv[1])
    lex(data)
run()