#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

__all__ = []


def higher_order_func(func):
  print(f"Calling {func.__name__}")
  func()


def outer():
  def inner():
    print("I am inner!")
  return inner


def map_examples():
  # Single mapping
  l = [1, 2, 3, 4, 5]
  print(list(map(lambda x: x ** 2, l)))
  
  # Multiple mappings
  l2 = [6, 7, 8, 9]
  print(list(map(lambda x, y: x + y, l, l2)))
  
  # Map with strings
  ids = ["id1", "id2", "id3"]
  print(list(map(lambda x: x[2:], ids)))
  
  # Strings to ints
  numbers = ["1", "2", "3"]
  print(list(map(int, numbers)))
  
  # Starmap
  from itertools import starmap
  print(list(starmap(pow, [(2, 7), (4, 3)])))
  print(list(map(pow, (2, 7), (4, 3))))
  
  # Sanitizing with filter()
  from math import sqrt
  numbers = [1, 27, -14, 0, 69]
  # print(list(map(sqrt, numbers)))
  print(list(map(sqrt, filter(lambda x: x >= 0, numbers))))
  
  # Map and reduce
  from functools import reduce
  from operator import add
  l = range(10, 100, 10)
  print(reduce(add, map(lambda x: x ** 2, l)))


def filter_examples():
  # Basic filtering
  l = range(1, 11)
  print(list(filter(lambda x: x % 2 == 0, l)))
  
  # Filtering strings
  names = ["maciej", "Maciej", "MACIEJ", "szymon", "SZYMON"]
  print(list(filter(lambda s: s.isupper(), names)))

  # Filter types
  l = [1, "24", "Cat", "id15", (6, "XD")]
  print(list(filter(lambda x: isinstance(x, str), l)))
  print(list(filter(lambda x: type(x) == str, l)))

  # Filterfalse
  from itertools import filterfalse
  l = range(1, 11)
  print(list(filterfalse(lambda x: x % 2 == 0, l)))


def reduce_examples():
  from functools import reduce
  # Basic reducing
  l = range(1, 11)
  print(list(l))
  add = lambda x, y: x + y
  print(reduce(add, l))

  # Concatenation
  l = ["hello", "cruel", "world"]
  print(reduce(add, l))

  # Reduce as max
  l = [12, 27, 1, 14, 49]
  print(reduce(lambda x, y: x if x > y else y, l))

  # Initial value
  l = range(1, 11)
  print(reduce(add, l, 100000))


def key_functions_examples():
  uuids = [
    "uuid21",
    "uuid3",
    "uuid67",
    "uuid4",
    "uuid15",
  ]

  print(sorted(uuids))
  print(sorted(uuids, key=lambda x: int(x[4:]))) # Sort by numbers in id
  print(uuids)
  uuids.sort(key=lambda x: int(x[4:]))
  print(uuids)

  # Max by length
  print(max(uuids, key=len))

  # Max by length and number
  print(max(uuids, key=lambda x: len(x) and int(x[4:])))

  # Min by default
  print(min(uuids))
    

if __name__ == "__main__":
  # higher_order_func(lambda: print("hello!"))
  # func = outer()
  # func()
  # outer()()
  # map_examples()
  # filter_examples()
  # reduce_examples()
  # key_functions_examples()
  pass
