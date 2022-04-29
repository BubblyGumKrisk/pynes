from opfuncs import *

opcodes = [
	{
		"bytes" : 2,
		"description" : "Add with Carry",
		"name" : ADC,
		"opcode" : 0x69,
		"mode" : "Immediate",
		"cycles": 2
	},
	{
		"opcode" : 0x65,
		"name" : ADC,
		"bytes" : 2,
		"description" : "Add with Carry",
		"mode" : "ZeroPage",
		"cycles": 3
	},
	{
		"description" : "Add with Carry",
		"bytes" : 2,
		"opcode" : 0x75,
		"name" : ADC,
		"mode" : "ZeroPage,X",
		"cycles": 4
	},
	{
		"name" : ADC,
		"opcode" : 0x6D,
		"bytes" : 3,
		"description" : "Add with Carry",
		"mode" : "Absolute",
		"cycles": 4
	},
	{
		"mode" : "Absolute,X",
		"name" : ADC,
		"opcode" : 0x7D,
		"bytes" : 3,
		"description" : "Add with Carry",
		"cycles": 4
	},
	{
		"mode" : "Absolute,Y",
		"name" : ADC,
		"opcode" : 0x79,
		"description" : "Add with Carry",
		"bytes" : 3,
		"cycles": 4
	},
	{
		"mode" : "(Indirect,X)",
		"description" : "Add with Carry",
		"bytes" : 2,
		"opcode" : 0x61,
		"name" : ADC,
		"cycles": 6
	},
	{
		"mode" : "(Indirect),Y",
		"bytes" : 2,
		"description" : "Add with Carry",
		"name" : ADC,
		"opcode" : 0x71,
		"cycles": 5
	},
	{
		"bytes" : 2,
		"description" : "Logical AND",
		"name" : AND,
		"opcode" : 0x29,
		"mode" : "Immediate",
		"cycles": 2
	},
	{
		"mode" : "ZeroPage",
		"name" : AND,
		"opcode" : 0x25,
		"bytes" : 2,
		"description" : "Logical AND",
		"cycles": 3
	},
	{
		"bytes" : 2,
		"description" : "Logical AND",
		"name" : AND,
		"opcode" : 0x35,
		"mode" : "ZeroPage,X",
		"cycles": 4
	},
	{
		"mode" : "Absolute",
		"opcode" : 0x2D,
		"name" : AND,
		"description" : "Logical AND",
		"bytes" : 3,
		"cycles": 4
	},
	{
		"description" : "Logical AND",
		"bytes" : 3,
		"name" : AND,
		"opcode" : 0x3D,
		"mode" : "Absolute,X",
		"cycles": 4
	},
	{
		"mode" : "Absolute,Y",
		"bytes" : 3,
		"description" : "Logical AND",
		"opcode" : 0x39,
		"name" : AND,
		"cycles": 4
	},
	{
		"description" : "Logical AND",
		"bytes" : 2,
		"opcode" : 0x21,
		"name" : AND,
		"mode" : "(Indirect,X)",
		"cycles": 6
	},
	{
		"name" : AND,
		"opcode" : 0x31,
		"description" : "Logical AND",
		"bytes" : 2,
		"mode" : "(Indirect),Y",
		"cycles": 5
	},
	{
		"description" : "Arithmetic Shift Left",
		"bytes" : 1,
		"opcode" : 0x0A,
		"name" : ASL,
		"mode" : "Accumulator",
		"cycles": 2
	},
	{
		"opcode" : 0x06,
		"name" : ASL,
		"bytes" : 2,
		"description" : "Arithmetic Shift Left",
		"mode" : "ZeroPage",
		"cycles": 5
	},
	{
		"description" : "Arithmetic Shift Left",
		"bytes" : 2,
		"name" : ASL,
		"opcode" : 0x16,
		"mode" : "ZeroPage,X",
		"cycles": 6
	},
	{
		"mode" : "Absolute",
		"description" : "Arithmetic Shift Left",
		"bytes" : 3,
		"name" : ASL,
		"opcode" : 0x0E,
		"cycles": 6
	},
	{
		"mode" : "Absolute,X",
		"description" : "Arithmetic Shift Left",
		"bytes" : 3,
		"name" : ASL,
		"opcode" : 0x1E,
		"cycles": 7
	},
	{
		"mode" : "Relative",
		"bytes" : 2,
		"description" : "Branch if Carry Clear",
		"opcode" : 0x90,
		"name" : BCC,
		"cycles": 2
	},
	{
		"mode" : "Relative",
		"bytes" : 2,
		"description" : "Branch if Carry Set",
		"name" : BCS,
		"opcode" : 0xB0,
		"cycles": 2
	},
	{
		"bytes" : 2,
		"description" : "Branch if Equal",
		"name" : BEQ,
		"opcode" : 0xF0,
		"mode" : "Relative",
		"cycles": 2
	},
	{
		"opcode" : 0x24,
		"name" : BIT,
		"bytes" : 2,
		"description" : "Bit Test",
		"mode" : "ZeroPage",
		"cycles": 3
	},
	{
		"mode" : "Absolute",
		"description" : "Bit Test",
		"bytes" : 3,
		"name" : BIT,
		"opcode" : 0x2C,
		"cycles": 4
	},
	{
		"mode" : "Relative",
		"description" : "Branch if Minus",
		"bytes" : 2,
		"name" : BMI,
		"opcode" : 0x30,
		"cycles": 2
	},
	{
		"opcode" : 0xD0,
		"name" : BNE,
		"description" : "Branch if Not Equal",
		"bytes" : 2,
		"mode" : "Relative",
		"cycles": 2
	},
	{
		"mode" : "Relative",
		"opcode" : 0x10,
		"name" : BPL,
		"description" : "Branch if Positive",
		"bytes" : 2,
		"cycles": 2
	},
	{
		"name" : BRK,
		"opcode" : 0x00,
		"description" : "Force Interrupt",
		"bytes" : 1,
		"mode" : "Implied",
		"cycles": 7
	},
	{
		"mode" : "Relative",
		"description" : "Branch if Overflow Clear",
		"bytes" : 2,
		"opcode" : 0x50,
		"name" : BVC,
		"cycles": 2
	},
	{
		"mode" : "Relative",
		"description" : "Branch if Overflow Set",
		"bytes" : 2,
		"name" : BVS,
		"opcode" : 0x70,
		"cycles": 2
	},
	{
		"mode" : "Implied",
		"opcode" : 0x18,
		"name" : CLC,
		"bytes" : 1,
		"description" : "Clear Carry Flag",
		"cycles": 2
	},
	{
		"bytes" : 1,
		"description" : "Clear Decimal Mode",
		"name" : CLD,
		"opcode" : 0xD8,
		"mode" : "Implied",
		"cycles": 2
	},
	{
		"mode" : "Implied",
		"bytes" : 1,
		"description" : "Clear Interrupt Disable",
		"opcode" : 0x58,
		"name" : CLI,
		"cycles": 2
	},
	{
		"mode" : "Implied",
		"description" : "Clear Overflow Flag",
		"bytes" : 1,
		"opcode" : 0xB8,
		"name" : CLV,
		"cycles": 2
	},
	{
		"opcode" : 0xC9,
		"name" : CMP,
		"bytes" : 2,
		"description" : "Compare",
		"mode" : "Immediate",
		"cycles": 2
	},
	{
		"mode" : "ZeroPage",
		"bytes" : 2,
		"description" : "Compare",
		"opcode" : 0xC5,
		"name" : CMP,
		"cycles": 3
	},
	{
		"opcode" : 0xD5,
		"name" : CMP,
		"bytes" : 2,
		"description" : "Compare",
		"mode" : "ZeroPage,X",
		"cycles": 4
	},
	{
		"mode" : "Absolute",
		"opcode" : 0xCD,
		"name" : CMP,
		"bytes" : 3,
		"description" : "Compare",
		"cycles": 4
	},
	{
		"name" : CMP,
		"opcode" : 0xDD,
		"bytes" : 3,
		"description" : "Compare",
		"mode" : "Absolute,X",
		"cycles": 4
	},
	{
		"opcode" : 0xD9,
		"name" : CMP,
		"bytes" : 3,
		"description" : "Compare",
		"mode" : "Absolute,Y",
		"cycles": 4
	},
	{
		"name" : CMP,
		"opcode" : 0xC1,
		"bytes" : 2,
		"description" : "Compare",
		"mode" : "(Indirect,X)",
		"cycles": 6
	},
	{
		"name" : CMP,
		"opcode" : 0xD1,
		"bytes" : 2,
		"description" : "Compare",
		"mode" : "(Indirect),Y",
		"cycles": 5
	},
	{
		"mode" : "Immediate",
		"name" : CPX,
		"opcode" : 0xE0,
		"description" : "Compare X Register",
		"bytes" : 2,
		"cycles": 2
	},
	{
		"mode" : "ZeroPage",
		"bytes" : 2,
		"description" : "Compare X Register",
		"opcode" : 0xE4,
		"name" : CPX,
		"cycles": 3
	},
	{
		"mode" : "Absolute",
		"description" : "Compare X Register",
		"bytes" : 3,
		"name" : CPX,
		"opcode" : 0xEC,
		"cycles": 4
	},
	{
		"mode" : "Immediate",
		"name" : CPY,
		"opcode" : 0xC0,
		"bytes" : 2,
		"description" : "Compare Y Register",
		"cycles": 2
	},
	{
		"opcode" : 0xC4,
		"name" : CPY,
		"bytes" : 2,
		"description" : "Compare Y Register",
		"mode" : "ZeroPage",
		"cycles": 3
	},
	{
		"bytes" : 3,
		"description" : "Compare Y Register",
		"name" : CPY,
		"opcode" : 0xCC,
		"mode" : "Absolute",
		"cycles": 4
	},
	{
		"bytes" : 2,
		"description" : "Decrement Memory",
		"name" : DEC,
		"opcode" : 0xC6,
		"mode" : "ZeroPage",
		"cycles": 5
	},
	{
		"opcode" : 0xD6,
		"name" : DEC,
		"description" : "Decrement Memory",
		"bytes" : 2,
		"mode" : "ZeroPage,X",
		"cycles": 6
	},
	{
		"bytes" : 3,
		"description" : "Decrement Memory",
		"name" : DEC,
		"opcode" : 0xCE,
		"mode" : "Absolute",
		"cycles": 6
	},
	{
		"name" : DEC,
		"opcode" : 0xDE,
		"description" : "Decrement Memory",
		"bytes" : 3,
		"mode" : "Absolute,X",
		"cycles": 7
	},
	{
		"description" : "Decrement X Register",
		"bytes" : 1,
		"name" : DEX,
		"opcode" : 0xCA,
		"mode" : "Implied",
		"cycles": 2
	},
	{
		"mode" : "Implied",
		"bytes" : 1,
		"description" : "Decrement Y Register",
		"opcode" : 0x88,
		"name" : DEY,
		"cycles": 2
	},
	{
		"opcode" : 0x49,
		"name" : EOR,
		"description" : "Exclusive OR",
		"bytes" : 2,
		"mode" : "Immediate",
		"cycles": 2
	},
	{
		"opcode" : 0x45,
		"name" : EOR,
		"bytes" : 2,
		"description" : "Exclusive OR",
		"mode" : "ZeroPage",
		"cycles": 3
	},
	{
		"mode" : "ZeroPage,X",
		"bytes" : 2,
		"description" : "Exclusive OR",
		"name" : EOR,
		"opcode" : 0x55,
		"cycles": 4
	},
	{
		"mode" : "Absolute",
		"name" : EOR,
		"opcode" : 0x4D,
		"bytes" : 3,
		"description" : "Exclusive OR",
		"cycles": 4
	},
	{
		"description" : "Exclusive OR",
		"bytes" : 3,
		"name" : EOR,
		"opcode" : 0x5D,
		"mode" : "Absolute,X",
		"cycles": 4
	},
	{
		"mode" : "Absolute,Y",
		"name" : EOR,
		"opcode" : 0x59,
		"description" : "Exclusive OR",
		"bytes" : 3,
		"cycles": 4
	},
	{
		"mode" : "(Indirect,X)",
		"description" : "Exclusive OR",
		"bytes" : 2,
		"name" : EOR,
		"opcode" : 0x41,
		"cycles": 6
	},
	{
		"mode" : "(Indirect),Y",
		"bytes" : 2,
		"description" : "Exclusive OR",
		"opcode" : 0x51,
		"name" : EOR,
		"cycles": 5
	},
	{
		"bytes" : 2,
		"description" : "Increment Memory",
		"name" : INC,
		"opcode" : 0xE6,
		"mode" : "ZeroPage",
		"cycles": 5
	},
	{
		"opcode" : 0xF6,
		"name" : INC,
		"description" : "Increment Memory",
		"bytes" : 2,
		"mode" : "ZeroPage,X",
		"cycles": 6
	},
	{
		"mode" : "Absolute",
		"bytes" : 3,
		"description" : "Increment Memory",
		"opcode" : 0xEE,
		"name" : INC,
		"cycles": 6
	},
	{
		"opcode" : 0xFE,
		"name" : INC,
		"bytes" : 3,
		"description" : "Increment Memory",
		"mode" : "Absolute,X",
		"cycles": 7
	},
	{
		"mode" : "Implied",
		"opcode" : 0xE8,
		"name" : INX,
		"description" : "Increment X Register",
		"bytes" : 1,
		"cycles": 2
	},
	{
		"description" : "Increment Y Register",
		"bytes" : 1,
		"name" : INY,
		"opcode" : 0xC8,
		"mode" : "Implied",
		"cycles": 2
	},
	{
		"mode" : "Absolute",
		"description" : "Jump",
		"bytes" : 3,
		"name" : JMP,
		"opcode" : 0x4C,
		"cycles": 3
	},
	{
		"mode" : "Indirect ",
		"opcode" : 0x6C,
		"name" : JMP,
		"description" : "Jump",
		"bytes" : 3,
		"cycles": 5
	},
	{
		"mode" : "Absolute",
		"name" : JSR,
		"opcode" : 0x20,
		"description" : "Jump to Subroutine",
		"bytes" : 3,
		"cycles": 6
	},
	{
		"description" : "Load Accumulator",
		"bytes" : 2,
		"name" : LDA,
		"opcode" : 0xA9,
		"mode" : "Immediate",
		"cycles": 2
	},
	{
		"mode" : "ZeroPage",
		"name" : LDA,
		"opcode" : 0xA5,
		"bytes" : 2,
		"description" : "Load Accumulator",
		"cycles": 3
	},
	{
		"opcode" : 0xB5,
		"name" : LDA,
		"description" : "Load Accumulator",
		"bytes" : 2,
		"mode" : "ZeroPage,X",
		"cycles": 4
	},
	{
		"name" : LDA,
		"opcode" : 0xAD,
		"bytes" : 3,
		"description" : "Load Accumulator",
		"mode" : "Absolute",
		"cycles": 4
	},
	{
		"mode" : "Absolute,X",
		"bytes" : 3,
		"description" : "Load Accumulator",
		"opcode" : 0xBD,
		"name" : LDA,
		"cycles": 4
	},
	{
		"mode" : "Absolute,Y",
		"name" : LDA,
		"opcode" : 0xB9,
		"bytes" : 3,
		"description" : "Load Accumulator",
		"cycles": 4
	},
	{
		"opcode" : 0xA1,
		"name" : LDA,
		"description" : "Load Accumulator",
		"bytes" : 2,
		"mode" : "(Indirect,X)",
		"cycles": 6
	},
	{
		"mode" : "(Indirect),Y",
		"name" : LDA,
		"opcode" : 0xB1,
		"description" : "Load Accumulator",
		"bytes" : 2,
		"cycles": 5
	},
	{
		"description" : "Load X Register",
		"bytes" : 2,
		"name" : LDX,
		"opcode" : 0xA2,
		"mode" : "Immediate",
		"cycles": 2
	},
	{
		"description" : "Load X Register",
		"bytes" : 2,
		"name" : LDX,
		"opcode" : 0xA6,
		"mode" : "ZeroPage",
		"cycles": 3
	},
	{
		"description" : "Load X Register",
		"bytes" : 2,
		"name" : LDX,
		"opcode" : 0xB6,
		"mode" : "ZeroPage,Y",
		"cycles": 4
	},
	{
		"mode" : "Absolute",
		"opcode" : 0xAE,
		"name" : LDX,
		"bytes" : 3,
		"description" : "Load X Register",
		"cycles": 4
	},
	{
		"bytes" : 3,
		"description" : "Load X Register",
		"name" : LDX,
		"opcode" : 0xBE,
		"mode" : "Absolute,Y",
		"cycles": 4
	},
	{
		"mode" : "Immediate",
		"opcode" : 0xA0,
		"name" : LDY,
		"description" : "Load Y Register",
		"bytes" : 2,
		"cycles": 2
	},
	{
		"name" : LDY,
		"opcode" : 0xA4,
		"bytes" : 2,
		"description" : "Load Y Register",
		"mode" : "ZeroPage",
		"cycles": 3
	},
	{
		"description" : "Load Y Register",
		"bytes" : 2,
		"name" : LDY,
		"opcode" : 0xB4,
		"mode" : "ZeroPage,X",
		"cycles": 4
	},
	{
		"name" : LDY,
		"opcode" : 0xAC,
		"description" : "Load Y Register",
		"bytes" : 3,
		"mode" : "Absolute",
		"cycles": 4
	},
	{
		"bytes" : 3,
		"description" : "Load Y Register",
		"name" : LDY,
		"opcode" : 0xBC,
		"mode" : "Absolute,X",
		"cycles": 4
	},
	{
		"mode" : "Accumulator",
		"description" : "Logical Shift Right",
		"bytes" : 1,
		"opcode" : 0x4A,
		"name" : LSR,
		"cycles": 2
	},
	{
		"mode" : "ZeroPage",
		"name" : LSR,
		"opcode" : 0x46,
		"description" : "Logical Shift Right",
		"bytes" : 2,
		"cycles": 5
	},
	{
		"mode" : "ZeroPage,X",
		"description" : "Logical Shift Right",
		"bytes" : 2,
		"name" : LSR,
		"opcode" : 0x56,
		"cycles": 6
	},
	{
		"mode" : "Absolute",
		"opcode" : 0x4E,
		"name" : LSR,
		"description" : "Logical Shift Right",
		"bytes" : 3,
		"cycles": 6
	},
	{
		"mode" : "Absolute,X",
		"name" : LSR,
		"opcode" : 0x5E,
		"description" : "Logical Shift Right",
		"bytes" : 3,
		"cycles": 7
	},
	{
		"mode" : "Implied",
		"description" : "No Operation",
		"bytes" : 1,
		"opcode" : 0xEA,
		"name" : NOP,
		"cycles": 2
	},
	{
		"name" : ORA,
		"opcode" : 0x09,
		"bytes" : 2,
		"description" : "Logical Inclusive OR",
		"mode" : "Immediate",
		"cycles": 2
	},
	{
		"opcode" : 0x05,
		"name" : ORA,
		"description" : "Logical Inclusive OR",
		"bytes" : 2,
		"mode" : "ZeroPage",
		"cycles": 3
	},
	{
		"mode" : "ZeroPage,X",
		"opcode" : 0x15,
		"name" : ORA,
		"description" : "Logical Inclusive OR",
		"bytes" : 2,
		"cycles": 4
	},
	{
		"opcode" : 0x0D,
		"name" : ORA,
		"bytes" : 3,
		"description" : "Logical Inclusive OR",
		"mode" : "Absolute",
		"cycles": 4
	},
	{
		"mode" : "Absolute,X",
		"description" : "Logical Inclusive OR",
		"bytes" : 3,
		"name" : ORA,
		"opcode" : 0x1D,
		"cycles": 4
	},
	{
		"mode" : "Absolute,Y",
		"description" : "Logical Inclusive OR",
		"bytes" : 3,
		"name" : ORA,
		"opcode" : 0x19,
		"cycles": 4
	},
	{
		"mode" : "(Indirect,X)",
		"bytes" : 2,
		"description" : "Logical Inclusive OR",
		"name" : ORA,
		"opcode" : 0x01,
		"cycles": 6
	},
	{
		"mode" : "(Indirect),Y",
		"description" : "Logical Inclusive OR",
		"bytes" : 2,
		"opcode" : 0x11,
		"name" : ORA,
		"cycles": 5
	},
	{
		"opcode" : 0x48,
		"name" : PHA,
		"bytes" : 1,
		"description" : "Push Accumulator",
		"mode" : "Implied",
		"cycles": 3
	},
	{
		"mode" : "Implied",
		"opcode" : 0x08,
		"name" : PHP,
		"description" : "Push Processor Status",
		"bytes" : 1,
		"cycles": 3
	},
	{
		"mode" : "Implied",
		"bytes" : 1,
		"description" : "Pull Accumulator",
		"name" : PLA,
		"opcode" : 0x68,
		"cycles": 4
	},
	{
		"description" : "Pull Processor Status",
		"bytes" : 1,
		"opcode" : 0x28,
		"name" : PLP,
		"mode" : "Implied",
		"cycles": 4
	},
	{
		"mode" : "Accumulator",
		"name" : ROL,
		"opcode" : 0x2A,
		"bytes" : 1,
		"description" : "Rotate Left",
		"cycles": 2
	},
	{
		"mode" : "ZeroPage",
		"description" : "Rotate Left",
		"bytes" : 2,
		"opcode" : 0x26,
		"name" : ROL,
		"cycles": 5
	},
	{
		"bytes" : 2,
		"description" : "Rotate Left",
		"opcode" : 0x36,
		"name" : ROL,
		"mode" : "ZeroPage,X",
		"cycles": 6
	},
	{
		"bytes" : 3,
		"description" : "Rotate Left",
		"name" : ROL,
		"opcode" : 0x2E,
		"mode" : "Absolute",
		"cycles": 6
	},
	{
		"name" : ROL,
		"opcode" : 0x3E,
		"bytes" : 3,
		"description" : "Rotate Left",
		"mode" : "Absolute,X",
		"cycles": 7
	},
	{
		"name" : ROR,
		"opcode" : 0x6A,
		"description" : "Rotate Right",
		"bytes" : 1,
		"mode" : "Accumulator",
		"cycles": 2
	},
	{
		"bytes" : 2,
		"description" : "Rotate Right",
		"opcode" : 0x66,
		"name" : ROR,
		"mode" : "ZeroPage",
		"cycles": 5
	},
	{
		"mode" : "ZeroPage,X",
		"opcode" : 0x76,
		"name" : ROR,
		"bytes" : 2,
		"description" : "Rotate Right",
		"cycles": 6
	},
	{
		"mode" : "Absolute",
		"bytes" : 3,
		"description" : "Rotate Right",
		"name" : ROR,
		"opcode" : 0x6E,
		"cycles": 6
	},
	{
		"mode" : "Absolute,X",
		"description" : "Rotate Right",
		"bytes" : 3,
		"name" : ROR,
		"opcode" : 0x7E,
		"cycles": 7
	},
	{
		"mode" : "Implied",
		"bytes" : 1,
		"description" : "Return from Interrupt",
		"opcode" : 0x40,
		"name" : RTI,
		"cycles": 6
	},
	{
		"mode" : "Implied",
		"name" : RTS,
		"opcode" : 0x60,
		"description" : "Return from Subroutine",
		"bytes" : 1,
		"cycles": 6
	},
	{
		"bytes" : 2,
		"description" : "Subtract with Carry",
		"opcode" : 0xE9,
		"name" : SBC,
		"mode" : "Immediate",
		"cycles": 2
	},
	{
		"name" : SBC,
		"opcode" : 0xE5,
		"bytes" : 2,
		"description" : "Subtract with Carry",
		"mode" : "ZeroPage",
		"cycles": 3
	},
	{
		"description" : "Subtract with Carry",
		"bytes" : 2,
		"name" : SBC,
		"opcode" : 0xF5,
		"mode" : "ZeroPage,X",
		"cycles": 4
	},
	{
		"name" : SBC,
		"opcode" : 0xED,
		"description" : "Subtract with Carry",
		"bytes" : 3,
		"mode" : "Absolute",
		"cycles": 4
	},
	{
		"opcode" : 0xFD,
		"name" : SBC,
		"description" : "Subtract with Carry",
		"bytes" : 3,
		"mode" : "Absolute,X",
		"cycles": 4
	},
	{
		"mode" : "Absolute,Y",
		"opcode" : 0xF9,
		"name" : SBC,
		"bytes" : 3,
		"description" : "Subtract with Carry",
		"cycles": 4
	},
	{
		"mode" : "(Indirect,X)",
		"opcode" : 0xE1,
		"name" : SBC,
		"description" : "Subtract with Carry",
		"bytes" : 2,
		"cycles": 6
	},
	{
		"bytes" : 2,
		"description" : "Subtract with Carry",
		"name" : SBC,
		"opcode" : 0xF1,
		"mode" : "(Indirect),Y",
		"cycles": 5
	},
	{
		"description" : "Set Carry Flag",
		"bytes" : 1,
		"name" : SEC,
		"opcode" : 0x38,
		"mode" : "Implied",
		"cycles": 2
	},
	{
		"name" : SED,
		"opcode" : 0xF8,
		"description" : "Set Decimal Flag",
		"bytes" : 1,
		"mode" : "Implied",
		"cycles": 2
	},
	{
		"mode" : "Implied",
		"opcode" : 0x78,
		"name" : SEI,
		"bytes" : 1,
		"description" : "Set Interrupt Disable",
		"cycles": 2
	},
	{
		"description" : "Store Accumulator",
		"bytes" : 2,
		"name" : STA,
		"opcode" : 0x85,
		"mode" : "ZeroPage",
		"cycles": 3
	},
	{
		"mode" : "ZeroPage,X",
		"bytes" : 2,
		"description" : "Store Accumulator",
		"name" : STA,
		"opcode" : 0x95,
		"cycles": 4
	},
	{
		"mode" : "Absolute",
		"opcode" : 0x8D,
		"name" : STA,
		"description" : "Store Accumulator",
		"bytes" : 3,
		"cycles": 4
	},
	{
		"bytes" : 3,
		"description" : "Store Accumulator",
		"opcode" : 0x9D,
		"name" : STA,
		"mode" : "Absolute,X",
		"cycles": 5
	},
	{
		"bytes" : 3,
		"description" : "Store Accumulator",
		"name" : STA,
		"opcode" : 0x99,
		"mode" : "Absolute,Y",
		"cycles": 5
	},
	{
		"mode" : "(Indirect,X)",
		"description" : "Store Accumulator",
		"bytes" : 2,
		"name" : STA,
		"opcode" : 0x81,
		"cycles": 6
	},
	{
		"bytes" : 2,
		"description" : "Store Accumulator",
		"opcode" : 0x91,
		"name" : STA,
		"mode" : "(Indirect),Y",
		"cycles": 6
	},
	{
		"bytes" : 2,
		"description" : "Store X Register",
		"name" : STX,
		"opcode" : 0x86,
		"mode" : "ZeroPage",
		"cycles": 3
	},
	{
		"mode" : "ZeroPage,Y",
		"name" : STX,
		"opcode" : 0x96,
		"bytes" : 2,
		"description" : "Store X Register",
		"cycles": 4
	},
	{
		"mode" : "Absolute",
		"name" : STX,
		"opcode" : 0x8E,
		"bytes" : 3,
		"description" : "Store X Register",
		"cycles": 4
	},
	{
		"mode" : "ZeroPage",
		"name" : STY,
		"opcode" : 0x84,
		"description" : "Store Y Register",
		"bytes" : 2,
		"cycles": 3
	},
	{
		"mode" : "ZeroPage,X",
		"name" : STY,
		"opcode" : 0x94,
		"bytes" : 2,
		"description" : "Store Y Register",
		"cycles": 4
	},
	{
		"bytes" : 3,
		"description" : "Store Y Register",
		"name" : STY,
		"opcode" : 0x8C,
		"mode" : "Absolute",
		"cycles": 4
	},
	{
		"mode" : "Implied",
		"name" : TAX,
		"opcode" : 0xAA,
		"description" : "Transfer Accumulator to X",
		"bytes" : 1,
		"cycles": 2
	},
	{
		"mode" : "Implied",
		"description" : "Transfer Accumulator to Y",
		"bytes" : 1,
		"name" : TAY,
		"opcode" : 0xA8,
		"cycles": 2
	},
	{
		"mode" : "Implied",
		"bytes" : 1,
		"description" : "Transfer Stack Pointer to X",
		"name" : TSX,
		"opcode" : 0xBA,
		"cycles": 2
	},
	{
		"mode" : "Implied",
		"bytes" : 1,
		"description" : "Transfer X to Accumulator",
		"opcode" : 0x8A,
		"name" : TXA,
		"cycles": 2
	},
	{
		"description" : "Transfer X to Stack Pointer",
		"bytes" : 1,
		"name" : TXS,
		"opcode" : 0x9A,
		"mode" : "Implied",
		"cycles": 2
	},
	{
		"mode" : "Implied",
		"description" : "Transfer Y to Accumulator",
		"bytes" : 1,
		"name" : TYA,
		"opcode" : 0x98,
		"cycles": 2
	}
]

