# All About Numpy Arithmatic Function , shaping and Re-Shaping ,  Comparison and Indexing and Slicing .....

#(1): Given an array of student marks, find:The minimum mark ,The maximum mark ,The index/position of the student with the minimum mark and maximum marks .

# import numpy as np
# marks = np.random.randint(1,20,10)
# print("Array is : ", marks)
# print("Minimum Marks : ", np.min(marks))
# print("Maximum Marks : ", np.max(marks))
# print("Minimum Marks index : ", np.argmin(marks))
# print("Maximum Marks index : ", np.argmax(marks)) 

#(2): A shop's daily sales are: sales = np.array([100, 150, 200, 120, 180]) : Find the cumulative sales after each day.
# import numpy as np
# sales = ([100, 150, 200, 120, 180])
# print("Cumulative Sales : ", np.cumsum(sales))

#(3):A company records sales of 12 products. Store the sales in a 3 × 4 array.Then find:The reshaped array Maximum sales Position of maximum sales
# import numpy as np
# sales = np.random.randint(1,100,12)
# print("Reshape : " , sales.reshape(3,4))
# print("Maximum Sales : ", np.max(sales))
# print("Maximum Sales Index : ", np.argmax(sales))

#(4):You have points (3, 4) and (7, 10). Calculate the distance between them using NumPy.

# import numpy as np
# x1 , y1 = 4 ,10
# x2 , y2 = 2 ,4
# distance  = np.sqrt((x2 - x1)**2 + (y2 - y1 )**2 )
# print("Total Distance is : ", distance)

#(5): For angles 0°, 30°, 45°, 60°, 90°, calculate both sine and cosine.
# import numpy as np
# angles  = np.array([0, 30, 45, 60, 90])
# radian = np.deg2rad(angles)
# print("Angles In Radian is : ", radian)
# sin  = np.sin(radian)
# print("Angles in sin : ", sin)
# cos = np.cos(radian)
# print("Angles in Cos : ", cos)

#(6):marks = np.array([45, 78, 32, 90, 55, 28, 67, 49])A student passes if their marks are 50 or higher. Find: Passing marks , Failing marks ,Highest mark Lowest mark

# import numpy as np
# marks = np.array([45, 78, 32, 90, 55, 28, 67, 49])
# passed = marks >= 50
# failed = marks < 50
# print("Passing Marks : ", marks[passed])
# print("Fail Marks : ", marks[failed])
# print("Highest Marks : ", np.max(marks))
# print("Lowest Marks : ", np.min(marks))

#(7): Question:Given daily website visitors:visitors = np.array([120, 80, 200, 150, 300, 90])Find:Days where visitors were greater than 150Cumulative visitorsMaximum number of visitors Index of the maximum
# import numpy as np
# visitor  = np.array([120, 80, 200, 150, 300, 90])
# print(visitor)
# high_visitor = visitor > 150
# print("Visitor Greater Than 150 : ", visitor[high_visitor])
# print("Cumulative Visitor : ", np.cumsum(visitor))
# print("Maximum Visitor : ", np.max(visitor))
# print("Maximum Visitor Index : ", np.argmax(visitor))

#(8):You have the marks of 3 students in 4 subjects:
# marks = np.array([
#     [78, 85, 90, 67],
#     [55, 72, 68, 80],
#     [92, 88, 95, 90]
# ])
# Find:The shape of the array The highest mark The lowest mark Which values are greater than 80 Cumulative marks of all values...
# import numpy as np
# marks = np.array([
#     [78, 85, 90, 67],
#     [55, 72, 68, 80],
#     [92, 88, 95, 90]
#  ])
# print(marks)
# print("Shape : ", np.shape(marks))
# print("Highest Marks : ", np.max(marks))
# print("Lowest Marks : ", np.min(marks))
# print("Makrs Greater Than 80 : ", marks[marks > 80])
# print("Cumulative Sum : ", np.cumsum(marks))
# print("Reshape : ", marks.reshape(6,2))
# print("Square Root : ", np.sqrt(marks))


# ALL ABOUT INDEXING AND SLICING ............
# (1):matrix = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]])
# Print:Second row , Third column, Element 80

# import numpy as np
# matrix = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]])
# print("Second Row : ", matrix[1])
# print("Third Column : ", matrix[:,2])
# print("Extract : ", matrix[2,1])

#(2): matrix = np.array([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16] 
# ]) EXTRACT
#              6  7
#              10 11
# import numpy as np
# matrix = np.array([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16] 
# ])
# print("Extract : ", matrix[1:3,1:3])

#(3):
# import numpy as np
# marks = np.array([45, 78, 32, 90, 55, 28, 67, 49])
# print("First Four Student : ", marks[:4])
# print("Last three Student : ", marks[-3:])
# print(marks)
# print("Reverse Order : ", marks[::-1])

#(4):
# import numpy as np
# salary = np.array([45000, 52000, 48000, 61000, 55000, 47000, 70000, 58000])
# print("Salary Of First Four Emp : ", salary[:4])
# print("Salary Of Last Four Emp : ", salary[-4:])
# print("Salary Of Every Second Emp : ", salary[::2])
# print(salary)
# print("All Salary In Reverse Order : ", salary[::-1])