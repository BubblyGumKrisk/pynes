class Bus:
	def __init__(self, cpu):
		self.ram = []
		for i in range(64*1024):
			self.ram.append(0)
		self.cpu = cpu

	def write(self, addr, data):
		if addr >= 0000 and addr <= 0xFFFF:
			self.ram[addr] = data

	def read(self, addr, readonly = False):
		if addr >= 0000 and addr <= 0xFFFF:
			return self.ram[addr]
		return 0