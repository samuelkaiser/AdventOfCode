""" Advent of Code 2015: Day 1, Part 1 """
""" Samuel Kaiser """

# Santa's Instructions File
inputPath = "../input.txt"

with open(inputPath) as file:
    instructions = file.read()

# Santa is lost in an apartment building starting at floor 0
floor = 0

# The instructions for getting to the correct floor are a string of parenthesis.
# "(" Indicates going up one floor
# ")" Indicates going down one floor

for instruction in instructions:
    if(instruction == "("):
        floor += 1
    elif(instruction == ")"):
        floor -= 1


print("floor is: " + str(floor))
