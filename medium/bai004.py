#!/bin/python3
"""
Viết một chương trình chấp nhận chuỗi là các dòng được nhập vào, chuyển các dòng này thành chữ in hoa và in ra màn hình. Giả sử đầu vào là:

Hello world
Practice makes perfect

Thì đầu ra sẽ là:
HELLO WORLD
PRACTICE MAKES PERFECT
"""

def main1(user_inp):
    print(user_inp.upper())

def main2(user_inp):
    answer=""
    lower=[str(x) for x in "abcdefghijklmnopqrstuvwxyzăâđêôơư"]
    upper=[str(x) for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZĂÂĐÊÔƠƯ"]
    for character in [char for char in user_inp]:
        if (character in lower):
            for i in range(0, len(lower), 1):
                if (character == lower[i]):
                    answer+=f"{upper[i]}"
        else:
            answer+=character
    print(answer)

if (__name__=="__main__"):
    user_inp=str(input("Input string: "))
    main1(user_inp)
    main2(user_inp)