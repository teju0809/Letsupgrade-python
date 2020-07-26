#!/usr/bin/env python
# coding: utf-8

# In[2]:



test_str = "What we think we become; we are python programmer"
test_sub = "we"
print("The original string is : " + test_str) 
print("The substring to find : " + test_sub) 
res = [i for i in range(len(test_str)) if test_str.startswith(test_sub, i)] 
print("The start indices of the substrings are : " + str(res)) 


# In[ ]:




