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

        self.dumplist = []
        self.dumpfile = None

    def opcodes(self):

        if self.firstbyte_firstnib == 0x0:
            if self.firstbyte_secondnib == 0xA:
                self.arithmetic_shift_left_accumulator()
                self.pc += 1
            elif self.firstbyte_secondnib == 0x0:
                self.break_interrupt()
                self.pc += 1
            elif self.firstbyte_secondnib == 0x1:
                self.bitwise_or_with_accumulator_I_x()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x5:
                self.bitwise_or_with_accumulator_z()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x8:
                self.push_processor_status()
                self.pc += 1
            elif self.firstbyte_secondnib == 0x9:
                self.bitwise_or_with_accumulator_i()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x6:
                self.arithmetic_shift_left_z()
                self.pc += 2
            elif self.firstbyte_secondnib == 0xD:
                self.bitwise_or_with_accumulator_a()
                self.pc += 3
            elif self.firstbyte_secondnib == 0xE:
                self.arithmetic_shift_left_a()
                self.pc += 3
            else:
                print("0 not handled yet.")
                self.dumplist.append("{:04X}  {:02X}{:02X}"
                                     "    0 not handled yet.".format(
                                         self.pc, self.firstbyte, self.secondbyte))
                self.pc += 2
        if self.firstbyte_firstnib == 0x1:
            if self.firstbyte_secondnib == 0x6:
                self.arithmetic_shift_left_z_x()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x1:
                self.bitwise_or_with_accumulator_I_y()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x5:
                self.bitwise_or_with_accumulator_z_x()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x0:
                self.branch_on_plus()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x8:
                self.clear_carry()
                self.pc += 1
            elif self.firstbyte_secondnib == 0x9:
                self.bitwise_or_with_accumulator_a_y()
                self.pc += 3
            elif self.firstbyte_secondnib == 0xD:
                self.bitwise_or_with_accumulator_a_x()
                self.pc += 3
            elif self.firstbyte_secondnib == 0xE:
                self.arithmetic_shift_left_a_x()
                self.pc += 3
            else:
                print("1 not handled yet.")
                self.dumplist.append("{:04X}  {:02X}{:02X}"
                                     "    1 not handled yet.".format(
                                         self.pc, self.firstbyte, self.secondbyte))
                self.pc += 2
        if self.firstbyte_firstnib == 0x2:
            if self.firstbyte_secondnib == 0x9:
                self.and_i()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x0:
                self.jump_to_subroutine()
                self.pc += 3
            elif self.firstbyte_secondnib == 0x4:
                self.bit_z()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x5:
                self.and_z()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x6:
                self.rotate_left_z()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x8:
                self.pull_processor_status()
                self.pc += 1
            elif self.firstbyte_secondnib == 0xA:
                self.rotate_left_a()
                self.pc += 1
            elif self.firstbyte_secondnib == 0xC:
                self.bit_a()
                self.pc += 3
            elif self.firstbyte_secondnib == 0xD:
                self.and_a()
                self.pc += 3
            elif self.firstbyte_secondnib == 0xE:
                self.rotate_left_A()
                self.pc += 3
            elif self.firstbyte_secondnib == 0x1:
                self.and_I_x()
                self.pc += 2
            else:
                print("2 not handled yet.")
                self.dumplist.append("{:04X}  {:02X}{:02X}"
                                     "    2 not handled yet.".format(
                                         self.pc, self.firstbyte, self.secondbyte))
                self.pc += 2
        if self.firstbyte_firstnib == 0x3:
            if self.firstbyte_secondnib == 0x5:
                self.and_z_x()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x6:
                self.rotate_left_z_x()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x0:
                self.branch_on_minus()
                self.pc += 2
            elif self.firstbyte_secondnib == 0xD:
                self.and_a_x()
                self.pc += 3
            elif self.firstbyte_secondnib == 0xE:
                self.rotate_left_A_x()
                self.pc += 3
            elif self.firstbyte_secondnib == 0x9:
                self.and_a_y()
                self.pc += 3
            elif self.firstbyte_secondnib == 0x1:
                self.and_I_y()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x8:
                self.set_carry()
                self.pc += 1
            else:
                print("3 not handled yet.")
                self.dumplist.append("{:04X}  {:02X}{:02X}"
                                     "    3 not handled yet.".format(
                                         self.pc, self.firstbyte, self.secondbyte))
                self.pc += 2
        if self.firstbyte_firstnib == 0x4:
            if self.firstbyte_secondnib == 0x1:
                self.bitwise_exclusive_or_I_x()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x0:
                self.return_from_interrupt()
                self.pc += 1
            elif self.firstbyte_secondnib == 0x5:
                self.bitwise_exclusive_or_z()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x8:
                self.push_accumulator()
                self.pc += 1
            elif self.firstbyte_secondnib == 0x9:
                self.bitwise_exclusive_or_i()
                self.pc += 2
            elif self.firstbyte_secondnib == 0xC:
                self.jump_a()
                self.pc += 3
            elif self.firstbyte_secondnib == 0xD:
                self.bitwise_exclusive_or_a()
                self.pc += 3
            else:
                print("4 not handled yet.")
                self.dumplist.append("{:04X}  {:02X}{:02X}"
                                     "    4 not handled yet.".format(
                                         self.pc, self.firstbyte, self.secondbyte))
            self.pc += 2
        if self.firstbyte_firstnib == 0x5:
            if self.firstbyte_secondnib == 0x0:
                self.branch_on_overflow_clear()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x1:
                self.bitwise_exclusive_or_I_y()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x5:
                self.bitwise_exclusive_or_z_x()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x8:
                self.clear_interrupt()
                self.pc += 1
            elif self.firstbyte_secondnib == 0x9:
                self.bitwise_exclusive_or_a_y()
                self.pc += 3
            elif self.firstbyte_secondnib == 0xD:
                self.bitwise_exclusive_or_a_x()
                self.pc += 3
            else:
                print("5 not handled yet.")
                self.dumplist.append("{:04X}  {:02X}{:02X}"
                                     "    5 not handled yet.".format(
                                         self.pc, self.firstbyte, self.secondbyte))
            self.pc += 2
        if self.firstbyte_firstnib == 0x6:
            if self.firstbyte_secondnib == 0x9:
                self.add_with_carry_i()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x0:
                self.return_from_subroutine()
                self.pc += 1
            elif self.firstbyte_secondnib == 0x1:
                self.add_with_carry_I_x()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x5:
                self.add_with_carry_z()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x6:
                self.rotate_right_z()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x8:
                self.pull_accumulator()
                self.pc += 1
            elif self.firstbyte_secondnib == 0xA:
                self.rotate_right_a()
                self.pc += 1
            elif self.firstbyte_secondnib == 0xC:
                self.jump_I()
                self.pc += 3
            elif self.firstbyte_secondnib == 0xD:
                self.add_with_carry_a()
                self.pc += 3
            elif self.firstbyte_secondnib == 0xE:
                self.rotate_right_A()
                self.pc += 3
            else:
                print("6 not handled yet.")
                self.dumplist.append("{:04X}  {:02X}{:02X}"
                                     "    6 not handled yet.".format(
                                         self.pc, self.firstbyte, self.secondbyte))
                self.pc += 2
        if self.firstbyte_firstnib == 0x7:
            if self.firstbyte_secondnib == 0x5:
                self.add_with_carry_z_x()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x0:
                self.branch_on_overflow_set()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x1:
                self.add_with_carry_I_x()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x6:
                self.rotate_right_z_x()
                self.pc += 2
            elif self.firstbyte_secondnib == 0xD:
                self.add_with_carry_a_x()
                self.pc += 3
            elif self.firstbyte_secondnib == 0xE:
                self.rotate_right_A_x()
                self.pc += 3
            elif self.firstbyte_secondnib == 0x8:
                self.set_interrupt()
                self.pc += 1
            elif self.firstbyte_secondnib == 0x9:
                self.add_with_carry_a_y()
                self.pc += 3
            else:
                print("7 not handled yet.")
                self.dumplist.append("{:04X}  {:02X}{:02X}"
                                     "    7 not handled yet.".format(
                                         self.pc, self.firstbyte, self.secondbyte))
                self.pc += 2
        if self.firstbyte_firstnib == 0x8:
            if self.firstbyte_secondnib == 0x5:
                self.stA_z()
                self.pc += 2
            elif self.firstbyte_secondnib == 0xD:
                self.stA_a()
                self.pc += 3
            elif self.firstbyte_secondnib == 0x1:
                self.stA_I_x()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x6:
                self.stX_z()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x8:
                self.decrement_y()
                self.pc += 1
            elif self.firstbyte_secondnib == 0xE:
                self.stX_a()
                self.pc += 3
            elif self.firstbyte_secondnib == 0x4:
                self.stY_z()
                self.pc += 2
            elif self.firstbyte_secondnib == 0xC:
                self.stY_a()
                self.pc += 3
            elif self.firstbyte_secondnib == 0xA:
                self.tXA()
                self.pc += 1
            else:
                print("8 not handled yet.")
                self.dumplist.append("{:04X}  {:02X}{:02X}"
                                     "    8 not handled yet.".format(
                                         self.pc, self.firstbyte, self.secondbyte))
                self.pc += 2
        if self.firstbyte_firstnib == 0x9:
            if self.firstbyte_secondnib == 0x5:
                self.stA_z_x()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x0:
                self.branch_on_carry_clear()
                self.pc += 2
            elif self.firstbyte_secondnib == 0xD:
                self.stA_a_x()
                self.pc += 3
            elif self.firstbyte_secondnib == 0x9:
                self.stA_a_y()
                self.pc += 3
            elif self.firstbyte_secondnib == 0x1:
                self.stA_I_y()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x6:
                self.stX_z_y()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x4:
                self.stY_z_x()
                self.pc += 2
            elif self.firstbyte_secondnib == 0xA:
                self.tXS()
                self.pc += 1
            elif self.firstbyte_secondnib == 0x8:
                self.tYA()
                self.pc += 1
            else:
                print("9 not handled yet.")
                self.dumplist.append("{:04X}  {:02X}{:02X}"
                                     "    9 not handled yet.".format(
                                         self.pc, self.firstbyte, self.secondbyte))
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
            elif self.firstbyte_secondnib == 0x0:
                self.ldY_i()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x4:
                self.ldY_z()
                self.pc += 2
            elif self.firstbyte_secondnib == 0xC:
                self.ldY_a()
                self.pc += 3
            elif self.firstbyte_secondnib == 0xA:
                self.tAX()
                self.pc += 1
            elif self.firstbyte_secondnib == 0x8:
                self.tAY()
                self.pc += 1
            else:
                print("A not handled yet.")
                self.dumplist.append("{:04X}  {:02X}{:02X}"
                                     "    A not handled yet.".format(
                                         self.pc, self.firstbyte, self.secondbyte))
                self.pc += 2

        if self.firstbyte_firstnib == 0xB:
            if self.firstbyte_secondnib == 0x5:
                self.ldA_z_x()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x0:
                self.branch_on_carry_set()
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
            elif self.firstbyte_secondnib == 0x8:
                self.clear_overflow()
                self.pc += 1
            elif self.firstbyte_secondnib == 0xE:
                self.ldX_a_x()
                self.pc += 3
            elif self.firstbyte_secondnib == 0xC:
                self.ldY_a_x()
                self.pc += 3
            elif self.firstbyte_secondnib == 0x4:
                self.ldY_z_x()
                self.pc += 2
            elif self.firstbyte_secondnib == 0xA:
                self.tSX()
                self.pc += 1
            else:
                print("B not handled yet.")
                self.dumplist.append("{:04X}  {:02X}{:02X}"
                                     "    B not handled yet.".format(
                                         self.pc, self.firstbyte, self.secondbyte))
                self.pc += 2
        if self.firstbyte_firstnib == 0xC:
            if self.firstbyte_secondnib == 0x9:
                self.compare_accumulator_i()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x1:
                self.compare_accumulator_I_x()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x5:
                self.compare_accumulator_z()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x6:
                self.decrement_memory_z()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x8:
                self.increment_y()
                self.pc += 1
            elif self.firstbyte_secondnib == 0xA:
                self.decrement_x()
                self.pc += 1
            elif self.firstbyte_secondnib == 0xD:
                self.compare_accumulator_a()
                self.pc += 3
            elif self.firstbyte_secondnib == 0xE:
                self.decrement_memory_a()
                self.pc += 3
            elif self.firstbyte_secondnib == 0x0:
                self.compare_y_register_i()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x4:
                self.compare_y_register_z()
                self.pc += 2
            elif self.firstbyte_secondnib == 0xC:
                self.compare_y_register_a()
                self.pc += 3
            else:
                print("C not handled yet.")
                self.dumplist.append("{:04X}  {:02X}{:02X}"
                                     "    C not handled yet.".format(
                                         self.pc, self.firstbyte, self.secondbyte))
            self.pc += 2
        if self.firstbyte_firstnib == 0xD:
            if self.firstbyte_secondnib == 0x0:
                self.branch_on_not_equal()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x5:
                self.compare_accumulator_z_x()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x6:
                self.decrement_memory_z_x()
                self.pc += 2
            elif self.firstbyte_secondnib == 0xD:
                self.compare_accumulator_a_x()
                self.pc += 3
            elif self.firstbyte_secondnib == 0xE:
                self.decrement_memory_a_x()
                self.pc += 3
            elif self.firstbyte_secondnib == 0x8:
                self.clear_decimal()
                self.pc += 1
            elif self.firstbyte_secondnib == 0x9:
                self.compare_accumulator_a_y()
                self.pc += 3
            elif self.firstbyte_secondnib == 0x1:
                self.compare_accumulator_I_y()
                self.pc += 2
            else:
                print("D not handled yet.")
                self.dumplist.append("{:04X}  {:02X}{:02X}"
                                     "    D not handled yet.".format(
                                         self.pc, self.firstbyte, self.secondbyte))
            self.pc += 2
        if self.firstbyte_firstnib == 0xE:
            if self.firstbyte_secondnib == 0x0:
                self.compare_x_register_i()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x1:
                self.subtract_with_carry_I_x()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x4:
                self.compare_x_register_z()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x5:
                self.subtract_with_carry_z()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x6:
                self.increment_memory_z()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x8:
                self.increment_x()
                self.pc += 1
            elif self.firstbyte_secondnib == 0x9:
                self.subtract_with_carry_i()
                self.pc += 2
            elif self.firstbyte_secondnib == 0xA:
                self.no_operation()
                self.pc += 1
            elif self.firstbyte_secondnib == 0xC:
                self.compare_x_register_a()
                self.pc += 3
            elif self.firstbyte_secondnib == 0xD:
                self.subtract_with_carry_a()
                self.pc += 3
            elif self.firstbyte_secondnib == 0xE:
                self.increment_memory_a()
                self.pc += 3
            else:
                print("E not handled yet.")
                self.dumplist.append("{:04X}  {:02X}{:02X}"
                                     "    E not handled yet.".format(
                                         self.pc, self.firstbyte, self.secondbyte))
            self.pc += 2
        if self.firstbyte_firstnib == 0xF:
            if self.firstbyte_secondnib == 0x0:
                self.branch_on_equal()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x1:
                self.subtract_with_carry_I_y()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x5:
                self.subtract_with_carry_z_x()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x6:
                self.increment_memory_z_x()
                self.pc += 2
            elif self.firstbyte_secondnib == 0x8:
                self.set_decimal()
                self.pc += 1
            elif self.firstbyte_secondnib == 0x9:
                self.subtract_with_carry_a_y()
                self.pc += 3
            elif self.firstbyte_secondnib == 0xD:
                self.subtract_with_carry_a_x()
                self.pc += 3
            elif self.firstbyte_secondnib == 0xE:
                self.increment_memory_a_x()
                self.pc += 3
            else:
                print("F not handled yet.")
                self.dumplist.append("{:04X}  {:02X}{:02X}"
                                     "    F not handled yet.".format(
                                         self.pc, self.firstbyte, self.secondbyte))
            self.pc += 2

    def subtract_with_carry_I_y(self):
        print("{:04X}  {:02X}{:02X}  SBC_I_y: ({:02X}), Y".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}  SBC_I_y: ({:02X}), Y".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def subtract_with_carry_I_x(self):
        print("{:04X}  {:02X}{:02X}  SBC_I_x: ({:02X}, X)".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}  SBC_I_x: ({:02X}, X)".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def subtract_with_carry_a_y(self):
        print("{:04X}  {:02X}{:02X}{:02X}  SBC_a_y: {:02X}{:02X}, Y".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}  SBC_a_y: {:02X}{:02X}, Y".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))

    def subtract_with_carry_a_x(self):
        print("{:04X}  {:02X}{:02X}{:02X}  SBC_a_x: {:02X}{:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}  SBC_a_x: {:02X}{:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))

    def subtract_with_carry_a(self):
        print("{:04X}  {:02X}{:02X}{:02X}    SBC_a:   {:02X}{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}    SBC_a:   {:02X}{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))

    def subtract_with_carry_z_x(self):
        print("{:04X}  {:02X}{:02X}  SBC_z_x: {:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}  SBC_z_x: {:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def subtract_with_carry_z(self):
        print("{:04X}  {:02X}{:02X}    SBC_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    SBC_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def subtract_with_carry_i(self):
        print("{:04X}  {:02X}{:02X}    SBC_i:  #{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    SBC_i:  #{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def rotate_right_A_x(self):
        print("{:04X}  {:02X}{:02X}{:02X}  ROR_A: {:02X}{:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}  ROR_A: {:02X}{:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))

    def rotate_left_A_x(self):
        print("{:04X}  {:02X}{:02X}{:02X}  ROL_A: {:02X}{:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}  ROL_A: {:02X}{:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))

    def rotate_right_A(self):
        print("{:04X}  {:02X}{:02X}{:02X}    ROR_A:   {:02X}{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}    ROR_A:   {:02X}{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))

    def rotate_left_A(self):
        print("{:04X}  {:02X}{:02X}{:02X}    ROL_A:   {:02X}{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}    ROL_A:   {:02X}{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))

    def rotate_right_z_x(self):
        print("{:04X}  {:02X}{:02X}  ROR_z_x: {:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}  ROR_z_x: {:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def rotate_left_z_x(self):
        print("{:04X}  {:02X}{:02X}    ROL_z_x: {:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    ROL_z_x: {:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def rotate_right_z(self):
        print("{:04X}  {:02X}{:02X}    ROR_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    ROR_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def rotate_left_z(self):
        print("{:04X}  {:02X}{:02X}    ROL_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    ROL_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def rotate_right_a(self):
        print("{:04X}  {:02X}{:02X}    ROR_a:   A".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    ROR_a:   A".format(
            self.pc, self.firstbyte, self.secondbyte))

    def rotate_left_a(self):
        print("{:04X}  {:02X}{:02X}    ROL_a:   A".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    ROL_a:   A".format(
            self.pc, self.firstbyte, self.secondbyte))

    def return_from_interrupt(self):
        print("{:04X}  {:02X} RTI".format(
            self.pc, self.firstbyte))
        self.dumplist.append("{:04X}  {:02X}      RTI".format(
            self.pc, self.firstbyte))

    def return_from_subroutine(self):
        print("{:04X}  {:02X} RTS".format(
            self.pc, self.firstbyte))
        self.dumplist.append("{:04X}  {:02X}      RTS".format(
            self.pc, self.firstbyte))

    def pull_processor_status(self):
        print("{:04X}  {:02X} PLP".format(
            self.pc, self.firstbyte))
        self.dumplist.append("{:04X}  {:02X}      PLP".format(
            self.pc, self.firstbyte))

    def push_processor_status(self):
        print("{:04X}  {:02X} PHP".format(
            self.pc, self.firstbyte))
        self.dumplist.append("{:04X}  {:02X}      PHP".format(
            self.pc, self.firstbyte))

    def pull_accumulator(self):
        print("{:04X}  {:02X} PLA".format(
            self.pc, self.firstbyte))
        self.dumplist.append("{:04X}  {:02X}      PLA".format(
            self.pc, self.firstbyte))

    def push_accumulator(self):
        print("{:04X}  {:02X} PHA".format(
            self.pc, self.firstbyte))
        self.dumplist.append("{:04X}  {:02X}      PHA".format(
            self.pc, self.firstbyte))

    def increment_y(self):
        print("{:04X}  {:02X} INY".format(
            self.pc, self.firstbyte))
        self.dumplist.append("{:04X}  {:02X}      INY".format(
            self.pc, self.firstbyte))

    def decrement_y(self):
        print("{:04X}  {:02X} DEY".format(
            self.pc, self.firstbyte))
        self.dumplist.append("{:04X}  {:02X}      DEY".format(
            self.pc, self.firstbyte))

    def increment_x(self):
        print("{:04X}  {:02X} INX".format(
            self.pc, self.firstbyte))
        self.dumplist.append("{:04X}  {:02X}      INX".format(
            self.pc, self.firstbyte))

    def decrement_x(self):
        print("{:04X}  {:02X} DEX".format(
            self.pc, self.firstbyte))
        self.dumplist.append("{:04X}  {:02X}      DEX".format(
            self.pc, self.firstbyte))

    def bitwise_or_with_accumulator_a_y(self):
        print("{:04X}  {:02X}{:02X}{:02X}  INC_a_y: {:02X}{:02X}, Y".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}  INC_a_y: {:02X}{:02X}, Y".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))

    def bitwise_or_with_accumulator_a_x(self):
        print("{:04X}  {:02X}{:02X}{:02X}  INC_a_x: {:02X}{:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}  INC_a_x: {:02X}{:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))

    def bitwise_or_with_accumulator_a(self):
        print("{:04X}  {:02X}{:02X}{:02X}  INC_a:   {:02X}{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}  INC_a:   {:02X}{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))

    def bitwise_or_with_accumulator_I_y(self):
        print("{:04X}  {:02X}{:02X}    ORA_I_y: ({:02X}), Y".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    ORA_I_y: ({:02X}), Y".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def bitwise_or_with_accumulator_I_x(self):
        print("{:04X}  {:02X}{:02X}    ORA_I_x: ({:02X}, X)".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    ORA_I_x: ({:02X}, X)".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def bitwise_or_with_accumulator_z_x(self):
        print("{:04X}  {:02X}{:02X}    ORA_z_x: {:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    ORA_z_x: {:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def bitwise_or_with_accumulator_z(self):
        print("{:04X}  {:02X}{:02X}    ORA_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    ORA_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def bitwise_or_with_accumulator_i(self):
        print("{:04X}  {:02X}{:02X}    ORA_i:  #{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    ORA_i:  #{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def no_operation(self):
        print("{:04X}  {:02X}      NOP".format(
            self.pc, self.firstbyte, self.firstbyte))
        self.dumplist.append(
            "{:04X}  {:02X}      NOP".format(self.pc, self.firstbyte, self.firstbyte))

    def jump_to_subroutine(self):
        print("{:04X}  {:02X}{:02X}{:02X}  JSR:     ({:02X}{:02X})".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}  JSR:     ({:02X}{:02X})".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))

    def jump_I(self):
        print("{:04X}  {:02X}{:02X}{:02X}  JMP_I:   ({:02X}{:02X})".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}  JMP_I:   ({:02X}{:02X})".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))

    def jump_a(self):
        print("{:04X}  {:02X}{:02X}{:02X}  JMP_a:   {:02X}{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}  JMP_a:   {:02X}{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))

    def increment_memory_a_x(self):
        print("{:04X}  {:02X}{:02X}{:02X}  INC_a_x: {:02X}{:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}  INC_a_x: {:02X}{:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))

    def increment_memory_a(self):
        print("{:04X}  {:02X}{:02X}{:02X}  INC_a:   {:02X}{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}  INC_a:   {:02X}{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))

    def increment_memory_z_x(self):
        print("{:04X}  {:02X}{:02X}    INC_z_x: {:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    INC_z_x: {:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def increment_memory_z(self):
        print("{:04X}  {:02X}{:02X}    INC_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    INC_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def set_decimal(self):
        print("{:04X}  {:02X}      SED:     {:02X}".format(
            self.pc, self.firstbyte, self.firstbyte))
        self.dumplist.append(
            "{:04X}  {:02X}      SED:     {:02X}".format(self.pc, self.firstbyte, self.firstbyte))

    def clear_decimal(self):
        print("{:04X}  {:02X}      CLD:     {:02X}".format(
            self.pc, self.firstbyte, self.firstbyte))
        self.dumplist.append(
            "{:04X}  {:02X}      CLD:     {:02X}".format(self.pc, self.firstbyte, self.firstbyte))

    def clear_overflow(self):
        print("{:04X}  {:02X}      CLV:     {:02X}".format(
            self.pc, self.firstbyte, self.firstbyte))
        self.dumplist.append(
            "{:04X}  {:02X}      CLV:     {:02X}".format(self.pc, self.firstbyte, self.firstbyte))

    def set_interrupt(self):
        print("{:04X}  {:02X}      SEI:     {:02X}".format(
            self.pc, self.firstbyte, self.firstbyte))
        self.dumplist.append(
            "{:04X}  {:02X}      SEI:     {:02X}".format(self.pc, self.firstbyte, self.firstbyte))

    def clear_interrupt(self):
        print("{:04X}  {:02X}      CLI:     {:02X}".format(
            self.pc, self.firstbyte, self.firstbyte))
        self.dumplist.append(
            "{:04X}  {:02X}      CLI:     {:02X}".format(self.pc, self.firstbyte, self.firstbyte))

    def set_carry(self):
        print("{:04X}  {:02X}      SEC:     {:02X}".format(
            self.pc, self.firstbyte, self.firstbyte))
        self.dumplist.append(
            "{:04X}  {:02X}      SEC:     {:02X}".format(self.pc, self.firstbyte, self.firstbyte))

    def clear_carry(self):
        print("{:04X}  {:02X}      CLC:     {:02X}".format(
            self.pc, self.firstbyte, self.firstbyte))
        self.dumplist.append(
            "{:04X}  {:02X}      CLC:     {:02X}".format(self.pc, self.firstbyte, self.firstbyte))

    def bitwise_exclusive_or_I_y(self):
        print("{:04X}  {:02X}{:02X}    XOR_I_y: ({:02X}), Y".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    XOR_I_y: ({:02X}), Y".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def bitwise_exclusive_or_I_x(self):
        print("{:04X}  {:02X}{:02X}    XOR_I_x: ({:02X}, X)".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    XOR_I_x: ({:02X}, X)".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def bitwise_exclusive_or_a_y(self):
        print("{:04X}  {:02X}{:02X}{:02X}  XOR_a_y: {:02X}{:02X}, Y".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}  XOR_a_y: {:02X}{:02X}, Y".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))

    def bitwise_exclusive_or_a_x(self):
        print("{:04X}  {:02X}{:02X}{:02X}  XOR_a_x: {:02X}{:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}  XOR_a_x: {:02X}{:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))

    def bitwise_exclusive_or_a(self):
        print("{:04X}  {:02X}{:02X}{:02X}  XOR_a:   {:02X}{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}  XOR_a:   {:02X}{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))

    def bitwise_exclusive_or_z_x(self):
        print("{:04X}  {:02X}{:02X}    XOR_z_x: {:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    XOR_z_x: {:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def bitwise_exclusive_or_z(self):
        print("{:04X}  {:02X}{:02X}    XOR_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    XOR_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def bitwise_exclusive_or_i(self):
        print("{:04X}  {:02X}{:02X}    XOR_i:  #{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    XOR_i:  #{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def decrement_memory_a_x(self):
        print("{:04X}  {:02X}{:02X}{:02X}  DEC_a_x: {:02X}{:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}  DEC_a_x: {:02X}{:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))

    def decrement_memory_a(self):
        print("{:04X}  {:02X}{:02X}{:02X}    DEC_a: {:02X}{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}    DEC_a: {:02X}{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))

    def decrement_memory_z_x(self):
        print("{:04X}  {:02X}{:02X}    DEC_z_x: {:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    DEC_z_x: {:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def decrement_memory_z(self):
        print("{:04X}  {:02X}{:02X}    DEC_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    DEC_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def compare_y_register_a(self):
        print("{:04X}  {:02X}{:02X}{:02X}    CPY_a: {:02X}{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}    CPY_a: {:02X}{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))

    def compare_y_register_z(self):
        print("{:04X}  {:02X}{:02X}    CPY_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    CPY_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def compare_y_register_i(self):
        print("{:04X}  {:02X}{:02X}    CPY_i:  #{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    CPY_i:  #{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def compare_x_register_a(self):
        print("{:04X}  {:02X}{:02X}{:02X}    CPX_a: {:02X}{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}    CPX_a: {:02X}{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))

    def compare_x_register_z(self):
        print("{:04X}  {:02X}{:02X}    CPX_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    CPX_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def compare_x_register_i(self):
        print("{:04X}  {:02X}{:02X}  C  PX_i:  #{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    CPX_i:  #{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def compare_accumulator_I_y(self):
        print("{:04X}  {:02X}{:02X}  CMP_I_y:   ({:02X}), Y".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}  CMP_I_y:   ({:02X}), Y".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def compare_accumulator_I_x(self):
        print("{:04X}  {:02X}{:02X}  CMP_I_x:   ({:02X}, X)".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}  CMP_I_x:   ({:02X}, X)".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def compare_accumulator_a_y(self):
        print("{:04X}  {:02X}{:02X}{:02X}  CMP_a_y: {:02X}{:02X}, Y".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}  CMP_a_y: {:02X}{:02X}, Y".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))

    def compare_accumulator_a_x(self):
        print("{:04X}  {:02X}{:02X}{:02X}  CMP_a_x: {:02X}{:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}  CMP_a_x: {:02X}{:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))

    def compare_accumulator_a(self):
        print("{:04X}  {:02X}{:02X}{:02X}  CMP_a:   {:02X}{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}  CMP_a:   {:02X}{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))

    def compare_accumulator_z_x(self):
        print("{:04X}  {:02X}{:02X}  CMP_z_x:   {:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}  CMP_z_x:   {:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def compare_accumulator_z(self):
        print("{:04X}  {:02X}{:02X}    CMP_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    CMP_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def compare_accumulator_i(self):
        print("{:04X}  {:02X}{:02X}    CMP_i:  #{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    CMP_i:  #{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def break_interrupt(self):
        print("{:04}  {:02X}      BRK".format(self.pc, self.firstbyte))
        self.dumplist.append(
            "{:04}  {:02X}      BRK".format(self.pc, self.firstbyte))

    def branch_on_equal(self):
        print("{:04X}  {:02X}{:02X}    BEQ:     {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append(
            "{:04X}  {:02X}{:02X}    BEQ:     {:02X}".format(
                self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def branch_on_not_equal(self):
        print("{:04X}  {:02X}{:02X}    BNE:     {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append(
            "{:04X}  {:02X}{:02X}    BNE:     {:02X}".format(
                self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def branch_on_carry_set(self):
        print("{:04X}  {:02X}{:02X}    BCS:     {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append(
            "{:04X}  {:02X}{:02X}    BCS:     {:02X}".format(
                self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def branch_on_carry_clear(self):
        print("{:04X}  {:02X}{:02X}    BCC:     {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append(
            "{:04X}  {:02X}{:02X}    BCC:     {:02X}".format(
                self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def branch_on_overflow_set(self):
        print("{:04X}  {:02X}{:02X}    BVS:     {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append(
            "{:04X}  {:02X}{:02X}    BVS:     {:02X}".format(
                self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def branch_on_overflow_clear(self):
        print("{:04X}  {:02X}{:02X}    BVC:     {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append(
            "{:04X}  {:02X}{:02X}    BVC:     {:02X}".format(
                self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def branch_on_minus(self):
        print("{:04X}  {:02X}{:02X}    BMI:     {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append(
            "{:04X}  {:02X}{:02X}    BMI:     {:02X}".format(
                self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def branch_on_plus(self):
        print("{:04X}  {:02X}{:02X}    BPL:     {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append(
            "{:04X}  {:02X}{:02X}    BPL:     {:02X}".format(
                self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def bit_a(self):
        print("{:04X}  {:02X}{:02X}{:02X}  BIT_a:   {:02X}{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}"
                             "  BIT_a:   {:02X}{:02X}".format(
                                 self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
                                 self.thirdbyte, self.secondbyte))

    def bit_z(self):
        print("{:04X}  {:02X}{:02X}    BIT_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    BIT_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def arithmetic_shift_left_a_x(self):
        print("{:04X}  {:02X}{:02X}{:02X}  ASL_a_x: {:02X}{:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}"
                             "  ASL_a_x: {:02X}{:02X}, X".format(
                                 self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
                                 self.thirdbyte, self.secondbyte))

    def arithmetic_shift_left_a(self):
        print("{:04X}  {:02X}{:02X}{:02X}  ASL_a:  {:02X}{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}"
                             "  ASL_a:  {:02X}{:02X}".format(
                                 self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
                                 self.thirdbyte, self.secondbyte))

    def arithmetic_shift_left_z_x(self):
        print("{:04X}  {:02X}{:02X}    ASL_z_x: {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}"
                             "    ASL_z_x: {:02X}, X".format(
                                 self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def arithmetic_shift_left_z(self):
        print("{:04X}  {:02X}{:02X}    ASL_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    ASL_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def arithmetic_shift_left_accumulator(self):
        print("{:04X}  {:02X}{:02X}    ASL:     A".format(
            self.pc, self.firstbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    ASL:     A".format(
            self.pc, self.firstbyte, self.secondbyte))

    def and_i(self):
        print("{:04X}  {:02X}{:02X}    AND_i:  #{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    AND_i:  #{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def and_z(self):
        print("{:04X}  {:02X}{:02X}    AND_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    AND_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def and_z_x(self):
        print("{:04X}  {:02X}{:02X}  AND_z_x:   {:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}"
                             "  AND_z_x:   {:02X}, X".format(
                                 self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def and_a(self):
        print("{:04X}  {:02X}{:02X}{:02X}  AND_a:   {:02X}{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}"
                             "  AND_a:   {:02X}{:02X}".format(
                                 self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
                                 self.thirdbyte, self.secondbyte))

    def and_a_x(self):
        print("{:04X}  {:02X}{:02X}{:02X}  AND_a_x: {:02X}{:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}"
                             "  AND_a_x: {:02X}{:02X}, X".format(
                                 self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
                                 self.thirdbyte, self.secondbyte))

    def and_a_y(self):
        print("{:04X}  {:02X}{:02X}{:02X}  AND_a_y: {:02X}{:02X}, Y".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}"
                             "  AND_a_y: {:02X}{:02X}, Y".format(
                                 self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
                                 self.thirdbyte, self.secondbyte))

    def and_I_x(self):
        print("{:04X}  {:02X}{:02X}    AND_I_x: ({:02X}, X)".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}"
                             "    AND_I_x: ({:02X}, X)".format(
                                 self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def and_I_y(self):
        print("{:04X}  {:02X}{:02X}    AND_I_y: ({:02X}), Y".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}"
                             "    AND_I_y: ({:02X}), Y".format(
                                 self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def add_with_carry_I_y(self):
        print("{:04X}  {:02X}{:02X}    ADC_I_y:   ({:02X}), Y".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}"
                             "    ADC_I_y:   ({:02X}), Y".format(
                                 self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def add_with_carry_I_x(self):
        print("{:04X}  {:02X}{:02X}  ADC_I_x: ({:02X}, X)".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}"
                             "    ADC_I_x: ({:02X}, X)".format(
                                 self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def add_with_carry_a_y(self):
        print("{:04X}  {:02X}{:02X}{:02X}  ADC_a_y: {:02X}{:02X}, Y".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}"
                             "  ADC_a_y: {:02X}{:02X}, Y".format(
                                 self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
                                 self.thirdbyte, self.secondbyte))

    def add_with_carry_a_x(self):
        print("{:04X}  {:02X}{:02X}{:02X}  ADC_a_x: {:02X}{:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}"
                             "  ADC_a_x: {:02X}{:02X}, X".format(
                                 self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
                                 self.thirdbyte, self.secondbyte))

    def add_with_carry_a(self):
        print("{:04X}  {:02X}{:02X}{:02X}  ADC_a:   {:02X}{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}"
                             "  ADC_a:   {:02X}{:02X}".format(
                                 self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
                                 self.thirdbyte, self.secondbyte))

    def add_with_carry_z_x(self):
        print("{:04X}  {:02X}{:02X}  ADC_z_x:   {:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}"
                             "    ADC_z_x:   {:02X}, X".format(
                                 self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def add_with_carry_z(self):
        print("{:04X}  {:02X}{:02X}  ADC_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    ADC_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def add_with_carry_i(self):
        print("{:04X}  {:02X}{:02X}  ADC_i:  #{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    ADC_i:  #{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def tYA(self):
        print("{:04X}  {:02X} TYA".format(
            self.pc, self.firstbyte))
        self.dumplist.append("{:04X}  {:02X}      TYA".format(
            self.pc, self.firstbyte))

    def tXS(self):
        print("{:04X}  {:02X} TXS".format(
            self.pc, self.firstbyte))
        self.dumplist.append("{:04X}  {:02X}      TXS".format(
            self.pc, self.firstbyte))

    def tXA(self):
        print("{:04X}  {:02X} TXA".format(
            self.pc, self.firstbyte))
        self.dumplist.append("{:04X}  {:02X}      TXA".format(
            self.pc, self.firstbyte))

    def tSX(self):
        print("{:04X}  {:02X} TSX".format(
            self.pc, self.firstbyte))
        self.dumplist.append("{:04X}  {:02X}      TSX".format(
            self.pc, self.firstbyte))

    def tAY(self):
        print("{:04X}  {:02X} TAY".format(
            self.pc, self.firstbyte))
        self.dumplist.append("{:04X}  {:02X}      TAY".format(
            self.pc, self.firstbyte))

    def tAX(self):
        print("{:04X}  {:02X} TAX".format(
            self.pc, self.firstbyte))
        self.dumplist.append("{:04X}  {:02X}      TAX".format(
            self.pc, self.firstbyte))

    def stY_a(self):
        print("{:04X}  {:02X}{:02X}{:02X}  STY_a:   {:02X}{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}"
                             "  STY_a:   {:02X}{:02X}".format(
                                 self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
                                 self.thirdbyte, self.secondbyte))

    def stY_z_x(self):
        print("{:04X}  {:02X}{:02X}  STY_z_x:   {:02X}, Y".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X} "
                             "   STY_z_x:   {:02X}, Y".format(
                                 self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def stY_z(self):
        print("{:04X}  {:02X}{:02X}  STY_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    STY_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def stX_a(self):
        print("{:04X}  {:02X}{:02X}{:02X}  STX_a:   {:02X}{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}"
                             "  STX_a:   {:02X}{:02X}".format(
                                 self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
                                 self.thirdbyte, self.secondbyte))

    def stX_z_y(self):
        print("{:04X}  {:02X}{:02X}  STX_z_y:   {:02X}, Y".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}"
                             "    STX_z_y:   {:02X}, Y".format(
                                 self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def stX_z(self):
        print("{:04X}  {:02X}{:02X}  STX_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    STX_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def stA_I_y(self):
        print("{:04X}  {:02X}{:02X}  STA_I_y:   ({:02X}), Y".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}"
                             "    STA_I_y: ({:02X}), Y".format(
                                 self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def stA_I_x(self):
        print("{:04X}  {:02X}{:02X}  STA_I_x: ({:02X}, X)".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}"
                             "    STA_I_x: ({:02X}, X)".format(
                                 self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def stA_a_y(self):
        print("{:04X}  {:02X}{:02X}{:02X}  STA_a_y:  {:02X}{:02X}, Y".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}"
                             "  STA_a_y: {:02X}{:02X}, Y".format(
                                 self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
                                 self.thirdbyte, self.secondbyte))

    def stA_a_x(self):
        print("{:04X}  {:02X}{:02X}{:02X}  STA_a_x:  {:02X}{:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}"
                             "  STA_a_x: {:02X}{:02X}, X".format(
                                 self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
                                 self.thirdbyte, self.secondbyte))

    def stA_a(self):
        print("{:04X}  {:02X}{:02X}{:02X}  STA_a:   #{:02X}{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}"
                             "  STA_a:  #{:02X}{:02X}".format(
                                 self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
                                 self.thirdbyte, self.secondbyte))

    def stA_z_x(self):
        print("{:04X}  {:02X}{:02X}  STA_z_x:   {:02X}, X".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}"
                             "    STA_z_x:   {:02X}, X".format(
                                 self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def stA_z(self):
        print("{:04X}  {:02X}{:02X}  STA_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    STA_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def ldA_i(self):
        print("{:04X}  {:02X}{:02X}  LDA_i:  #{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    LDA_i:  #{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def ldA_z(self):
        print("{:04X}  {:02X}{:02X}  LDA_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    LDA_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def ldA_a(self):
        print("{:04X}  {:02X}{:02X}{:02X}  LDA_a:   {:02X}{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte,
            self.thirdbyte, self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}"
                             "  LDA_a:   {:02X}{:02X}".format(
                                 self.pc, self.firstbyte, self.secondbyte,
                                 self.thirdbyte, self.thirdbyte, self.secondbyte))

    def ldA_I_x(self):
        print("{:04X}  {:02X}{:02X}  LDA_I_x: ({:02X} + X)".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}"
                             "    LDA_I_x: ({:02X} + X)".format(
                                 self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def ldA_z_x(self):
        print("{:04X}  {:02X}{:02X}  LDA_z_x: {:02X} + X".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}"
                             "    LDA_z_x: {:02X} + X".format(
                                 self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def ldA_a_x(self):
        print("{:04X}  {:02X}{:02X}{:02X}  LDA_a_x: {:02X}{:02X} + X".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}"
                             "  LDA_a_x: {:02X}{:02X} + X".format(
                                 self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
                                 self.thirdbyte, self.secondbyte))

    def ldA_a_y(self):
        print("{:04X}  {:02X}{:02X}{:02X}  LDA_a_y: {:02X}{:02X} + Y".format(
            self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
            self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}"
                             "  LDA_a_y: {:02X}{:02X} + Y".format(
                                 self.pc, self.firstbyte, self.secondbyte, self.thirdbyte,
                                 self.thirdbyte, self.secondbyte))

    def ldA_I_y(self):
        print("{:04X}  {:02X}{:02X}  LDA_I_y: ({:02X}) + Y".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}"
                             "    LDA_I_y: ({:02X}) + Y".format(
                                 self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def ldX_i(self):
        print("{:04X}  {:02X}{:02X}  LDX_i:  #{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    LDX_i:  #{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def ldX_z(self):
        print("{:04X}  {:02X}{:02X}  LDX_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    LDX_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def ldX_z_x(self):
        print("{:04X}  {:02X}{:02X}  LDX_z_x:   {:02X} + X".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}"
                             "    LDX_z_x:   {:02X} + X".format(
                                 self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def ldX_a(self):
        print("{:04X}  {:02X}{:02X}{:02X}  LDX_a:   {:02X}{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte,
            self.thirdbyte, self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}"
                             "  LDX_a:   {:02X}{:02X}".format(
                                 self.pc, self.firstbyte, self.secondbyte,
                                 self.thirdbyte, self.thirdbyte, self.secondbyte))

    def ldX_a_x(self):
        print("{:04X}  {:02X}{:02X}{:02X}  LDX_a_x: {:02X}{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte,
            self.thirdbyte, self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}"
                             "  LDX_a_x: {:02X}{:02X}".format(
                                 self.pc, self.firstbyte, self.secondbyte,
                                 self.thirdbyte, self.thirdbyte, self.secondbyte))

    def ldY_i(self):
        print("{:04X}  {:02X}{:02X}  LDY_i:  #{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    LDY_i:  #{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def ldY_z(self):
        print("{:04X}  {:02X}{:02X}  LDY_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}    LDY_z:   {:02X}".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))

    def ldY_a(self):
        print("{:04X}  {:02X}{:02X}{:02X}  LDY_a:   {:02X}{:02X}".format(
            self.pc, self.firstbyte, self.secondbyte,
            self.thirdbyte, self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}"
                             "  LDY_a:   {:02X}{:02X}".format(
                                 self.pc, self.firstbyte, self.secondbyte,
                                 self.thirdbyte, self.thirdbyte, self.secondbyte))

    def ldY_a_x(self):
        print("{:04X}  {:02X}{:02X}{:02X}  LDY_a_x: {:02X}{:02X} + X".format(
            self.pc, self.firstbyte, self.secondbyte,
            self.thirdbyte, self.thirdbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}{:02X}"
                             "  LDY_a_x: {:02X}{:02X} + X".format(
                                 self.pc, self.firstbyte, self.secondbyte,
                                 self.thirdbyte, self.thirdbyte, self.secondbyte))

    def ldY_z_x(self):
        print("{:04X}  {:02X}{:02X}  LDY_z_x:   {:02X} + X".format(
            self.pc, self.firstbyte, self.secondbyte, self.secondbyte))
        self.dumplist.append("{:04X}  {:02X}{:02X}"
                             "    LDY_z_x:   {:02X} + X".format(
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

    def _dump_to_file(self):
        with open("dump.txt", "w") as self.dumpfile:
            for item in self.dumplist:
                self.dumpfile.write(item + "\n")


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

    length = len(memory)
    dis.pc = 0x0
    while dis.pc < (length - 2):
        next_byte = memory[dis.pc + 1]
        next_byte = int(next_byte, 16)
        first_byte = memory[dis.pc]
        first_byte = int(first_byte, 16)
        third_byte = memory[dis.pc + 2]
        third_byte = int(third_byte, 16)
        dis.disassembler(first_byte, next_byte, third_byte)
    dis._dump_to_file()


if __name__ == "__main__":
    main()
