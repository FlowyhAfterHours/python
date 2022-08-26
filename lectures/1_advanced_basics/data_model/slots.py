from pympler import asizeof
from sys import getsizeof


class WithoutSlots(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y


class WithSlots(object):
  __slots__ = ["x", "y"]

  def __init__(self, x, y):
    self.x = x
    self.y = y

  # def __setattr__(self, name, value):
  #   self.__slots__.append(name)
  #   # TODO: where should I assign value to stop AttributeError


class SlotsWithNewAttributes(WithSlots):
  def __init__(self):
    pass


class WithSlotsAndDict(object):
  __slots__ = ["x", "y", "__dict__"]

  def __init__(self, x, y):
    self.x = x
    self.y = y


if __name__ == "__main__":
  without = WithoutSlots(1, 2)
  with_ = WithSlots(1, 2)

  print(getsizeof(without))
  print(getsizeof(with_))

  print(asizeof.asizeof(without))
  print(asizeof.asizeof(with_))

  print(dir(without))
  # print(without.__dict__)
  print(dir(with_))
  print(with_.x)
  print(with_.y)

  with2 = SlotsWithNewAttributes()
  with2.z = 3
  print(with2.z)
  print(dir(with2))

  without.z = 3
  print(asizeof.asizeof(without))
  print(asizeof.asizeof(with2))

  with3 = WithSlotsAndDict(1, 2)
  with3.z = 3
  print(with3.z)
  print(dir(with3))
  print(asizeof.asizeof(with3))
