class Player:
	def __init__(self):
		self.fuel = 0
		self.food = 0
		self.health = 100
		self.money = 30
		self.trader = True
		self.hunter = False
		self.lumberjack = False
		self.base = True
		self.weapon = None
		self.armor = None
		self.inventory = {"weapon": [], "armor": []}
	
	

player = Player()