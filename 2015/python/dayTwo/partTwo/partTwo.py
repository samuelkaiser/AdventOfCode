""" Advent of Code 2015: Day 2, Part 2 """
""" Samuel Kaiser """
""" Today we are helping the Elves determine how much ribbon they need """

# Input file of
file = "../input.txt"

with open(file) as f:
    data = f.readlines()


# Ribbon required is the smallest perimeter of any one face plus the cubic feet of volume
# Volume = l*w*h

totalRibbonRequired = 0

for gift in data:
    # Each gift's dimensions are delimited by an "x" character as "LxWxH"
    # Turn dimension strings into lists of numeric dimensions
    dimensions = list(map(int, gift.replace('\n','').split('x')))

    length = dimensions[0]
    width = dimensions[1]
    height = dimensions[2]

    volume = length*width*height

    # Gifts require additional wrapping paper that's equal to the area of the smallest side
    allPerimetersOfGift = []

    # Determine possible variations of side areas
    allPerimetersOfGift.append((2*width)+(2*height))
    allPerimetersOfGift.append((2*width)+(2*length))
    allPerimetersOfGift.append((2*length)+(2*height))


    # Determine possible variations of perimiter
    totalRibbonRequired += (min(allPerimetersOfGift) + volume)

# Spit out the answer
print("total ribbon required: " + str(totalRibbonRequired))
