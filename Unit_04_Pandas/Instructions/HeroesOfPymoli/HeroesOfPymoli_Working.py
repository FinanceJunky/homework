#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[1]:


#  Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data_pd = pd.read_csv(file_to_load)


# ## Player Count

# * Display the total number of players
# 

# In[2]:


#Finding Number of Unique Players
users = purchase_data_pd['SN'].unique()
total_unique_players = len(users)
#or nuunique
player_summary_table = pd.DataFrame({'Total Players': total_unique_players}, index = [0])
player_summary_table


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[3]:


#Calculate the Variabe values
item_name = purchase_data_pd['Item ID'].unique()
unique_item_count = len(item_name)
total_items_purchased = purchase_data_pd['Purchase ID'].count()
avg_price = purchase_data_pd['Price'].mean()
total_revenue = purchase_data_pd['Price'].sum()
# Create the DataFrame
purchasing_analysis_table = pd.DataFrame({'Number of Unique Items': unique_item_count, 'Average Price': avg_price, 'Number of Purchases': total_items_purchased, 'Total Revenue' : total_revenue}, index = ['0'])
# Use Mapto format
purchasing_analysis_table['Average Price'] = purchasing_analysis_table['Average Price'].map("${:.2f}".format)
purchasing_analysis_table['Total Revenue'] = purchasing_analysis_table['Total Revenue'].map("${:,.2f}".format)
#purchasing_analysis_table = pd.DataFrame(raw_data_info, columns=["Number of Unique Items", "Average Price", "Number of Purchases", "Total Revenue"])
purchasing_analysis_table


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[4]:


# created gender unique DataFrame
gender_unique_df = purchase_data_pd.drop_duplicates('SN', 'first', False)


# In[5]:


# Define list values
gendercounts= gender_unique_df.Gender.value_counts()
gender_perc= gender_unique_df.Gender.value_counts(normalize=True)
# New DataFrame
summary_gdf = pd.DataFrame()
summary_gdf["Total Count"] = gendercounts
summary_gdf["Percentage of Players"] = gender_perc
summary_gdf['Percentage of Players'] = pd.Series(["{0:.2f}%".format(val * 100) for val in summary_gdf['Percentage of Players']], index = summary_gdf.index)
#summary_gdf"Percentage of Players") = summary_gdf["Percentage of Players"]
summary_gdf


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[6]:


# Group dataframe by gender and rename
group_gender = purchase_data_pd.groupby("Gender")


# In[7]:


# setting up list variables
gender_avg_price = group_gender['Price'].mean()
gender_price = group_gender['Price'].sum()
purchase_count = group_gender['SN'].count()
total_purchase_gender = gender_price / gendercounts


# In[8]:


# Create the DataFrame
gender_analysis_table = pd.DataFrame()
# Organize columns
gender_analysis_table["Purchase Count"] = purchase_count
gender_analysis_table["Average Purchase Price"] = gender_avg_price
gender_analysis_table["Total Purchase Value"] = gender_price
gender_analysis_table["Avg Total Purchase per Person"] = total_purchase_gender
# formatting
gender_analysis_table["Average Purchase Price"] = gender_analysis_table["Average Purchase Price"].map("${:.2f}".format)
gender_analysis_table["Total Purchase Value"] = gender_analysis_table["Total Purchase Value"].map("${:,.2f}".format)
gender_analysis_table["Avg Total Purchase per Person"] = gender_analysis_table["Avg Total Purchase per Person"].map("${:,.2f}".format)
gender_analysis_table


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[9]:


# Setting up bins and groupings
bins = [0, 9.9, 14.9, 19.9, 24.9, 29.9, 34.9, 39.9, 200]
groups = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "34-39", "40+"]


# In[10]:


# Binning and grouping
gender_unique_df["Age_Group"] = pd.cut(gender_unique_df.Age, bins, labels=groups)


# In[11]:


# Count by Age prep
age_counts = gender_unique_df.Age_Group.value_counts()


# In[12]:


# Percentage by age prep
age_perc = gender_unique_df.Age_Group.value_counts(normalize=True)


# In[13]:


# New DataFrame
age_table = pd.DataFrame()


# In[14]:


# Setting up Columns
age_table["Total Count"] = age_counts
age_table["Percentage of Players"] = age_perc
# Formatting
age_table['Percentage of Players'] = pd.Series(["{0:.2f}%".format(val * 100) for val in age_table['Percentage of Players']], index = age_table.index)
age_table.sort_index()


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[15]:


# setting up
age_analysis_df = purchase_data_pd
age_analysis_df["Age_Group"] = pd.cut(age_analysis_df.Age, bins, labels=groups)
age_analysis_df = age_analysis_df.groupby("Age_Group")


# In[16]:


# Define variables and lists
ageA_count = age_analysis_df.Price.count()
ageA_price = age_analysis_df.Price.mean()
ageA_purch = age_analysis_df.Price.sum()
age_tot_purch = ageA_purch / age_counts


# In[17]:


# Setting up Table
age_analysis_table = pd.DataFrame()
age_analysis_table['Purchase Count'] = ageA_count
age_analysis_table['Average Purchase Price'] = ageA_price
age_analysis_table['Total Purchase Value'] = ageA_purch
age_analysis_table['Avg Total Purchase per Person'] = age_tot_purch
# Formatting
age_analysis_table["Average Purchase Price"] = age_analysis_table["Average Purchase Price"].map("${:.2f}".format)
age_analysis_table["Total Purchase Value"] = age_analysis_table["Total Purchase Value"].map("${:,.2f}".format)
age_analysis_table["Avg Total Purchase per Person"] = age_analysis_table["Avg Total Purchase per Person"].map("${:.2f}".format)
age_analysis_table


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[18]:


top_spenders_df = purchase_data_pd
top_spenders_df = top_spenders_df.groupby("SN")
#top_spenders_df


# In[19]:


spenderA_count = top_spenders_df.Price.count()
spenderA_price = top_spenders_df.Price.mean()
spenderA_purch = top_spenders_df.Price.sum()


# In[20]:


# Setting up Table
top_spenders_table = pd.DataFrame()
top_spenders_table['Purchase Count'] = spenderA_count
top_spenders_table['Average Purchase Price'] = spenderA_price
top_spenders_table['Total Purchase Value'] = spenderA_purch
# Formatting - Changes occur when formating applied and incorrect result displays
#top_spenders_table["Average Purchase Price"] = top_spenders_table["Average Purchase Price"].map("${:.2f}".format)
#top_spenders_table["Total Purchase Value"] = top_spenders_table["Total Purchase Value"].map("${:,.2f}".format)
top_spenders_table.sort_values(by='Total Purchase Value', ascending=False).head()


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[21]:


# Extract item Data
pop_item_data = purchase_data_pd.loc[:,["Item ID", "Item Name", "Price"]]

# Perform basic calculations
tot_item_purch = pop_item_data.groupby(["Item ID", "Item Name"]).sum()["Price"].rename("Total Purchase Value")
avg_item_purch = pop_item_data.groupby(["Item ID", "Item Name"]).mean()["Price"]
pop_item_count = pop_item_data.groupby(["Item ID", "Item Name"]).count()["Price"].rename("Purchase Count")


# In[22]:


pop_item_table = pd.DataFrame()
pop_item_table["Purchase Count"] = pop_item_count
pop_item_table["Item Price"] = avg_item_purch
pop_item_table["Total Purchase Value"] = tot_item_purch
# formatting - decide not to include formatting due to time constaints - fixing "Most Profitable Items" Section
#pop_item_table["Item Price"] = pop_item_table["Item Price"].map("${:.2f}".format)
#pop_item_table["Total Purchase Value"] = pop_item_table["Total Purchase Value"].map("${:,.2f}".format)
# Sorting
pop_item_table.sort_values(by='Purchase Count', ascending=False).head()


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[23]:


pop_item_table.sort_values(by='Total Purchase Value', ascending=False).head()

