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

noise_magnitude = 0.1 * np.mean(data)

noise = np.random.normal(0, noise_magnitude, data.shape)

noisy_data = data + noise_magnitude * noise

print ("Original_data:", data)
print("Noisy-data:", noisy_data)

negative_noise_mask = data > noisy_data
negative_data = data[negative_noise_mask]
neg_magnitude = np.linalg.norm(negative_data, ord=2)

print ("Negative-noise-condition:", negative_noise_mask)
print ("Data-with-negative-noise:", negative_data)
print ("Magnitude-of-negative-noise: -{neg_magnitude}")

# Use weightst to get a weighted sum of single input of data
weights_transposed = weights.T
output = np.dot(weights_transposed, data)

print ("Data-shape:", data.shape)
print ("Transposed-weights- shape:", weights_transposed.shape)
print ("Output-shape:", output.shape)

# Expand dimension
data = data.reshape(data.shape[0], 1)
output = np.dot(weights_transposed, data)

print ("New-Data-shape:", data.shape)
print ("Output-shape:", output.shape)

# Batch Operation
data = np.random.rand(data.shape[0], 100)
output = np.dot(weights_transposed, data)

print ("Batch-data-shape:", data.shape)
print ("Batch-output-shape:", output.shape)

# Calculate the covariance matrix on centered data
data_centered = data-np.mean
cov_matrix = np.cov(data - np.mean(data_centered, axis=0, rowvar=False))

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)

# Sort eigenvalues and corresponding eigenvectors
sorted_indices = np.argsort(eigenvalues)[::-1]
sorted_eigenvalues = eigenvalues[sorted_indices]
sorted_eigenvectors = eigenvectors[:, sorted_indices]

# Select the top k eigenvectors (e.g., k=2)
k = 2
top_k_eigenvectros = sorted_eigenvectors[:, :k]

# Transform the original data
principle_components = np.dot(data_centered, top_k_eigenvectros)

print("Principle-components-shape:", principle_components.shape)

#reading and writing arrays to files
np.savetext('array.txt', arr)
arr_loaded = np.loadtext('array.txt')
