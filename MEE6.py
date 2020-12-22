import discord
import asyncio
from discord.ext import tasks
from discord.ext import commands
import os
import ctypes
from colorama import init, Fore, Back, Style
from datetime import datetime

init(convert=True)
def settings():
 os.system('mode con: cols=75 lines=10')
 ctypes.windll.kernel32.SetConsoleTitleW("MEE6 Tool - remix#9999")
def gettime():
   now = datetime.now()
   global current_time
   current_time = now.strftime("%H:%M:%S")
def info():
 global token
 gettime()
 token = input(Fore.CYAN + '[' + current_time + '] Discord Token:')
 os.system('cls')
 global idn
 gettime()
 idn = int(input(Fore.CYAN + '[' + current_time + '] Channel ID: '))
 os.system('cls')
 global message
 gettime()
 message = input(Fore.CYAN + '[' + current_time + '] Message: ')
 os.system('cls')
 global inv
 gettime()
 inv = int(input(Fore.CYAN + '[' + current_time + '] Message Interval: '))
 os.system('cls')
def design():
 logo = Fore.CYAN + '''
 \t\t ███╗   ███╗███████╗███████╗ ██████╗
 \t\t ████╗ ████║██╔════╝██╔════╝██╔════╝
 \t\t ██╔████╔██║█████╗  █████╗  ███████╗
 \t\t ██║╚██╔╝██║██╔══╝  ██╔══╝  ██╔═══██╗
 \t\t ██║ ╚═╝ ██║███████╗███████╗╚██████╔╝
 \t\t ╚═╝     ╚═╝╚══════╝╚══════╝ ╚═════╝
                                    '''

 print(logo)
 print(Fore.CYAN + '\t\t [' + current_time + ']' + '\t\t [' + client.user.name + '#' +  client.user.discriminator + ']')

settings()
gettime()
info()

client = discord.Client()


@client.event
async def on_ready():
	print(Fore.CYAN + '[' + current_time + '] Connected!')
	sendit.start()
	change_status.start()

@tasks.loop(seconds=0.0001)
async def sendit():
	general_channel = client.get_channel(idn)
	await general_channel.send(message)
	os.system('cls')
	gettime()
	design()

client.run(token, bot=False)
