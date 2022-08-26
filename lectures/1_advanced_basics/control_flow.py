#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Examples of advanced control flow in Python"""


def tenaries():
  a = None

  if a == None:
    print(
      """Hello, in this file you'll see several examples of nice to know
      \b\b\b\b\b\bPython control flow mechanism.

      \b\b\b\b\b\bYou are probably familiar with if/elif/else syntax, but did you know
      \b\b\b\b\b\bthat you can inline if else into one line?
      """
    )
  elif a == 1:
    pass
  else:
    pass

  print("This is inlined if/else") if a is None else print("Oops!")
  print("""
  \b\bYou can also use 'or' as a short-hand tenary statement:
  """)
  a = a or 1
  print(f"a is now {a}")
  print("""
  \b\bBut be careful, 'or' is falsey, which means that things like
  \b\bFalse, None, 0, empty list and other objects which are considered
  \b\b"empty are equal to False in or context
  """)
  a = 0
  a = 0 or False
  print(a)
  print("Shouldn't it stay 0?")


def for_else():
  print("Python also supports a for/else statement!")
  for i in range(1, 10):
    print(i, end=" ")
  else:
    print("\nI execute only after the loop completes")

  print()

  try:
    print("But what if I was interrupted by the same stop error?")
    for i in range(1, 10):
      raise StopIteration
    else:
      print("42")
  except StopIteration:
    print("Well it doesn't work")

  print("""
  \b\bIt's useful, when you want to for example search for an item
  \b\band implement some mechanism, when nothing was found:
  """)
  for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print( n, 'equals', x, '*', n/x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')


def list_checking():
  print("Slight digression: list's emptiness should be checked with a bare")
  print("'if list' instead of checking it's length!!!")

  empty_list = []
  if empty_list:
    print("It's the right method")

  print("""
  \b\bWhy? Because truth value testing first checks if an __bool__ is
  \b\bimplemented, then it checks if __len__ is implemented and len() is
  \b\bnon-zero. If neither of above are implemented the object is 
  \b\bconsidered true.
  """)


def where_is_switch():
  print("""Before Python 3.10 there was no switch/case statement.
  \b\bBut in Python 3.10 a match-case was introduced, which
  \b\bresembles pattern matching like in Rust-lang.
  """)

  status = 418
  print(f"Status: {status}")
  match status:
    case 400:
      print("Bad request")
    case 404:
      print("Not found")
    case 418:
      print("I'm a teapot")

  print()
  print("You can also unionize multiple patterns:")

  match status:
    case 200 | 201 | 202:
      print("Accepted")
    case 400 | 404 | 418:
      print("Denied")

  print("""
  \b\bIf you're still using <3.10, you have to either write
  \b\ba ton of if/elif/else statements, or make a dictionary which maps
  \b\breponses to given values.
  """)


if __name__ == "__main__":
  tenaries()
  print("===================================================================")
  for_else()
  print("===================================================================")
  list_checking()
  print("===================================================================")
  where_is_switch()