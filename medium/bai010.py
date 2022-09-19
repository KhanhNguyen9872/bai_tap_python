#!/bin/python3
"""
Viết một chương trình tính giá trị của a+aa+aaa+aaaa với a là số được nhập vào bởi người dùng.

Giả sử a được nhập vào là 1 thì đầu ra sẽ là: 1234
"""

def main(a):
    answer=""
    for i in range(1,5,1):
        answer+=f"{a*i}"
    print(answer)

if (__name__=="__main__"):
    a=int(input("Input a: "))
    main(a)