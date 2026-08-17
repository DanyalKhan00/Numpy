# Creation Of Array ...........

# import numpy as np
# x = np.array([1,2,3,4,1,2,3,4])
# print(x)


# Creation of N number array ...
# import numpy as np
# l = []
# n = int(input("Enter No Of array Element : "))
# for i in range(n):
#     num = int(input("Enter Array Element : "))
#     l.append(num)
# print(np.array(l))

# ndim Function

# for 1D ARRAY......
# import numpy as np
# x = np.array([1,2,3,4])
# print(x.ndim)
           # ==> OUTPUT : 1

#  for 2D ARRAY......
# import numpy as np
# x = np.array([[1,2,3,4],[5,6,7,8]])
# print(x)
# print(x.ndim)
          # ==> OUTPUT : 2


#  for 3D ARRAY......
# import numpy as np
# x = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
# print(x)
# print(x.ndim)
          # ==> OUTPUT : 3

# N dimension Array .....
# import numpy as np
# x = np.array([1,2,3,4],ndmin= 6)
# print(x)
# print(x.ndim)

# NUMPY ARRAY FUNCTION .......

#(a) zeros Function ......
#(1)
# import numpy as np
# x = np.zeros(5)
# print(x)

#(2)
# import numpy as np
# x = np.zeros((2,3))
# print(x)


#(b) eye Function ......

#(1)
# import numpy as np
# x = np.eye(5)
# print(x)

#(2)
# import numpy as np
# x = np.eye(4,5)
# print(x)

#c)diag Function ......
# import numpy as np
# arr = np.diag([1,3,5,7,9])
# print(arr)


#(d): randint:
# import numpy as np
# arr = np.random.randint(1,10,4)
# print(arr)

#(e): random.....
# import numpy as np
# arr = np.random.rand(5)
# print(arr)


#(f: randn....
# import numpy as np
# arr = np.random.randn(5)
# print(arr)

#(g:range.
# import numpy as np
# arr = np.arange(5)
# print(arr)
