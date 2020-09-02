from rrepr import RRepr

from dataclasses import dataclass
from functools import partial
from random import randint
randint = partial(randint, 0, 256)


WIDTH = 3
HEIGHT = 2


@dataclass
class Rgb:
	red: int
	green: int
	blue: int


@dataclass
class Container:
	values: tuple


rrepr = RRepr.from_objects(Rgb, Container, width=WIDTH, height=HEIGHT)


if __name__ == '__main__':
	pixels = Container(tuple(Rgb(randint(), randint(), randint()) for i in range(WIDTH * HEIGHT)))
	print(repr(pixels))
	print(repr(rrepr(repr(pixels))))
	print(repr(rrepr("width * height")))
