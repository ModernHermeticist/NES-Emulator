from typing import List


HEADER_SIZE = 16
KB_SIZE = 1024


class ROM(object):

    def __init__(self, rom_bytes: List[int]):
        # TODO unhardcode, pull from rom header
        self.num_prg_blocks = 2

        # program data starts after HEADER_SIZE
        # and lasts for a set number of 16KB blocks
        self.data_bytes = rom_bytes[
            HEADER_SIZE:HEADER_SIZE + (16 * KB_SIZE * self.num_prg_blocks)]

    def get_byte(self, position: int) -> int:
        """
        Gets byte at given position
        :return: int
        """
        return self.data_bytes[position]
