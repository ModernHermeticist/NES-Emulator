from cpu import *
from rom import *


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

    cpu = CPU()
    rom = ROM()

    for byte in bytes_from_file("SMB.nes"):
        rom.memory.append(hex(byte))


if __name__ == "__main__":
    main()
