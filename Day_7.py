# Flatten vs Ravel ....
# import numpy as np
# arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
# res = arr.flatten()
# print(res)

# import numpy as np
# arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
# res = arr.ravel()
# print(res)


# import numpy as np
# arr = np.array([10, 20, 30, 40, 50])
# Copy = arr.copy()
# Copy[0] = 100
# print("Original : ", arr)
# print("Copy : ", Copy)
# print(arr)



# import numpy as np
# arr = np.array([10, 20, 30, 40, 50])
# View = arr.view()
# View[2]= 99
# print("Orignal : ",arr)
# print("View : ",View)


# import numpy as np
# arr = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])
# rev = arr.ravel()
# rev[0] = 100
# print("Orignal : ", arr)
# print("Ravel : ", rev)

# print()
# flt = arr.flatten()
# flt[0]=999
# print("Flatten : ",flt)


# import numpy as np
# A = np.array([
#     [1, 2],
#     [3, 4]
# ])
# B = np.array([
#     [5, 6],
#     [7, 8]
# ])
# result = np.stack((A, B), axis=0)
# print("Stacked array:")
# print(result)
# print("Shape:", result.shape)


# import numpy as np
# arr = np.array([[10, 20, 30, 40],
#  [50, 60, 70, 80]])
# res=  np.split(arr,2,axis =1)
# print("Part 1 : ", res[0])
# print("Part 2 : ", res[1])



# import numpy as np
# arr = np.array([
#     [10, 20, 30],
#     [5, 15, 25],
#     [2, 4, 6]
# ])
# for r in arr:
#     sum = 0
#     for value in arr:
#         sum +=value
# print("Total : ", sum)

# import numpy as np
# arr = np.array([
#     [12, 7, 5],
#     [8, 11, 20],
#     [3, 14, 9]
# ])
# odd = 0 
# even = 0
# for i in np.nditer(arr):
#     if i%2==0:
#         even +=1
#     else:
#         odd +=1
# print("Even : ",even)
    
# print("Odd :: ",odd )


# import numpy as np
# arr = np.array([
#     [12, 45, 23, 18],
#     [67, 34, 89, 21],
#     [10, 5, 32, 15]
# ])
# for row in arr:

#     largest = row[0]
#     for value in row:
#         if value > largest:
#             largest = value
#     print("Largest : ", largest)