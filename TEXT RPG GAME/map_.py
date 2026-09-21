import random
from preset import utils as u
from preset import npc_dia as n
from plr.player import player

class Base:
	@staticmethod
	def camp():
		u.clear()
		print(rf"""
		You are in the Camp.
		Fuel: {player.fuel}  Food: {player.food}  Health: {player.health} Money: {u.money_text(player.money)}
		1. Find Fuel
		2. Find Food
		3. Explore
		9. NPC
		0. Quit(No Save!)
		""")
		x = u.getch()
		if x == "1":
			Base.chop_wood()
		elif x == "2":
			Base.find_food()
		elif x == "3":
			Base.explore()
		elif x == "9":
			Base.NPC()
		elif x == "0":
			return False
		return True

	@staticmethod
	def chop_wood():
		u.clear()
		gained = random.randint(1, 3)
		player.fuel += gained
		u.slow_print(f"You gain {gained} fuel.")
		u.getch()

	@staticmethod
	def find_food():
		u.clear()
		gained = random.randint(1, 3)
		player.food += gained
		u.slow_print(f"You gain {gained} food.")
		u.getch()

	@staticmethod
	def explore():
		u.clear()
		gained = random.randint(1, 3)
		player.money += gained
		u.slow_print(f"You gained {gained} money.")
		u.getch()

	@staticmethod
	def NPC():
		while True:
			u.clear()
			print("===== NPC =====")
			if player.trader:
				print("1. Trader")
			if player.hunter:
				print("2. Hunter")
			if player.lumberjack:
				print("3. Lumberjack")
			print("0. Back")

			x = u.getch()
			if x == "1" and player.trader:
				n.NPC.Trader()
			elif x == "2" and player.hunter:
				pass
			elif x == "3" and player.lumberjack:
				n.NPC.Lumberjack()
			elif x == "0":
				return

if __name__ == '__main__':
	while Base.camp():
		pass