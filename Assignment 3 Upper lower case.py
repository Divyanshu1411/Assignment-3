#!/usr/bin/env python
# coding: utf-8

# In[2]:


def count_upper_lower(string1):
    upper_count = 0
    lower_count = 0
    for char in string1:
        if char.isupper():
            upper_count +=1
        elif char.islower():
            lower_count +=1
    print("Upper Case Count is %d Lower Case Count is %d"%(upper_count, lower_count))    
    
    
    
temp=("The quick Brown Fox ")
count_upper_lower(temp)
        


# In[ ]:




