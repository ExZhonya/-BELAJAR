from preset import utils as u

class shop:
	@staticmethod
	def Weapon():
		u.clear()
		print("""
1. Wooden Sword | 10 Bronze
2. Stone Sword  | 40 Bronze
3. Bronze Sword | 1  Silver
4. Iron Sword   | 5  Silver
5. Diamond Sword| 35 Silver
""")
		x = u.getch()
		