import time, os, sys
import map_ as m


def clear(): #cls for win and clear for linux, apparently it'll show error code if i kept use "cls;clear"
	if sys.platform == "win32":
		os.system("cls")
	else:
		os.system("clear")


# Source - https://stackoverflow.com/a/9246096
# Posted by Andrew Walker, modified by community. See post 'Timeline' for change history
# Retrieved 2026-09-10, License - CC BY-SA 3.0

import time
import sys

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


def start():
	clear()
	print(".")
	time.sleep(1.5)
	print(".")
	time.sleep(1.5)
	print(".")
	time.sleep(1.5)
	delay_print_f("It's dark. You don't know where you are.")
	time.sleep(2)
	print(".")
	time.sleep(1.5)
	print(".")
	time.sleep(1.5)
	print(".")
	time.sleep(1.5)
	delay_print_m("You slowly opens your eyes.")
