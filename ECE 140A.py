#!/usr/bin/env python
# coding: utf-8

# In[48]:


list_1=[1,2,3,4,5,6,7,8,9]


# In[49]:


list_2=[11.0,12.0,13.0,14.0,15.0,16.0,17.0,18.0,19.0,20.0]


# In[50]:


list_1[0]="one";
list_1[1]="two";
list_1[2]="three";
print(list_1)


# In[51]:


list_2[0]="eleven";
list_2[1]="twelve";
list_2[2]="thirteen";
print(list_2)


# In[52]:


list_1.extend(list_2);
joint_1=list_1;
print(joint_1);


# In[53]:


joint_2=list_1+list_2;
print(joint_2)


# In[54]:


def list_shift(base_list, new_data):
    joint_2=base_list+new_data
    return joint_2[(len(joint_2)-len(base_list)):len(joint_2)]


# In[55]:


base_list = [1,2,3,4]
new_data = [5,6,7]
list_shift(base_list, new_data)


# In[56]:


list_3=["STOP","LISTEN","SLEEP","GO"];


# In[57]:


for char in list_3:
    print(char)


# In[58]:


list_4=["CONNECTION FAILURE", "BANANAS", "CONNECTION SUCCESS", "APPLES"];


# In[59]:


text="SUCCESS";


# In[60]:


list_5=["SUCCESS","ijoisafjoijiojSUCCESS","ijoisafjoijiojSUCCESS",text];
if "SUCCESS" in list_5[0]:
    print("SUCCESS in SUCCESS")
else: 
    print("error");
        
if "SUCCESS" in list_5[1]:
    print("SUCCESS in ijoisafjoijiojSUCCESS")
else:
    print("error");
if "SUCCESS" == list_5[2]:
    print("SUCCESS == ijoisafjoijiojSUCCESS")
else:
    print("error");
if "SUCCESS" == list_5[3]:
    print("SUCCESS == text");
else: 
    print("error");


# In[61]:


while 1:
    if text in list_4[0]:
        print("This worked!")
        break;
    else:
        print(list_4[0]);
        pass;
    if text in list_4[1]:
        print("This worked!")
        break;
    else:
        print(list_4[1]);
        pass;
    if text in list_4[2]:
        print("This worked!")
        break;
    else:
        print(list_4[2]);
        pass;
    if text in list_4[3]:
        print("This worked!")
        break;
    else:
        print(list_4[3]);
        pass;


# In[62]:


name="Frank"


# In[63]:


byte_name = name.encode('utf-8')


# In[64]:


byte_name_bad = byte_name + b'\xef'


# In[65]:


byte_name_bad.decode()


# In[ ]:


def test_name(byte1):
  try:
      assert (isinstance(byte1, bytes)), "Inputs must be bytes!"
      print("Input is confirmed to be bytes")
      return byte1
  except AssertionError: 
      print("Attempting to cast to byte")
  try:
      byte1=bytes(byte1)
      return byte1
  except UnicodeDecodeError:
      print("Could not cast to bytes, inputs are not bytes")
      return ""


# In[ ]:





# In[ ]:


a=int(input("Enter a number of seconds:"))
for number in range(a,-1,-1):
    from time import sleep  # import just the sleep module from the time library
    sleep(1)
    print(number)


# In[ ]:


from time import sleep  # import just the sleep module from the time library
sleep(1)


# In[ ]:


import time
time.sleep(1)


# In[ ]:




