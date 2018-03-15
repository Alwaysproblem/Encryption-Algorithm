import argparse

def argument_sys():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type = str, help = 'input file name', action = 'store')

    return parser.parse_args()

def input_file(filename):
    try:
        with open(filename, 'r+') as f:
            content = f.read()
    except FileNotFoundError:
        print("I don't find file.")
    return content

def main():
    arg = argument_sys()
    # print(arg.filename)
    content = input_file(arg.filename)
    # print(content)
    c = [ord(i)^3 for i in content]
    d = [chr(i) for i in c]
    s = ''.join(d)
    # print(d)
    with open("Jarvis.txt", 'w+') as d:
        d.write(s)


if __name__ == '__main__':
    main()