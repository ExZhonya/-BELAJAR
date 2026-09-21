from preset import utils as u
from preset.shop import shop as s
from plr.player import player

LUMBER = {
	"1": (10, 10),
	"2": (20, 20),
	"3": (30, 30),
}

class NPC:
	@staticmethod
	def Trader():
		while True:
			u.clear()
			print("Welcome, Adventurer! I have everything you need.\nWhat do you want to buy?")
			print(f"{'-'*10}\n1.Weapon\n2.Armor\n3.Food\n0.Back")
			x = u.getch()
			if x == "1":
				s.Weapon()
			elif x == "2":
				s.Armor()
			elif x == "3":
				pass
			elif x == "0":
				return

	@staticmethod
	def Lumberjack():
		msg = ""
		while True:
			u.clear()
			print("Ay, Adventurer! What do you need?")
			for key, (wood, price) in LUMBER.items():
				print(f"{key}.+{wood} Wood | {u.money_text(price)}")
			print("0.Back")
			if msg:
				print(f"\n{msg}")

			x = u.getch()
			if x == "0":
				return
			if x not in LUMBER:
				msg = ""
				continue

			wood, price = LUMBER[x]
			if player.money >= price:
				player.money -= price
				player.fuel += wood
				msg = f"Will be done soon, boss! | +{wood} Wood"
			else:
				msg = "You don't have enough money, boss."

if __name__ == '__main__':
	NPC.Trader()