import sys, subprocess, os

#subprocess.check_output(["echo", "Hello World!"]# )

os.chdir("C:")

#subprocess.call(["echo", "Hello World!"])

subprocess.call(["echo"])


print ("version ")
print (sys.version)
a=1
b=2
d=3
x ="The story of {0}, {1}, and {c}".format(a, b, c=d)
print (x)

#exec(open("D:/repositorydef/SeismicRisk/python3/instruciones_python3.py").read())