import os

def clear():
	if (os.name == 'nt'):
		os.system('cls')
	else:
		os.system('clear')

error=1
morse2text={".-":"A","-...":"B","-.-.":"C","-..":"D",".":"E","..-.":"F","--.":"G","....":"H","..":"I",".---":"J","-.-":"K",".-..":"L","--":"M","-.":"N","---":"O",".--.":"P","--.-":"Q",".-.":"R","...":"S","-":"T","..-":"U","...-":"V",".--":"W","-..-":"X","-.--":"Y","--..":"Z",".--.-":"Â","-..-.":"Ê","---.":"Ô","-----":" "}
text2morse={v: k for k, v in morse2text.items()}

if (__name__ == '__main__'):
	try:
		while 1:
			clear()
			chon = input('''
 ===> TRÌNH DỊCH VÀ CHUYỂN ĐỔI MÃ MORSE <===
	1. Dịch mã morse.
	2. Chuyển sang mã morse.
	3. Thoát.
	===================================
Nhập lựa chọn: ''')
			if chon == '1':
				print("\nNhập mã morse: ",end="")
				list=[str(x) for x in input().split(" ")]
				for i in list:
					try:
						print(morse2text[i],end="")
					except:
						continue
			elif chon == '2':
				print("\nNhập văn bản cần chuyển sang morse: ",end="")
				list=[char for char in input().upper()]
				for i in list:
					try:
						print(text2morse[i],end=" ")
					except:
						continue
			elif chon == '3':
				clear()
				print("\nBạn đã thoát chương trình!")
			else:
				continue
			print("\n")
			error=0
			exit()
	except:
		if (error == "1"):
			print("\nChương trình gặp lỗi!\n Hãy liên hệ nhà phát triển!\n\n")
		exit()