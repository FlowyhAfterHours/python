#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

__all__ = []


def greet(name, greeting="Hello"):
  print(f"{greeting}, {name}")


def pow_2(number: int) -> int:
  return number ** 2


def typed_greet(name: str, greeting: str = "Hello"):
  print(f"{greeting}, {name}")


def positional_only(x, y, /):
  print(f"X={x}, Y={y}")


def keyword_only(*, x, y):
  print(f"X={x}, Y={y}")


def positional_and_keyword_only(x, /, y, *, z):
  print(f"X={x}, Y={y}, Z={z}")


def args_kwargs_example(*args, **kwargs):
  print(f"Args={args}, Kwargs={kwargs}")


def keyword_only_with_args(*args, x, y):
  print(f"X={x}, Y={y}, Args={args}")


def foo(x, y, /, *args, **kwargs):
  print(f"X={x}, Y={y}, Args={args}, Kwargs={kwargs}")


global_var = 42


def change_global_var(num: int):
  global_var = num


def change_global_var_the_right_way(num: int):
  global global_var
  global_var = num


def returning_multiple_things(x: int, y: int, z: int):
  return x ** 2, y ** 2, z ** 2


if __name__ == "__main__":
  # greet("Maciej", "Czesc")
  # greet("Maciej", greeting="Czesc")
  # greet(greeting="Czesc", name="Maciej")
  # greet("Maciej")
  # greet("Maciej", "Siema")
  # greet("Maciej", greeting="Hej")
  # print(pow_2(2))
  # print(pow_2("Ala ma kota")) # TypeError
  # print(pow_2(2.15))
  # print(type(pow_2(2)))
  # print(isinstance(pow_2(2), int))
  # typed_greet(12, 14)
  # positional_only(1, 2)
  # positional_only(1, y=3) # TypeError
  # keyword_only(x=4, y=6)
  # keyword_only(1, 2) # TypeError
  # positional_and_keyword_only(1, 2, z=3)
  # positional_and_keyword_only(1, y=2, z=3)
  # args_kwargs_example(1, 2, 3, 4, x=5, z=6)
  # keyword_only_with_args(1, 2, 3, x=4, y=5)
  # foo(1, 2, 3, 4, 5, z=6)
  # foo(1, 2, 3, 4, 5)
  # print(global_var)
  # change_global_var(21)
  # print(global_var)
  # change_global_var_the_right_way(21)
  # print(global_var) 
  # print(returning_multiple_things(2, 4, 6))

  args = [1, 2, 3]
  kwargs = {
    "really_important_list": 4,
    "b": 5
  }
  args_kwargs_example(*args, **kwargs)

  def bar(x, *args, really_important_list, **kwargs):
    print(f"X={x}, List={really_important_list}, Args={args}, Kwargs={kwargs}")

  bar(*args, **kwargs)

  pass
