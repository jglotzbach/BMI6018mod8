#numpy assignment
#Jason Glotzbach

#Question 1:
import numpy as np
print("Question 1:")
print(np.version)

#Question 2:
arr_ques2 = np.array([0,1,2,3,4,5,6,7,8,9])
print("Question 2:")
print(arr_ques2)

#Question 3:
data = np.genfromtxt("iris.data.txt", dtype=str, encoding=None, delimiter=",") 
print("Question 3:")
print(data)

#Question 4:
print("Question 4:")
iris_array = np.array(data)
column4 = iris_array[:, 3]
for index, value in np.ndenumerate(column4):
    v = float(value)
    if v > 1.0:
        print("the position of the first occurence of petalwidth > 1.0 is at index",index, "and the value is ",v)
        break
    
#Question 5:
print("Question 5:")
np.random.seed(100)
a = np.random.uniform(1,50, 20)
a = np.where(a > 30, 30, a)
a = np.where(a < 10, 10, a)
a