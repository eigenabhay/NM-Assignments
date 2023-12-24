#!/usr/bin/env python
# coding: utf-8

# In[9]:


# String
S = 'mumbai'

# Using a for loop to print each character and its Unicode code point
print("1. Printing each character and its Unicode code point:")
for char in S:
    unicode_point = ord(char)
    print(f"Character: {char}, Unicode Code Point: {unicode_point}")

# Using a for loop to compute the sum of Unicode code points
unicode_sum = 0
for char in S:
    unicode_sum += ord(char)
print("\n2. Sum of Unicode code points:", unicode_sum)

# Using list methods to create a list of Unicode code points
unicode_list_method = list(map(ord, S))
print("\n3. List of Unicode code points using list methods:", unicode_list_method)

# Using list comprehension to create a list of Unicode code points
unicode_list_comprehension = [ord(char) for char in S]
print("\n4. List of Unicode code points using list comprehension:", unicode_list_comprehension)

# Using the map class to create a list of Unicode code points
unicode_map = list(map(ord, S))
print("\n5. List of Unicode code points using map class:", unicode_map)


# In[ ]:




