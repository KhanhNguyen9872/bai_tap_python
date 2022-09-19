#!/bin/python3
"""
Viết một chương trình chấp nhận đầu vào là chuỗi các số nhị phân 4 chữ số, phân

tách bởi dấu phẩy, kiểm tra xem chúng có chia hết cho 5 không. Sau đó in các số chia hết cho 5 thành dãy phân tách bởi dấu phẩy.

Ví dụ đầu vào là: 0100,0011,1010,1001 Đầu ra sẽ là: 0100,1010
"""

def main1():
    for i in user_inp:
        if (int(i)%5==0):
            answer.append(i)
    print(','.join(answer))

if (__name__=="__main__"):
    global user_inp, answer
    answer=[]
    user_inp=[str(x) for x in input("Input: ").split(",")]
    main1()