import time


def open_file(name):
    try:
        with open(name, 'r') as data_file:
            for line in data_file:
                print(line)
    except FileNotFoundError:
        with open(name, 'w') as new_file:
            print(f'file {name} has been created')
            new_file.write(str(time.time()))