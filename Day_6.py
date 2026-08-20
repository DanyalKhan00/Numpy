# import numpy as np
# print(np.all(np.array([1,2,3,4,5])> 0 ))
# print()
# print(np.any(np.array([1,2,3,4,5])> 0 ))
# All About The axis Parameter 	Mean, Median, and Standard Deviation np.any() and np.all() 	np.unique
#(1): Given the following 2D array, find the mean, median, and standard deviation of each column.
# import numpy as np
# marks = np.array([
#     [70, 80, 90],
#     [60, 75, 85],
#     [80, 85, 95]
# ])
# print("Mean : ", np.mean(marks , axis=0))
# print("Median : ", np.median(marks , axis = 0))
# print("Standard Deviation : ", np.std(marks , axis=0))

#(2): Given the marks of 3 students in 3 subjects, determine: Whether each subject has at least one student who scored above 80 Whether all students scored above 50 in each subject
# import numpy as np
# marks = np.array([
#     [85, 70, 90],
#     [60, 80, 75],
#     [90, 65, 88]
# ])
# print(np.any(marks > 80, axis =0))
# print(np.all(marks > 50 , axis=0))

# (3): A teacher has the following marks. Find:
# The unique marks
# import numpy as np
# marks = np.array([50, 60, 70, 60, 80, 70, 60, 90, 50])
# res = np.unique(marks)
# print(res)


# SORTING NUMPY ARRAY ..............
#(1) : Given an array of numbers, sort it in ascending order and then display it in descending order.

# import numpy as np
# arr = np.array([45, 12, 78, 34, 23, 89, 10])
# asc = np.sort(arr)
# print("Array In Ascending Order : ", asc)
# print()
# des = np.sort(arr) [::-1]
# print("Array In Descending Order : ",des)

#(2): Given a 2D array, sort its elements separately along rows and columns.

# import numpy as np
# arr = np.array([
#     [30, 10, 20],
#     [60, 40, 50],
#     [90, 70, 80]
# ])
# print(arr)
# print()
# row_wise = np.sort(arr, axis =1 )
# print("Sorting Through Row Wise : ", row_wise)
# print()
# col_wise = np.sort(arr, axis = 0)
# print("Sorting Through Column Wise : ", col_wise)

#(3):Given student marks, sort them and display the top 3 highest marks.

# import numpy as np
# marks = np.array([67, 89, 45, 92, 76, 81, 55, 95])
# sorted = np.sort(marks)
# print("Sorted Marks : ", sorted)
# top = sorted[-3:][::-1]
# print("Highest 3 Marks : ", top)

#(4) : Given an array containing duplicate values, sort the array and display only the unique sorted values.

# import numpy as np
# arr = np.array([40, 20, 10, 40, 30, 20, 50, 10])
# print(arr)
# sort = np.sort(arr)
# print("Sorted Array : ", sort)
# print()
# unique =np.unique(sort)
# print("Unique Element sorted Array : ", unique)
#(5):
# import numpy as np
# employees = np.array([
#     [101, 25, 50000],
#     [102, 30, 35000],
#     [103, 28, 70000],
#     [104, 24, 45000],
#     [105, 32, 60000]
# ])
# sorted_employees = employees[employees[:, 2].argsort()]
# print("Employees sorted by salary:")
# print(sorted_employees)
# ..... ALL ABOUT TRANSPOSING OF ARRAY

# (1) :import numpy as np    # Array Trasnposing ............
# employees = np.array([
#     [101, 25, 50000],
#     [102, 30, 35000],
#     [103, 28, 70000],
#     [104, 24, 45000],
#     [105, 32, 60000]
# ])
# x=np.transpose(employees)
# print(x)
#(2)Create a 2D array representing a matrix and find its transpose.
# import numpy as np
# arr = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])
# tra = np.transpose(arr)
# print( tra)

#(3):Given a matrix, transpose it and calculate the sum of each row of the transposed matrix.

# import numpy as np
# arr = np.array([
#     [10, 20, 30],
#     [40, 50, 60]
# ])
# tr = np.transpose(arr)
# print(tr)
# sum = np.sum(tr,axis=1)
# print(sum)

#(4)Given a matrix, find its transpose and calculate A × Aᵀ.

# import numpy as np
# A = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])
# tr = np.transpose(A)
# print(tr)
# cal = np.dot(A, tr)
# print(cal)
