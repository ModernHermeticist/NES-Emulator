

class ROM(object):

    def __init__(self):

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

        self.memory = []
