from preset import utils as u

class NPC:
	@staticmethod
	def Trader():
		u.clear()
		print("Welcome, Adventurer! I have everything you need.\nWhat do you want to buy?")
		print(f"{'-'*10}\n1.Weapon\n2.Armor\n3.Food\n0.Back")
		x = u.getch()
		if x == "1":
			pass
		elif x == "2":
			pass
		elif x == "3":
			pass
		elif x == "0":
			import map_ as m
			m.Base.camp()
		else:
			NPC.Trader()

	@staticmethod
	def Lumberjack():
		import plr.player as p
		print("Ay, Adventurer. What do you need?\n1.+10 Wood | 1 silver\2.+20 Wood | 2 silver\n3.+30 Wood | 3 silver\n0.Back")
		x = u.getch()
		if x == "1":
			if p.player.money >= 10:
				print("Will be done soon, boss.\n+10 Wood")
				p.player.money -= 10
				u.getch()
			elif p.player.money < 10:
				print("You don't have enough money.")
				u.getch()
		elif x == "2":
			if p.player.money >= 20:
				print("Will be done soon, boss.\n+20 Wood")
				p.player.money -= 20
				u.getch()
			elif p.player.money < 20:
				print("You don't have enough money.")
		elif x == "3":
			if p.player.money >= 30:
				print("Will be done soon, boss.\n+30 Wood")
				p.player.money -= 30
				u.getch()
			elif p.player.money < 30:
				print("You don't have enough money.")
		elif x == "0":
			return
		else:
			NPC.Trader()
			




if __name__ == '__main__':
	NPC.Trader()