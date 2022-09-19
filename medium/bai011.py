#!/bin/python3
"""
Sử dụng một danh sách để lọc các số lẻ từ danh sách được người dùng nhập vào.

Giả sử đầu vào là: 1,2,3,4,5,6,7,8,9 thì đầu ra phải là: 1,3,5,7,9
"""

def main():
    answer=[]
    for num in [int(x) for x in input("Input number: ").split(",")]:
        if (num % 2 != 0):
            answer.append(str(num))
    print(','.join(answer))

if (__name__=="__main__"):
    main()