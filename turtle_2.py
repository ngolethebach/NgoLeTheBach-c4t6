from turtle import*
turtle_list = []
t = Turtle()
turtle_list.append(t)
while True:
    command = input("command to move turtle (fd, rt, lt, bd): ")
    command_list = command.split(" ")
    print(command)
    command = command.lower()
    for c in command_list:
        if c == "fd":
            t.fd(100)
        elif c == "lt":
            t.lt(90)
        elif c == "rt":
            t.rt(90)
        elif c == "bd":
            t.bd(100)
        else:
            print("only use fd, lt, rt, bd")
mainloop()