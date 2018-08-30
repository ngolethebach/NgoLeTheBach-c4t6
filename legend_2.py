player = {
    "NAME": "JOHN WICK",
    "CLASS": "HUMAN",
    "HP": 100,
    "STR": 15,
    "DEF": 10,
}
cmd = input("Bạn muốn xem thông tin của nhân vật thì hãy nhấn stats!!! ")
if cmd == "stats":
    print("NAME:", player["NAME"])
    print("CLASS:", player["CLASS"])
    print("HP:", player["HP"])
    print("STR:", player["STR"])
    print("DEF:", player["DEF"])
    print("Bạn vào vai 1 người đàn ông rất yêu thương chú chó của mình")
    print("Nhưng vào 1 ngày, tên trùm EXCITER đến trộm chú chó của bạn")
    print("Bạn sẽ quyết định làm gì? ")
    print("Bạn có 3 lựa chọn: ")
    print("1. Bạn sẽ mua 1 chú chó mới")
    print("2. Bạn sẽ sống hết cuộc đời còn lại trong đau khổ mà thiếu đi chú chó mình yêu quý")
    print("3. Bạn sẽ đi trả thù")
    option = input("Lựa chọn của bạn: ")
    if option == "1":
        print("Đây không phải việc làm của thằng đàn ông =(((")
        print("Game over")
        option = input("Lựa chọn của bạn: ")
    elif option == "2":
        print("Khóc lóc nhiều chẳng để làm gì cả")
        print("Nhập lại đi")
    elif option == "3":
        print("Đây mới là đàn ông chứ =))")
        print("Bạn đã lần theo dấu vết của tên trùm và phát hiện ra ổ trộm chó của hắn")
        print("Nhưng bạn gặp 1 exciter boy lởn vởn bên ngoài ")
        print("Bạn quyết định xử lý hắn")
        print("EXCITER BOY'S STATS:")
        exciterboy = {
                "HP": 5,
                "STR": 10,
                "DEF": 10,
            }
        print("HP", exciterboy["HP"])
        print("STR", exciterboy["STR"])
        print("DEF", exciterboy["DEF"])
        damage = player["STR"] - exciterboy["DEF"]
        if damage > 0:
            exciterboy["HP"] = exciterboy["HP"] - damage
            print("Hắn vừa mất", damage, "HP")
            print("HP hiện tại của hắn:", exciterboy["HP"])
        print("Bạn đã dễ dàng vượt qua hắn")
        print("Bạn thấy 1 cây bút chì trước mặt")
        print("1. Bỏ qua")
        print("2. Nhặt lên làm vũ khí")
        option = input("Lựa chọn của bạn: ")
        if option == "1":
            print("Tiếc quá")
        elif option == "2":
            print("Bạn đc tăng tấn công")
            player["STR"] = 100
            print("STR:", player["STR"])
        else:
            print("Nhập lại đi")
        print("Bạn đã gặp tên trùm EXCITER")
        exciterboss = {
            "HP": 100,
            "ATK": 50,
            "DEF": 50,
            "SPEED": 100,
    }
        print("Bạn dùng bút chì xiên hắn trước")
        damage = player["STR"] - exciterboss["DEF"]
        if damage > 0:
            exciterboss["HP"] = exciterboss["HP"] - damage
            print("Hắn mất", damage, "HP")
            print("HP hiện tại của hắn:", exciterboss["HP"])
            print("Hắn nhanh chóng nhét bả vào mồm bạn")
            print("Bạn bị choáng")
            print("Hắn tấn công bạn")
            damage = exciterboss["ATK"] - player["DEF"]
            if damage > 0:
                player["HP"] = player["HP"] - damage
                print("Bạn mất", damage, "HP")
                print("HP hiện tại của bạn:", player["HP"])
            else:
                print("Bạn không sao cả ")
            print("Bạn cầm bút chì đâm hắn")
            damage = player["STR"] - exciterboss["DEF"]
            exciterboss["HP"] = exciterboss["HP"] - damage
            print("Hắn mất", damage, "HP")
            print("HP hiện tại của hắn:", exciterboss["HP"])
            print("Game là dễ")
            print("Bạn dành chiến thắng")
else:
    print("Nhập lại đi")










