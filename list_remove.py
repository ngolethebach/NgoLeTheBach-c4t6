color_list = ["red", "blue", "yellow", "teal"]
while True:
    command = input("What's your command (add, remove, draw)? ")
    if command == "add":
        new_color = input("new color: ")
        color_list.append(new_color)
    elif command == "remove":
        color_to_remove = input("color to remove: ")
        color_list.remove(color_to_remove)
    elif command == "draw":
        from turtle import*
        shape("turtle")
        penup()
        for c in color_list:
            fillcolor(c)
            stamp()
            forward(20)
            left(30)
        mainloop()

    else:
        print("I could not understand")
    print("* " * 10)
    for c in color_list:
        print(c)
    print("* " * 10)




