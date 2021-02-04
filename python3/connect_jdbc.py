#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
import sys

con = None

try:
    import os

    dirpath = os.getcwd()
    print("current directory is : " + dirpath)
    foldername = os.path.basename(dirpath)
    print("Directory name is : " + foldername)


except:
    print ("")

try:

    con = psycopg2.connect(database='postgres', user='postgres',
        password='postgres')

    cur = con.cursor()
    cur.execute('SELECT version()')

    #cur.execute('SELECT * from article')


    version = cur.fetchone()[0]
    print(version)

except psycopg2.DatabaseError as e:

    print('Error {e}')
    #sys.exit(1)

finally:

    if con:
        con.close()

'''
filename = "D:/repositorydef/SeismicRisk/python3/connect_jdbc.py"
exec(open(filename).read())

filename = "D:/repositorydef/SeismicRisk/python3/compiler_pyqt5.py"
exec(open(filename).read())

'''

'''

'D:\Bitnami\djangostack-2.2.5-0\python\python.exe' 'D:\repositorydef\SeismicRisk\python3\connect_jdbc.py'  

'D:/Bitnami/djangostack-2.2.5-0/python/python.exe' 'D:/repositorydef/SeismicRisk/python3/connect_jdbc.py'  

set PYTHONPATH='D:/ProgramFiles/apps/Python37'

instruction for instalations
https://github.com/addisonElliott/pyqt5ac

pip install pyqt5ac

'''