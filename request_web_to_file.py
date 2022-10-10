try:
    import requests,sys
except:
    import os,sys
    if os.name=='nt':
        os.system("python -m pip install requests")
    else:
        os.system("python3 -m pip install requests")
    import requests
web=requests.get("http://{0}:{1}/{2}".format(sys.argv[1],sys.argv[2],sys.argv[3]))
file=open(sys.argv[3], "w")
file.write(web.text)
file.close()