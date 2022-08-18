#!/bin/python3
## Làm tăng 1 chuỗi, nếu chuỗi kết thúc bằng số thì cộng thêm 1, nếu chuỗi không có số thì thêm số 1
## VD: foo -> foo1
# khanh12 -> khanh13
# khanh0 -> khanh1
# khanh999 -> khanh1000

import string
def main(a):
    get_str = str(a.rstrip(string.digits))
    get_int = a[len(get_str):]
    if (get_int == ""):
        return get_str + "1"
    else:
        return get_str + str(int(get_int) + 1)

print(main("foo"))
print(main("khanh12"))
print(main("khanh0"))
print(main("khanh999"))