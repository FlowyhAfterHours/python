#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Let's now assume, that our foo and bar implementations have grown too big.

We would like to split out implementations into separate folders containing
each module.

Our folder structure would look something like this:
super_package
├── __init__.py
├── module_1
│   ├── foo_implementation.py
│   └── __init__.py
└── module_2
    ├── bar_implementation.py
    └── __init__.py

What are we gonna do?

First move all imporant implementation into respective files. Export wanted
methods/functions/classes using __init__.py in each subfolder.
Then import each submodule as we've done before in this file.

If we want to extend our API just add another submodule import here,
or add new feature into already existing submodules.

If we want to hide some implementations from our end-user (for example
experimental changes), we can further narrow down exported objects
by using __all__ dunder here.
"""

from .module_1 import *
from .module_2 import *
from .module_3 import *

__all__ = ["foo", "bar"] # don't export Baz or xyz!
