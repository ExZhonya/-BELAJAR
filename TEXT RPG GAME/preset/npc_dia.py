from preset import utils as u
from preset.utils import cost, money_text
from preset.shop import Shop as s
from preset import balance as b
from plr.player import player

LUMBER = {
	"1": (10, 10),
	"2": (20, 20),
	"3": (30, 30),
}

HUNTER = {
	"1": (10,10),
	"2": (20, 20),
	"3": (30, 30),
}

def _buy_menu(greeting, items, resources, labels, bought, broke):
	msg = ""
	while True:
		u.clear()
		print(greeting)
		print(f"money: {money_text(player.money)}\n")
		for key, (amount, price) in items.items():
			print(f"{key}.{amount} {labels} | {money_text(price)}")
		print("0. Back")
		if msg:
			print(f"\n{msg}")

		x = u.getch()
		if x == "0":
			return
		if x not in items:
			msg = ""
			continue

		amount, price = items[x]
		if player.money >= price:
			player.money -= price
			setattr(player, resources, getattr(player, resources) + amount)
			msg = f"{bought} | +{amount} {labels}"
		else:
			msg = broke

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
		_buy_menu("Ay, Adventurer! What do you need?", LUMBER, "fuel", "Wood",
				  "Will be done soon, boss!", "You don't have enough money, boss.")

	@staticmethod
	def Hunter():
		_buy_menu("Hello, Adventurer. Perhaps you need some meat?", HUNTER, "food", "Food",
				  "Thank you for your purchase.", "Sorry, you don't have enough money.")

if __name__ == '__main__':
	NPC.Trader()