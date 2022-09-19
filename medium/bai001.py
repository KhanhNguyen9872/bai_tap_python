#!/bin/python3
"""
Viết chương trình và in giá trị theo công thức cho trước: Q = √([(2 * C * D)/H]) 
(bằng chữ: Q bằng căn bậc hai của [(2 nhân C nhân D) chia H]. 
Với giá trị cố định của C là 50, H là 30. 
D là dãy giá trị tùy biến, được nhập vào từ giao diện người dùng
các giá trị của D được phân cách bằng dấu phẩy.S
Ví dụ: Giả sử chuỗi giá trị của D nhập vào là 100,150,180 thì đầu ra sẽ là 18,22,24.
"""
def main(C,H):
    for D in user_inp:
        Q.append(str(round(sqrt((2 * C * D) / H))))
    print(','.join(Q))

if (__name__ == '__main__'):
    from math import sqrt
    C=int(50)
    H=int(30)
    global user_inp, Q
    Q=[]
    user_inp=[int(x) for x in input("Input D: ").split(",")]
    main(C,H)