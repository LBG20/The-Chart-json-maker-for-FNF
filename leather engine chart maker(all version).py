import random, time
def end():
    t = int(3)
    for _ in range(t):
        print('\r输出完成,将在' + str(t) + '秒后结束程序','(It'"'"'done'',''will closed in ' + str(t) + ' second)', end='')
        t = t - 1
        time.sleep(1)
def print_json_start():
    print("{", '"', "song", '"', ":{", '"', "player1", '"', ":", '"', "bf", '"', ",", '"', "keyCount", '"', ":",
          b1 + 1, ",", '"', "playerKeyCount", '"', ":", b1 + 1, ",", '"', "notes", '"', ":[{", '"'"sectionNotes", '"',
          ":[", sep="", end="", file=f)
def print_json_end():
    print("]", ",", '"', "lengthInSteps", '"', ":", "16", ","'"', "typeOfSection", '"', ":", "0", ",", '"',
          "mustHitSection", '"', ":", "true", ",", '"', "bpm", '"', ":", "0.1}]", ",", '"', "player2", '"',
          ":", '"', "bf", '"', ",", '"', "chartOffset", '"', ":", "0", ",", '"', "modchartPath", '"', ":",
          '"', '"', ",", '"', "mania", '"', ":null", ",", '"', "modchartingTools", '"', ":", "false", ",",
          '"', "endCutscene", '"', ":", '"', '"', ",", '"', "song", '"', ":", '"', songname, '"', ",", '"',
          "validScore", '"', ":", "false", ",", '"', "speed", '"', ":", speed, ",", '"', "sectionLengths",
          '"', ":", "[]", ",", '"', "ui_Skin", '"', ":", '"', "default", '"', ",", '"', "events", '"', ":",
          "[]", ",", '"', "cutscene", '"', ":", '"', '"', ",", '"', "timescale", '"', ":[4,4],", '"',
          "needsVoices", '"', ":true,", '"', "stage", '"', ":", '"', "stage", '"', ",", '"', "sections",
          '"', ":0,", '"', "bpm", '"', ":", BPM, ",", '"', "gf", '"', ":", '"', "gf", '"', "}}", "'",
          sep="", end="", file=f)
mode = int(input("请输入模式前的数字\n1.纯大粪 2.随机箭头 3.随机双压箭头 4.随机3押箭头:\nPlease enter the number of the mode\n1.spam 2.random note 3.Double random note 4.Triple random note\n:"))
if mode == 1:
    way = input("请输入你要输出的路径(比如D:/test.json,不能使用\\)\nPlease enter the file you want print path(such as:'D:/test.json',but you can't used\\)\n:")
    f = open(way, 'w')
    b = int(0)
    for _ in range(1):
        a = -1
        c = int(0)
        open_3second_no_note = str(input("是否启用前3秒无箭头(填True或False)\nwith no note in 3 second?(Ture or False)\n:"))
        if open_3second_no_note == "True":
            a = int(2999)
        else:
            a = -1
        songname = input("请输入歌名\nPlease enter song name\n:")
        speed = input("请输入歌曲速度\nPlease enter the speed of the chart\n:")
        BPM = int(input("请输入歌曲BPM(只能填数字否则报错)\nPlease enter the bpm of the song(fill out with only number)\n:"))
        a1 = int(input("请输入歌曲总秒数(只能填数字否则报错)\nPlease enter total seconds of the song(fill out with only number)\n:"))
        a1 = a1 * 1000
        section = BPM * a1 / 240
        b1 = int(input("请输入歌曲总key数(只能填数字否则报错)\nPlease enter keys of the song(fill out with only number)\n:"))
        b1 = b1 - 1
        note = str(input("请输入使用的箭头(比如default)\nPlease enter the kinds of the note(such as 'default')\n:"))
        num1 = int(input("请输入每个箭头间隔多少毫秒(只能填数字否则报错)\nPlease enter the number of milliseconds between Last notes and next note(fill out with only number)\n:"))
        list1 = [","]
        a1 = a1 - num1
        print_json_start()
        while a <= a1:
            a = int(a + num1)
            if a1 - a <= num1 and a + num1 >= a1:
                print("[", a, ",", b, ",", "0", ",", "0", ","'"', note, '"', "]", sep="", end="", file=f)
                print(' '.join(list1), sep="", end="", file=f)
                list1 = [""]
                if b <= b1:
                    b = int(b + 1)
                else:
                    b = int(0)
            else:
                print("[", a, ",", b, ",", "0", ",", "0", ","'"', note, '"', "]", ",", sep="", end="", file=f)
                if b <= b1:
                    b = int(b + 1)
                else:
                    b = int(0)
        print_json_end()
    f.close()
    end()
else:
    if mode == 2:
        way = input("请输入你要输出的路径(比如D:/test.json,不能使用\\)\nPlease enter the file you want print path(such as:'D:/test.json',but you can't used\\)\n:")
        f = open(way, 'w')
        list1 = [","]
        for _ in range(1):
            a = -1
            b = int(0)
            c = int(0)
            open_3second_no_note = str(
                input("是否启用前3秒无箭头(填True或False)\nwith no note in 3 second?(Ture or False)\n:"))
            if open_3second_no_note == "True":
                a = int(2999)
            else:
                a = -1
            songname = input("请输入歌名\nPlease enter song name\n:")
            speed = input("请输入歌曲速度\nPlease enter the speed of the chart\n:")
            BPM = int(input(
                "请输入歌曲BPM(只能填数字否则报错)\nPlease enter the bpm of the song(fill out with only number)\n:"))
            a1 = int(input(
                "请输入歌曲总秒数(只能填数字否则报错)\nPlease enter total seconds of the song(fill out with only number)\n:"))
            a1 = a1 * 1000
            section = BPM * a1 / 240
            b1 = int(input(
                "请输入歌曲总key数(只能填数字否则报错)\nPlease enter keys of the song(fill out with only number)\n:"))
            b1 = b1 - 1
            note = str(input("请输入使用的箭头(比如default)\nPlease enter the kinds of the note(such as 'default')\n:"))
            num1 = int(input(
                "请输入每个箭头间隔多少毫秒(只能填数字否则报错)\nPlease enter the number of milliseconds between Last notes and next note(fill out with only number)\n:"))
            a1 = a1 - num1
            print_json_start()
            while a <= a1:
                a = int(a + num1)
                if a1 - a <= num1 and a + num1 >= a1:
                    b = random.randint(0, b1)
                    print("[", a, ",", b, ",", "0", ",", "0", ","'"', note, '"', "]", sep="", end="", file=f)
                    print(' '.join(list1), sep="", end="", file=f)
                    list1 = [""]
                else:
                    b = random.randint(0, b1)
                    print("[", a, ",", b, ",", "0", ",", "0", ","'"', note, '"', "]", ",", sep="", end="", file=f)
            print_json_end()
        f.close()
        end()
    else:
        if mode == 3:
            way = input("请输入你要输出的路径(比如D:/test.json,不能使用\\)\nPlease enter the file you want print path(such as:'D:/test.json',but you can't used\\)\n:")
            f = open(way, 'w')
            list1 = [","]
            for _ in range(1):
                a = -1
                b = int(0)
                c = int(0)
                open_3second_no_note = str(
                    input("是否启用前3秒无箭头(填True或False)\nwith no note in 3 second?(Ture or False)\n:"))
                if open_3second_no_note == "True":
                    a = int(2999)
                else:
                    a = -1
                songname = input("请输入歌名\nPlease enter song name\n:")
                speed = input("请输入歌曲速度\nPlease enter the speed of the chart\n:")
                BPM = int(input(
                    "请输入歌曲BPM(只能填数字否则报错)\nPlease enter the bpm of the song(fill out with only number)\n:"))
                a1 = int(input(
                    "请输入歌曲总秒数(只能填数字否则报错)\nPlease enter total seconds of the song(fill out with only number)\n:"))
                a1 = a1 * 1000
                section = BPM * a1 / 240
                b1 = int(input(
                    "请输入歌曲总key数(只能填数字否则报错)\nPlease enter keys of the song(fill out with only number)\n:"))
                b1 = b1 - 1
                note = str(input("请输入使用的箭头(比如default)\nPlease enter the kinds of the note(such as 'default')\n:"))
                num1 = int(input(
                    "请输入每个箭头间隔多少毫秒(只能填数字否则报错)\nPlease enter the number of milliseconds between Last notes and next note(fill out with only number)\n:"))
                a1 = a1 - num1  # 玩家角色                               敌方箭头数                       我方箭头数
                print_json_start()
                while a <= a1:
                    a = int(a + num1)
                    if a1 - a <= num1 and a + num1 >= a1:
                        b = random.randint(0, b1)
                        b2 = b
                        print("[", a, ",", b, ",", "0", ",", "0", ","'"', note, '"', "]", ",", sep="", end="", file=f)
                        b = random.randint(0, b1)
                        for i in range(0, -1, -1):
                            if b == b2:
                                b = random.randint(0, b1)
                            if b != b2:
                                continue
                        print("[", a, ",", b, ",", "0", ",", "0", ","'"', note, '"', "]", sep="", end="", file=f)
                        print(' '.join(list1), sep="", end="", file=f)
                        list1 = [""]
                    else:
                        b = random.randint(0, b1)
                        b2 = b
                        print("[", a, ",", b, ",", "0", ",", "0", ","'"', note, '"', "]", ",", sep="", end="", file=f)
                        b = random.randint(0, b1)
                        for i in range(0, -1, -1):
                            if b == b2:
                                b = random.randint(0, b1)
                            if b != b2:
                                continue
                        print("[", a, ",", b, ",", "0", ",", "0", ","'"', note, '"', "]", ",", sep="", end="", file=f)
                print_json_end()
            f.close()
            end()
        else:
            way = input("请输入你要输出的路径(比如D:/test.json,不能使用\\)\nPlease enter the file you want print path(such as:'D:/test.json',but you can't used\\)\n:")
            f = open(way, 'w')
            list1 = [","]
            for _ in range(1):
                a = -1
                b = int(0)
                c = int(0)
                open_3second_no_note = str(
                    input("是否启用前3秒无箭头(填True或False)\nwith no note in 3 second?(Ture or False)\n:"))
                if open_3second_no_note == "True":
                    a = int(2999)
                else:
                    a = -1
                songname = input("请输入歌名\nPlease enter song name\n:")
                speed = input("请输入歌曲速度\nPlease enter the speed of the chart\n:")
                BPM = int(input(
                    "请输入歌曲BPM(只能填数字否则报错)\nPlease enter the bpm of the song(fill out with only number)\n:"))
                a1 = int(input(
                    "请输入歌曲总秒数(只能填数字否则报错)\nPlease enter total seconds of the song(fill out with only number)\n:"))
                a1 = a1 * 1000
                section = BPM * a1 / 240
                b1 = int(input(
                    "请输入歌曲总key数(只能填数字否则报错)\nPlease enter keys of the song(fill out with only number)\n:"))
                b1 = b1 - 1
                note = str(input("请输入使用的箭头(比如default)\nPlease enter the kinds of the note(such as 'default')\n:"))
                num1 = int(input(
                    "请输入每个箭头间隔多少毫秒(只能填数字否则报错)\nPlease enter the number of milliseconds between Last notes and next note(fill out with only number)\n:"))
                a1 = a1 - num1
                print_json_start()
                while a <= a1:
                    a = int(a + num1)
                    if a1 - a <= num1 and a + num1 >= a1:
                        b = random.randint(0, b1)
                        b2 = b
                        print("[", a, ",", b, ",", "0", ",", "0", ","'"', note, '"', "]", ",", sep="", end="", file=f)
                        b = random.randint(0, b1)
                        for i in range(0, -1, -1):
                            if b == b2:
                                b = random.randint(0, b1)
                            if b != b2:
                                continue
                        print("[", a, ",", b, ",", "0", ",", "0", ","'"', note, '"', "]", ",", sep="", end="", file=f)
                        b3 = b
                        b = random.randint(0, b1)
                        for i in range(0, -1, -1):
                            if b == b3 or b == b2:
                                b = random.randint(0, b1)
                            if b != b3 and b != b2:
                                continue
                        print("[", a, ",", b, ",", "0", ",", "0", ","'"', note, '"', "]", sep="", end="", file=f)
                        print(' '.join(list1), sep="", end="", file=f)
                        list1 = [""]
                    else:
                        b = random.randint(0, b1)
                        b2 = b
                        print("[", a, ",", b, ",", "0", ",", "0", ","'"', note, '"', "]", ",", sep="", end="", file=f)
                        b = random.randint(0, b1)
                        for i in range(0, -1, -1):
                            if b == b2:
                                b = random.randint(0, b1)
                            if b != b2:
                                continue
                        print("[", a, ",", b, ",", "0", ",", "0", ","'"', note, '"', "]", ",", sep="", end="", file=f)
                        b3 = b
                        b = random.randint(0, b1)
                        for i in range(0, -1, -1):
                            if b == b3 or b == b2:
                                b = random.randint(0, b1)
                            if b == b3 and b == b2:
                                continue
                        print("[", a, ",", b, ",", "0", ",", "0", ","'"', note, '"', "]", ",", sep="", end="", file=f)
                print_json_end()
            f.close()
            end()