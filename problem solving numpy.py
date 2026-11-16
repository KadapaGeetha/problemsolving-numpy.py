import numpy as np
n = np.array(10)
print(n)
print("dimensions:", n.ndim)
print("shape:", n.shape)
print("size:", n.size)

#
b = np.array([10, 20, 30, 40])

print(b)
print("Dimensions:", b.ndim)
print("Shape:", b.shape)
print("Size:", b.size)



c = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(c)
print("Dimensions:", c.ndim)
print("Shape:", c.shape)
print("Size:", c.size)


d = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])

print(d)
print("Dimensions:", d.ndim)
print("Shape:", d.shape)
print("Size:", d.size)

#Generate numbers from 1 to 100 with a step of 5.
n=np.arange(1,101,5)
print(n)
#: Generate 10 equally spaced numbers between 1 and 50.
n=np.linspace(1,50,10)
print(n)

#Create a 3×3 zero matrix.
n=np.zeros((3,3))
print(n)
#Create a 4×4 ones matrix.
n=np.ones((4,4))
print(n)

#Create a 2×3 matrix filled with 100.
n=np.full((2,3),100)
print(n)
#generate random intergers 
import numpy as np

a = np.random.randint(1, 101, size=20)

print("Random Array:", a)
print("Maximum:", np.max(a))
print("Minimum:", np.min(a))
print("Average:", np.mean(a))
print("Sum:", np.sum(a))



#Generate 5 logarithmically spaced values between \(10^1\) and \(10^5\).

a = np.logspace(1, 5, 5)

print(a)

#import numpy as np
#type conversion

a = np.array([10.5, 20.8, 30.9, 40.2])

integer = a.astype(int)
float_32 = a.astype(np.float32)
float_64 = a.astype(np.float64)

print("Original:", a, a.dtype)
print("Integer:", integer, integer.dtype)
print("Float32:", float_32, float_32.dtype)
print("Float64:", float_64, float_64.dtype)

#: Create a 5×5 array using np.arange() and find:
import numpy as np

a = np.arange(1, 26).reshape(5, 5)

print("Array:\n", a)
print("Shape:", a.shape)
print("Size:", a.size)
print("Dimensions:", a.ndim)
print("Data Type:", a.dtype)
print("Item Size:", a.itemsize)

#Create an array of 100 elements using int64 and calculate its total memory usage.
import numpy as np

a = np.arange(1, 101, dtype=np.int64)

memory = a.size * a.itemsize

print("Size:", a.size)
print("Data Type:", a.dtype)
print("Item Size:", a.itemsize)
print("Total Memory:", memory, "bytes")
print("Memory in KB:", memory / 1024)

#10 – 2D Array Indexing.
import numpy as np

a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("10:", a[0, 0])
print("50:", a[1, 1])
print("90:", a[2, 2])
print("30:", a[0, 2])
print("70:", a[2, 0])

#Create an array from 1 to 20 and extract:
#1. First 5 elements.
#2. Last 5 elements.
#3. Every second element.
#4. Reverse the array.
import numpy as np

a = np.arange(1, 21)

print("First 5:", a[:5])
print("Last 5:", a[-5:])
print("Every second:", a[::2])
print("Reverse:", a[::-1])


#Create a 5×5 matrix using np.arange(1, 26) and extract:
import numpy as np

a = np.arange(1, 26).reshape(5, 5)

result = a[1:4, 1:4]

print("Original Matrix:")
print(a)

print("Extracted Matrix:")
print(result)

#Create a 3D array with shape (2, 3, 4) and extract:
import numpy as np

a = np.arange(1, 25).reshape(2, 3, 4)

print("Original Array:")
print(a)

print("First Matrix:")
print(a[0])

print("Second Matrix:")
print(a[1])

print("Last Two Columns:")
print(a[:, :, -2:])

#Extract elements at indexes 1, 3, 5 and 7 using fancy indexing.
import numpy as np

a = np.array([10, 20, 30, 40, 50, 60, 70, 80])

result = a[[1, 3, 5, 7]]

print("Selected Elements:", result)

#Generate 20 random integers between 1 and 100 and extract:
import numpy as np

a = np.random.randint(1, 101, size=20)

print("Original Array:", a)

print("Above 50:", a[a > 50])

print("Below 25:", a[a < 25])

print("Between 30 and 70:",
      a[(a >= 30) & (a <= 70)])

#Analyse student marks using NumPy.
import numpy as np

marks = np.array([45, 78, 90, 32, 88, 56, 95, 25, 67, 85])

print("Marks above 60:", marks[marks > 60])

print("Failed marks:", marks[marks < 35])

passed = marks >= 35
print("Passed students:", np.sum(passed))

marks[marks < 35] = 0
print("Updated marks:", marks)

print("Average marks:", np.mean(marks))

#Create a 3×3 matrix and use np.nditer() to:
import numpy as np

a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

total = 0
count = 0

print("Every element:")
for i in np.nditer(a):
    print(i)

    total += i

    if i % 2 == 0:
        count += 1

print("Sum:", total)
print("Even numbers:", count)

print("Values greater than 50:")
for i in np.nditer(a):
    if i > 50:
        print(i)

#Create a 3×3 matrix and use np.ndenumerate() to:
import numpy as np

a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Elements with indexes:")

for index, value in np.ndenumerate(a):
    print(index, value)

print("Diagonal elements:")

for index, value in np.ndenumerate(a):
    if index[0] == index[1]:
        print(value)

#A company wants to analyse its daily sales data and identify its sales performance.
import numpy as np

sales = np.array([1000, 2500, 500, 4000, 1500, 5000, 3000, 800])

print("Total Sales:", np.sum(sales))
print("Highest Sales:", np.max(sales))
print("Lowest Sales:", np.min(sales))

print("Sales above 2000:", sales[sales > 2000])

sales[sales < 1000] = 1000
print("Updated Sales:", sales)

print("Average Sales:", np.mean(sales))

#A company wants to analyse employee salaries and calculate a 10% salary increment.
import numpy as np

salary = np.array([25000, 35000, 45000, 20000,
                   60000, 55000, 30000, 75000])

print("Highest Salary:", np.max(salary))
print("Lowest Salary:", np.min(salary))

print("Salaries above 40000:", salary[salary > 40000])

updated_salary = salary + (salary * 0.10)
print("Updated Salaries:", updated_salary)

count = np.sum(salary > 50000)
print("Employees earning above 50000:", count)

print("Average Salary:", np.mean(salary))