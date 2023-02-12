#!/usr/bin/env python
# coding: utf-8

# ## Programming Assignment_3
# ----------------

# ### 1. Write a Python Program to Check if a Number is Positive, Negative or Zero?

# In[7]:


a=float(input("Enter The number"))
if a==0:
    print("Number is zero")
elif a > 0:
          print("Number is positie")
elif a < 0:
    print("Number is Negative")


# ### 2. Write a Python Program to Check if a Number is Odd or Even?
# 

# In[12]:


num=int(input("Enter Number"))
if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is odd")


# ### 3. Write a Python Program to Check Leap Year?
# 

# In[29]:


year=int(input("Enter the year"))

if year % 400 == 0 and year % 100 == 0:
    print(year,"is a leap year")
elif year % 4 ==0 and year % 100 != 0:
    print(year,"is leap year")
else:
    print(year,"is not leap year")


# ### 4. Write a Python Program to Check Prime Number?

# In[30]:


num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is not a prime number")
else:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")


# ### 5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

# In[32]:


prime_numbers = []
for num in range(1, 10001):
    if num <= 1:
        continue
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        prime_numbers.append(num)

print(prime_numbers)



# In[ ]:




