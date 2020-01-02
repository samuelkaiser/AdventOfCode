""" Advent of Code 2015: Day 2, Part 1 """
""" Samuel Kaiser """
""" Today we are helping the Elves determine how much wrapping paper they need """

# Input file of
file = "../input.txt"

with open(file) as f:
    data = f.readlines()

# Counting up the total wrapping paper needed by the Elves
totalWrappingPaper = 0

for gift in data:
    # Each gift's dimensions are delimited by an "x" character as "LxWxH"
    # Turn dimension strings into lists of numeric dimensions
    dimensions = list(map(int, gift.replace('\n','').split('x')))

    length = dimensions[0]
    width = dimensions[1]
    height = dimensions[2]

    # All presents are rectangular prisms
    # Surface area: 2*l*w + 2*w*h + 2*h*l
    surfaceAreaOfGift = (2*length*width) + (2*width*height) + (2*height*length)

    # Gifts require additional wrapping paper that's equal to the area of the smallest side
    allSidesOfGift = []

    # Determine possible variations of side areas
    allSidesOfGift.append(length*width)
    allSidesOfGift.append(width*height)
    allSidesOfGift.append(height*length)

    areaOfSmallestSideOfGift = min(allSidesOfGift)

    wrappingPaperRequired = surfaceAreaOfGift + areaOfSmallestSideOfGift

    # Add each gift's required wrapping paper
    totalWrappingPaper += wrappingPaperRequired

# Spit out the answer
print("total paper required: " + str(totalWrappingPaper))
