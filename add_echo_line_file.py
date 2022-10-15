a=str(input("Input file: "))
try:
    file=open(a,"r",encoding='utf-8')
    en=[]
    for line in file.readlines():
        en.append(line.strip())
except:
    file=open(a,"r",encoding='latin-1')
    en=[]
    for line in file.readlines():
        en.append(line.strip())
file.close()
file2=open("output.txt","w",encoding='utf-8')
for line in en:
    file2.write("echo {0}\n".format(str(line)))
