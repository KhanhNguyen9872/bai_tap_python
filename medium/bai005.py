#!/bin/python3
"""
Viết một chương trình chấp nhận đầu vào là một chuỗi các từ tách biệt bởi khoảng trắng, 
loại bỏ các từ trùng lặp, sắp xếp theo thứ tự bảng chữ cái, rồi in chúng.

Giả sử đầu vào là: hello world and practice makes perfect and hello world again
Thì đầu ra là: again and hello makes perfect practice world
"""

def main1():
    print(' '.join(sorted(user_inp)))

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
    print(' '.join(answer))

if (__name__=="__main__"):
    global user_inp
    user_inp=[str(x) for x in input("Input string: ").split(" ")]
    for i in user_inp:
        while (i in user_inp):
            user_inp.remove(i)
        user_inp.append(i)
    print(user_inp)
    main1()
    main2()