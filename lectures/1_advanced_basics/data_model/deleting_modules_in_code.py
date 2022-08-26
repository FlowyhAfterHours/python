from sys import modules
import delete_me


# https://stackoverflow.com/a/1668289
def delete_module(modname):
  try:
    thismod = modules[modname]
  except KeyError:
    raise ValueError(modname)

  del thismod

  for mod in modules.values():
    try:
      delattr(mod, modname)
    except AttributeError:
      pass


def try_oh_noing():
  try:
    delete_me.oh_no()
  except NameError:
    print("delete_me.oh_no() not found!")


if __name__ == "__main__":
  try_oh_noing()
  delete_module('delete_me')
  try_oh_noing()
