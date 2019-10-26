#!/usr/bin/env python3

# FakeNnections
# Author: Aldas - https://github.com/axdz

try:
	#importing requirements
	import json
	import time
	import requests
	from termcolor import colored
	from getpass import getpass
	
	#function to login to check if token is valid
	def checktoken(token):
		"""checks if token is valid"""
		headers = {
		"authorization": token
		}
		src = requests.get('https://discordapp.com/api/v6/auth/login', headers=headers)
		global tokenvalid
		if src.status_code == 200:
			print(colored('Token is valid', 'green'))
			tokenvalid = True
		else:
			print(colored('Token is invalid', 'red'))
			tokenvalid = False
			
	
	#function for connecting
	def connect(token, type, id, name):
		"""function to add the connection"""
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
	token_input = True
	while token_input:
		try:
			usertoken = getpass(f"[{colored('*', 'red')}] Token: ")
			checktoken(usertoken)
			if tokenvalid == True:
				token_input = False
			else:
				continue
		except Exception:
			print('Error has occured!')
	
	
	#options for connections
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
	
	
	#name input for connection
	print(colored('Just press enter if you wanna have an invisible name', 'magenta'))
	name = input(f"[{colored('*', 'red')}] Name: ")
	if name == '':
		name = "ㅤ"
	else:
		pass
	
	
	#id of the connection
	print(colored('Just press enter if you want it to generate an id', 'magenta'))
	id = input(f"[{colored('+', 'green')}] Id: ")
	if id == '':
		id = round(time.time() * 1)
	else:
		pass
	
	#executes the function to add the connection based on all the other options
	connect(usertoken, choice, id, name)

#if user tries to close the script by using CTRL + C combination
except KeyboardInterrupt:
	print(colored('\nBye!', 'green'))
	exit()
	
#if some packages arent installed
except ImportError:
	print('''Please install packages from requirements.txt
Use command "pip install -r requirements.txt" to install all the required plugins''')