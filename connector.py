import parser
import cmdinput
import executor
import loader
import variables

class connector:
	def __init__(self):
		self.loader = loader.loader()
		self.parser = parser.parser()
		self.cmdinput = cmdinput.cmdinput()
		self.executor = executor.executor()
		self.variables = variables.vars()