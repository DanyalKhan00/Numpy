# All About Numpy Arithmatic Function ........

 #All Function Are : min(), max(), argmax(), sqrt(), sin(), cos(), and cumsum().

#(1):Create a NumPy array containing marks of 6 students. Find the lowest and highest marks.
# import numpy as np
# marks = np.array([67,90,87,66,55,34])
# print("Minimum Number : ", np.min(marks))
# print("Maximum Number : ", np.max(marks))

 #(2)Create an array of marks. Find the index of the student who obtained the highest marks.
# import numpy as np
# marks = np.array([23,56,43,78,99,76])
# print("maximum Number : ",np.max(marks) ,"Maximum Number Index : ", np.argmax(marks))

#(3): Create an array of employee salaries. Display the minimum salary, maximum salary, a
# nd the position of the employee with the highest salary.

# import numpy as np
# salary = np.array([12000,34500,45000,67000,1000])
# print("Minimum Salary : ", np.min(salary))
# print("Maximum Salary : ", np.max(salary))
# print("Maxmimum Salary Index : ", np.argmax(salary))

#(4): Create a NumPy array containing [16, 25, 36, 49, 64] and calculate the square root of every element.
# import numpy as np
# arr = np.array([16, 25, 36, 49, 64])
# print("Square Root : ", np.sqrt(arr))

#(5): A shop makes the following daily sales:
# 1000, 1500, 2000, 1200, 1800
# Use NumPy to calculate the cumulative sales after each day.

# import numpy as np
# sales = np.array([1000, 1500, 2000, 1200, 1800])
# print("Cumulative Sales : ",np.cumsum(sales))

#(6):Take an angle in degrees from the user and calculate its sine using NumPy.
# import numpy as np
# degree = float(input("Enter Degree : "))
# print("You have Enter Degree : ", degree)
# print()
# radian = np.deg2rad(degree)
# result = np.sin(radian)
# print("sin : " , result)

#(7):#(6):Take an angle in degrees from the user and calculate its cos using NumPy.
# import numpy as np
# degree = int(input("Enter Degree :  "))
# radian = np.deg2rad(degree)
# result = np.cos(radian)
# print("Degree In Cos : ", result)

# import numpy as np

# marks = np.array([64, 81, 49, 100, 72])
# print("Maximum : " , np.max(marks))
# print("Minimum : " , np.min(marks))
# print("Square Root : " , np.sqrt(marks))
# print("Cumsum : " , np.cumsum(marks))
# print("Index Of Highest Marks : " , np.argmax(marks))

