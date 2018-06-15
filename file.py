import random


class File:
    def __init__(self, filename):
        self.open_file(filename)

    def open_file(self, filename):
        try:
            file = open(filename)
            self.read_file(file)

            # lines = file.read().splitlines()
            # line = random.choice(lines)
            # return line
        except IOError:
            print("Can't open a file!")

    def read_file(self, file):
        for line in file:
            print(line)
