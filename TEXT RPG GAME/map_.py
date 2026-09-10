import time, os, sys
import no_input as getch

def clear(): #cls for win and clear for linux, apparently it'll show error code if i kept use "cls;clear"
	if sys.platform == "win32":
		os.system("cls")
	else:
		os.system("clear")

def delay_print_m(s):
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.2)

def delay_print_f(s):
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.1)


class Base:
	def camp():
		print
