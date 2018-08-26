from turtle import*
turtle_list = []
for i in range(5):
    t = Turtle()
    turtle_list.append(t)
while True:
    position = int(input("Turtle position: "))
    colour = (input("Turtle color: "))
    shapes = (input("Turtle shape: "))
    cmd = (input("Turtle command: "))
    cmd_list = cmd.split(" ")
    turtle_list[position] = t
    t.colour(colour)
    t.shape(shape)
    for command in cmd_list:
        if cmd == "fd":
            t.fd(100)
        elif cmd == "rt":
            cmd_list[command] = cmd_list["command + 1"]
        elif cmd == "lt":
            cmd_list[command] = cmd_list["command + 1"]
        elif cmd == "bd":
            t.bd(100)
mainloop()





