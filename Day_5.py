# All about Boolean indexing and Fancy Indexing .......

#(1): Given the marks array, print students who scored 80 or more.
# import numpy as np
# marks = np.array([56,78,89,90,98,110])
# print("Marks Greater than 60 : ",marks[marks > 60])

#(2):From the array, print numbers that are greater than 30 AND less than 80.
# import numpy as np
# number = np.array([10, 25, 35, 50, 65,78, 76,8,11,10, 80, 95])
# print("Number > 30 AND < 80 : ", number[(number > 30) & (number < 80)])
# print("Boolean Mask : ", [(number > 30) & (number < 80)])

#(3): Given student marks, replace every mark below 50 with 0.
# import numpy as np
# marks = np.array([45, 78, 32, 90, 55, 28, 67,43,28,35,30])
# marks[marks < 50]=0
# print(marks)

#(4):  Given a 2-D matrix, print all elements that are greater than 50.
# import numpy as np
# matrix = np.array([
#     [25, 60, 45],
#     [75, 30, 90],
#     [55, 20, 80]
# ])
# r=matrix[matrix > 50]
# print(r)

#(5): Given an array of temperatures, find:Temperatures above 30 Temperatures below 15 Temperatures between 15 and 30
# import numpy as np
# temp = np.array([12, 18, 25, 32, 35, 10, 28, 40, 22])
# print(temp)
# hot = temp > 30
# print("HOT : ", temp[hot])
# cold = temp < 15
# print("COLD : ", temp[cold])
# warm = (temp > 15) & (temp < 30)
# print("WARM : ", temp[warm])

#(6): Given an array, print numbers that are even AND greater than 20.
# import numpy as np
# arr = np.array([10, 15, 22, 27, 34, 41, 48, 55])
# even = arr[(arr % 2 == 0)& (arr > 20)]
# print("Filtered Even # : ", even)

#(7):  Given employee salaries, increase salaries below 50,000 by 5,000.
# import numpy as np
# salary = np.array([45000, 60000, 38000, 75000, 42000, 90000])
# print(salary)
# salary[salary < 50000]+= 500
# print("New _ salary : ", salary )

#(8): Print all numbers that are outside the range 20–60.
# import numpy as np
# arr = np.array([10, 25, 35, 65, 45, 75, 55, 15])
# res = arr[(arr < 20)| (arr > 60)]
# print(res)


# All About Fancy Indexing .....\
# (1) : Given a 3×4 array, use fancy indexing to select the elements at (row 0, col 1), (row 1, col 3), and (row 2, col 0).

# import numpy as np
# arr = np.array([
#     [10, 20, 30, 40],
#     [50, 60, 70, 80],
#     [90, 100, 110, 120]
# ])
# row = [0,1,2]
# col = [1,3,0]
# res=arr[row,col]
# print("Result : ", res)

#(2)Increase the marks of students at index 1, 3, and 4 by 5.
# import numpy as np
# marks = np.array([45, 60, 72, 55, 80, 40])
# ind = [1,3,4]
# marks[ind] +=5
# print("Updated marks : ", marks)

#(3):Select rows 0, 2, and 3 from the following array using fancy indexing.
# import numpy as np
# arr = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90],
#     [100, 110, 120]
# ])
# idx = [0,2,3]
# re = arr[idx]
# print(re)

#(4):From a 3×4 array, select columns 0 and 2.

# import numpy as np
# arr = np.array([
#     [10, 20, 30, 40],
#     [50, 60, 70, 80],
#     [90, 100, 110, 120]
# ])
# idx= [0,2]
# res = arr[:, idx]
# print(res)

#(5): Change the values at (0,1), (1,2), and (2,3) to 99.
# import numpy as np
# arr = np.array([
#     [10, 20, 30, 40],
#     [50, 60, 70, 80],
#     [90, 100, 110, 120]
# ])
# row = [0,1,2]
# col = [1,2,3]
# arr [row , col ] =99
# print("Updated Array :", arr)

#(6) : A company's employee salaries are stored in an array. Increase the salaries of employees at indices 0, 2, and 4 by 10%.

# import numpy as np
# salary = np.array([40000, 50000, 60000, 45000, 70000])

# idx = [0,2,4]
# salary[idx]=salary[idx] * 1.10
# print(salary)

import numpy as np
x= np.array([2,4,6,8])
y = np.array([6,3,4,2])

b= np.power(x,y)
print(b)