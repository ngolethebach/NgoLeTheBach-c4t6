#player = ["MAD", "Teacher", 100, 7, 1, 8, 2]
player = {
    "NAME": "MAD",
    "CLASS": "TEACHER",
    "HP": 60,
    "STR": 8,
    "AGI": 1,
    "LV": 1,
    "DEF": 10,
}
cmd = input("Your command: ")
if cmd == "stats":
    print("NAME:", player["NAME"])
    print("CLASS:", player["CLASS"])
    print("HP:", player["HP"])
    print("STR:", player["STR"])
    print("DEF:", player["DEF"])
    print("LV:", player["LV"])
elif cmd == "info":
    print("Ban dg o truoc lau dai")
    print("Ban co 2 lua chon")
    print("1. Quay tro ve lau dai")
    print("2. Di vao canh rung doi dien")
    option = input("Lua chon cua ban? ")
    if option == "1":
        print("Xin loi, da het gio lam viec")
    elif option == "2":
        print("Ban da buoc vao rung")
        print("Ban thay 1 binh thuy tinh o tren mat dat")
        print("1. Bo qua")
        print("2. Nhat len uong")
        option = input("Lua chon cua ban? ")
        if option == "1":
            print("Tiec qua")
        elif option == "2":
            player["HP"] = 100
            print("Ban da duoc hoi  phuc hoan toan HP")
            print("HP:", player["HP"])
        print("Ban gap 1 con orc")
        print("Ban se")
        print("1. Chay tron")
        print("2. Nap vao hang da ben canh")
        print("3. Danh")
        option = input("Lua chon cua ban: ")
        if option == "1":
            print("Do ban chay k du nhanh nen bi bat di")
        elif option == "2":
            print("Con orc k nhin thay ban va bo di")
            print("Tuy nhien khi ban quay lai nhin vao trong hang thi thay mot dan soi")
        elif option == "3":
            print("ORC'S STATS: ")
            orc = {
                "NAME": "ORC CO BAN",
                "HP": 10,
                "STR": 5,
                "DEF": 3,
            }
            print("OPPONENT:", orc["NAME"])
            print("HP:", orc["HP"])
            print("STR:", orc["STR"])
            print("DEF:", orc["DEF"])
            damage = player["STR"] - orc["DEF"]
            if damage > 0:
                orc["HP"] = orc["HP"] - damage
                print("orc vua mat", damage, "HP")
            print("Orc dung day va lai ban ")
            damage = orc["STR"] - player["DEF"]
            player["HP"]= player["HP"] - damage
            if damage > 0:
                player["HP"] = player["HP"] - damage
                print("ban vua mat", damage, "HP")
            else:
                print("ban k sao ca")
            damage = player["STR"] - orc["DEF"]
            orc["HP"] = orc["HP"] - damage
            print("HP hiện tại của Orc :", orc["HP"])
            print("Ban da thang")
            print("Het game")





























    else:
        print("Nhap lai di")


#cmd = input("your command")
#if cmd == "stats":