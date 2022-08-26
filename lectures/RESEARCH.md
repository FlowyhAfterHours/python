# Table of contents: <!-- omit in toc -->
  
- [Useful links](#useful-links)
    - [Functions](#functions)
    - [Decorators](#decorators)
    - [Annotations](#annotations)
    - [Generators](#generators)
    - [Classes/Objects](#classesobjects)
      - [Attributes](#attributes)
    - [Docs/PEPs](#docspeps)
      - [Docs howto:](#docs-howto)
      - [Standard functions/methods](#standard-functionsmethods)
    - [Dunder methods](#dunder-methods)
    - [Strings](#strings)
    - [OS](#os)
    - [Lists/Tuples/Dicts](#liststuplesdicts)
    - [Other collections](#other-collections)
    - [General](#general)
    - [Syntax](#syntax)
    - [Secure APIs](#secure-apis)
      - [Importing/modules](#importingmodules)
    - [Python2](#python2)
    - [Standard libraries](#standard-libraries)

***

# Useful links

- [Python Cheatsheet](https://www.pythoncheatsheet.org/)
- [Python Tips](https://book.pythontips.com/en/latest/)
- [Mypy](https://mypy.readthedocs.io/en/stable)
- [Dunder methods cheatsheet](https://blog.finxter.com/python-dunder-methods-cheat-sheet/)
- [Pep8.org](https://pep8.org/#source-file-encoding)
- [Pep8 cheatsheet (gist)](https://gist.github.com/RichardBronosky/454964087739a449da04)
- [Python time complexity](https://wiki.python.org/moin/TimeComplexity)

***

### Functions

- [mypy: generics](https://mypy.readthedocs.io/en/stable/generics.html)
- [stackoverflow: optional function parameters](https://stackoverflow.com/questions/9539921/how-do-i-define-a-function-with-optional-arguments)
- [stackoverflow: equivalent of static variables in function](https://stackoverflow.com/questions/279561/what-is-the-python-equivalent-of-static-variables-inside-a-function)
- [stackoverflow: is there a generic way for a function to reference itself](https://stackoverflow.com/questions/5063607/is-there-a-generic-way-for-a-function-to-reference-itself)
- [stackoverflow: is there a decorator to cache function return values?](https://stackoverflow.com/questions/815110/is-there-a-decorator-to-simply-cache-function-return-values)
- [docs.python: @classmethod](https://docs.python.org/3.10/library/functions.html#classmethod)

***

### Decorators

- [stackoverflow: __all__ export decorator](https://stackoverflow.com/questions/41895077/export-decorator-that-manages-all)
- [realpython: decorators](https://realpython.com/primer-on-python-decorators)
- [stackoverflow: decorators and globals](https://stackoverflow.com/questions/47357635/decorators-and-globals)

***

### Annotations

- [stackoverflow: annotate a function that takes another function as parameter](https://stackoverflow.com/questions/53227628/how-annotate-a-function-that-takes-another-function-as-parameter)

***

### Generators

- [realpython: generators](https://realpython.com/introduction-to-python-generators)

***

### Classes/Objects

- [geeksforgeeks: @classmethod](https://www.geeksforgeeks.org/classmethod-in-python/)
- [towardsdatascuebce OOP Python 8 tips](https://towardsdatascience.com/8-tips-for-object-oriented-programming-in-python-3e98b767ae79)
- [stackoverflow: why do classes inherit object?](https://stackoverflow.com/questions/4015417/why-do-python-classes-inherit-object)
  
#### Attributes
- [stackoverflow: how can dataclasses be better with \_\_slots__](https://stackoverflow.com/questions/50180735/how-can-dataclasses-be-made-to-work-better-with-slots)
- [towardsdatascience: understand \_\_slots__ in Python](https://towardsdatascience.com/understand-slots-in-python-e3081ef5196d)
- [medium: attribute access using \_\_getattr__ and \_\_getattribute__](https://medium.com/@satishgoda/python-attribute-access-using-getattr-and-getattribute-6401f7425ce6)
- [tutorialspoint: accessing attributes and methods in Python](https://www.tutorialspoint.com/accessing-attributes-and-methods-in-python)
- [geeksforgeeks: \_\_getitem__ and \_\_setitem__](https://www.geeksforgeeks.org/__getitem__-and-__setitem__-in-python/)

***

### Docs/PEPs

- [PEP 8 - Style guide](https://peps.python.org/pep-0008/)
- [PEP 257 - Docstring Conventions](https://peps.python.org/pep-0257/)
- [docs.python: data model](https://docs.python.org/3.10/reference/datamodel.html)
- [docs.python: classes](https://docs.python.org/3/tutorial/classes.html)
- [docs.python: weakref](https://docs.python.org/3/library/weakref.html)
- [docs.python: typing](https://docs.python.org/3/library/typing.html)
- [docs.python: inspect](https://docs.python.org/3/library/inspect.html)
- [docs.python: control flow](https://docs.python.org/3/tutorial/controlflow.html)
- [docs.python: modules/packages](https://docs.python.org/3/tutorial/modules.html#packages)
- [docs.python: contextlib](https://docs.python.org/3/library/contextlib.html)

#### Docs howto:

- [docs.python howto: descriptor](https://docs.python.org/3/howto/descriptor.html)
- [docs.python howto: annotations best practices](https://docs.python.org/3/howto/annotations.html)

#### Standard functions/methods

- [docs.python: standard functions list](https://docs.python.org/3/library/functions.html)
- [docs.python: id()](https://docs.python.org/3.10/library/functions.html#id)

***

### Dunder methods

- [geeksforgeeks: \_\_call\_\_](https://www.geeksforgeeks.org/__call__-in-python/)
- [geeksforgeeks: str() vs repr()](https://www.geeksforgeeks.org/str-vs-repr-in-python/)
- [finxter: dunder methods cheatsheet](https://blog.finxter.com/python-dunder-methods-cheat-sheet/)
- [programiz: \_\_iter\_\_](https://www.programiz.com/python-programming/methods/built-in/iter)
- [stackoverflow: module level dunders](https://stackoverflow.com/questions/39044343/coding-style-pep8-module-level-dunders)
- [stackoverflow: what does \_\_all\_\_ mean in Python?](https://stackoverflow.com/questions/44834/what-does-all-mean-in-python)
- [stackoverlow: what is \_\_init\_\_.py](https://stackoverflow.com/questions/448271/what-is-init-py-for)

***

### Strings

- [stackoverflow: Strings are immutable, why a + " " + b works?](https://stackoverflow.com/questions/9097994/arent-python-strings-immutable-then-why-does-a-b-work)

***

### OS

- [stackoverflow: how to os.chdir into a dir created by os.path.join](https://stackoverflow.com/questions/67554847/how-to-os-chdir-into-a-directory-previously-made-through-os-path-join-within-loo)

***

### Lists/Tuples/Dicts

- [tutorialspoint: compare two lists](https://www.tutorialspoint.com/how-to-compare-two-lists-in-python)
- [pythonguides: get first key in dict](https://pythonguides.com/get-first-key-in-dictionary-python/)

***

### Other collections

- [Python Tips: enumerate](https://book.pythontips.com/en/latest/enumerate.html)

***

### General

- [mCoding: fastest way to loop (yt)](https://www.youtube.com/watch?v=Qgevy75co8c)
- [medium: 10 advanced Python tricks to write faster, cleaner code](https://medium.com/pythonland/10-advanced-python-tricks-to-write-faster-cleaner-code-f9ee76fa878f)
- [stackify: performance tips](https://stackify.com/20-simple-python-performance-tuning-tips/)
- [davidamos: comparing floats](https://davidamos.dev/the-right-way-to-compare-floats-in-python/)
- [stackoverflow: assign value if doesn't exist](https://stackoverflow.com/questions/7338501/python-assign-value-if-none-exists)
- [stackoverflow: what does the Ellipsis object do](https://stackoverflow.com/questions/772124/what-does-the-ellipsis-object-do)

***

### Syntax

- [stackoverflow: whad does ** or * do for parameters?](https://stackoverflow.com/questions/36901/what-does-double-star-asterisk-and-star-asterisk-do-for-parameters)
- [stackoverflow: unpacking, extendend unpacking, and nested extended unpacking](https://stackoverflow.com/questions/6967632/unpacking-extended-unpacking-and-nested-extended-unpacking)
- [datacamp: role of underscore in Python](https://www.datacamp.com/tutorial/role-underscore-python)
- [realpython: Python constants](https://realpython.com/python-constants/)
- [learnpython: match-case statement](https://learnpython.com/blog/python-match-case-statement/)
- [towardsdatascience: match case is not that simple](https://towardsdatascience.com/the-match-case-in-python-3-10-is-not-that-simple-f65b350bb025)

***

### Secure APIs

- [stackoverflow: why are private methods not private?](https://stackoverflow.com/questions/70528/why-are-pythons-private-methods-not-actually-private)
- [stackoverflow: hide methods with __](https://stackoverflow.com/questions/12117087/python-hide-methods-with)

#### Importing/modules
- [stackoverflow: hide external modules when importing a module](https://stackoverflow.com/questions/16509012/hide-external-modules-when-importing-a-module-e-g-regarding-code-completion)
- [stackoverflow: hide import in library](https://stackoverflow.com/questions/45331744/hide-import-in-library-python)
- [docstore.mik.ua: module objects](https://docstore.mik.ua/orelly/other/python/0596001886_pythonian-chp-7-sect-1.html)
- [realpython: Python import](https://realpython.com/python-import/#basic-python-import)
- [stackoverflow: private module in a package](https://stackoverflow.com/questions/3602110/python-private-module-in-a-package)
- [stackoverflow: can you hide imported modules from a subpackage?](https://stackoverflow.com/questions/63229633/can-you-hide-imported-modules-from-a-sub-package-in-python)
- [stackoverflow: Python modules hidden even though \_\_init__ is used](https://stackoverflow.com/questions/26088917/python-modules-hidden-though-init-py-is-used)

***

### Python2

- [mypy: type checking Python 2 code](https://mypy.readthedocs.io/en/stable/python2.html)
- [python-future: writing Python 2-3 compatibile code](https://python-future.org/compatible_idioms.html)
- [Python Tips: targeting Python 2+3](https://book.pythontips.com/en/latest/targeting_python_2_3.html)
- [geeksforgeeks: range vs xrange in Python 2](https://www.geeksforgeeks.org/range-vs-xrange-in-python/)
- [guru99: Python 2 vs Python 3](https://www.guru99.com/python-2-vs-python-3.html#3)

***

### Standard libraries

- [stackoverflow: customize argparse help message](https://stackoverflow.com/questions/35847084/customize-argparse-help-message)

***

_END_
