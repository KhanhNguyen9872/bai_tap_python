#!/bin/python3
"""
Viết một chương trình chấp nhận đầu vào là một câu, đếm số chữ cái và chữ số trong câu đó. 
Giả sử đầu vào sau được cấp cho chương trình: hello world! 123

Thì đầu ra sẽ là:
Số chữ cái là: 3 số, 10 chữ
"""

def main(user_input):
    character=0
    number=0
    lower=[str(x) for x in "abcdefghijklmnopqrstuvwxyz"]
    upper=[str(x) for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    for char in [x for x in user_input]:
        try:
            int(char)
            number+=1
        except:
            if (char in lower) or (char in upper):
                character+=1
    
    print("Số chữ cái là: {} số, {} chữ".format(number,character))

if (__name__=="__main__"):
    user_input=str(input("Input string: "))
    main(user_input)