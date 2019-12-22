mydir = dict()
while True:
    try:
        command = input()
    except EOFError:
        break
    if command == "" or command == ".":
        break
    if command[0] == "#":
        continue
    index = command.find("=")
    try:

        if index != -1:
            comm = command.split("=", 1)
            try:

                if comm[0][0].isnumeric():
                    raise NameError("invalid identifier " + "'" +comm[0] + "'")
                mydir[comm[0]] = eval(comm[1], mydir)
            except SyntaxError:
                print("invalid assignment '" + command + "'")

        else:
            print(eval(command, mydir))
    except Exception as err:
        print(err)


