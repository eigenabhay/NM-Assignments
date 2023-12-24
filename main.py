#!/usr/bin/env python
# coding: utf-8

# In[8]:


# main.py
from fibonacci import generate_fibonacci
import timeit

if __name__ == "__main__":
    # Print the first 10 Fibonacci numbers using a lambda function
    print("First 10 Fibonacci numbers:", list(map(lambda x, a=0, b=1: a + b if (a:=b) or (b:=x) else x, range(10))))

    # Use the module to print the first 100 Fibonacci numbers
    fib_100 = generate_fibonacci(100)
    print("First 100 Fibonacci numbers:", fib_100)

    # Measure the time it takes to generate 100 Fibonacci numbers
    time_taken = timeit.timeit("generate_fibonacci(100)", globals=globals(), setup="from fibonacci import generate_fibonacci", number=1000)
    print(f"Time taken to generate 100 Fibonacci numbers: {time_taken:.6f} seconds")


# In[ ]:




