"""See:
https://towardsdatascience.com/python-descriptors-and-how-to-use-them-5167d506af84
"""


from genericpath import getsize


class DataDescriptor:
  def __set_name__(self, owner, name):
      self.name = name

  def __get__(self, instance, owner=None):
    default_value = f"{self.name} not defined"
    print(f"In __get__ of {self}")
    return instance.__dict__.get(self.name, default_value)

  def __set__(self, instance, value):
    instance.__dict__[self.name] = value


class NonDataDescriptor:
  def __set_name__(self, owner, name):
    self.name = name

  def __get__(self, instance, owner=None):
    default_value = f"{self.name} not defined"
    print(f"In __get__ of {self}")
    return instance.__dict__.get(self.name, default_value)


class DatavsNonData:
  a = DataDescriptor()
  b = NonDataDescriptor()


class BoundedInteger(object):
  """Data descriptor bounding integer between two given values (low & high)"""
  def __init__(self, low, high):
    self.low = low
    self.high = high

  def __set_name__(self, owner, name):
    self.name = name
  
  def __get__(self, instance, owner=None):
    return instance.__dict__[self.name]

  def __set__(self, instance, value):
    if value < self.low:
      raise ValueError(f"Value of {instance} cannot be negative, value={value}, low_bound={self.low}")
    if value > self.high:
      raise ValueError(f"Value of {instance} cannot be that big, value={value}, upper_bound={self.high}")
    instance.__dict__[self.name] = value


# TODO: real example
class Person(object):
  age = BoundedInteger(0, 250)
  def __init__(self, age, name):
    self.age = age
    self.name = name


if __name__ == "__main__":
  # example = DatavsNonData()
  # example.__dict__['a'] = 'AAA'
  # example.__dict__['b'] = 'BBB'
  # print(example.__dict__)
  # print(example.a)
  # print(example.b)

  maciek = Person(260, "Maciek")
  print(maciek.age)
  print(maciek.name)
