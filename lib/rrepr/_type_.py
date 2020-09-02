from ._parser_ import rrepr


class RRepr:
	def __init__(self, variables: dict):
		self.variables = variables

	def __call__(self, source: str):
		return rrepr(self.variables, source)
