#!/bin/python3
## Nhập bất kỳ 1 chữ và in ra chữ đó dưới dạng phóng to bằng dấu *
## VD: A
#      *    
#    *   *   
#   *****  
#  *       * 
#  *       *

###########
A={3: '^', 7: '/', 9: '\\', 11: '-', 12: '-', 13: '-', 14: '-', 15: '-', 16: '|', 20: '|', 21: '|', 25: '|', 'l': 5, 'p': 5}
B={1: '-', 2: '-', 3: '-', 4: '-', 5: '.', 6: '|', 10: '|', 11: '|', 12: '-', 13: '-', 14: '•', 16: '|', 20: '|', 21: '-', 22: '-', 23: '-', 24: '-', 25: '`', 'l': 5, 'p': 5}
C={1: '_', 2: '_', 3: '_', 4: '_', 5: '_', 6: '|', 11: '|', 16: '|', 21: '-', 22: '-', 23: '-', 24: '-', 25: '-', 'l': 5, 'p': 5}
D={1: '-', 2: '-', 3: '-', 4: '.', 6: '|', 10: '\\', 11: '|', 15: '|', 16: '|', 20: '/', 21: '-', 22: '-', 23: '-', 24: '`', 'l': 5, 'p': 5}
###########

print("Nhập chữ [A-Z]: ",end="")
user_input=[x for x in input().upper().split(" ")]
#user_input=[char for char in input().upper()]
size=1
portrait=0
landscape=100
for i in user_input:
    try:
        temp=eval(i)["p"]
        temp1=eval(i)["l"]
    except:
        print(f"{i} not found!")
        exit()
    if (int(temp) > portrait):
	    portrait=int(temp)
    if (int(temp1) < landscape):
	    landscape=int(temp1)
del temp
del temp1

size_landscape=int(landscape)
for i in range (1,portrait+1,1):
    for char in user_input:
        for i in range(size,size_landscape+1,1):
            if (i in eval(char)):
                print(eval(char)[i],end="")
            else:
                print(" ",end="")
            if (char == user_input[-1]):
                size+=1
                size_landscape+=1
        print(end="  ")
    print(end="\n")
        
