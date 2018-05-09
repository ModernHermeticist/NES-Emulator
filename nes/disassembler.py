class NESDisassembler(object):

    def __init__(self):

        self.accumulator = [0x0]
        self.index_x = [0x0]
        self.index_y = [0x0]
        self.pc = 0x0
        self.sp = [0x0]
        self.sr = [0x0]

        self.firstbyte = 0x0
        self.firstbyte_firstnib = 0x0
        self.firstbyte_secondnib = 0x0
        self.secondbyte = 0x0
        self.secondbyte_firstnib = 0x0
        self.secondbyte_secondnib = 0x0
        self.thirdbyte = 0x0
        self.thirdbyte_firstnib = 0x0
        self.thirdbyte_secondnib = 0x0

    def opcodes(self):

        if self.firstbyte_firstnib == 0x0:
            print("0 not handled yet.")
            self.pc += 2
        if self.firstbyte_firstnib == 0x1:
            print("1 not handled yet.")
            self.pc += 2
        if self.firstbyte_firstnib == 0x2:
            print("2 not handled yet.")
            self.pc += 2
        if self.firstbyte_firstnib == 0x3:
            print("3 not handled yet.")
            self.pc += 2
        if self.firstbyte_firstnib == 0x4:
            print("4 not handled yet.")
            self.pc += 2
        if self.firstbyte_firstnib == 0x5:
            print("5 not handled yet.")
            self.pc += 2
        if self.firstbyte_firstnib == 0x6:
            print("6 not handled yet.")
            self.pc += 2
        if self.firstbyte_firstnib == 0x7:
            print("7 not handled yet.")
            self.pc += 2
        if self.firstbyte_firstnib == 0x8:
            print("8 not handled yet.")
            self.pc += 2
        if self.firstbyte_firstnib == 0x9:
            print("9 not handled yet.")
            self.pc += 2
        if self.firstbyte_firstnib == 0xA:
            if self.firstbyte_secondnib == 0x9:
                self.ldA_i()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x5:
                self.ldA_z()
                self.pc += 2
            elif self.firstbyte_secondnib == 0xD:
                self.ldA_a()
                self.pc += 3
            elif self.firstbyte_secondnib == 0x1:
                self.ldA_I_x()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x2:
                self.ldX_i()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x6:
                self.ldX_z()
                self.pc += 2
            elif self.firstbyte_secondnib == 0xE:
                self.ldX_a()
                self.pc += 3
            else:
                print("A not handled yet.")
                self.pc += 2

        if self.firstbyte_firstnib == 0xB:
            if self.firstbyte_secondnib == 0x5:
                self.ldA_z_x()
                self.pc += 2
            elif self.firstbyte_secondnib == 0xD:
                self.ldA_a_x()
                self.pc += 3
            elif self.firstbyte_secondnib == 0x9:
                self.ldA_a_y()
                self.pc += 3
            elif self.firstbyte_secondnib == 0x1:
                self.ldA_I_y()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x6:
                self.ldX_z_x()
                self.pc += 2
            elif self.firstbyte_secondnib == 0xE:
                self.ldX_a_x()
                self.pc += 3
            else:
                print("B not handled yet.")
                self.pc += 2
        if self.firstbyte_firstnib == 0xC:
            print("C not handled yet.")
            self.pc += 2
        if self.firstbyte_firstnib == 0xD:
            print("D not handled yet.")
            self.pc += 2
        if self.firstbyte_firstnib == 0xE:
            print("E not handled yet.")
            self.pc += 2
        if self.firstbyte_firstnib == 0xF:
            print("F not handled yet.")
            self.pc += 2

    def ldA_i(self):
        print("{:03X}  {:02X}{:02X}  LDA_i: {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def ldA_z(self):
        print("{:03X}  {:02X}{:02X}  LDA_z: {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def ldA_a(self):
        print("{:03X}  {:02X}{:02X}[:02X}  LDA_a: {:02X}{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte,
            self.thirdbyte, self.thirdbyte, self.secondbyte))

    def ldA_I_x(self):
        print("{:03X}  {:02X}{:02X}  LDA_I_x: {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def ldA_z_x(self):
        print("{:03X}  {:02X}{:02X}  LDA_z_x: {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def ldA_a_x(self):
        print("{:03X}  {:02X}{:02X}{:02X}  LDA_a_x: {:02X}{:02}".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))

    def ldA_a_y(self):
        print("{:03X}  {:02X}{:02X}{:02X}  LDA_a_y: {:02X}{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))

    def ldA_I_y(self):
        print("{:03X}  {:02X}{:02X}  LDA_I_y: {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def ldX_i(self):
        print("{:03X}  {:02X}{:02X}  LDX_i: {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def ldX_z(self):
        print("{:03X}  {:02X}{:02X}  LDX_z: {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def ldX_z_x(self):
        print("{:03X}  {:02X}{:02X}  LDX_z_x: {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def ldX_a(self):
        print("{:03X}  {:02X}{:02X}  LDX_a: {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def ldX_a_x(self):
        print("{:03X}  {:02X}{:02X}  LDX_a_x: {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def disassembler(self, firstbyte, secondbyte, thirdbyte):
        self.firstbyte = firstbyte
        self.firstbyte_firstnib = self.firstbyte >> 4
        self.firstbyte_secondnib = self.firstbyte & 0x0F
        self.secondbyte = secondbyte
        self.secondbyte_firstnib = self.secondbyte >> 4
        self.secondbyte_secondnib = self.secondbyte & 0x0F
        self.thirdbyte = thirdbyte
        self.thirdbyte_firstnib = self.thirdbyte >> 4
        self.thirdbyte_secondnib = self.thirdbyte & 0x0F
        self.opcodes()


def bytes_from_file(filename, chunksize=8192):
    with open(filename, "rb") as f:
        while True:
            chunk = f.read(chunksize)
            if chunk:
                for b in chunk:
                    yield b
            else:
                break


def main():

    dis = NESDisassembler()

    memory = []
    next_byte = 0
    first_byte = 0
    third_byte = 0

    for byte in bytes_from_file("SMB.nes"):
        memory.append(hex(byte))

    l = len(memory)
    dis.pc = 0x0
    while dis.pc < (l - 2):
        next_byte = memory[dis.pc + 1]
        next_byte = int(next_byte, 16)
        first_byte = memory[dis.pc]
        first_byte = int(first_byte, 16)
        third_byte = memory[dis.pc + 2]
        third_byte = int(third_byte, 16)
        dis.disassembler(first_byte, next_byte, third_byte)


if __name__ == "__main__":
    main()
