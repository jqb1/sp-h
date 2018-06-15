import argparse
from file import File


# here is where we start
def main():
    # parsing arguments passed when calling script
    parser = argparse.ArgumentParser(description="Choosing task file and max velocity")
    parser.add_argument('file', help="type: -file filename if you want to pass your file", type=str)
    # parser.add_argument('velocity', help="1-easy, other-hard , default - easy", type=int)

    arg = parser.parse_args()

    # pass a filename to file class constructor
    File(arg.file)


main()
