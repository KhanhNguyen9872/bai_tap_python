#!/bin/python3
## Nhập bất kỳ 1 chữ và in ra chữ đó dưới dạng phóng to bằng dấu *
## VD: A
#      *    
#    *   *   
#   *****  
#  *       * 
#  *       *

###########
A=[3, 7, 9, 11, 12, 13, 14, 15, 16, 20, 21, 25, '5@', '5@']
B=[1, 2, 3, 4, 6, 10, 11, 12, 13, 14, 16, 20, 21, 22, 23, 24, '5@', '5@']
C=[2, 3, 4, 5, 6, 11, 16, 22, 23, 24, 25, '5@', '6@']
D=[1, 2, 3, 6, 10, 11, 15, 16, 20, 21, 22, 23, '5@', '5@']
E=[1, 2, 3, 4, 5, 6, 11, 12, 13, 14, 15, 16, 21, 22, 23, 24, 25, '5@', '5@']
F=[1, 2, 3, 4, 5, 6, 11, 12, 13, 14, 15, 16, 21, '5@', '5@']
TAMGIAC=[5, 13, 15, 21, 25, 29, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, '9@', '5@']
T=[1, 2, 3, 4, 5, 8, 13, 18, 23, '5@', '5@']
KHONG=[2, 3, 4, 6, 10, 11, 15, 16, 20, 22, 23, 24, '5@', '5@']
CHIN=[2, 3, 4, 6, 10, 12, 13, 14, 15, 20, 22, 23, 24, '5@', '5@']
###########

print("Nhập chữ [A-Z]: ",end="")
user_input=[x for x in input().upper().split(" ")]
#user_input=[char for char in input().upper()]
size=1
portrait=0
landscape=100
for i in user_input:
    try:
        temp=str(eval(i)[-1])
    except:
        print(f"{i} not found!")
        exit()
    if (int(temp.replace('@','')) > portrait):
	    portrait=int(temp.replace("@",""))
    temp=str(eval(i)[-2])
    if (int(temp.replace('@','')) < landscape):
	    landscape=int(temp.replace('@',''))

size_landscape=int(landscape)
for i in range (1,portrait+1,1):
    for char in user_input:
        for i in range(size,size_landscape+1,1):
            if (i in eval(char)):
                print("*",end="")
            else:
                print(" ",end="")
            if (char == user_input[-1]):
                size+=1
                size_landscape+=1
        print(end="  ")
    print(end="\n")
        
