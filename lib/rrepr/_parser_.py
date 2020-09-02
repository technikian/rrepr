class Wrap:
	def __init__(self, value=None):
		self.value = value


def gen_variables(callables) -> dict:
	return {f.__name__: f for f in callables}


def rrepr(variables: dict, source: str):
	__rrepr_intern_r = Wrap()
	__rrepr_intern_source = "".join(f"{k}={v}" for k, v in variables.items())
	exec(__rrepr_intern_source)
	__rrepr_intern_source = f"__rrepr_intern_r.value={source}"
	exec(__rrepr_intern_source)
	return __rrepr_intern_r.value
