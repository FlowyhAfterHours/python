#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import isclose, sqrt


# Functions can be treated as classes, you can assign variables to them and reference them later.
def function_is_also_an_object(x: float = None, y: float = None, r: float = None) -> float:
    self = function_is_also_an_object
    self.x = 1.0 or x
    self.y = 1.0 or y
    self.r = sqrt(2) if r is None else r
    return f"{self.x}^2 + {self.y}^2 == {self.r:.2f}^2 ? {isclose(self.x ** 2 + self.y ** 2, self.r ** 2)}"


# Setattr sets an attribute to a given object
def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate


@static_vars(x=2.0, y=2.0, r=sqrt(8))
def func_obj_vars_with_decorator() -> float:
    self = func_obj_vars_with_decorator
    return f"{self.x}^2 + {self.y}^2 == {self.r:.2f}^2 ? {isclose(self.x ** 2 + self.y ** 2, self.r ** 2)}"


if __name__ == "__main__":
    print()
    print("function_is_also_an_object attributes before call:", dir(function_is_also_an_object), sep="\n")
    print(function_is_also_an_object())
    print("function_is_also_an_object attributes after call:", dir(function_is_also_an_object), sep="\n")

    print()
    print("func_obj_vars_with_decorator attributes before call:", dir(func_obj_vars_with_decorator), sep="\n")
    print(func_obj_vars_with_decorator())
    print("func_obj_vars_with_decorator attributes after call:", dir(func_obj_vars_with_decorator), sep="\n")
    print()

    print(hasattr(function_is_also_an_object, "x"))
    print(getattr(function_is_also_an_object, "x"))
    delattr(function_is_also_an_object, "x")
    print(hasattr(function_is_also_an_object, "x"))
    print(getattr(function_is_also_an_object, "x"))
