#!/usr/bin/env python
# coding: utf-8

# In[6]:


# fibonacci.py

def generate_fibonacci(n):
    fib_list = [0, 1]
    while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list


# In[ ]:




