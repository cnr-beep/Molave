import math #this imports the math library so i can code in the functions.
#these are the following variables, categorized in x and y's and 1 and 2.
x1 = int(input("Enter the first x value: "))
y1 = int(input("Enter the first y value: "))

#the second pair of x and y's are the following:

x2 = int(input("Enter the second x value: "))
y2 = int(input("Enter the second y value: "))

#This is the formula to get the distance
distance = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))

print(f"The distance between points ({x1},{y1}), and ({x2},{y2}) is {distance:.2f}") #prints out the conclusion and is the end of the program

#my reflection about the activity :D
"""Reflection: The activity was fulfilling. Throughout answering the assessment, i figured some of the things out a bit quickly, like the input and curly brackets, which made the activity really fun for me. Initially i thought i was wrong, since the outcome would be 7.81, but after rechecking the khub study guide i had used 1,3,7,8 instead of 2,3,7,8.  """
