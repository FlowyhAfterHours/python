***

0. Good style
    - [x] Naming conventions (PEP 8):
        - [x] Proper naming with underscores: weak internal use, name mangling,
              magic objects, keyword conflicts
        - [x] Variables, classes, functions, modules naming
    - [x] Module level dunder names
    - [x] Internal dunder names
    - [x] General style recommendations
    - [x] Docstrings (PEP 257)
    - [x] Packages and submodules management with \_\_init__.py

***

1. "More advanced" basics:
    - [x] Underscores:
        - [x] Ignoring variables
        - [x] Digits separating
        - [x] Interpreter expression storing
    - [x] List/Tuple unpacking
    - [?] Everything is an object
    - [?] Inline if/else
    - [?] Class dunder names
    - [ ] Sort by keys
    - [ ] Control flow:
        - [ ] Tenary
        - [ ] For else
        - [ ] List checking
    - [ ] Useful functions/arguments:
      - [ ] type()/id()/dir()/inspect module
      - [ ] sys.getsizeof()
      - [ ] print arguments (end=, sep=)
    - [ ] Walrus operator (:=)
    - [ ] \_\_import__

***

2. Functions:
    - [ ] Default parameters, keyword arguments
    - [ ] Parameter typing
    - [ ] *args, **kwargs
    - [ ] return multiple objects
    - [ ] global
    - [ ] Lambda functions
    - [ ] Nested functions
    - [ ] Return function objects:
        - [ ] @functools.wraps(func)
    - [ ] Generic funcions
    - [ ] Higher order functions
    - [ ] map()/filter()/reduce()
    - [ ] Function caching

***

3. Lists/Tuples:
    - [ ] len()
    - [ ] Slicing
    - [ ] Slice-copying
    - [ ] Negative indexes
    - [ ] Concatenation/Repetition
    - [ ] Looping:
        - [ ] for .. in 
        - [ ] enumerate()
        - [ ] zip()
    - [ ] in/not in
    - [ ] Unpacking
    - [ ] Swapping
    - [ ] .index()
    - [ ] append()/insert()
    - [ ] del/remove()/pop()
    - [ ] Sorting:
        - [ ] reverse=
        - [ ] key=
        - [ ] sorted()
            - [ ] sorted(, key=)
    - [ ] Converting lists <-> Tuples
    - [ ] Flattening

***

4. Dictionaries:
    - [ ] values()/keys()/items()
    - [ ] for key, value in items()
    - [ ] in
    - [ ] get()
    - [ ] setdefault()
    - [ ] Merging:
        - [ ] update()
        - [ ] { **dict1, **dict2 }
        - [ ] dict1 | dict2
    - [ ] Sort by keys or values
    - [ ] Combine two lists into a dict
    - [ ] Unpacking
    - [ ] Key renaming

***

5. Sets:
    - [ ] add()/update()
    - [ ] remove()/discard()
    - [ ] union()/intersection()/difference()/symmetric_difference()

***

6. Comprehensions:
    - [ ] List
    - [ ] Tuple
    - [ ] Dictionary
    - [ ] Set
    - [ ] Conditionals
    - [ ] General tips/tricks

***

7. Generators (good tutorial here):
    - [ ] yield
    - [ ] Comprehensions
    - [ ] cProfiling
    - [ ] send()/throw()/close()
    - [ ] Example: palindromes
    - [ ] Example: data pipelines (!!!)

***

8. Strings:
    - [ ] Escape characters
    - [ ] Raw strings
    - [ ] Multiline strings
    - [ ] Slicing
    - [ ] Char array
    - [ ] in/not in
    - [ ] Immutability
    - [ ] isX()/upper()/lower()
    - [ ] startswith()/endswith()
    - [ ] join()/split()
    - [ ] ljust()/center()/rjust()
    - [ ] strip()/lstrip()/rstrip()
    - [ ] Formatting
    - [ ] Template strings

***

9. Regex:
    - [ ] compile()
    - [ ] search()
    - [ ] group()/groups()
    - [ ] Symbols:
        - [ ] Pipe (multiple groups)
        - [ ] ? - optional
        - [ ] * - zero or more
        - [ ] + - one or more
        - [ ] {} - repetitions/range
        - [ ] ^ - starts with
        - [ ] $ - ends with
        - [ ] . - wildcard
        - [ ] .* - match anything
    - [ ] Greedy/non-greedy matching
    - [ ] findall()
    - [ ] Custom character classes
    - [ ] Case-insensitive matching (re.I)
    - [ ] String substitution
    - [ ] Complex regular expressions:
        - [ ] Multiline regex
        - [ ] Comments

***

10. Files/Directories
    - [ ] os/pathlib
    - [ ] Path joining
    - [ ] getcwd()/chdir()
    - [ ] parent=True
    - [ ] Absolute/relative paths
    - [ ] Validity:
        - [ ] exists()
        - [ ] isfile()/is_file()
        - [ ] isdir()/is_dir()
        - [ ] Get file size
    - [ ] List directory
    - [ ] Deletion
    - [ ] shutil
      - [ ] copy()/copytree()
      - [ ] move()
      - [ ] rmtree()
    - [ ] Walking a directory tree

***

11. File I/O:
    - [ ] Most likely you are using open() wrong
    - [ ] with open() args
    - [ ] read()/readlines()
    - [ ] Writting/appending to a file
    - [ ] JSON
    - [ ] Using generators to read a file

***

12. Context managers:
    - [ ] Custom context managers:
        - [ ] Using functions
        - [ ] Using classes
    - [ ] Tricks

***

13. Classes:
    - [ ] New styles classes
    - [ ] Naming conventions
    - [ ] Magic/dunder methods:
        - [ ] \_\_eq__
        - [ ] \_\_repr__
        - [ ] \_\_str__
    - [ ] Name mangling
    - [ ] Inheritance
    - [ ] Private/Internal fields/methods
    - [ ] \_\_slots__
    - [ ] @staticmethod
    - [ ] @property
    - [ ] @{name}.setter
    - [ ] @dataclass

***

14. Decorators:
    - [ ] Simple decorators:
        - [ ] Function decorators
        - [ ] Returning values from decorators
        - [ ] Decorating functions with parameters
        - [ ] @functools.wraps(func)
    - [ ] Classes:
        - [ ] Decorating methods
        - [ ] Decorating classes
    - [ ] Nesting
    - [ ] Decorator with parameters
    - [ ] Remembering states
    - [ ] Classes as decorators
    - [ ] Singletons
    - [ ] Caching
    - [ ] Set function parameters

***

15. Debugging:
    - [ ] try except finally
    - [ ] raise
    - [ ] Custom exceptions
    - [ ] Traceback
    - [ ] assert
    - [ ] Logging
    - [ ] Unit testing

***

16. Standard libraries:
    - [ ] Datetime
    - [ ] Itertoorls
    - [ ] JSON
    - [ ] Random
    - [ ] Dataclasses
    - [ ] Argparse
    - [ ] Importlib

***

17. Python 2+3 targetting
    - [ ] \_\_future__
    - [ ] module naming
    - [ ] try except ImportError
    - [ ] Obsolete Python 2 builtins
    - [ ] enum/singledispatch/pathlib

***

18. More builtins

***

19. setup.\py

***

20. Virtual Environment

***

21. C extensions

***

22. Coroutines  

***
