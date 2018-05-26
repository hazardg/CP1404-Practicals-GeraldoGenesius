name = str(input("Enter name: "))
menu = """(H)ello
(G)oodbye
(Q)uit"""

print(menu)

choose_menu = str(input(">>> "))
while choose_menu != 'Q':

    if choose_menu == 'H':
        print("Hello ", name)

    elif choose_menu == 'G':
        print("Goodbye ", name)

    print(menu)
    choose_menu = str(input(">>> "))
