
# NumPy Practice – 20 Questions

## About This Repository
This repository contains my hands-on practice of NumPy, a Python library used for numerical computing and data analysis.

I completed 20 practical exercises covering array creation, data types, array properties, indexing, slicing, Boolean masking, iteration, and real-world data analysis.

## Tools & Technologies
- Python
- NumPy
- VS Code

## 1. Array Creation and Dimensions

### Create arrays with different dimensions
```python
import numpy as np

a = np.array(10)
b = np.array([10, 20, 30])
c = np.array([[10, 20], [30, 40]])
d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
```

### Use arange() and linspace()
```python
print(np.arange(1, 11, 2))
print(np.linspace(1, 10, 5))
```

### Create arrays using zeros(), ones() and full()
```python
print(np.zeros((2, 3)))
print(np.ones((2, 3)))
print(np.full((2, 3), 5))
```

### Generate random integers
```python
random_array = np.random.randint(1, 100, size=10)

print(random_array)
print("Maximum:", np.max(random_array))
print("Minimum:", np.min(random_array))
print("Mean:", np.mean(random_array))
print("Sum:", np.sum(random_array))
```

### Use logspace()
```python
print(np.logspace(1, 5, 5))
```

## 2. Data Types and Array Properties

### Convert an array into int, float32 and float64
```python
a = np.array([10.5, 20.8, 30.9, 40.2])

int_array = a.astype(int)
float32_array = a.astype(np.float32)
float64_array = a.astype(np.float64)

print(int_array, int_array.dtype)
print(float32_array, float32_array.dtype)
print(float64_array, float64_array.dtype)
```

Expected dtypes:
```text
int64
float32
float64
```
*Note: The integer dtype can vary by operating system and NumPy environment.*

### Create a 5×5 array and check its properties
```python
a = np.arange(1, 26).reshape(5, 5)

shape = a.shape
size = a.size
dimensions = a.ndim
data_type = a.dtype
item_size = a.itemsize

print("Shape:", shape)
print("Size:", size)
print("Dimensions:", dimensions)
print("Data type:", data_type)
print("Item size:", item_size)
```

### Calculate memory consumption of 100 int64 elements
```python
a = np.arange(100, dtype=np.int64)

memory = a.size * a.itemsize

print("Number of elements:", a.size)
print("Item size:", a.itemsize)
print("Total memory:", memory, "bytes")
```

Expected total memory: **800 bytes** (100 × 8 bytes).

## 3. Indexing and Slicing

### Positive and negative indexing
```python
a = np.arange(10, 101)

print("First element:", a[0])
print("Last element:", a[-1])
print("Third element:", a[2])
print("Second-last element:", a[-2])
```

### 2D array indexing
```python
a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(a[0, 0])  # 10
print(a[1, 1])  # 50
print(a[2, 2])  # 90
print(a[0, 2])  # 30
print(a[2, 0])  # 70
```

### 1D array slicing
```python
a = np.arange(1, 21)

print("First five:", a[:5])
print("Last five:", a[-5:])
print("Every second element:", a[::2])
print("Reversed array:", a[::-1])
```

### 2D array slicing
```python
a = np.arange(1, 26).reshape(5, 5)

sub_matrix = a[1:4, 1:4]

print(sub_matrix)
```

Output:
```text
[[ 7  8  9]
 [12 13 14]
 [17 18 19]]
```

### 3D array creation and slicing
```python
a = np.arange(1, 25).reshape(2, 3, 4)

print("First matrix:")
print(a[0])

print("Second matrix:")
print(a[1])

print("Last two columns from both matrices:")
print(a[:, :, -2:])
```

## 4. Fancy Indexing and Boolean Masking

### Fancy indexing
```python
a = np.array([10, 20, 30, 40, 50, 60, 70, 80])

result = a[[1, 3, 5, 7]]

print(result)
```

Output:
```text
[20 40 60 80]
```

### Boolean masking with random integers
```python
a = np.random.randint(1, 101, size=20)

print("Original array:", a)
print("Values above 50:", a[a > 50])
print("Values below 25:", a[a < 25])
print("Values between 30 and 70:", a[(a >= 30) & (a <= 70)])
```

### Student marks analysis
```python
marks = np.array([45, 78, 90, 32, 88, 56, 95, 25, 67, 85])

print("Above 60:", marks[marks > 60])
print("Failed marks:", marks[marks < 35])
print("Passed count:", np.sum(marks >= 35))

marks[marks < 35] = 0

print("Updated marks:", marks)
print("Average:", np
