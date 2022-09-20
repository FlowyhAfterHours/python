# Source: https://realpython.com/python-walrus-operator
# Repeated function calls

# 1. Bad:

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# stats = {
#   "length": len(numbers),
#   "sum": sum(numbers),
#   "mean:": sum(numbers) / len(numbers)
# }

# 2. Extract variables:

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# # They are still visible after stats
# num_length = len(numbers)
# num_sum = sum(numbers)

# stats = {
#   "length": num_length,
#   "sum": num_sum,
#   "mean:": num_sum / num_length
# }

# We would have to delete them here
# del num_length
# del num_sum

# 3. With walrus:

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# stats = {
#   "length": (num_length := len(numbers)),
#   "sum": (num_sum := sum(numbers)),
#   "mean:": num_sum / num_length
# }

# 4. File statistics:

# import pathlib
# import sys

# for filename in sys.argv[1:]:
#   path = pathlib.Path(filename)
#   stats = (
#     path.read_text().count("\n"),  # no. lines
#     len(path.read_text().split()), # no. words
#     len(path.read_text())          # no. characters
#   )
#   print(*stats, path)

# 5. Reading a file once:

# import pathlib
# import sys

# for filename in sys.argv[1:]:
#   path = pathlib.Path(filename)
#   stats = (
#     (text := path.read_text()).count("\n"),  # no. lines
#     len(text.split()),                       # no. words
#     len(text)                                # no. characters
#   )
#   print(*stats, path)

# List comprehensions

import time
import timeit


def slow(num):
  time.sleep(num)
  return num

numbers = list(range(1, 4))

# def compute_results():
#   return [slow(num) for num in numbers if slow(num) > 0]

# print(timeit.Timer(compute_results).timeit(number=1))

# Idea 1:
# results = []
# for num in numbers:
#     value = slow(num)
#     if value > 0:
#         results.append(value)

# Idea 2:
# results = filter(lambda value: value > 0, (slow(num) for num in numbers))

# Idea 3:
# def compute_results_3():
#   return [value for value in (slow(num) for num in numbers) if value > 0] 

# print(timeit.Timer(compute_results_3).timeit(number=1))

# Idea 4 (walrus):
# def compute_results_4():
#   return [value for num in numbers if (value := slow(num)) > 0]

# print(timeit.Timer(compute_results_4).timeit(number=1))

# While loops

valid_answers = {"Y", "y", "N", "n"}

# Input from user without walrus:
# while True:
#   answer = input("Nuke your hard drive? [Y/N]? ")
#   if answer in valid_answers:
#     break
#   print(f"Invalid answer, choose one of the following: {valid_answers}")

# With walrus:
# while (answer := input("Nuke your hard drive? [Y/N]? ")) not in valid_answers:
  # print(f"Invalid answer, choose one of the following: {valid_answers}")
   
# Check any() exit argument

my_fav_games = [
  "Noita", 
  "Darkest Dungeon", 
  "TBoIR", 
  "Enter the Gungeon", 
  "Hades", 
  "Nethack", 
  "Dead Cells", 
  "FTL", 
  "Into the Breach",
  "Rogue legacy",
  "Spelunky"
]

# print(any(len(game) > 10 for game in my_fav_games))
# print(any(len(game.split()) == 2 for game in my_fav_games))
# print(any(len(game) < 3 for game in my_fav_games))

# print(any(len((witness := game)) > 10 for game in my_fav_games))
# print(witness)
# print(any(len((witness := game).split()) == 2 for game in my_fav_games))
# print(witness)
# print(any(len((witness := game)) < 3 for game in my_fav_games))
# print(witness)