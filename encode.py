import argparse
import random

def argument_sys():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type = str, help = 'input file name', action = 'store')

    return parser.parse_args()

def input_file(filename):
    try:
        with open(filename, 'rb') as f:
            content = f.read()
    except FileNotFoundError:
        print("I don't find file.")
    return content

def main():
    arg = argument_sys()
    # print(arg.filename)
    content = input_file(arg.filename)
    # print(content, end='*'*50+'\n')
    c = [i^3 for i in content]
    # print(c, end="*"*50+'\n')
    # c = bytes([i^3 for i in c])
    # print(c)
    s = bytes(c)
    # s = ''.join(d)
    # print(d, end="*"*50+'\n')
    # k = bytes([i^3 for i in d])
    # print(k, end="*"*50+'\n')
    with open("Jarvis.txt", 'wb') as d:
        d.write(s)


if __name__ == '__main__':
    main()