from turtle import*
turtle_list = []
for _ in range(5):
    t = Turtle()
    turtle_list.append(t)
n = len(turtle_list)
print("i have", n, "turtles")
position = int(input("Which one do u want to control? "))
color_str = input("What color? ")
shape_str = input("What shape? ")
cmd = input("What command (fd, bd, lt, rt")
t = turtle_list[position - 1]
t.color(color_str)
t.forward(100)
t.shape(shape_str)
if cmd == "fd" or cmd == "forward":
    t.fd(100)
elif cmd == "bd":
    t.bd(100)
mainloop()