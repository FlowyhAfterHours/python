#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""See https://realpython.com/python-lambda/ for more in-depth examples. 
Probably the best Python tutorials out there"""


def syntax():
  def identity(x):
    return x
  iden = lambda x: x

  print(identity(1) == iden(1))

  split_into_lines = (lambda x:
                     ('odd' if x % 2 == 1 else 'even')
                     )
  print(split_into_lines(3))


def iife():
  # IIFE
  print((lambda x: x + 14)(4))


def lambda_parameters():
  higher_order_function = lambda x, func: x + func(x)
  # print(higher_order_function(2, lambda x: x * x))
  # print((lambda x, func: x + func(x))(2, lambda x: x * x))
  # print((lambda x, y, z: x + y + z)(1, 2, 3))
  # print((lambda x, y, z=3: x + y + z)(1, 2))
  # print((lambda x, y, z=3: x + y + z)(1, y=2))
  # print((lambda *args: sum(args))(1,2,3))
  # print((lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3))
  # print((lambda x, *, y=0, z: x + y + z)(1, y=2, z=3))
  # print((lambda x, *, y=0, z: x + y + z)(x=1, y=2, z=3))
  # print((lambda x, /, y, z=0: x + y + z)(1, y=2, z=3))
  # print((lambda x, /, y, z=0: x + y + z)(1, 2, 3))
  # print((lambda x, /, y, *, z=0: x + y + z)(1, 2, z=3))
  # print((lambda x, /, y, *, z=0: x + y + z)(1, y=2, z=3))


def caller(func):
  def wraps(*args, **kwargs):
    print(f"Function called: {func.__name__}, args={args}, kwargs={kwargs}")
    return func(*args, **kwargs)
  return wraps


def decorating_lambdas():
  adder = lambda x, y: x + y
  decorated_adder = caller(adder)
  print(decorated_adder(3, 4))
  print(list(map(caller(lambda x: x * 3), range(5))))


def lambda_closure():
  x = 21
  y = 37
  return lambda z: x + y + z
  

def evaluation():
  l = []
  for i in range(5):
    l.append(lambda: i)
  print([func() for func in l])

  # How do we fix that?
  l = []
  for i in range(5):
    l.append(lambda i=i: i) # or lambda x=i: x
  print([func() for func in l])


if __name__ == "__main__":
  # syntax()
  # iife()
  # lambda_parameters()
  # decorating_lambdas()
  # print(lambda_closure()(5))
  evaluation()