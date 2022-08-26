# Table of contents: <!-- omit in toc -->

- [Syntax](#syntax)
    - [Tenary](#tenary)
    - [For/else](#forelse)
    - [Check if list is empty](#check-if-list-is-empty)
    - [Match case](#match-case)
- [Dunders overloading](#dunders-overloading)
    - [Basic overloading](#basic-overloading)
    - [Simulate iterables](#simulate-iterables)
    - [Descriptors](#descriptors)
- [Functions](#functions)
    - [Default (para-static) variables of a function:](#default-para-static-variables-of-a-function)
- [Classes](#classes)
    - [\_\_slots__](#__slots__)
- [Decorators](#decorators)
    - [Export function decorator](#export-function-decorator)
    - [Set an attribute to a given object (with kwargs)](#set-an-attribute-to-a-given-object-with-kwargs)
- [Annotations](#annotations)
- [Generators](#generators)
- [Importing](#importing)
    - [Splitting code into submodules](#splitting-code-into-submodules)
    - [Deleting imported modules in code (don't do that)](#deleting-imported-modules-in-code-dont-do-that)
- [Style](#style)
    - [PEP8/PEP257](#pep8pep257)

***

# Syntax

### Tenary

**Snippet:**

```py
# One line if/else
# Syntax:
# execute_if_true if expression else execute_if_false
print("True") if var is True else print("False")

# Or
# Syntax:
# expression or expression

# For example, used to assign default values to a variable:
a = a or new_value
# Be careful, or will fail when expression is "falsey" (False, 0, None, empty list etc.)
# Anything that values to False can break it

```

### For/else

**Snippet:**

```py
for i in iterable:
  # do something
else:
  # execute if the WHOLE if passed successfully

```

**Usage:**

```py
# Finding prime numbers from 2 to 9
for n in range(2, 10):
  for x in range(2, n):
    if n % x == 0:
      print( n, 'equals', x, '*', n/x)
      break
  else:
    # loop fell through without finding a factor
    print(n, 'is a prime number')

```

### Check if list is empty

**Snippet:**

```py
# Don't use len(my_list) == 0!!!
if my_list:
  # do something

```

### Match case

**Snippet:**

```py
match var:
  case 1:
    # do sth when 1
  case 2:
    # do sth when 2
  case 3 | 4 | 5: # Combining
    # do sth when 3 or 4 or 5
  case _:
    # default

```

```py
match var:
  case ['evening', action]: # Match list with specific element
    # match when var is a 2-el list, first one is 'evening'
  case [time, action]: # Match any list with same size
    # match when var is a 2-el list
  case [time, *actions]: # Match any list with any size greater or equal to 2
    # match when var is a 2 or more elements list
  case _:
    # default

match var:
  case [('morning' | 'afternoon' | 'evening') | action]: # Sub-pattern
    # match when var is a 2-el list, first one is either 'morning', 'afternon' or 'evening;
  case _:
    # default

match var:
  case ['evening', action] if action not in ['work', 'study']: # Conditions (!!!)
    # match when var is a 2-el list, first one is 'evening', 
    # and action is neither 'work' or 'study'
  case ['evening', _]: # Match 2-el list with one specific element and any
    # match when var is a 2-el list, first one is 'evening', 
    # and action is anything (excluding previous case)
  case [time, action]:
    # match when var is a 2-el list
  case [time, *actions]:
    # match when var is a 2 or more elements list
  case _:
    # default

```

```py
# See: https://towardsdatascience.com/the-match-case-in-python-3-10-is-not-that-simple-f65b350bb025
class Direction:
  def __init__(self, horizontal=None, vertical=None):
    self.horizontal = horizontal
    self.vertical = vertical

match loc: # Object matching (!!!)
  case Direction(horizontal='east', vertical='north'):
    print('You head towards northeast')
  case Direction(horizontal='east', vertical='south'):
    print('You head towards southeast')
  case Direction(horizontal='west', vertical='north'):
    print('You head towards northwest')
  case Direction(horizontal='west', vertical='south'):
    print('You head towards southwest')
  case Direction(horizontal=None):
    print(f'You head towards {loc.vertical}')
  case Direction(vertical=None):
    print(f'You head towards {loc.horizontal}')
  case _:
    print('Invalid Direction')   
   
```

***

# Dunders overloading

### Basic overloading

**Snippet:**

```py
class BasicCustomized(object):
  def __init__(self):
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
```

### Simulate iterables

**Snippet:**

```py
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
```

### Descriptors

**Snippet:**

```py
class DataDescriptor:
  def __set_name__(self, owner, name):
      self.name = name

  def __get__(self, instance, owner=None):
    default_value = f"{self.name} not defined"
    print(f"In __get__ of {self}")
    return instance.__dict__.get(self.name, default=default_value)

  def __set__(self, instance, value):
    instance.__dict__[self.name] = value


class NonDataDescriptor:
  def __set_name__(self, owner, name):
    self.name = name

  def __get__(self, instance, owner=None):
    default_value = f"{self.name} not defined"
    print(f"In __get__ of {self}")
    return instance.__dict__.get(self.name, default=default_value)

```

**Usage:**

```py
class DatavsNonData:
  a = DataDescriptor()
  b = NonDataDescriptor()

# When accessing elements, Python first looks, whether a data descriptor is present
# Then it checks __dict__
# And at the end it checks a non-data descriptor


example = DatavsNonData()
example.__dict__['a'] = 'AAA'
example.__dict__['b'] = 'BBB'
print(example.__dict__) 
# {'a': 'AAA', 'b': 'BBB'}
print(example.a) 
# In __get__ of <__main__.DataDescriptor object at 0x7fedaaafbfd0> 
# AAA
print(example.b) # It goes straight to __dict__, because example.b is a non-data descriptor
# BBB
```

Other useful example:

**Snippet:**

```py
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
      raise ValueError(f"Value of {instance} cannot be negative, value={value}, lower_bound={self.low}")
    if value > self.high:
      raise ValueError(f"Value of {instance} cannot be that big, value={value}, upper_bound={self.high}")
    instance.__dict__[self.name] = value

```

**Usage:**

```py
class Person(object):
  age = BoundedInteger(0, 250)
  def __init__(self, age, name):
    self.age = age
    self.name = name

maciek = Person(260, "Joe") 
# ValueError: Value of <__main__.Person object at 0x7fedaaafbbb0> cannot be that big, value=260, upper_bound=250
print(maciek.age)
print(maciek.name)

```


***

# Functions

### Default (para-static) variables of a function:

**Snippet:**

```py
# Functions can be treated as classes, you can assign variables to them and reference them later.
def function_is_also_an_object(x: float = None, y: float = None, r: float = None) -> float:
    self = function_is_also_an_object
    self.x = 1.0 or x
    self.y = 1.0 or y
    self.r = sqrt(2) if r is None else r
    return f"{self.x}^2 + {self.y}^2 == {self.r:.2f}^2 ? {isclose(self.x ** 2 + self.y ** 2, self.r ** 2)}"

```

***

# Classes

### \_\_slots__

**Snippet:**

```py
class WithoutSlots(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y


class WithSlots(object):
  __slots__ = ["x", "y"]

  def __init__(self, x, y):
    self.x = x
    self.y = y

# You can't add new attributes to a class which has __slots__ only
# But you can inherit it, which adds the ability to add new attributes

class SlotsWithNewAttributes(WithSlots):
  def __init__(self):
    pass

# Or add __dict__ manually:

class WithSlotsAndDict(object):
  __slots__ = ["x", "y", "__dict__"]

  def __init__(self, x, y):
    self.x = x
    self.y = y

```

**Usage:**

```py
from pympler import asizeof

without = WithoutSlots(1, 2)
with_ = WithSlots(1, 2)

print(asizeof.asizeof(without)) # 328
print(asizeof.asizeof(with_)) # 112 (!!!)

without.z = 3

with2 = SlotsWithNewAttributes()
with2.z = 3
print(with2.z) # 3

with3 = WithSlotsAndDict(1, 2)
with3.z = 3
print(with3.z) # 3


print(asizeof.asizeof(without)) # 456
print(asizeof.asizeof(with2)) # 256 (!!!)
print(asizeof.asizeof(with3)) # 312

```

***

# Decorators

### Export function decorator

Adds ```fn``` function to \_\_all__.
```fn``` will be visible in all import statements 

**Snippet:**

```py
def export(fn):
    mod = sys.modules[fn.__module__]
    name = fn.__name__
    if hasattr(mod, "__all__"):
        all_ = mod.__all__
        if name not in all_:
            all_.append(name)
    else:
        mod.__all__ = [name]
    return fn

```

**Usage:**

```py
@export
def super_function(name):
    return "Super %s" % name

```

### Set an attribute to a given object (with kwargs)

**Snippet**:

```py
def static_vars(**kwargs):
  def decorate(func):
    for k in kwargs:
      setattr(func, k, kwargs[k])
    return func
  return decorate

```

**Usage:**:

```py
from math import sqrt, isclose

# Now this function has x, y, and r attributes bound to it
@static_vars(x=2.0, y=2.0, r=sqrt(8))
def func_obj_vars_with_decorator() -> float:
  self = func_obj_vars_with_decorator
  return f"{self.x}^2 + {self.y}^2 == {self.r:.2f}^2 ? " \
    + f"{isclose(self.x ** 2 + self.y ** 2, self.r ** 2)}"

```

***

# Annotations

*Placeholder*

***

# Generators

*Placeholder*

***

# Importing

### Splitting code into submodules

Let's say we've two really important API functions: 
foo() and bar()

foo() implementation is present in module_1.py
bar() implementation is present in module_2.py

Let's assume first that we have following folder structure:

great_package
├── \_\_init__.py
├── module_1.py
└── module_2.py

How do we export our functions safely and let the end user use both foo() 
and bar() with only one import statement?

```py
# __init__.py
from .module_1 import *
from .module_2 import *


__all__ = ["foo", "bar"]

```

```py
# module_1.py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Really important foo implementation"""

__all__ = ["foo"]
__version__ = "0.1"
__author__ = "Myself"


important_1 = important_2 = None


def foo():
  pass # just a placeholder!

```

```py
# module_2.py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Really important bar implementation"""

__all__ = ["bar"]
__version__ = "0.1"
__author__ = "Myself"


important_1 = important_2 = None


def bar():
  pass # just a placeholder!

def baz():
  pass

```

Now everything is safely guarded when using ```from_great_package import *```.

If we'd like to split our code into separate folders for each submodule, we have to create
```__init__.py``` in each directory, export functions using ```__all__``` and import each of them
in our ```__init__.py``` in the parent folder.

### Deleting imported modules in code (don't do that)

See: https://stackoverflow.com/a/1668289

**Snippet:**

```py
def delete_module(modname):
  try:
    thismod = modules[modname]
  except KeyError:
    raise ValueError(modname)

  del thismod

  for mod in modules.values():
    try:
      delattr(mod, modname)
    except AttributeError:
      pass

```

**Usage:**

```py
# delete_me.py
def oh_no():
  print("Oh no!")

```

```py
import delete_me

def try_oh_noing():
  try:
    delete_me.oh_no()
  except NameError:
    print("delete_me.oh_no() not found!")


if __name__ == "__main__":
  try_oh_noing() # Oh no!
  delete_module('delete_me')
  try_oh_noing() # delete_me.oh_no() not found!

```

***

# Style

### PEP8/PEP257

Please see [this file](./0_good_style/pep8_257.py) for general style tips.