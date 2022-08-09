import super_package

super_package.foo()
super_package.bar()
super_package.xyz() # pure import doesn't hide objects which are not present in __all__!
obj = super_package.Baz()
