import map_ as m
import no_input as getch
import cutscenes as cs
import os, time, sys


def clear(): #cls for win and clear for linux, apparently it'll show error code if i kept use "cls;clear"
	if sys.platform == "win32":
		os.system("cls")
	else:
		os.system("clear")

if sys.platform == "win32":
	import msvcrt

	def getch():
		return msvcrt.getch().decode('utf-8')

else:
	import tty
	import termios

	def getch():
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(fd)
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch

def clear(): #cls for win and clear for linux, apparently it'll show error code if i kept use "cls;clear"
	if sys.platform == "win32":
		os.system("cls")
	else:
		os.system("clear")

while True:
	clear()
	print(r"""
         ,-.-.     ,----.              _,.----.     _,.---._           ___      ,----.  
,-..-.-./  \==\ ,-.--` , \   _.-.    .' .' -   \  ,-.' , -  `.  .-._ .'=.'\  ,-.--` , \ 
|, \=/\=|- |==||==|-  _.-` .-,.'|   /==/  ,  ,-' /==/_,  ,  - \/==/ \|==|  ||==|-  _.-` 
|- |/ |/ , /==/|==|   `.-.|==|, |   |==|-   |  .|==|   .=.     |==|,|  / - ||==|   `.-. 
 \, ,     _|==/==/_ ,    /|==|- |   |==|_   `-' \==|_ : ;=:  - |==|  \/  , /==/_ ,    / 
 | -  -  , |==|==|    .-' |==|, |   |==|   _  , |==| , '='     |==|- ,   _ |==|    .-'  
  \  ,  - /==/|==|_  ,`-._|==|- `-._\==\.       /\==\ -    ,_ /|==| _ /\   |==|_  ,`-._ 
  |-  /\ /==/ /==/ ,     //==/ - , ,/`-.`.___.-'  '.='. -   .' /==/  / / , /==/ ,     / 
  `--`  `--`  `--`-----`` `--`-----'                `--`--''   `--`./  `--``--`-----``  
                                                                               
Welcome to the the amazing digital world! You will live as a stranded person in an camp alone- for now!

		    Please Choose One of The Options.
				1. START
				2. QUIT
			  """)
	x = getch()
	if x == "1":
		cs.start()
	elif x == "2":
		quit
