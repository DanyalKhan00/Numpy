# (1) : Create a NumPy array containing the numbers from 10 to 50. Print the array 
# find its number of dimensions using ndim.

# import numpy as np
# x = np.arange(10,51)
# print("Array :  ", x)
# print("Dimension : ", x.ndim)

#(2)Create a 3×3 matrix of zeros and a 3×3 matrix of ones. Print both matrices and their dimensions.

# import numpy as np
# zero = np.zeros((3,3))
# print("Array : ", zero)
# print("Dimension : ", zero.ndim)

# one = np.ones((3,3))
# print("Array : ", one)
# print("Dimension : ", one.ndim)

#(3)Create a diagonal matrix using the values [10, 20, 30, 40]. Then check the number of dimensions of the matrix.
# import numpy as np
# x = np.diag([10, 20, 30, 40,50,60])
# print("Diagonal Matrix:",x)
# print("Dimensions:",x.ndim)

#(4)Create a 5×5 identity matrix using NumPy. Print the matrix and find its dimensions.
# import numpy as np
# x = np.eye(5,5)
# print("Array : ", x)
# print("Dimension : ", x.ndim)


#(5)Generate a 2×3 array of random numbers using randn(). Print the array and its dimensions.

# import numpy as np
# x = np.random.randn(2,3)
# print("Random Array : ", x)
# print("Dimension : ", x.ndim)

# ALL IN ONE FUNCTION ....

# import numpy as np
# y= np.zeros ([4,5])
# x= np.ones ([4,5])
# z= np.eye  (5)
# z1= np.diag  ([1,3,5,7])
# t= np.random.randint(1,100,20)
# s= np.random.rand(4)
# p= np.random.randn(4)
# k= np.arange(20)
# print(x)
# print(x.itemsize)
# print(y)
# print(z)
# print(z1)
# print(t)
# print(s)
# print(p)
# print(k)


# Arithmatic Operation On Numpy Array ...........
#(1) Create two NumPy arrays and calculate their addition ...

# import numpy as np
# arr1 = np.array([1,2,3,4])
# print(arr1)
# arr2 = np.array([5,6,7,8])
# print(arr2)
# res = arr1 + arr2
# print("Addition Array : ", res)

#(2) Create two arrays from the user and perform all arithmatic Operation in One program .... 

# import numpy as np
# size = int(input("Enter size of array : " ))
# arr1 = []
# for i in range(size):
#     num = int(input("Enter Array 1 element : " ))
#     arr1.append(num)
# arr1 = np.array(arr1)
# print("1st Array Element : ", arr1)
# print()
# arr2 = []
# for i in range(size):
#     num = int(input("Enter Array 2 element : " ))
#     arr2.append(num)
# arr2 = np.array(arr2)
# print("2nd Array Element : ", arr2)
# print()
# print( "----- ARITHMATIC OPERATION ON BOTH ARRAY : " )
# print("Addition : ", arr1 + arr2 )
# print("Subtraction : ", arr1 - arr2 )
# print("Multiplication : ", arr1 * arr2 )
# print("Division : ", arr1 / arr2 )
# print("Modulus : ", arr1 % arr2 )
# print("Power : ", arr1 ** arr2 )


#(3) : Create a NumPy array and take array element from user and find the square of each element using arithmetic operation.

# import numpy as np
# arr1 = []
# size = int(input("Enter Size Of Array : "))
# for i in range(size):
#     num = int(input("Enter Array Element : "))
#     arr1.append(num)
# arr1 = np.array(arr1)
# print("Square of Each Element :", arr1**2)

#(4):Create an array of marks and add 10 bonus marks to every student.

# import numpy as np
# marks = []
# size = int(input("Enter Size Of Array: "))
# for i in range(size):
#     num = int(input("Enter Array Element : " ))
#     marks.append(num)
# marks = np.array(marks)
# print("Orignal Array : ",marks)
# print("Bonus Number",marks + 10)

#(5): You have the prices of five products and their quantities. Calculate the total price of each product
# import numpy as np
# price  = np.array([120,349,90,240])
# quantity  = np.array([6,3,9,12])
# total = price  * quantity 
# print("Total Price per item is : ", total)


#(6):you have the salaries of employees. Add a 10% bonus and then subtract 5% tax from the new salary.
# import numpy as np
# salary = np.array([3500, 8900, 6700, 5000])
# print("Original Salary:", salary)
# bonus = salary * 10 / 100
# print("Bonus:", bonus)
# new_salary = salary + bonus
# print("New Salary:", new_salary)
# tax = new_salary * 5 / 100
# print("Total Tax:", tax)
# final_salary = new_salary - tax
# print("Final Salary:", final_salary)

#(7): Take the price and quantity of 5 products from the user. Calculate:
# Total price
# 10% discount
# Final price

# import numpy as np
# size = int(input("Enter price and quantity of product "))
# price = []
# quantity =[]
# for i in range(size):
#     p = int(input("Enter Price : "))
#     price.append(p)
#     q = int(input("Enter Quantity : "))
#     quantity.append(q)
# price = np.array(price)
# quantity = np.array(quantity)
# total  = price * quantity
# print("Total price : " , total)
# discount = total * 10 / 100
# print("Total Discount : " , discount)
# final_price = total - discount
# print("Final Price : " , final_price)
# print("Grand Total:", np.sum(final_price))


