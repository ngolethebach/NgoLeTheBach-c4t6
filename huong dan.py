cmd = input("your commnand")
print(type(cmd))
cmd_list = cmd.split(" ")
for c in cmd_list:
    print(c)