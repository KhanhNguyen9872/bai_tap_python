#!/bin/python3
import os

def clear():
	if (os.name == 'nt'):
		os.system("cls")
	else:
		os.system("clear")

clear()
limit=int(input("Nhập độ dài: "))
user_input=""""""
print(f"Nhập dấu * [Độ dài: {limit}] | Gõ [exit] để hoàn tất!")
while True:
    inp=str(input())
    if (inp == "exit"):
        break
    elif (len(inp)!=5):
        clear()
        print(f"Độ dài là {limit} | Gõ [exit] để hoàn tất!")
        print(user_input,end="")
    else:
        user_input+=inp

count=1
answer=[]
for line in user_input:
    if (line == "*"):
        answer.append(count)
    count+=1
        
print(f"\n Kết quả: \n{answer}")
