from turtle import*
width(0)
color_list = ['red', 'blue', 'brown', 'yellow', 'grey']
x = 0
y = 3
for c in color_list:
    x = x + 180
    color(c)
    for i in range(y):
        forward(100)
        left(180 - (x / y))
    y = y + 1
mainloop()