#!/bin/python3
import os

def clear():
    if (os.name == 'nt'):
        os.system("cls")
    else:
        os.system("clear")
        
def main():
	global limit, num
	print(f"Nhập dấu * [Độ dài: {limit}]\n Gõ [exit] để hoàn tất!\n Gõ [clear] để xóa!\n\n{num}")

answer={}
user_input=""""""
show=""""""
num=""
count=1
lines=0

clear()
limit=int(input("Nhập độ dài: "))
if (limit > 50) or (limit < 1):
	print("Sai giới hạn [1-50]")
	exit()
for _ in range(0,limit,1):
    num+=str(count)
    count+=1
    if (count==10):
        count=0

main()
while True:
    inp=str(input())
    if (inp == "exit"):
        break
    elif (inp == "clear"):
        user_input=""""""
        show=""""""
        lines=0
        clear()
        main()
        print(show,end="")
    elif (len(inp)!=limit):
        clear()
        main()
        print(show,end="")
    else:
        user_input+=inp
        show+=f"{inp}\n"
        lines+=1

count=1
for line in user_input:
    if (line != " "):
        answer[count]=line
    count+=1

answer["l"]=limit
answer["p"]=lines
print(f"\n Kết quả: \n{answer}")
