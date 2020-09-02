from ._type_ import Namespace
from ._parser_ import rrepr


class RRepr:
	@classmethod
	def from_functions(cls, *functions):
		return cls(Namespace.from_functions(functions))

	@classmethod
	def from_objects(cls, *functions, **variables):
		return cls(Namespace.from_objects(*functions, **variables))

	def __init__(self, namespace: Namespace):
		self.namespace = namespace

	def __call__(self, source: str):
		return rrepr(self.namespace, source)
