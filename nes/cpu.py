from instruction import Instruction


class CPU(object):

    def __init__(self):
        # TODO proper registers
        self.registers = []

        self.rom = None
        # program counter stores current execution point
        self.pc = 16
        self.running = True

    def run_rom(self, rom: ROM):
        # load rom
        self.rom = rom

        # run program
        self.running = True
        while self.running:
            # get the current byte at pc
            identifier_byte = self.rom.get_byte(self.pc)

            # turn the byte into an Instruction

    def process_instruction(self, instruction: Instruction):
        # TODO process the instruction
        instruction.process()
