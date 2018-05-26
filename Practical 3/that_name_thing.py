#version 1
def version_1():
    name = input("name: ")
    while name == "":
        print("Invalid Name")
        name = input("name: ")

    print(name[::2])


def main():
    name = get_name()
    print_parts(name, 3)

def print_parts(name, step=2):
    print(name[::step])

def get_name():
    name = input("name: ")
    while name == "":
        print("Invalid Name")
        name = input("name: ")
    return name

main()
