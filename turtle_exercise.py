from turtle import*
color_list = ['red', 'blue', 'brown', 'yellow', 'gray']
shape("arrow")
hideturtle()
for c in color_list:
    color(c)
    begin_fill()
    for i in range(2):
        forward(50)
        left(90)
        forward(100)
        left(90)
    forward(50)
    end_fill()
mainloop()