#!/bin/python3
# Chuyển đổi toàn bộ file trong path với đuôi file là old_type thành new_type (Chỉ tác động với file có đuôi tệp giống với old_type)
## Ví dụ: khanh.xml > khanh.csv
#  khanh.xml.xml -> khanh.xml.csv
#  xml -> xml
#  khanh-baitap.sh -> khanh-baitap.sh

import os
path = './'
old_type="xml"
new_type="csv"
files = os.listdir(path)
for file in files:
    if os.path.isfile(file):
        temp=file.split(".")
        if (len(temp) > 1):
            if (temp[-1] == old_type):
                del temp[-1]
                new_name=str('.'.join(temp))
                os.rename(os.path.join(path, file), os.path.join(path, f"{new_name}.{new_type}"))