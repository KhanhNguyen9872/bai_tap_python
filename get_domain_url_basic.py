#!/bin/python3
## Lấy Domain name từ URL (Cơ bản) (Nếu là IP thì in ra màn hình)
## VD: https://google.com.vn -> google
# http://youtube.com -> youtube
# https://www.mediafire.com -> mediafire
# https://google.co.jp -> google
# https://dashboard.ngrok.com -> ngrok
# https://raw.githubusercontent.com -> githubusercontent
# https://github.com/KhanhNguyen9872 -> github
# http://127.0.0.1 -> 127.0.0.1

except_name=["http", "https", "www", "dashboard", "raw"]

def domain_name(url):
    url=url.split("://")
    ip=' '.join(url).split("/")
    ip=' '.join(ip).split(" ")
    try:
        int(ip[1].replace(".", ""))
        url=ip.copy()
    except:
        url=' '.join(url).split(".")
        url=' '.join(url).split(" ")
    for ex in except_name:
        try:
            url.remove(ex)
        except:
            pass
    return url[0]

print(domain_name("https://google.com.vn"))
print(domain_name("http://youtube.com"))
print(domain_name("https://www.mediafire.com"))
print(domain_name("https://google.co.jp"))
print(domain_name("https://dashboard.ngrok.com"))
print(domain_name("https://raw.githubusercontent.com"))
print(domain_name("https://github.com/KhanhNguyen9872"))
print(domain_name("http://127.0.0.1"))

    