#Provided are the lengths of two sides of a right-angled triangle. Assign the length of the hypotenuse the the variable hypo_len. (Hint: x ** 0.5 will return the square root, or use sqrt from the math module)

import math

side1 = 3
side2 = 4
hypo_len = math.sqrt(side1*side1+side2*side2)

print(hypo_len)
