#!/usr/bin/env python
# coding: utf-8

# Q1. What are the benefits of the built-in array package, if any?
# 

# the built-in array package is simple, efficient, memory-friendly, compatible, and integrated with programming languages.

# Q2. What are some of the array package's limitations?
# 

#  arrays have limitations related to size flexibility, inefficient modifications, memory usage, data type constraints, complex element manipulation, limited functionality, and lack of bounds checking.

# Q3. Describe the main differences between the array and numpy packages.
# 

# numpy provides advanced functionality, optimized performance, supports multidimensional arrays, has better integration, and a larger ecosystem compared to the basic array package.

# Q4. Explain the distinctions between the empty, ones, and zeros functions.
# 

# empty: Creates an array without initializing its elements.
# ones: Creates an array with all elements set to 1.
# zeros: Creates an array with all elements set to 0.

# Q5. In the fromfunction function, which is used to construct new arrays, what is the role of the callable argument?
# 

# he callable argument in the fromfunction function defines the rule or formula for generating values for each element of the new array based on the indices.

# Q6. What happens when a numpy array is combined with a single-value operand (a scalar, such as an int or a floating-point value) through addition, as in the expression A + n?
# 

# A numpy array is combined with a scalar through addition, the scalar value is broadcasted to match the shape of the array, and element-wise addition is performed between the array and the scalar value.

# Q7. Can array-to-scalar operations use combined operation-assign operators (such as += or *=)? What is the outcome?
# 

# combined operation-assign operators cannot be directly used for array-to-scalar operations in numpy. Separate steps are required to perform the operation and assign the result back to the array.

# Q8. Does a numpy array contain fixed-length strings? What happens if you allocate a longer string to one of these arrays?
# 

# a numpy array can contain fixed-length strings defined using the numpy.string_ data type. If you assign a longer string to an element of a fixed-length string array, the longer string will be truncated to fit the specified length, and any excess characters will be discarded.

# Q9. What happens when you combine two numpy arrays using an operation like addition (+) or multiplication (*)? What are the conditions for combining two numpy arrays?
# 

# In[10]:


#example:

import numpy as np
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
c = a + b
print(c)


# In[11]:


d = a * b


# In[12]:


print(d)


# Q10. What is the best way to use a Boolean array to mask another array?
# 

# #example 
# 
# import numpy as np
# 
# arr = np.array([1,2,3,4,5,6,7,8,9,10])
# 
# mask = np.array ([True, False, True,False,True,False])
# 
# masked_arr = arr[mask]
# 
# #a Boolean array as an indexing mask is the recommended approach for masking another array in numpy. It provides an efficient way to select or manipulate specific elements based on the corresponding Boolean values in the mask.

# Q11. What are three different ways to get the standard deviation of a wide collection of data using both standard Python and its packages? Sort the three of them by how quickly they execute.
# 

# The three different ways to get the standard deviation, sorted by execution speed from fastest to slowest, are:
# 
# Numpy
# Statistics module (Standard Python)
# Manual Calculation (Standard Python)

# 12. What is the dimensionality of a Boolean mask-generated array?
# 

# the dimensionality of a Boolean mask-generated array generally matches the dimensionality of the original array, but the specific shape and structure of the mask and the indexing pattern can affect the resulting dimensionality.

# In[ ]:




