import os, subprocess

import sys

print(sys.version)


os.environ['PATH'] += r';D:/Bitnami/djangostack-2.2.5-0/python/'
cmds = "python.exe D:/repositorydef/SeismicRisk/python3/connect_jdbc.py > D:/log/log.txt"

cmds = ["python.exe", "D:/repositorydef/SeismicRisk/python3/connect_jdbc.py", ">", "D:/log/log.txt"]


#subprocess.call(["ls", "-l"])
subprocess.call(cmds, shell=True)


try:
     5/0
except ZeroDivisionError as err: # 'as' is needed in Python 3.x
     print (err, 'Error Caused')


#exec(open("D:/repositorydef/SeismicRisk/python3/ejecutar.py").read())

#exec(open("D:/repositorydef/SeismicRisk/python3/ejecutar.py").read())
