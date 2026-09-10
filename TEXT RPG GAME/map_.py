# map_.py
import random
from preset import utils as u
from plr.player import player

class Base:
	@staticmethod
	def camp():
		u.clear()
		print(rf"""
	You are in the Camp.
	Fuel: {player.fuel}  Food: {player.food}  Health: {player.health} Money: {player.money}
	1. Find Fuel
	2. Find Food
	3. Explore
	0. Quit(No Save!)
""")
		x = u.getch()
		if x == "1":
			Base.chop_wood()
		elif x == "2":
			Base.find_food()
		elif x == "3":
			pass
		elif x == "0":
			from preset import wc_gb
			wc_gb.bye_asc()
			wc_gb.bye_text()

	@staticmethod
	def chop_wood():
		gained = random.randint(1, 3)
		player.fuel += gained
		u.slow_print(f"You gain {gained} fuel.")
		u.getch()
		Base.camp()

	@staticmethod
	def find_food():
		gained = random.randint(1, 3)
		player.food += gained
		u.slow_print(f"You gain {gained} food.")
		u.getch()
		Base.camp()


if __name__ == '__main__':
	Base.camp()