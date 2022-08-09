class UnderscoresExample(object):

    def __init__(self) -> None:
        self.visible = 1
        self._internal = 2
        self.__mangled = 3


if __name__ == "__main__":
    # Ignoring values
    a, _, b = (1, 2, 3) # (a, _, b) = (1, 2, 3)
    print(a, b)
    print(_) # I can still access 2,

    # Ignoring multiple values
    a, *_, b = (1, 2, 3, 4) # (a, *_, b) = (1, (2,3), 4)
    print(a, b)
    print(_) # Ignored values will be stored in a list
    a, *_, b = (1, 2, 3)
    print(a, b)
    print(_)

    # Looping
    # It's common to use underscore as iter variable in
    # for loops, if we would like to ignore iterator's value:

    for _ in range(3):
        print("SIEMA")
        print("I can still access _ value:", _)

    # Separating digits
    # We can use underscore to separate binary/octal/hex parts of numbers
    print("Milion equals milion:", 1000000 == 1_000_000)
    print("Binary 5 equals binary 5:", 0b0101 == 0b_0101)
    print("Hex 5 equals hex 5:", 0x0101 == 0x_01_01)

    # Internal use/mangling
    obj = UnderscoresExample()
    print("UnderscoresExample.visible:", obj.visible)
    print("UnderscoresExample._internal:", obj._internal)

    try:
        print("UnderscoresExample.__mangled:", obj.__mangled)
    except AttributeError:
        print("I can't access UnderscoresExample.__mangled!")
    finally:
        print("Double leading underscores == true private!")

    print("Attributes of UnderscoresExample:", dir(obj))
