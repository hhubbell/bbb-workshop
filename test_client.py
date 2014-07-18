#!/usr/bin/python

import requests

myData = {'temp':12}
requests.post('http://10.10.4.175:8888', data=myData)


