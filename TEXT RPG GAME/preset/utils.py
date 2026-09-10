import sys, os, time

def clear():
	os.system("cls" if sys.platform == "win32" else "clear")

if sys.platform == "win32":
	import msvcrt
	def getch():
		return msvcrt.getch().decode('utf-8')
else:
	import tty, termios
	def getch():
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(fd)
			return sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def _delay_print(text, delay):
	for c in text:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(delay)
	print()

def v_fast_print(text): _delay_print(text, 0.01)
def fast_print(text):   _delay_print(text, 0.03)
def slow_print(text):   _delay_print(text, 0.05)