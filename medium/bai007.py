#!/bin/python3
"""
Viết một chương trình tìm tất cả các số trong đoạn 1000 và 3000 (tính cả 2 số này) 
sao cho tất cả các chữ số trong số đó là số chẵn. 
In các số tìm được thành chuỗi cách nhau bởi dấu phẩy, trên một dòng.
"""

def main():
    answer=[]
    for num in range(1000,3001,1):
        if (num%2==0):
            answer.append(str(num))
    print(','.join(answer))

if (__name__=="__main__"):
    main()