#!/bin/python3
"""
Viết một chương trình có 2 chữ số, X, Y nhận giá trị từ đầu vào và tạo ra một mảng 2 chiều.
Giá trị phần tử trong hàng thứ i và cột thứ j của mảng phải là i*j.
Lưu ý: i=0,1,…,X-1; j=0,1,…,Y-1.
Ví dụ: Giá trị X, Y nhập vào là 3,5 thì đầu ra là: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
"""
def main():
    answer=[]
    temp_list=[]
    temp=0
    x,y=input("Input x,y: ").split(",")
    for i in range(0,int(x),1):
        for j in range(0,int(y),1):
            sum=int(i*j)
            temp_list.append(sum)
        answer.append(temp_list)
        temp_list=[]
    print(answer)

if (__name__=="__main__"):
    main()