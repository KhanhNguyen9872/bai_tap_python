#!/bin/python3
import os

def clear():
	if (os.name == 'nt'):
		os.system("cls")
	else:
		os.system("clear")

clear()
help=" Gõ [exit] để hoàn tất!\n Gõ [clear] để xóa!\n"
limit=int(input("Nhập độ dài: "))
user_input=""""""
show=""""""
lines=0
print(f"Nhập dấu * [Độ dài: {limit}]\n{help}")
while True:
    inp=str(input())
    if (inp == "exit"):
        break
    elif (inp == "clear"):
        user_input=""""""
        show=""""""
        clear()
        print(f"Độ dài là {limit}\n{help}")
        print(show,end="")
    elif (len(inp)!=limit):
        clear()
        print(f"Độ dài là {limit}\n{help}")
        print(show,end="")
    else:
        user_input+=inp
        show+=f"{inp}\n"
        lines+=1

count=1
answer=[]
for line in user_input:
    if (line == "*"):
        answer.append(count)
    count+=1

answer.append(f"{limit}@")
answer.append(f"{lines}@")
print(f"\n Kết quả: \n{answer}")
