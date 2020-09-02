from ._type_ import Namespace


class Wrap:
	def __init__(self, value=None):
		self.value = value


def rrepr(namespace: Namespace, source: str):
	__rrepr_intern_r = Wrap()
	__rrepr_intern_namespace = namespace
	__rrepr_intern_source = "".join(f"{k}=__rrepr_intern_namespace.{k}\n" for k in namespace)
	exec(__rrepr_intern_source)
	__rrepr_intern_source = f"__rrepr_intern_r.value={source}"
	exec(__rrepr_intern_source)
	return __rrepr_intern_r.value
