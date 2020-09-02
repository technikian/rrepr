class Namespace:
	@classmethod
	def from_functions(cls, *functions):
		return cls({f.__name__: f for f in functions})

	@classmethod
	def from_objects(cls, *functions, **variables: dict):
		return cls({**{f.__name__: f for f in functions}, **{k: v for k, v in variables.items()}})

	def __init__(self, names: dict):
		object.__setattr__(self, "names", names)

	def __repr__(self):
		return f"Namespace({repr(object.__getattribute__(self, 'names'))})"

	def __iter__(self):
		return iter(object.__getattribute__(self, "names"))

	def __getattr__(self, item):
		return object.__getattribute__(self, "names").__getitem__(item)

	def __setattr__(self, key, value):
		return object.__getattribute__(self, "names").__setitem__(key, value)
