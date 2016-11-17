#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from random import randint
import sys
import warnings
import os
from math import *

warnings.filterwarnings('ignore')

try:
    response = requests.get('https://docs.google.com/spreadsheets/d/1mCibfM5pYqhvJbomy_TJJEafk3vXI-u-upZ6Q5PnmSI/pub?gid=0&single=true&output=tsv')
    if response.status_code == 200:
        multipleLines = response.content.split('\n')
except:
    if os.path.isfile(os.environ['HOME']+"/Downloads/questions - Arkusz1.tsv"):
        with open(os.environ['HOME']+"/Downloads/questions - Arkusz1.tsv", 'r') as content_file:
            multipleLines = content_file.read().split('\n')
    else:
        print ("Nie można pobrać bazy pytań. Ręcznie ściągnij arkusz pytań w formacie tsv pod ścieżkę: "+os.environ['HOME']+"/Downloads/questions - Arkusz1.tsvs")
        sys.exit()





pytania = []
i=-1
length=0
c=' '
last='r'
for line in multipleLines:
    tmp = line.split('\t')
    # if tmp[0] == "": continue
    pytania.append(tmp)
length=len(pytania)
if length<1:
    print ("Błąd przy pobieraniu danych")
    sys.exit()
print ("Baza zawiera "+str(length)+" pytań. \nZakres pytań:")

start = int(raw_input('\nOd: '))
stop = int(raw_input('\nDo: '))


ostatnie = [0]

while True:
    c = sys.stdin.readline()
    if c[0]=="q":
        break
    if c=='\n':
        c=last
    if c[0]=="n":
        last = "n"
        i = (i+1)%stop
    elif c[0]=="i" and len(c)>2:
        i=int(c[2:])
        if i<0 or i>=stop:
            i = 0
    else:
        last = "r"
        los = []
        var = (stop-1-start)%10
        j = randint(0, var)
        while (True):
            if not(j in los):
                break
            else:
                j = randint(0, var)

        if (len(los)>=var):
            los = []
        else:
            los.append(j)

        i = randint(0,10)
        wylosowany = j+i

        while (True):
            i = randint(start,stop-1)
            if not(i in ostatnie):
                break
            elif len(ostatnie)==stop:
                print ("Koniec")
                exit(0)



        ostatnie.append(i)
        rozmiar = stop+2-len(ostatnie)-start

    print ("- - - - - - - - - -\nPytanie "+str(i)+" -- ["+str(rozmiar)+" left]: ")
    print (pytania[i][0])
    command = sys.stdin.readline()
    print ("-> "+pytania[i][1])
    odp = sys.stdin.readline()
    if odp[0]=="r":
    	print ("repeat")
    	ostatnie.remove(i)
