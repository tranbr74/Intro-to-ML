import numpy as np 
data = np.array ([1, 2, 3, 4, 5])
weights = np.random.rand(5,1)

print (data.shape)
print (data.dtype)

print (weights.shape)
print (weights.dtype)

print (weights.T)
print (weights [0])   # 1st inded
print (weights [1])   # 2nd index
print (weights [1:3]) # 2nd and 3rd index
print (weights [-1])  # Last index

def weight_summary(weight_array):
    for i in range (len(weight_array)):
        print("Weight-Index-", i, ";", weight_array[i])

weight_summary(weights)


        