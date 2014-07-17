#!/usr/bin/python


import requests


myData = {'id':1, 'temp':12}

r1 = requests.post('localhost:8888', data=myData)




