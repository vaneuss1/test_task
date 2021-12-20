import json
import sys

def display(struct, spaces=1):
    for i in struct:
        for j in i:
            if isinstance(i[j], list):
                print(f"{' ' * spaces}{j}: ")
                display(i[j], spaces + 4)
            else:
                print(f"{' ' * spaces}{j}: {i[j]}")


def dicts(struct, values):
    for test in struct:
        for val in test.values():
            if isinstance(val, list):
                dicts(val, values)
            for vals in values['values']:
                if test['id'] == vals['id']:
                    test['value'] = vals['value']
                    break


if __name__ == '__main__':
    tests_file = sys.argv[1]
    values_file = sys.argv[2]
    with open(tests_file, 'r') as f:
        with open(values_file, 'r') as f1:
            tests = json.load(f)
            value = json.load(f1)
            dicts(tests['tests'], value)
            display(tests['tests'])
