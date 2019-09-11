#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Dependencies
import pandas as pd


# In[2]:


temp = int
profit = []
change = []


# In[3]:


# Create reference to CSV file
pybank_csv = "Resources/budget_data.csv"
# Import the CSV into a pandas DataFrame
pybank_df = pd.read_csv(pybank_csv)


# In[4]:


file = open('pybank_output.txt', 'a')


# In[5]:


print('Financial Analysis')


# In[6]:


file = open('pybank_output.txt', 'a')
file.write('Financial Analysis'+'\n')
file.close()


# In[7]:


print('****************************')


# In[8]:


file = open('pybank_output.txt', 'a')
file.write('****************************'+'\n')
file.close()


# In[9]:


# Finding the total number of months
duration = pybank_df["Date"].count()
print(f"The total number of months in the dataset is {duration}.")


# In[10]:


file = open('pybank_output.txt', 'a')
file.write(f'The total number of months in the dataset is {duration}.'+'\n')
file.close()


# In[11]:


# Finding the Total Profit
total_profit = pybank_df["Profit/Losses"].sum()
print(f"The total profit for these months is ${total_profit}")


# In[12]:


file = open('pybank_output.txt', 'a')
file.write(f"The total profit for these months is ${total_profit}"+'\n')
file.close()


# In[13]:


# making new DataFrame to keep original data intact
change_df = pybank_df[["Date", "Profit/Losses"]]


# In[14]:


# making a list for manipulation and calculation
profit = change_df["Profit/Losses"]


# In[15]:


# Looping to make new list with monthly changes
for k,v in profit.items():
    temp = change_df.iloc[k,1] - change_df.iloc[k - 1,1]
    change.append(temp)
#Remove unwanted values from list
change.pop(0)
print('')


# In[16]:


# Finding Average monthly change
average_change = sum(change) / len(change)
print(f"Average Change: ${average_change}")


# In[17]:


file = open('pybank_output.txt', 'a')
file.write(f"Average Change: ${average_change}"+'\n')
file.close()


# In[18]:


# Finding greatest increase in profits
max_value = max(change)
max_index = change.index(max_value)
print(f"Greatest Increase in Profits: {change_df.iloc[max_index+1,0]} (${max_value})")


# In[19]:


file = open('pybank_output.txt', 'a')
file.write(f"Greatest Increase in Profits: {change_df.iloc[max_index+1,0]} (${max_value})"+'\n')
file.close()


# In[20]:


# Finding greatest decrease in profits
min_value = min(change)
min_index = change.index(min_value)
print(f"Greatest Decrease in Profits: {change_df.iloc[min_index+1,0]} (${min_value})")


# In[21]:


file = open('pybank_output.txt', 'a')
file.write(f"Greatest Decrease in Profits: {change_df.iloc[min_index+1,0]} (${min_value})"+'\n')
file.close()

