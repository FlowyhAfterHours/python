# From: https://stackoverflow.com/questions/6967632/unpacking-extended-unpacking-and-nested-extended-unpacking

a, b = 1, 2                          # simple sequence assignment
a, b = ['green', 'blue']             # list asqignment
a, b = 'XY'                          # string assignment
a, b = range(1,5,2)                  # any iterable will do

# nested sequence assignment

(a,b), c = "XY", "Z"                 # a = 'X', b = 'Y', c = 'Z' 

(a,b), c = "XYZ"                     # ERROR -- too many values to unpack
(a,b), c = "XY"                      # ERROR -- need more than 1 value to unpack

(a,b), c, = [1,2],'this'             # a = '1', b = '2', c = 'this'
(a,b), (c,) = [1,2],'this'           # ERROR -- too many values to unpack


# extended sequence unpacking

a, *b = 1,2,3,4,5                    # a = 1, b = [2,3,4,5]
*a, b = 1,2,3,4,5                    # a = [1,2,3,4], b = 5
a, *b, c = 1,2,3,4,5                 # a = 1, b = [2,3,4], c = 5

a, *b = 'X'                          # a = 'X', b = []
*a, b = 'X'                          # a = [], b = 'X'
a, *b, c = "XY"                      # a = 'X', b = [], c = 'Y'
a, *b, c = "X...Y"                   # a = 'X', b = ['.','.','.'], c = 'Y'

a, b, *c = 1,2,3                     # a = 1, b = 2, c = [3]
a, b, c, *d = 1,2,3                  # a = 1, b = 2, c = 3, d = []

a, *b, c, *d = 1,2,3,4,5             # ERROR -- two starred expressions in assignment

(a,b), c = [1,2],'this'              # a = '1', b = '2', c = 'this'
(a,b), *c = [1,2],'this'             # a = '1', b = '2', c = ['this']

(a,b), c, *d = [1,2],'this'          # a = '1', b = '2', c = 'this', d = []
(a,b), *c, d = [1,2],'this'          # a = '1', b = '2', c = [], d = 'this'

(a,b), (c, *d) = [1,2],'this'        # a = '1', b = '2', c = 't', d = ['h', 'i', 's']

*a = 1                               # ERROR -- target must be in a list or tuple
*a = (1,2)                           # ERROR -- target must be in a list or tuple
*a, = (1,2)                          # a = [1,2]
*a, = 1                              # ERROR -- 'int' object is not iterable
*a, = [1]                            # a = [1]
*a = [1]                             # ERROR -- target must be in a list or tuple
*a, = (1,)                           # a = [1]
*a, = (1)                            # ERROR -- 'int' object is not iterable

*a, b = [1]                          # a = [], b = 1
*a, b = (1,)                         # a = [], b = 1

(a,b),c = 1,2,3                      # ERROR -- too many values to unpack
(a,b), *c = 1,2,3                    # ERROR - 'int' object is not iterable
(a,b), *c = 'XY', 2, 3               # a = 'X', b = 'Y', c = [2,3]


                                     # extended sequence unpacking -- NESTED

(a,b),c = 1,2,3                      # ERROR -- too many values to unpack
*(a,b), c = 1,2,3                    # a = 1, b = 2, c = 3

*(a,b) = 1,2                         # ERROR -- target must be in a list or tuple
*(a,b), = 1,2                        # a = 1, b = 2

*(a,b) = 'XY'                        # ERROR -- target must be in a list or tuple
*(a,b), = 'XY'                       # a = 'X', b = 'Y'

*(a, b) = 'this'                     # ERROR -- target must be in a list or tuple
*(a, b), = 'this'                    # ERROR -- too many values to unpack
*(a, *b), = 'this'                   # a = 't', b = ['h', 'i', 's']

*(a, *b), c = 'this'                 # a = 't', b = ['h', 'i'], c = 's'

*(a,*b), = 1,2,3,3,4,5,6,7           # a = 1, b = [2, 3, 3, 4, 5, 6, 7]

*(a,*b), *c = 1,2,3,3,4,5,6,7        # ERROR -- two starred expressions in assignment
*(a,*b), (*c,) = 1,2,3,3,4,5,6,7     # ERROR -- 'int' object is not iterable
*(a,*b), c = 1,2,3,3,4,5,6,7         # a = 1, b = [2, 3, 3, 4, 5, 6], c = 7
*(a,*b), (*c,) = 1,2,3,4,5,'XY'      # a = 1, b = [2, 3, 4, 5], c = ['X', 'Y']

*(a,*b), c, d = 1,2,3,3,4,5,6,7      # a = 1, b = [2, 3, 3, 4, 5], c = 6, d = 7
*(a,*b), (c, d) = 1,2,3,3,4,5,6,7    # ERROR -- 'int' object is not iterable
*(a,*b), (*c, d) = 1,2,3,3,4,5,6,7   # ERROR -- 'int' object is not iterable
*(a,*b), *(c, d) = 1,2,3,3,4,5,6,7   # ERROR -- two starred expressions in assignment


*(a,b), c = 'XY', 3                  # ERROR -- need more than 1 value to unpack
*(*a,b), c = 'XY', 3                 # a = [], b = 'XY', c = 3
(a,b), c = 'XY', 3                   # a = 'X', b = 'Y', c = 3

*(a,b), c = 'XY', 3, 4               # a = 'XY', b = 3, c = 4
*(*a,b), c = 'XY', 3, 4              # a = ['XY'], b = 3, c = 4
(a,b), c = 'XY', 3, 4                # ERROR -- too many values to unpack

# UNPACKING MECHANISM

"""
"XY" -> ("X", "Y")
"X", "Y" -> ("X", "Y")

((a, b), c) = "XY", "Z" ->  (("X", "Y"), "Z")
((a, b), c) = "XYZ" -> ("X", "Y", "Z")

((a,b), c) = [1,2], 'siema' -> ((1,2), ("s", "i", "e", "m", "a")) -> ((1,2), "siema")
((a,b), (c,)) = [1,2], 'siema' -> ((1,2), ("s", "i", "e", "m", "a"))
        (c,)  = ("s", "i", "e", "m", "a")
(a, *b, c) = "X...Y" -> ("X", [".", ".". "."], "Y")

*(a,b) = 1,2 -> (1,2)
*((a,b),) = (1,2)

*((a, *b), c) = 'this' -> (t, h, i, s)
"""
