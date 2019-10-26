#importing requirements
import json
import time
import requests
from termcolor import colored
from getpass import getpass


		

#function for connecting
def connect(token, type, id, name):
	url = f'https://canary.discordapp.com/api/v6/users/@me/connections/{type}/{id}'
	
	data = {'name': name,
	 			'visibility': 1
	 			}
	
	headers = {'content-type':'application/json', 
	'authorization':token
	}
	
	response = requests.put(url, data=json.dumps(data), headers=headers)
	if response.status_code == 200:
		print(colored(f'Connected {type} with username "{name}"', "green"))
	elif response.status_code == 401:
		print(colored('Authorization error!', 'red'))
	else:
		print(colored('Error has occured it seems like', 'red'))
		print(response.text)


#token
usertoken = getpass(f"[{colored('*', 'red')}] Token: ")


#options
options_menu = True
while options_menu:
	try:
		print(f"[{colored('1', 'magenta')}] Skype")
		print(f"[{colored('2', 'magenta')}] Battle.net")
		print(f"[{colored('3', 'magenta')}] League of Legends")
		userchoice = int(input('> '))
		if userchoice == 1:
			choice = 'skype'
			options_menu = False
		elif userchoice == 2:
			choice = 'battlenet'
			options_menu = False
		elif userchoice == 3:
			choice = 'leagueoflegends'
			options_menu = False
		else:
			print(colored('Invalid choice!', 'red'))
			continue
		
		
	except ValueError:
		print(colored('Invalid choice!', 'red'))
		continue
		
	except KeyboardInterrupt:
		print(colored('Bye!', 'green'))
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
connect(usertoken, choice, id, name)