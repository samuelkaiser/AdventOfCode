""" Advent of Code 2015: Day 1, Part 2 """
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
# In this solution we must determine which instruction first puts Santa in the basement
# The basement is indicated by floor -1

iteration = 1
for instruction in instructions:
    if(instruction == "("):
        floor += 1
    elif(instruction == ")"):
        floor -= 1

    if (floor == -1):
        # if the current floor is below 0, Santa has reached the basement
        print("Santa reached the basement at instruction: " + str(iteration))
        break

    iteration += 1
