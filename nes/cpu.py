


class CPU(object):

	def __init__(self):

		self.accumulator = [0x0]
		self.index_x = [0x0]
		self.index_y = [0x0]
		self.pc = 0x0
		self.sp = [0x0]
		self.sr = [0x0]
		self.memory = []