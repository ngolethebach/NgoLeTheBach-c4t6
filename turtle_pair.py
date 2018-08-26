from turtle import*
hideturtle()
turtle_list = []
for i in range(5):
    t = Turtle()
    turtle_list.append(t)
j = int(input("Turtle position? "))
turtle_list[j].color('pink')
turtle_list[j].shape('turtle')
n = 90
for tt in turtle_list:
    tt.left(n)
    tt.forward(100)
    n += 90










