#!/usr/bin/env python
# coding: utf-8

# In[1]:


#  Pymaceuticals  -  Donald Stegman  -  Unit_05-Matplotlib


# In[2]:


# Dependencies and Setup
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Hide warning messages in notebook
import warnings
warnings.filterwarnings('ignore')

# File to Load (Remember to Change These)
mouse_drug_data_to_load = "data/mouse_drug_data.csv"
clinical_trial_data_to_load = "data/clinicaltrial_data.csv"

# Read the Mouse and Drug Data and the Clinical Trial Data
clinical_trial_df = pd.read_csv(clinical_trial_data_to_load)
mouse_drug_df = pd.read_csv(mouse_drug_data_to_load)

# Combine the data into a single dataset
Pymacueticals_df = pd.merge(clinical_trial_df, mouse_drug_df, on="Mouse ID", how="left")

# Display the data table for preview
Pymacueticals_df.head()


# ## Tumor Response to Treatment

# In[3]:


# Store the Mean Tumor Volume Data Grouped by Drug and Timepoint 
avg_tum_vol = Pymacueticals_df.groupby(['Drug', 'Timepoint'])['Tumor Volume (mm3)'].mean()
# Convert to DataFrame
avg_tum_vol = pd.DataFrame(avg_tum_vol)
avg_tum_vol = avg_tum_vol.reset_index()
# Preview DataFrame
avg_tum_vol.head()


# In[4]:


# Minor Data Munging to Re-Format the Data Frames
avg_tum_vol_table = avg_tum_vol.pivot(index='Timepoint', columns='Drug', values='Tumor Volume (mm3)')
# Preview that Reformatting worked
avg_tum_vol_table.head()


# In[5]:


# Store the Standard Error of Tumor Volumes Grouped by Drug and Timepoint
std_err_tum = Pymacueticals_df.groupby(['Drug', 'Timepoint'])['Tumor Volume (mm3)'].sem()
# Convert to DataFrame
std_err_tum = pd.DataFrame(std_err_tum)
std_err_tum = std_err_tum.reset_index()
# Preview DataFrame
std_err_tum


# In[6]:


# Minor Data Munging to Re-Format the Data Frames
std_err_tum_table = std_err_tum.pivot(index='Timepoint', columns='Drug', values='Tumor Volume (mm3)')
# Preview that Reformatting worked
std_err_tum_table.head()


# In[7]:


# Generate the Plot (with Error Bars)
fig, ax = plt.subplots()

ax.errorbar(std_err_tum_table.index, avg_tum_vol_table['Capomulin'], std_err_tum_table['Capomulin'],
            fmt="o", color='red', label = 'Capomulin', ls='--')
ax.errorbar(std_err_tum_table.index, avg_tum_vol_table['Infubinol'], std_err_tum_table['Infubinol'],
            fmt="^", color='blue', label = 'Infubinol', ls='--')
ax.errorbar(std_err_tum_table.index, avg_tum_vol_table['Ketapril'], std_err_tum_table['Ketapril'],
            fmt="s", color='green', label = 'Ketapril', ls='--')
ax.errorbar(std_err_tum_table.index, avg_tum_vol_table['Placebo'], std_err_tum_table['Placebo'],
            fmt="d", color='black', label = 'Placebo', ls='--')

ax.set_xlim(-1, 47)
ax.set_ylim(30, 75)

ax.set_xlabel("Time (Days)")
ax.set_ylabel("Tumor Volume (mm3)")
ax.set_title("Tumor Response to Treatment")
ax.legend()
plt.grid(axis='y')

# Save the Figure
plt.savefig('Fig1.png')
plt.show()


# ![Tumor Response to Treatment](../Images/treatment.png)

# ## Metastatic Response to Treatment

# In[8]:


# Store the Mean Met. Site Data Grouped by Drug and Timepoint 
met_site_vol = Pymacueticals_df.groupby(['Drug', 'Timepoint'])['Metastatic Sites'].mean()
# Convert to DataFrame
met_site_vol = pd.DataFrame(met_site_vol)
met_site_vol = met_site_vol.reset_index()
# Preview DataFrame
met_site_vol.head()


# In[9]:


# Minor Data Munging to Re-Format the Data Frames
met_site_vol_table = met_site_vol.pivot(index='Timepoint', columns='Drug', values='Metastatic Sites')
# Preview that Reformatting worked
met_site_vol_table.head()


# In[10]:


# Store the Standard Error associated with Met. Sites Grouped by Drug and Timepoint 
std_err_met_site = Pymacueticals_df.groupby(['Drug', 'Timepoint'])['Metastatic Sites'].sem()
# Convert to DataFrame
std_err_met_site = pd.DataFrame(std_err_met_site)
std_err_met_site = std_err_met_site.reset_index()
# Preview DataFrame
std_err_met_site.head()


# In[11]:


# Minor Data Munging to Re-Format the Data Frames
std_err_met_site_table = std_err_met_site.pivot(index='Timepoint', columns='Drug', values='Metastatic Sites')
# Preview that Reformatting worked
std_err_met_site_table.head()


# In[12]:


# Generate the Plot (with Error Bars)
fig, ax = plt.subplots()

ax.errorbar(std_err_met_site_table.index, met_site_vol_table['Capomulin'], std_err_met_site_table['Capomulin'],
            fmt="o", color='red', label = 'Capomulin', ls='--')
ax.errorbar(std_err_met_site_table.index, met_site_vol_table['Infubinol'], std_err_met_site_table['Infubinol'],
            fmt="^", color='blue', label = 'Infubinol', ls='--')
ax.errorbar(std_err_met_site_table.index, met_site_vol_table['Ketapril'], std_err_met_site_table['Ketapril'],
            fmt="s", color='green', label = 'Ketapril', ls='--')
ax.errorbar(std_err_met_site_table.index, met_site_vol_table['Placebo'], std_err_met_site_table['Placebo'],
            fmt="d", color='black', label = 'Placebo', ls='--')

ax.set_xlim(-1, 47)
ax.set_ylim(0, 4)

ax.set_xlabel("Time (Days)")
ax.set_ylabel("Met Sites")
ax.set_title("Metastatic Spread During Treatment")
ax.legend()
plt.grid(axis='y')

# Save the Figure
plt.savefig('Fig2.png')
plt.show()


# ![Metastatic Spread During Treatment](../Images/spread.png)

# ## Survival Rates

# In[13]:


# Store the Count of Mice Grouped by Drug and Timepoint (W can pass any metric)
mice_count = Pymacueticals_df.groupby(['Drug', 'Timepoint'])['Mouse ID'].count()
# Convert to DataFrame
mice_count = pd.DataFrame(mice_count)
mice_count = mice_count.reset_index()
# Preview DataFrame
mice_count.head()


# In[14]:


# Minor Data Munging to Re-Format the Data Frames
mice_count_table = mice_count.pivot(index='Timepoint', columns='Drug', values='Mouse ID')
# Preview that Reformatting worked
mice_count_table.head()


# In[15]:


((mice_count_table['Capomulin']/mice_count_table['Capomulin'][0]) * 100)


# In[16]:


# Generate the Plot (Accounting for percentages)
fig, ax = plt.subplots()

ax.plot(mice_count_table.index, ((mice_count_table['Capomulin']/mice_count_table['Capomulin'][0]) * 100),
        marker="o", color='red', label = 'Capomulin', ls='--')
ax.plot(mice_count_table.index, ((mice_count_table['Infubinol']/mice_count_table['Infubinol'][0]) * 100),
        marker="^", color='blue', label = 'Infubinol', ls='--')
ax.plot(mice_count_table.index, ((mice_count_table['Ketapril']/mice_count_table['Ketapril'][0]) * 100),
        marker="s", color='green', label = 'Ketapril', ls='--')
ax.plot(mice_count_table.index, ((mice_count_table['Placebo']/mice_count_table['Placebo'][0]) * 100),
        marker="d", color='black', label = 'Placebo', ls='--')

ax.set_xlim(-1, 47)
ax.set_ylim(33, 105)

ax.set_xlabel("Time (Days)")
ax.set_ylabel("Survival Rate(%)")
ax.set_title("Survival During Treatment")
ax.legend()
plt.grid()

# Save the Figure
plt.savefig('Fig3.png')
plt.show()


# ![Metastatic Spread During Treatment](../Images/survival.png)

# ## Summary Bar Graph

# In[17]:


# Display the data to confirm calculation source
avg_tum_vol_table


# In[18]:


# Calculate Percent Change of Tumor Volume  -  Drugs not needed commented out
perc_change = []
Capomulin = ((avg_tum_vol_table.iloc[9, 0]) - (avg_tum_vol_table.iloc[0, 0])) / (avg_tum_vol_table.iloc[0, 0])
perc_change.append(Capomulin)
# Ceftamin = ((avg_tum_vol_table.iloc[9, 1]) - (avg_tum_vol_table.iloc[0, 1])) / (avg_tum_vol_table.iloc[0, 1])
# perc_change.append(Ceftamin)
Infubinol = ((avg_tum_vol_table.iloc[9, 2]) - (avg_tum_vol_table.iloc[0, 2])) / (avg_tum_vol_table.iloc[0, 2])
perc_change.append(Infubinol)
Ketapril = ((avg_tum_vol_table.iloc[9, 3]) - (avg_tum_vol_table.iloc[0, 3])) / (avg_tum_vol_table.iloc[0, 3])
perc_change.append(Ketapril)
# Naftisol = ((avg_tum_vol_table.iloc[9, 4]) - (avg_tum_vol_table.iloc[0, 4])) / (avg_tum_vol_table.iloc[0, 4])
# perc_change.append(Naftisol)
Placebo = ((avg_tum_vol_table.iloc[9, 5]) - (avg_tum_vol_table.iloc[0, 5])) / (avg_tum_vol_table.iloc[0, 5])
perc_change.append(Placebo)
# Propriva = ((avg_tum_vol_table.iloc[9, 6]) - (avg_tum_vol_table.iloc[0, 6])) / (avg_tum_vol_table.iloc[0, 6])
# perc_change.append(Propriva)
# Ramicane = ((avg_tum_vol_table.iloc[9, 7]) - (avg_tum_vol_table.iloc[0, 7])) / (avg_tum_vol_table.iloc[0, 7])
# perc_change.append(Ramicane)
# Stelasyn = ((avg_tum_vol_table.iloc[9, 8]) - (avg_tum_vol_table.iloc[0, 8])) / (avg_tum_vol_table.iloc[0, 8])
# perc_change.append(Stelasyn)
# Zoniferol = ((avg_tum_vol_table.iloc[9, 9]) - (avg_tum_vol_table.iloc[0, 9])) / (avg_tum_vol_table.iloc[0, 9])
# perc_change.append(Zoniferol)

# Display the data to confirm
perc_change


# In[19]:


# Create a list of Drugs
#drug_list = Pymacueticals_df['Drug']
#drug_list = drug_list.drop_duplicates('first')
#drug_list = drug_list.sort_values(ascending=True)
#drug_list.index = range(len(drug_list.index))


# In[20]:


# Create a list of Drugs
drug_list = ["Capomulin", "Infubinol", "Ketapril", "Placebo"]


# In[21]:


# Create a DataFrame
drug_percs = [(drug_list[x], perc_change[x]) for x in range(4)]
drugsDF = pd.DataFrame(drug_percs)
drugsDF.columns = ["Drug", "Perc_Change"]


# In[22]:


# Plot the data
ax = drugsDF.plot(
    kind='bar',
    x = "Drug",
    y = "Perc_Change",
    color=['#AA0000' if row.Perc_Change > 0 else '#000088' for name,row in drugsDF.iterrows()],
    rot=45
)
# formatting
percent_fmt = ["{}%".format(int(100.*row.Perc_Change)) for name,row in drugsDF.iterrows()]
for i,child in enumerate(ax.get_children()[:drugsDF.index.size]):
    if i == 0:
        ax.text(i, child.get_bbox().y1+0.21, percent_fmt[i], horizontalalignment ='center')
    else:
        ax.text(i, child.get_bbox().y1+0.01, percent_fmt[i], horizontalalignment ='center')

    ax.patch.set_facecolor('#FFFFFF')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['left'].set_linewidth(1)
    ax.spines['top'].set_color('#CCCCCC')
    ax.spines['top'].set_linewidth(1)
    ax.spines['right'].set_color('#CCCCCC')
    ax.spines['right'].set_linewidth(1)

    
ax.set_title("Tumor Change over 45 Day Treatment")
ax.set_ylabel("% Tumor Change")
ax.set_ylim(-0.3, 1)
plt.axhline(0, ls="--", color="grey", lw=3)
# Save the Figure
plt.savefig('Fig4.png')
# Show the Figure
plt.show()


# ![Metastatic Spread During Treatment](../Images/change.png)
