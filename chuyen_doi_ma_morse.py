import os

def clear():
    if (os.name == 'nt'):
        os.system('cls')
    else:
        os.system('clear')

error=1
dichMorse={".-":"A","-...":"B","-.-.":"C","-..":"D",".":"E","..-.":"F","--.":"G","....":"H","..":"I",".---":"J","-.-":"K",".-..":"L","--":"M","-.":"N","---":"O",".--.":"P","--.-":"Q",".-.":"R","...":"S","-":"T","..-":"U","...-":"V",".--":"W","-..-":"X","-.--":"Y","--..":"Z",".--.-":"Â","-..-.":"Ê","---.":"Ô","-----":" "}
chuyenKiTuSangMorse={"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..","Â":".--.-","Ê":"-..-.","Ô":"---."," ":"-----"}

if (__name__ == '__main__'):
    while 1:
        try:
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
                        print(dichMorse[i],end="")
                    except:
                        continue
            elif chon == '2':
                print("\nNhập văn bản cần chuyển sang morse: ",end="")
                list=[char for char in input().upper()]
                for i in list:
                    try:
                        print(chuyenKiTuSangMorse[i],end=" ")
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
        except KeyboardInterrupt:
            print("\n\n==============================\n\nBạn không thể thoát bằng Ctrl + C\n Vui lòng chọn Thoát trong menu để thoát!\n\n==============================\n\nBấm phím Enter để tiếp tục!\n")
            input()
            continue
        except:
            if (error == "1"):
                print("\nChương trình gặp lỗi!\n Hãy liên hệ nhà phát triển!\n\n")
            exit()