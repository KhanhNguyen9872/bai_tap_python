#!/bin/python3
## Nhập bất kỳ 1 chữ và in ra chữ đó dưới dạng phóng to bằng dấu *
## VD: A
#      *    
#    *   *   
#   *****  
#  *       * 
#  *       *
## Ngang: 9
## Dọc: 5
count=0
A=[5,13,15,21,22,23,24,25,29,35,37,45]
user_input=str(input("Nhập 1 chữ [A-Z]: ").upper())
for i in range (1,46,1):
    if (i in (eval(user_input))):
        print("*",end="")
    else:
        print(" ",end="")
    count+=1
    if (count == 9):
        print("\n")
        count=0
        
