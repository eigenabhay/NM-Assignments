#!/usr/bin/env python
# coding: utf-8

# In[2]:


for divisor in range(6):
    try:
        result = 1 / divisor
        print(f"1 / {divisor} = {result}")
    except ZeroDivisionError:
        print(f"1 / {divisor} = indeterminate")


# In[ ]:




