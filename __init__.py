# Progress bar like this | ----------------------------- | 00:00:00 00 MB / OO MB 00:00:00 ETC

import time
import colorama


def Progress_bar(MB, needTime, secondWithMB):
    global usedSecond
    usedSecond = 0
    global usedTime
    usedTime = ""
    global d
    d = 0
    for i in range(t2s(needTime)):
        a = "-" * i
        b = 100 - i
        c = " " * b
        d = d + secondWithMB
        usedSecond = usedSecond + 1
        usedTime = s2t(usedSecond)
        need_second = t2s(needTime)
        ETC = need_second - usedSecond
        RealETC = s2t(ETC)
        print(
            "| " + colorama.Fore.GREEN + a + c + colorama.Fore.RESET + " |" + colorama.Fore.RED + usedTime + " " + str(
                d) + " MB / " + str(
                MB) + " MB " + colorama.Fore.RESET + colorama.Fore.LIGHTBLUE_EX + RealETC + " ETC" + colorama.Fore.RESET,
            end="")
        time.sleep(1)
        print("\b" * 3000, end="")
    return 0


def t2s(t):  # t format is hh:mm:ss
    if t != '0':
        h, m, s = t.strip().split(":")
        return int(h) * 3600 + int(m) * 60 + int(s)
    else:
        return 0


def s2t(s):  # s is a number
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)


if __name__ == '__main__':
    Progress_bar(1000, "00:01:00", 10)
