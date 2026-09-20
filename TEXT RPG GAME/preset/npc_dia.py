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




if __name__ == '__main__':
	NPC.Trader()