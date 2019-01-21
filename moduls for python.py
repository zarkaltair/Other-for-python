# import os
# import time
# from sys import version


# print(os.getcwd())
# print()
# print(time.localtime())
# print()
# print(version)
# print()
# print(dir(time))
# print()



# import requests


# check internet connection
# def internetConnection():
# 	try:
# 		requests.get('http://google.com', timeout=3)
# 		print('connected')
# 	except requests.exceptions.ConnectionError:
# 		print('not connected')
		
# internetConnection()



import requests


# отключение SSL
url = 'https://free-proxy-list.net/'
response = requests.get(url, verify=False)
print(response)