
# coding: utf-8

# # Python Tutorial

# ## Data Structure

# ### List Data Strutures
# 
# Python knows a number of compound data types, used to group together other values. The most versatile is the list, which can be written as a list of comma-separated values (items) between square brackets. Lists might contain items of different types, but usually the items all have the same type.
# 
# List is mutable means we can change the value.

# #### How to define list

# In[1]:


list = [2, 5, 10, 25, 30]
list
print(list)


# #### Find length of list

# In[20]:


len(list)


# #### Indexing in list

# In[3]:


list[2]


# In[4]:


list[-3]


# In[5]:


list[:]


# In[6]:


list[2:]


# In[7]:


list[-2:]


# In[8]:


list[-3:-1]


# In[9]:


list[:]


# #### List Concatenation

# In[10]:


list + ['a', 100, 'b', 50, 78]


# In[11]:


cubes = [1, 8, 27, 65, 125]
cubes[3] = 4**3
cubes


# #### Append value in list

# In[12]:


cubes.append(7**3)
cubes


# #### Remove from list

# In[14]:


cubes.remove(cubes[5])
cubes


# In[15]:


cubes[3:4] = []
cubes


# #### Create list containg other list

# In[16]:


numList = [1, 5, 7]
alphaList = ['a', 'b', 'c']

combinedList = [numList, alphaList]
combinedList


# In[17]:


combinedList[0]


# In[18]:


combinedList[1]


# In[19]:


combinedList[0][2]

