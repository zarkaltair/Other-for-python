import os
import time
from sys import version


print(os.getcwd())
print()
print(time.localtime())
print()
print(version)
print()
print(dir(time))
print()


import requests


def internetConnection():
	try:
		requests.get('http://google.com', timeout=3)
		print('connected')
	except requests.exceptions.ConnectionError:
		print('not connected')
		
internetConnection()