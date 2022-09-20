# Table of contents: <!-- omit in toc -->

- [Useful links](#useful-links)
    - [Variables](#variables)
    - [Operators](#operators)
    - [Control flow](#control-flow)
    - [Functions](#functions)
      - [Parameters](#parameters)
      - [Lambda functions](#lambda-functions)
      - [Higher order functions](#higher-order-functions)
      - [Key functions](#key-functions)
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
      - [List](#list)
      - [Dict](#dict)
      - [Comprehensions](#comprehensions)
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

### Variables

- [stackoverflow: using global variables in function](https://stackoverflow.com/questions/423379/using-global-variables-in-a-function)
- [realpython: variables](https://realpython.com/python-variables/#object-references)
- [stackoverflow: function global variables](https://stackoverflow.com/questions/10588317/python-function-global-variables)

***

### Operators

- [realpython: walrus operator](https://realpython.com/python-walrus-operator)

***

### Control flow

- [stackoverflow: how to print nothing when using if statements](https://stackoverflow.com/questions/59548434/how-to-print-nothing-when-using-if-statements)

***

### Functions

- [mypy: generics](https://mypy.readthedocs.io/en/stable/generics.html)
- [medium: using generics in Python](https://medium.com/@steveYeah/using-generics-in-python-99010e5056eb)
- [stackoverflow: is there a generic way for a function to reference itself](https://stackoverflow.com/questions/5063607/is-there-a-generic-way-for-a-function-to-reference-itself)
- [stackoverflow: is there a decorator to cache function return values?](https://stackoverflow.com/questions/815110/is-there-a-decorator-to-simply-cache-function-return-values)
- [docs.python: @classmethod](https://docs.python.org/3.10/library/functions.html#classmethod)
- [stackoverflow: read and reassign a global dict within a function](https://stackoverflow.com/questions/20153512/read-and-reassign-a-global-dictionary-within-a-function)
- [pythontutorial: function docstrings](https://www.pythontutorial.net/python-basics/python-function-docstrings/)
- [stackoverflow: what does @functools.wraps do](https://stackoverflow.com/questions/308999/what-does-functools-wraps-do)
- [realpython: functional programming](https://realpython.com/python-functional-programming)
- [realpython: inner functions](https://realpython.com/inner-functions-what-are-they-good-for)

#### Parameters

- [medium: keyword-only arguments in Python](https://medium.com/analytics-vidhya/keyword-only-arguments-in-python-3c1c00051720)
- [realpython: positional only arguments](https://realpython.com/lessons/positional-only-arguments)
- [stackoverflow: optional function parameters](https://stackoverflow.com/questions/9539921/how-do-i-define-a-function-with-optional-arguments)
- [stackoverflow: equivalent of static variables in function](https://stackoverflow.com/questions/279561/what-is-the-python-equivalent-of-static-variables-inside-a-function)
- [stackoverflow: why can't both args and keyword-only arguments be mixed with *args and **kwargs simultaneously](https://stackoverflow.com/questions/64423083/why-cant-both-args-and-keyword-only-arguments-be-mixed-with-args-and-kwargs)
- [pythontutorial: *args](https://www.pythontutorial.net/python-basics/python-args/)
- [stackoverflow: why is the empty dictionary a dangerous default value in Python](https://stackoverflow.com/questions/26320899/why-is-the-empty-dictionary-a-dangerous-default-value-in-python)
- [stackoverflow: use list as function parameters](https://stackoverflow.com/questions/4979542/python-use-list-as-function-parameters)
- [stackoverflow: can I pass a defined dictionary to kwargs](https://stackoverflow.com/questions/51751929/how-can-i-pass-a-defined-dictionary-to-kwargs-in-python)
- [stackoverflow: converting dict to kwargs](https://stackoverflow.com/questions/5710391/converting-python-dict-to-kwargs)

#### Lambda functions

- [ckl-it.de: Python lambda functions quick cheat sheet](https://ckl-it.de/python3-lambda-functions-quick-cheat-sheet)
- [pythontutorial: lambda expressions](https://www.pythontutorial.net/python-basics/python-lambda-expressions/)
- [realpython: lambda](https://realpython.com/python-lambda/)

#### Higher order functions

- [Python Tips: map, filter](https://book.pythontips.com/en/latest/map_filter.html)
- [pythontutorial: partial functions](https://www.pythontutorial.net/python-basics/python-partial-functions/)
- [realpython: map](https://realpython.com/python-map-function)
- [realpython: reduce](https://realpython.com/python-reduce-function/)
- [realpython: filter](https://realpython.com/python-filter-function/)
- [geeksforgeeks: filter list elements based on given prefix](https://www.geeksforgeeks.org/python-filter-list-elements-starting-with-given-prefix/)

#### Key functions

- [realpython: how to use sorted() and sort()](https://realpython.com/python-sort/)

***

### Decorators

- [stackoverflow: __all__ export decorator](https://stackoverflow.com/questions/41895077/export-decorator-that-manages-all)
- [realpython: decorators](https://realpython.com/primer-on-python-decorators)
- [stackoverflow: decorators and globals](https://stackoverflow.com/questions/47357635/decorators-and-globals)
- [Miguel Grinberg: ultimate guide to Python decorators](https://blog.miguelgrinberg.com/post/the-ultimate-guide-to-python-decorators-part-i-function-registration)
- [machinelearningmastery: gentle introduction to decorators](https://machinelearningmastery.com/a-gentle-introduction-to-decorators-in-python/)
- [towardsdatascience: closures and decorators in Python](https://towardsdatascience.com/closures-and-decorators-in-python-2551abbc6eb6)
- [towardsdatascience: decorators in 10 minutes](https://towardsdatascience.com/python-decorators-in-10-minutes-c8bca1020235)
- [stackoverflow: using decorators to set global variables](https://stackoverflow.com/questions/40987151/using-decorators-in-python-to-set-global-variables)
- [ron.sh: how decorators based routing works in Python](https://ron.sh/how-decorator-based-routing-works-in-python/)
- [stackoverflow: register functions from imported module](https://stackoverflow.com/questions/63583334/python-register-functions-from-imported-module)
- [stackoverflow: how can I decorate all functions imported from a file](https://stackoverflow.com/questions/39184338/how-can-i-decorate-all-functions-imported-from-a-file)

***

### Annotations

- [stackoverflow: annotate a function that takes another function as parameter](https://stackoverflow.com/questions/53227628/how-annotate-a-function-that-takes-another-function-as-parameter)
- [stackoverflow: how do Python functions handle the types of parameters that you pass in](https://stackoverflow.com/questions/2489669/how-do-python-functions-handle-the-types-of-parameters-that-you-pass-in)
- [stackoverflow: how to annotate length of string](https://stackoverflow.com/questions/65521239/how-to-type-annotate-length-of-string)
- [towardsdatascience: type annotations in Python](https://towardsdatascience.com/type-annotations-in-python-d90990b172dc)
- [stackoverflow: how to properly annotate a list of strings](https://stackoverflow.com/questions/31905597/how-to-properly-function-annotate-type-hint-a-list-of-strings)
- [kaggle: Beginner's Cheat Sheet to Python Type Hinting](https://www.kaggle.com/code/debanga/beginner-s-cheat-sheet-to-python-type-hinting/notebook)
- [pythonsheets: Python typing](https://www.pythonsheets.com/notes/python-typing.html)
- [pythontutorial: type hints](https://www.pythontutorial.net/python-basics/python-type-hints/)

***

### Generators

- [realpython: generators](https://realpython.com/introduction-to-python-generators)
- [stackoverflow: what does for i in generator() do](https://stackoverflow.com/questions/30422300/what-does-for-i-in-generator-do)
- [stackoverflow: converting yield from statement to Python 2.7](https://stackoverflow.com/questions/17581332/converting-yield-from-statement-to-python-2-7-code)
- [python.astrotech.io: yield from](https://python.astrotech.io/advanced/generator/yield-from.html)
- [stackoverflow: in practice, what are the main uses for the "yield from" syntax in Python 3.3?](https://stackoverflow.com/questions/9708902/in-practice-what-are-the-main-uses-for-the-yield-from-syntax-in-python-3-3)

***

### Classes/Objects

- [geeksforgeeks: @classmethod](https://www.geeksforgeeks.org/classmethod-in-python/)
- [towardsdatascuebce OOP Python 8 tips](https://towardsdatascience.com/8-tips-for-object-oriented-programming-in-python-3e98b767ae79)
- [stackoverflow: why do classes inherit object?](https://stackoverflow.com/questions/4015417/why-do-python-classes-inherit-object)
- [stackoverflow: class with a registry of methods based on decorators](https://stackoverflow.com/questions/50372342/class-with-a-registry-of-methods-based-on-decorators)
- [stackoverflow:uUpdate a list every time a function within a class is executed with the function arguments and values](https://stackoverflow.com/questions/39154006/update-a-list-every-time-a-function-within-a-class-is-executexecuted-with-the-fu)

#### Attributes
- [stackoverflow: how can dataclasses be better with \_\_slots__](https://stackoverflow.com/questions/50180735/how-can-dataclasses-be-made-to-work-better-with-slots)
- [towardsdatascience: understand \_\_slots__ in Python](https://towardsdatascience.com/understand-slots-in-python-e3081ef5196d)
- [medium: attribute access using \_\_getattr__ and \_\_getattribute__](https://medium.com/@satishgoda/python-attribute-access-using-getattr-and-getattribute-6401f7425ce6)
- [tutorialspoint: accessing attributes and methods in Python](https://www.tutorialspoint.com/accessing-attributes-and-methods-in-python)
- [geeksforgeeks: \_\_getitem__ and \_\_setitem__](https://www.geeksforgeeks.org/__getitem__-and-__setitem__-in-python/)
- [stackoverflow: how to dynamically change \_\_slots__](https://stackoverflow.com/questions/27907373/how-to-dynamically-change-slots-attribute)

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
- [stackoverflow: proper indentation of multiline strings](https://stackoverflow.com/questions/2504411/proper-indentation-for-multiline-strings)
- [stackoverflow: how to remove '\n' from a list element](https://stackoverflow.com/questions/3849509/how-to-remove-n-from-a-list-element)

***

### OS

- [stackoverflow: how to os.chdir into a dir created by os.path.join](https://stackoverflow.com/questions/67554847/how-to-os-chdir-into-a-directory-previously-made-through-os-path-join-within-loo)
- [stackoverflow: how to reliably open a file in the same directory as the currently running script](https://stackoverflow.com/questions/4060221/how-to-reliably-open-a-file-in-the-same-directory-as-the-currently-running-scrip)

***

### Lists/Tuples/Dicts

#### List

- [tutorialspoint: compare two lists](https://www.tutorialspoint.com/how-to-compare-two-lists-in-python)
- [stackoverflow: can I create a "view" on Python list](https://stackoverflow.com/questions/3485475/can-i-create-a-view-on-a-python-list)

#### Dict

- [pythonguides: get first key in dict](https://pythonguides.com/get-first-key-in-dictionary-python/)
- [stackoverflow: flatten nested dictionaries](https://stackoverflow.com/questions/6027558/flatten-nested-dictionaries-compressing-keys)
- [freecodecamp: flatten a dictionary in 4 different ways](https://www.freecodecamp.org/news/how-to-flatten-a-dictionary-in-python-in-4-different-ways/)
- [stackoverflow: hashable dicts](https://stackoverflow.com/questions/1151658/python-hashable-dicts)
- [stackoverflow: how to avoid "RuntimeError: dictionary changed size during iteration"](https://stackoverflow.com/questions/11941817/how-to-avoid-runtimeerror-dictionary-changed-size-during-iteration-error)
- [cito.github.io: never iterate a changing dict](https://cito.github.io/blog/never-iterate-a-changing-dict/)
- [stackoverflow: how to copy a dictionary and only edit the copy](https://stackoverflow.com/questions/2465921/how-to-copy-a-dictionary-and-only-edit-the-copy)
- [stackoverflow: why does my dictionary doesn't get updated outside of the function](https://stackoverflow.com/questions/65306669/why-does-my-dictionary-doesnt-get-updated-outside-of-the-function-python)
- [stackoverflow: Update global dict initialized in module 1 using function from module 2 based on same dict](https://stackoverflow.com/questions/47783867/update-global-dict-initialized-in-module-1-using-function-from-module-2-based-on)
- [stackoverflow: check if given key already exists in dict](https://stackoverflow.com/questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary)
- [stackoverflow: write once dictionary](https://stackoverflow.com/questions/21601593/write-once-dictionary)

#### Comprehensions

- [stackoverflow: list comprehension - want to avoid double evaluation](https://stackoverflow.com/questions/15812779/python-list-comprehension-want-to-avoid-repeated-evaluation)

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
- [stackoverflow: why is list access O(1) in Python](https://stackoverflow.com/questions/37350450/why-is-a-list-access-o1-in-python)
- [stackoverflow: block scope in Python](https://stackoverflow.com/questions/6167923/block-scope-in-python)

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
- [stackoverflow: importing a module based on Python version](https://stackoverflow.com/questions/1875259/importing-a-module-based-on-installed-python-version)
- [stackoverflow: how to change a module variable from another module](https://stackoverflow.com/questions/3536620/how-to-change-a-module-variable-from-another-module)
- [docs.python: how do I share global variables across modules](https://docs.python.org/3/faq/programming.html#how-do-i-share-global-variables-across-modules)

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
- [stackoverflow: require either of two arguments using argparse](https://stackoverflow.com/questions/11154946/require-either-of-two-arguments-using-argparse)
- [stackoverflow: calling a function using argparse](https://stackoverflow.com/questions/40408461/calling-a-function-using-argparse)

***

_END_
