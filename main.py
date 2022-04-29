from cpu import CPU
from bus import Bus

cpu = CPU()
bus = Bus(cpu)
cpu.bus = bus