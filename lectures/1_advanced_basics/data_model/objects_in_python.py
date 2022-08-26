"""
The first important thing to know about Python is that 
EVERYTHING IS AN OBJECT.

And by EVERYTHING I mean EVERYTHING:
code, variables, functions, descriptors, classes, classes instances,
weakrefs etc.

Each object has an identity, a type and a value.

- Object's identity never changes once it has been created.
  To get an integer representing object's identity we use id() function.
  'is' operator compares identities between two objects.

- Object's type determines the operations that the object supports and
defines the possible values for objects of that type.
  type() function returns object's type (which is obviously an object itself),
  Type is immutable.

An immutable object which holds a reference to a mutable may of course
change it's value, if the mutable's value changes. However, the immutable
object is still considered as immutable, because the type of objects that
it holds cannot be changed.

Mutability is determined by object's type. For instance: numbers, strings,
tuples are immutable, while dicts and lists are mutables.


Objects are never explicitly destroyed. When they become unreachable they
MAY be garbage-collected.

From docs.python.org, Chapter 3. Data model:

"Note that the use of the implementation's tracing or debugging facilities 
may keep objects alive that would normally be collectable. 
Also note that catching an exception with a 'try…except' 
statement may keep objects alive.

Some objects contain references to “external” resources such as open files 
or windows. It is understood that these resources are freed when 
the object is garbage-collected, but since garbage collection 
IS NOT GUARANTEED to happen, such objects also provide an explicit way to 
release the external resource, usually a close() method. 

Programs are strongly recommended to explicitly close such objects. 
The 'try…finally' statement and the 'with' statement provide convenient 
ways to do this."

"Some objects contain references to other objects; these are called containers. 
Examples of containers are tuples, lists and dictionaries. The references are 
part of a container's value.

[...]

if an immutable container (like a tuple) contains a reference to a mutable
object, its value changes if that mutable object is changed."

"Types affect almost all aspects of object behavior. Even the importance 
of object identity is affected in some sense: for immutable types, operations 
that compute new values may actually return a reference to any existing object 
with the same type and value, while for mutable objects this is not allowed. 
E.g., after a = 1; b = 1, a and b may or may not refer to the same object with 
the value one, depending on the implementation, but after 
c = []; d = [], c and d are guaranteed to refer to two different, unique, 
newly created empty lists."

Standard types:
None - singleton, truth value is false.
NotImplemented - singleton, numeric methods/rich comparison methods should 
          return this if they do not implement operation for given operands
Ellipsis - singleton, accessed through ..., truth value is true

Number:
  Integral:
    int
    bool
  Real (float)
  Complex (complex) (z.real, z.imag)

Sequences (indexed, have lengths, can be sliced):
  Immutable:
    String
    Tuple
    Bytes
  Mutable:
    List
    Byte Arrays (bytearra())

Set types:
  Sets (set())
  Frozen sets (fronzenset())

Mappings:
  Dictionaries

Callable types:
  Function
  Instance methods (classes)
  Generator functions
  Coroutine functions
  Asyncrhonoous generators
  Built-in functions/methods
  Classes (calls create new instances)
  Class instances (they can be made callable by defining __call__)

Modules - basic organizational unit of Python code, imports etc
Custom classes/instances - self-explanatory
I/O objects (file objects)

Internal types:
  Code object
  Frame object
  Traceback object
  Slice object
  Static method object (staticmethod()
  Class method object (classmethod())
"""
