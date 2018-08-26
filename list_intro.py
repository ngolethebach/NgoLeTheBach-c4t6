color_list = ["red", "blue", "purple", "orange"]
while True:
    new_color = input("new color? ")
    color_list.append(new_color)
    print("* " * 10)
    for color in color_list:
        print(color)
    print("* " * 10)
