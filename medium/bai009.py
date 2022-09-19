#!/bin/python3
"""
Viết một chương trình chấp nhận đầu vào là một câu, đếm chữ hoa, chữ thường.
Giả sử đầu vào là: Cafedev - Kênh Thông Tin IT
Thì đầu ra là:
Chữ hoa: 6
Chữ thường: 15
"""

def main1(user_input,low,up):
    up=0
    low=0
    for char in [x for x in user_input]:
        if (char.islower()):
            low+=1
        elif (char.isupper()):
            up+=1
    print("Chữ hoa: {}\nChữ thường: {}".format(up,low))

def main2(user_input,low,up):
    lower=[str(x) for x in "abcdefghijklmnopqrstuvwxyzăâđêôơư"]
    upper=[str(x) for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZĂÂĐÊÔƠƯ"]
    for char in [x for x in user_input]:
        if (char in lower):
            low+=1
        elif (char in upper):
            up+=1
    print("Chữ hoa: {}\nChữ thường: {}".format(up,low))

if (__name__=="__main__"):
    user_input=str(input("Input string: "))
    main1(user_input,0,0)
    main2(user_input,0,0)