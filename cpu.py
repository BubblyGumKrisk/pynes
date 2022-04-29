from opcodes import opcodes


class INS:
	def __init__(self, name, mode, cycles):
		self.name = name
		self.mode = mode
		self.cycles = cycles


class CPU:
	def __init__(self):
		self.bus = None

		self.ops = []
		for op in opcodes:
			self.ops.append(INS(op["name"], op["mode"], op["cycles"]))

		self.a = 0x00
		self.x = 0x00
		self.y = 0x00
		self.stkp = 0x00
		self.pc = 0x00
		self.status = 0x00

		self.addr_abs = 0x0000
		self.addr_rel = 0x00
		self.opcode = 0x00
		self.cycles = 0x00

	def read(self, addr):
		if self.bus:
			self.bus.read(addr)
		return 0

	def write(self, addr, data):
		if self.bus:
			self.bus.write(addr, data)