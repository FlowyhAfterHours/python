#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This is just an example how to manage your API with __init__.py

This file is reponsible for tying submodules into one package.

For instance, let's say we've two really important API functions: 
foo() and bar()

foo() implementation is present in module_1.py
bar() implementation is present in module_2.py

Let's assume first that we have following folder structure:

great_package
├── __init__.py
├── module_1.py
└── module_2.py

How do we export our functions safely and let the end user use both foo() 
and bar() with only one import statement?
"""

from .module_1 import *
from .module_2 import *


__all__ = ["foo", "bar"]

# We have imported both submodules into this __init__.py file, 
# but what does it achieve?

# If you've looked into module_1.py and module_2.py you would have noticed
# that both foo() and bar() are explicitly exported using __all__ dunder.
# Because of that, we can then try to import this whole great_package
# folder as a whole module containing both foo() and bar() submodules.
# See test1.py for more details.
