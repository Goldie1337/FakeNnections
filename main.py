#importing requirements
import json
import time
import requests
from termcolor import colored
from getpass import getpass


#function for connecting
def connect(type, id, name):
	url = f'https://canary.discordapp.com/api/v6/users/@me/connections/{type}/{id}'
	
	data = {'name': name,
	 			'visibility': 1
	 			}
	
	headers = {'content-type': 'application/json', 
	'authorization': 'NDcyMzQ0NDgxMTY5OTMyMjg4.XVwO8A.9qZ4NGPYgEPCIJ2W47nrposwPl8'
	}
	
	response = requests.put(url, data=data, headers=headers)
	
	res = response.json()
	
	print(res)


#token
usertoken = getpass(f"[{colored('*', 'red')}] Token: ")


#options
print(f"[{colored('1', 'magenta')}] Skype")
print(f"[{colored('2', 'magenta')}] Battle.net")
print(f"[{colored('3', 'magenta')}] League of Legends")
userchoice = int(input('> '))
if userchoice == 1:
	choice = 'skype'
elif userchoice == 2:
	choice = 'battlenet'
elif userchoice == 3:
	choice = 'leagueoflegends'
else:
	print('Invalid choice')
	exit()


#name
print('Just press enter if you wanna have an invisible name')
name = input(f"[{colored('*', 'red')}] Name: ")


#id
print('Just press enter if you want it to generate an id')
id = input(f"[{colored('+', 'green')}] Id: ")
if id == '':
	id = round(time.time() * 1)
else:
	pass

#executes the function to connect
connect(choice, id, name)