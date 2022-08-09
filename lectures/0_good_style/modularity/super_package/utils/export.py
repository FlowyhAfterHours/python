#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Export decorator"""

__all__ = ["export"]
__version__ = "0.1"
__author__ = "Maciej Bazela"

from sys import modules


# PROBABLY THE MOST USEFUL DECORATOR YOU'LL SEE THROUGHOUT MY LECTURES
def export(fn):
    mod = modules[fn.__module__]
    name = fn.__name__
    if hasattr(mod, "__all__"):
        all_ = mod.__all__
        if name not in all_:
            all_.append(name)
    else:
        mod.__all__ = [name]
    return fn
