from opcodes import opcodes

class INS:
	def __init__(self, name, opcode, mode, cycles):
		self.name = name
		self.opcode = opcode
		self.mode = mode
		self.cycles = cycles


class CPU:
	def __init__(self):
		self.bus = None

		self.ops = []
		
		for op in self.getops():
			self.ops.append(INS(op["name"], op["opcode"], op["mode"], op["cycles"]))

		self.a = 0
		self.x = 0
		self.y = 0
		self.stkp = 0
		self.pc = 0
		self.status = 0

		self.addr_abs = 0
		self.addr_rel = 0
		self.opcode = None
		self.cycles = 0
		
		self.fetched = 0
		
	def getop(self):
		for op in self.ops:
			if op.opcode == self.opcode:
				return op

	def read(self, addr):
		if self.bus:
			self.bus.read(addr)
		return 0

	def write(self, addr, data):
		if self.bus:
			self.bus.write(addr, data)
	
	def clock(self):
		if self.cycles == 0:
			self.opcode = self.read(self.pc)
			self.pc += 1
			
			op = self.getop()
			
			cycles = op.cycles
			
			moderes = op.mode()
			nameres = op.name()
			cycles += (modres and nameres)
		cycles -= 1
		
		# flags
		
	def getflag(f):
		return 1 if ((status & f) > 0) else 0
	
	def setflag(f, v):
		if v:
			status |= f
		else:
			status &= ~f
	
	# Addr Mode
	def IMP(self):
		self.fetched = self.a
		return 0
	
	def IMM(self):
		self.addr_abs = self.pc
		pc += 1
		return 0
	
	def ZPO(self):
		self.addr_abs = self.read(self.pc)
		pc += 1
		self.addr_abs &= 0x00FF
		return 0
	
	def ZPX(self):
		self.addr_abs = (self.read(self.pc) + self.x)
		self.pc += 1
		self.addr_abs &= 0x00FF
		return 0
	
	def ZPY(self):
		self.addr_abs = (self.read(self.pc) + self.y)
		self.pc += 1
		self.addr_abs &= 0x00FF
		return 0
	
	def REL(self):
		self.addr_rel = self.read(self.pc)
		self.pc += 1
		if self.addr_rel and 0x80:
			self.addr_rel |= 0xFF00
		return 0
	
	def ABS(self):
		lo = self.read(self.pc)
		self.pc += 1
		hi = self.read(self.pc)
		self.pc += 1
		
		self.addr_abs = (hi << 8) | lo
		return 0
	
	def ABX(self):
		lo = self.read(self.pc)
		self.pc += 1
		hi = self.read(self.pc)
		self.pc += 1
		
		self.addr_abs = (hi << 8) | lo			
		self.addr_abs += self.x

		if (self.addr_abs and 0xFF00) != (hi << 8):
			return 1
		else:
			return 0

	def ABY(self):
		lo = self.read(self.pc)
		self.pc += 1
		hi = self.read(self.pc)
		self.pc += 1

		self.addr_abs = (hi << 8) | lo
		self.addr_abs += self.y

		if (self.addr_abs and 0xFF00) != (hi << 8):
			return 1
		else:
			return 0

		ptrlo = self.read(self.pc)
		self.pc += 1
		ptrhi = self.read(self.pc)
		self.pc += 1

		ptr = (ptrhi << 8) | ptrlo

		if ptrlo == 0x00FF:
			self.addr_abs = (self.read(ptr & 0xFF00) << 8) | self.read(ptr + 0)
		else:
			self.addr_abs = (self.read(ptr + 1) << 8) | self.read(ptr + 0)
			return 0

	def IZX(self):
		t = self.read(self.pc)
		self.pc += 1

		lo = self.read((t + self.x) & 0x00FF)
		hi = self.read((t + self.x + 1) & 0x00FF)

		self.addr_abs = (hi << 8) | lo
		return 0

	def IZY(self):
		t = self.read(self.pc)
		self.pc += 1

		lo = self.read(t & 0x00FF)
		hi = self.read((t + 1) & 0x00FF)

		self.addr_abs = (hi << 8) | lo

		self.addr_abs += y

		if (self.addr_abs & 0xFF00) != (hi << 8):
			return 1
		else:
			return 0


	def fetch(self):
		if not (self.getop().mode == IMP):
			self.fetched = self.read(self.addr_abs)
		return self.fetched


	# ops
	C = (1 << 0)
	Z = (1 << 1)
	I = (1 << 2)
	D = (1 << 3)
	B = (1 << 4)
	U = (1 << 5)
	V = (1 << 6)
	N = (1 << 7)

	def ADC(self):
		pass

	def AND(self):
		a = a & self.fetch(self)
		self.setflag(Z, a == 0)
		self.setflag(N, a & 0x80)
		return 1

	def ASL(self):
		self.fetch(self)
		temp = self.fetched << 1
		self.setflag(C, (temp & 0xFF00) > 0)
		self.setflag(Z, (temp & 0x00FF) == 0)
		self.setflag(N, temp & 0x80)
		if self.getop().mode == self.IMP:
			self.a = temp & 0x00FF
		else:
			self.write(self.addr_abs, temp & 0x00FF)
		return 0

	def BCC(self):
		if self.getflag(C) == 0:
			self.cycles += 1
			self.addr_abs = self.pc + self.addr_rel
			if (self.addr_abs & 0xFF00) != (self.pc & 0xFF00):
				cycles += 1
				
			self.pc = self.addr_abs
		return 0

	def BCS(self):
		if self.getflag(C) == 1:
			cycles += 1
			self.addr_abs = self.pc + self.addr_rel
			
			if (self.addr_abs & 0xFF00) != (self.pc & 0xFF00):
				self.cycles += 1
				
			self.pc = self.addr_abs
		return 0

	def BEQ(self):
		if self.getflag(Z) == 1:
			cycles += 1
			self.addr_abs = self.pc + self.addr_rel
			
			if (self.addr_abs & 0xFF00) != (self.pc & 0xFF00):
				self.cycles += 1
				
			self.pc = self.addr_abs
		return 0

	def BIT(self):
		fetch()
		temp = a & self.fetched
		self.setflag(Z, (temp & 0x00FF) == 0)
		self.setflag(N, self.fetched & (1 << 7))
		self.setflag(V, self.fetched & (1 << 6))
		return 0

	def BMI(self):
		if self.getflag(N) == 1:
			cycles += 1
			self.addr_abs = self.pc + self.addr_rel
			
			if (self.addr_abs & 0xFF00) != (self.pc & 0xFF00):
				self.cycles += 1
				
			self.pc = self.addr_abs
		return 0

	def BNE(self):
		if self.getflag(Z) == 0:
			cycles += 1
			self.addr_abs = self.pc + self.addr_rel
			
			if (self.addr_abs & 0xFF00) != (self.pc & 0xFF00):
				self.cycles += 1
				
			self.pc = self.addr_abs
		return 0

	def BPL(self):
		if self.getflag(N) == 0:
			cycles += 1
			self.addr_abs = self.pc + self.addr_rel
			
			if (self.addr_abs & 0xFF00) != (self.pc & 0xFF00):
				self.cycles += 1
				
			self.pc = self.addr_abs
		return 0

	def BRK(self):
		self.pc += 1
		
		self.setflag(I, 1)
		self.write(0x0100 + self.stkp, (self.pc >> 8) & 0x00FF)
		self.stkp -= 1
		self.write(0x0100 + self.stkp, self.pc & 0x00FF)
		self.stkp -= 1
		
		self.setflag(B, 1)
		self.write(0x0100 + self.stkp, self.status)
		self.stkp -= 1
		self.setflag(B, 0)
		
		self.pc = self.read(0xFFFE) | (self.read(0xFFFF) << 8)
		return 0
		
	def BVC(self):
		if self.getflag(V) == 0:
			cycles += 1
			self.addr_abs = self.pc + self.addr_rel
			
			if (self.addr_abs & 0xFF00) != (self.pc & 0xFF00):
				self.cycles += 1
				
			self.pc = self.addr_abs
		return 0

	def BVS(self):
		if self.getflag(V) == 1:
			cycles += 1
			self.addr_abs = self.pc + self.addr_rel
			
			if (self.addr_abs & 0xFF00) != (self.pc & 0xFF00):
				self.cycles += 1
				
			self.pc = self.addr_abs
		return 0

	def CLC(self):
		self.setflag(C, False)
		return 0

	def CLD(self):
		self.setflag(D, False)
		return 0

	def CLI(self):
		self.setflag(I, False)
		return 0

	def CLV(self):
		self.setflag(V, False)
		return 0

	def CMP(self):
		self.fetch()
		temp = self.a - self.fetched
		self.setflag(C, self.a >= self.fetched)
		self.setflag(Z, (temp & 0x00FF) == 0)
		self.setflag(N, temp & 0)
		return 1

	def CPX(self):
		self.fetch()
		temp = self.x - self.fetched
		self.setflag(C, self.a >= self.fetched)
		self.setflag(Z, (temp & 0x00FF) == 0)
		self.setflag(N, temp & 0)
		return 1

	def CPY(self):
		self.fetch()
		temp = self.y - self.fetched
		self.setflag(C, self.a >= self.fetched)
		self.setflag(Z, (temp & 0x00FF) == 0)
		self.setflag(N, temp & 0)
		return 1

	def DEC(self):
		fetch()
		temp = self.fetched - 1
		self.write(self.addr_abs, temp & 0x00FF)
		self.setflag(Z, (temp & 0x00FF) == 0)
		self.setflag(N, temp & 0x0080)
		return 0

	def DEX(self):
		self.x -= 1
		self.setflag(Z, self.x == 0)
		self.setflag(N, self.x & 0x80)
		return 0

	def DEY(self):
		self.y -= 1
		self.setflag(Z, self.y == 0)
		self.setflag(N, self.y & 0x80)
		return 0

	def EOR(self):
		fetch()
		a = a ^ self.fetched
		self.setflag(Z)

	def INC(self):
		pass

	def INX(self):
		pass

	def INY(self):
		pass

	def JMP(self):
		pass

	def JSR(self):
		pass

	def LDA(self):
		pass

	def LDX(self):
		pass

	def LDY(self):
		pass

	def LSR(self):
		pass

	def NOP(self):
		pass

	def ORA(self):
		pass

	def PHA(self):
		pass

	def PHP(self):
		pass

	def PLA(self):
		pass

	def PLP(self):
		pass

	def ROL(self):
		pass

	def ROR(self):
		pass

	def RTI(self):
		pass

	def RTS(self):
		pass

	def SBC(self):
		pass

	def SEC(self):
		pass

	def SED(self):
		pass

	def SEI(self):
		pass

	def STA(self):
		pass

	def STX(self):
		pass

	def STY(self):
		pass

	def TAX(self):
		pass

	def TAY(self):
		pass

	def TSX(self):
		pass

	def TXA(self):
		pass

	def TXS(self):
		pass

	def TYA(self):
		pass

	def getops(self):
		return eval(opcodes)


