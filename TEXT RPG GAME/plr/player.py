class Player:
	MAX_HEALTH = 100

	def __init__(self):
		self.day = 1
		self.fuel = 0
		self.food = 0
		self.health = self.MAX_HEALTH
		self.money = 30
		self.trader = False
		self.hunter = False
		self.lumberjack = False
		self.base = True
		self.weapon = None
		self.armor = None
		self.inventory = {"weapon": [], "armor": []}
	
	

player = Player()