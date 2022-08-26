#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python allows lots of customizability when it comes to it's objects.

The list of dunders, that can be overloaded can be found in python docs:
https://docs.python.org/3.10/reference/datamodel.html#special-method-names

Below you will find basic examples of object customizations.
"""


class BasicCustomized(object):
  def __init__(self):
    # Hey, you just customized your class!
    # __init__ is called after an instance has been created and
    # before returning to the caller
    print("Custom hello!", end="\n\n")

  def __del__(self):
    print("Custom bye!")
    del self

  def __repr__(self):
    return """This should be an \"official\" string representation of this class
    \b\b\b\bIt should even look as a valid Python expression if possible
    """
  
  def __str__(self):
    return "This should be an informal or nicely printable representation"

  def __bytes__(self):
    return b"This should return a bytes object"
    # Or:
    # return bytes("This should return a bytes object", "utf-8")
  
  def __lt__(self, other):
    # If you don't support rich comparisons for this class, just return
    # NotImplemented singleton.
    # Other comparison methods:
    # __le__ (<=)
    # __eq__ (==), by default classes use 'is' as equality operator
    # __ne__ (!=)
    # __gt__ (>)
    # __ge__ (>=)
    print(f"What is other? {type(other)}")
    return NotImplemented

  def __setattr__(self, name, value):
    print(f"I am modified assignment! {name}={value}")
    print(f"Object now has obj.{name}={value}")
    self.__dict__[name] = value

  def __delattr__(self, name):
    print(f"Bye bye {name} :(")
    del self.__dict__[name]


def basicExample():
  basic = BasicCustomized()
  print(basic, end="\n\n")
  print(repr(basic), end="\n\n")
  print(bytes(basic), end="\n\n")

  try: 
    print(basic < 1)
  except TypeError:
    print("Whoops, not implemented!", end="\n\n")

  setattr(basic, "x", 21)
  setattr(basic, "y", 37)

  print(basic.x, basic.y, end="\n\n")

  print(f"Does basic have x? {hasattr(basic, 'x')}")
  print(f"Does basic have y? {hasattr(basic, 'y')}", end="\n\n")

  print(f"What's the value of basic.x? {getattr(basic, 'x')}")
  print(f"What's the value of basic.y? {getattr(basic, 'y')}", end="\n\n")

  delattr(basic, "x")
  delattr(basic, "y")
  print()

  del basic


class ContainerCustomized(object):
  def __init__(self):
    print("I'm a useless container, that only has one slot")
    self.only_slot = None

  def __len__(self):
    return 0 if self.only_slot is None else 1

  def __getitem__(self, key): # obj[a]
    print(f"I don't need a key={key}!")
    return self.only_slot

  def __setitem__(self, key, value): # obj[a] = 3
    print(f"I don't need a key={key}!")
    self.only_slot = value
  
  def __delitem__(self, key): # del obj[a]
    print(f"I don't need a key={key}!")
    self.only_slot = None

  def __iter__(self):
    print("Why would I want to iterate over one slot?")
    return self

  def __next__(self):
    if (self.only_slot is None):
      raise StopIteration
    self.only_slot = None
    return self.only_slot

  def __contains__(self, item):
    print(f"Slot: {self.only_slot}, Item: {item}")
    return self.only_slot == item

  # Other nice to overload methods:
  # __reversed__ - called by reversed()
  # __missing__ - implements self[key] for dict-like classes


def containerExample():
  container = ContainerCustomized()
  print()
  print(f"Getting container length! {len(container)}", end="\n\n")
  print(f"Getting container slot with key 1000: {container[1000]}", end="\n\n")
  print(f"Setting container slot")
  container[500] = 42
  print() 
  print(f"Getting container slot with key 200: {container[200]}", end="\n\n")
  print(f"Deleting key")
  del container[700]
  print()
  print(f"Getting container slot with key 300: {container[300]}", end="\n\n")

  for _ in container:
    print("I can't iterate!")

  container[1] = 1

  print()
  print(f"Does container has a 2? {2 in container}")
  print(f"Does container has a 1? {1 in container}")
  print()

  for _ in container:
    print("I can iterate!")

  print()
  print(f"Does container has a 2? {2 in container}")
  print(f"Does container has a 1? {1 in container}")
  print()


class DescriptorCustomized(object):
  """This will be a read-only descriptor"""
  def __init__(self, value):
    self.value = value
  
  def __set_name__(self, owner, name):
    self.name = name

  def __get__(self, instance, owner=None):
    return self.value
  
  def __set__(self, instance, value):
    raise AttributeError(f"{self.name} is a read-only attribute!")


class Student(object):
  speak = DescriptorCustomized("Piwo")


def descriptorExample():
  debil = Student()
  print(debil.speak)
  debil.speak = "Woda"


if __name__ == "__main__":
  # basicExample()
  # containerExample()
  descriptorExample()