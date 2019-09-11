#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Dependencies
import pandas as pd


# In[2]:


# Create reference to CSV file
pypoll_csv = "Resources/election_data.csv"
# Import the CSV into a pandas DataFrame
pypoll_df = pd.read_csv(pypoll_csv)


# In[3]:


print('Election Results')


# In[4]:


print('****************************')


# In[5]:


# Finding total votes
total_votes = pypoll_df["Candidate"].count()
print("Total Votes: "+f"{total_votes}")


# In[6]:


print('****************************')


# In[7]:


# making new DataFrame to keep original data intact
pypoll_2_df = pypoll_df
#


# In[8]:


# Setting Candidate column as index for use as a key
pypoll_2_df = pypoll_2_df.set_index('Candidate')


# In[9]:


# Create Candidate DataFrames
Khan_df = pypoll_2_df[pypoll_2_df.index == "Khan"]
Correy_df = pypoll_2_df[pypoll_2_df.index == "Correy"]
Li_df = pypoll_2_df[pypoll_2_df.index == "Li"]
O_Tooley_df = pypoll_2_df[pypoll_2_df.index == "O'Tooley"]


# In[10]:


# Find number of votes cast per candidate
khan_count = Khan_df["County"].count()
Correy_count = Correy_df["County"].count()
Li_count = Li_df["County"].count()
O_Tooley_count = O_Tooley_df["County"].count()


# In[11]:


# Find percentage of votes cast per candidate
khan_prct = khan_count / total_votes * 100
correy_prct = Correy_count / total_votes * 100
li_prct = Li_count / total_votes * 100
o_tooley_prct = O_Tooley_count / total_votes * 100


# In[12]:


# Printing results
print(f'Khan: {"%.3f" % khan_prct}% ({khan_count})')
print(f'Correy: {"%.3f" % correy_prct}% ({Correy_count})')
print(f'Li: {"%.3f" % li_prct}% ({Li_count})')
print("O'"+f'Tooley: {"%.3f" % o_tooley_prct}% ({O_Tooley_count})')


# In[13]:


print('****************************')


# In[14]:


#Finding the Winner
if [khan_count > Correy_count & khan_count > Li_count & khan_count > O_Tooley_count]: 
    winner = ('Khan')
    print(f'Winner: {winner}') 
elif [Correy_count > Li_count & Correy_count > O_Tooley_count]:
    winner = ('Correy')
    print(f'Winner: {winner}')
elif [Li_count > O_Tooley_count]:
    winner = ('Li')
    print(f'Winner: {winner}')
else:
    winner = ("O'Tooley")
    print(f"Winner: {winner}")


# In[15]:


print('****************************')


# In[16]:


# Writing output to text
file = open('pypoll_output.txt', 'a')
file.write('Election Results'+'\n')
file.write('****************************'+'\n')
file.write("Total Votes: "+f"{total_votes}"+'\n')
file.write('****************************'+'\n')
file.write(f'Khan: {"%.3f" % khan_prct}% ({khan_count})'+'\n')
file.write(f'Correy: {"%.3f" % correy_prct}% ({Correy_count})'+'\n')
file.write(f'Li: {"%.3f" % li_prct}% ({Li_count})'+'\n')
file.write("O'"+f'Tooley: {"%.3f" % o_tooley_prct}% ({O_Tooley_count})'+'\n')
file.write('****************************'+'\n')
file.write(f'Winner: {winner}'+'\n')
file.write('****************************'+'\n')
file.close()

