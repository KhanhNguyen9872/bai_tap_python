#!/bin/python3
"""
Viết một chương trình chấp nhận chuỗi từ do người dùng nhập vào
, phân tách nhau bởi dấu phẩy và in những từ đó thành chuỗi theo thứ tự bảng chữ cái
, phân tách nhau bằng dấu phẩy.
Giả sử đầu vào được nhập là: without,hello,bag,world, thì đầu ra sẽ là: bag,hello,without,world.
"""
def main1():
    print(sorted(user_inp))

def main2():
    answer=[]
    sort=user_inp[0]
    while (user_inp != []):
        for word in user_inp:
            if (sort > word):
                sort=word
        answer.append(sort)
        user_inp.remove(sort)
        try:
            sort=user_inp[0]
        except:
            pass
    print(answer)

if (__name__=="__main__"):
    global user_inp
    user_inp=[str(x) for x in input("Input string: ").split(",")]
    main1()
    main2()