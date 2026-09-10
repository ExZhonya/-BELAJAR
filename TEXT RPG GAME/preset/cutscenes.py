import time, os, sys
from preset import utils as u

def start():
	u.clear()
	print(".")
	time.sleep(1.5)
	print(".")
	time.sleep(1.5)
	print(".")
	time.sleep(1.5)
	u.slow_print("It's dark. You don't know where you are.")
	time.sleep(2)
	print(".")
	time.sleep(1.5)
	print(".")
	time.sleep(1.5)
	print(".")
	time.sleep(1.5)
	u.slow_print("You slowly opens your eyes and sees that you're in some kind of camp.")
	import map_ as m
	m.Base.camp()


