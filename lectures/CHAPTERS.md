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
    - [x] Data model
        - [x] type()/id()/dir()
        - [x] Object attributes customization
            - [x] Standard dunders
            - [x] Descriptors
            - [x] \_\_len\_\_
            - [x] \_\_iter\_\_, \_\_next\_\_, \_\_reversed\_\_, \_\_contains\_\_
            - [x] Numeric types
            - [x] \_\_slots\_\_
          - [x] getattr(), setattr(), hasattr(), delattr()
        - [x] Functions as objects
        - [x] Deleting modules in code 
    - [x] Control flow:
        - [x] Inline if/else aka tenary
        - [x] For/else
        - [x] List checking
        - [x] Where is switch case
    - [ ] Useful functions/arguments:
      - [ ] Sort by keys
      - [x] sys.getsizeof()/pympler
      - [x] print arguments (end=, sep=)
      - [ ] \_\_import__
    - [ ] Walrus operator (:=)

***

1. Functions:
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
    - [ ] Positional arguments

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
    - [ ] Itertools
    - [ ] Functools
    - [ ] JSON
    - [ ] Random
    - [ ] Dataclasses
    - [ ] Argparse
    - [ ] Importlib
    - [ ] Inspect

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

22. Coroutines/Asyncs

***

23. Python 3.10
    - [ ] Type union operator
    - [ ] Type aliasing
    - [ ] Match case
