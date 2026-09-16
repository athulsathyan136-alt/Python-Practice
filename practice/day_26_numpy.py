import numpy as np

print("="*50)
print("CREATING ARRAY")
print("="*50)

arr1 = np.array([2,3,6,5,4,7,8])
print(f"Array: {arr1}")
print(f"Array Type: {type(arr1)}")
print(f"Array Shape: {arr1.shape}")
print(f"Array Datatype: {arr1.dtype}")

print("="*50)
print("2D-ARRAY")
print("="*50)

mat = np.array([[1,2,3],[4,5,6]])
print(f"\nMatrix : \n{mat}")
print(f"Matrix shape : {mat.shape}")

print("="*50)
print("SPECIAL-ARRAY")
print("="*50)

print(f"Zero : {np.zeros(6)}")
print(f"Ones : {np.ones(6)}")
print(f"Range : {np.arange(0,11,3)}")
print(f"Linspace : {np.linspace(0.10,2)}")
print(f"Random : {np.random.rand(6)}")


print("="*50)
print("ARRAY OPEARTIONS")
print("="*50)

a = np.array([1,2,3,4])
b = np.array([10,11,12,13])

print(f"a : {a}")
print(f"b : {b}")
print(f"a + b: {a + b}")
print(f"a * b: {a * b}")
print(f"a ** 2 : {a**2}")
print(f"a + 100: {a + 100}")

print("="*50)
print("STATISTICS")
print("="*50)

data =  np.array([1,20,25,44,66,88,99,77,55,44,11,22])

print(f"Data: {data}")
print(f"Sum: {data.sum()}")
print(f"Mean: {data.mean()}")
print(f"Max: {data.max()}")
print(f"Min: {data.min()}")
print(f"std Dev: {data.std():.2f}")

print("="*50)
print("MATRIX MULTIPLICATION")
print("="*50)

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[9,8]])

print(f"\nMatrix X:\n{x}")
print(f"\nMatrix Y:\n{y}")
print(f"\nMatrix A @ B:\n{x @ y}")
print(f"\nMatrix A * B:\n{x * y}")

print("="*50)
print("SIMULATED EMBEDDING")
print("="*50)

emb1 = np.array([0.2,0.5,-0.1,0.8,0.3])
emb2 = np.array([0.3,0.4,-0.2,0.7,0.5])

dot_product  = np.dot(emb1,emb2)
norm1 = np.linalg.norm(emb1)
norm2 = np.linalg.norm(emb2)
similarity = dot_product / (norm1 * norm2)

print(f"Dot Product : {dot_product:.4f}")
print(f"Cosine Similarity : {similarity:.4f}")
