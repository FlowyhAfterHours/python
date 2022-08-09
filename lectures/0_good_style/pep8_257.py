#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This is the example module.

This module does stuff.

This is a multi-line docstring. Paragraphs should be separated with 
blank lines. All lines should be at most 79-characters long.

For flowing long blocks of text with fewer structural restrictions 
(docstrings or comments), the line length should be limited to 72 
characters (but mostly no one cares).

Module/packages names should be short, all-lowercase with underscores 
(snake_case).

C/C++ modules shall have a leading underscore (e.g. _epic_c_module)

See: https://peps.python.org/pep-0008/ for other PEP-8 details.
See below links for more condensed explanations:
https://pep8.org/#source-file-encoding
https://gist.github.com/RichardBronosky/454964087739a449da04
"""


from __future__ import barry_as_FLUFL # meme

__all__ = []
__version__ = "0.1"
__author__ = "Maciej Bazulon"


import os  # Standard libraries are imported first
import sys  # Alphabetically, inline comments should be separated by two space
from typing import Any

# import non_existent_lib  # Other libraries next, also alphabetical

# import local_stuff  # Local modules next

# How long are 79 chars?
# thiiislooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong
XD = 5
CONSTANTS_SHOULD_BE_ALL_UPPERCASE = 42
_OMITTED_BY_FROM_IMPORT_ASTERIKS = 21 
# unless we specifically state to import this with from foo import _bar


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


# 2 empty lines between functions or classes (top-level)
@export
def super_function(name):
    return "Super %s" % name


@export
class PascalCase(object):
    """Docstrings start right after first triple-quotes.
    
    Classes/Exceptions should be PascalCase.
    
    Close quotes in new line.
    """

    # Fields declarations, you don't have to declare them, because everything
    # in Python is an object, and you can always do shit like
    # def func():
    #     func.i_hate_python = true
    # or
    # def __init__(self, x, y)
    #     self.x = x
    #     self.y = y
    # and it will automatically set declared attribute.
    # But to keep everything clear, you should declare important vars
    # or constants beforehand. 
    foo = 21
    bar = 37
    _internal_var = "2137"
    class_ = "CamelCase"  # avoid conlficts with keywords

    # Triggers name mangling, useful when you want to truly
    # hide a variable or avoid conflicting in subclasses with
    # same field names.
    # 
    # This one will be expanded to _Camel_case__name_mangling,
    # see print(dir(CamelCase)) and check if it's there :).
    __name_mangling = 4

    __dont_fucking_do_it__ = "Seriously, dunder methods are sacred"

    # also use spaces after each comma, unless it's the last one
    # don't put
    please_dont_use_these_names = ["1", "l", "J", "0", "O", "I", "L"]

    # 1 line break between in-class fields/methods
    # def __init__(self, super_long_variable, another_super_long_variable,
                #  even_longer_super_long_variable, who_cares_at_this_point):
        # if super_long_variable in [42, "42"] \
                # and another_super_long_variable == "7" \
                # or even_longer_super_long_variable < -1 \
                # and who_cares_at_this_point == "nobody":
            # it's good to indicate that our long and useless if ends here
            # raise ValueError("How wtf")
        # 
        # Line breaks enhance readability
        # if super_long_variable < "1" and (another_super_long_variable == "?"
                                        #   or who_cares_at_this_point is None):
            # raise ValueError("Another wtf")
# 
        # self.foo = super_long_variable
        # self.bar = another_super_long_variable

    def __init__(self):
        pass
    
    short_dict = {"XDXDXDXDXDXDXDXDXDXDXDXDXD": "bfsword",
                  "???": "dog"}

    big_long_dict = {
        "foo": "John",
        "bar": "Paul",
        "fizz": "II"
    }

    def methods_should_be_snake_case(self, xd):
        """Functions should be too.

        Use self as first argument. ALWAYS.
        """
        pass

    @classmethod
    def bar(cls):
        """Use cls, keep one-liners in one line!"""
        pass


def naming_conventions():
    print(
    """Naming conventions:
    --------------------------------------------------------------------------
    snake_case: modules, packages, function/method names, variables
    MACRO_CASE: global constants
    PascalCase/CapWords: Classes, Exceptions, Type variable names
                        capitalize abbreviations, e.g: HTTPServerError
    kebab-case: nobody uses it
    --------------------------------------------------------------------------
    _single_leading_underscore: weak "internal use", 
                                from x import * doesn't import this,
                                use for non-public methods/instance variables
    single_trailing_underscore: avoid conflicts with Python keywords
    __double_leading_underscore: name mangling in class atributes, use in 
                                inherited classes
    __double_leading_and_trailing_underscores__: dunder/magic methods,
                                                never invent them,
                                                use them as documented
    --------------------------------------------------------------------------
    AVOID: l (lowercase el), 1 (one), O (uppercase oh), 0 (zero), 
           I (uppercase I), J (uppercase jay), L (uppercase el)
    --------------------------------------------------------------------------
    Always use self for the first argument to instance methods.
    Always use cls for the first argument to class methods.
    --------------------------------------------------------------------------
    Documented interfaces are conisdered PUBLIC.
    All undocumented interfaces are assumed to be internal.
    --------------------------------------------------------------------------
    Declare all exported in __all__.
    Empty __all__ indicates that everything here is internal.
    Even with __all__ you should be using _single_leading_underscore for
    prefixing internal methods/functions/variables/classes/objects etc.
    --------------------------------------------------------------------------
    """
    )


def pet_peeves():
    print(
    """Yes/No vs. pet peeves:

    --------------------------------------------------------------------------
    No:
        spam ( ham[ -1 ], { eggs: 2 } )
    Yes:
        spam(ham[-1], {eggs: 2})
    --------------------------------------------------------------------------
    No:
        bar = (0, )
    Yes:
        bar = (0,)
    --------------------------------------------------------------------------
    No:
        if x == 4 : print x , y ; x , y = y , x
    Yes:
        if x == 4: print x, y; x, y = y, x
    --------------------------------------------------------------------------
    No:
        ham[lower + offset:upper + offset]
        ham[1: 9], ham[1 :9], ham[1:9 :3]
        ham[lower : : upper]
        ham[ : upper]
    Yes:
        ham[lower+offset : upper+offset]
        ham[lower + offset : upper + offset]
        ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
        ham[lower:upper], ham[lower:upper:], ham[lower::step]
        ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
    --------------------------------------------------------------------------
    Fucking no:
        spam (1)
        dict ["key"] = list [index]
        
        x        = 1
        y        = 2
        long_var = 3

        x=1
        y=2
        y=3
    --------------------------------------------------------------------------
    No: (don't use spaces between = in kwargs)
        def complex(real, imag = 0.0):
            return magic(r = real, i = imag)
    Yes:
        def complex(real, imag=0.0):
            return magic(r=real, i=imag)
    --------------------------------------------------------------------------
    No: (use space after semicolon annotations, both spaces for ->)
        def munge(input:AnyStr): ...
        def munge()->PosInt: ...
        def munge(input: AnyStr=None): ...
        def munge(input: AnyStr, limit = 1000): ...
    Yes:
        def munge(input: AnyStr): ...
        def munge() -> AnyStr: ...
        def munge(sep: AnyStr = None): ...
        def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...
    --------------------------------------------------------------------------
    No for compond statements:
        if foo == 'blah': do_blah_thing()
        do_one(); do_two(); do_three()

    Yes: (trailing comma in one-el tuples)
        FILES = ('setup.cfg',)
    --------------------------------------------------------------------------
    No:
        foo = long_function_name(var_one, var_two,
            var_three, var_four)
        def long_function_name(
            var_one, var_two, var_three,
            var_four):
            print(var_one)
    Yes:
        foo = long_function_name(var_one, var_two,
                                var_three, var_four)
        def long_function_name(
                var_one, var_two, var_three,
                var_four):
            print(var_one)
    --------------------------------------------------------------------------
    NO:
        income = (gross_wages +
            taxable_interest +
            (dividends - qualified_dividends) -
            ira_deduction -
            student_loan_interest)
    YES:
        income = (gross_wages
        + taxable_interest
        + (dividends - qualified_dividends)
        - ira_deduction
        - student_loan_interest)
    --------------------------------------------------------------------------
    No:
        import os, sys
    Yes:
        # imports should be separated by new lines
        import os
        import sys

        # It's okay to write from imports in one line:
        from sys import foo, bar, xyz

        # Use breaks between each group of imports.
        # Use absolute imports:
        import mypkg.sibling
        from mypkg import sibling
        from mypkg.sibling import example
    --------------------------------------------------------------------------
    """
    )
    

# Python equivalent of main function.
# This block will only be executed if we run pep8_257.py directly
# using: python3 pep8_257.py
if __name__ == "__main__":
    print(
    """This is an example of using internal dunder names

    You can consider them as constants.

    __name__ is either set to a module name, if you are importing it
    or __main__ if you are running this file using python interpreter

    For example, run this command in your shell:
    python3 -c "print(__name__)"

    __file__ contains path to the module from which you're using
    or accessing this attribute.
    """
    )
    print(f"__name__: {__name__}")
    print(f"__file__: {__file__}")
    print(f"__doc__: {__doc__}")

# New line at the end
