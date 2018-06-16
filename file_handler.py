import csv


class FileHandler:
    @staticmethod
    def read_file(filename):
        task_list = []
        try:
            with open(filename, 'r') as f:
                # read data from file
                reader = csv.DictReader(f)
                for row in reader:
                    task_list.append(row)
                return task_list
        except IOError:
            print("Can't open the file! Did you type correct name?")
