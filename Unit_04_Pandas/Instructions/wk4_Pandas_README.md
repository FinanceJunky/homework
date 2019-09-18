# Week 4 - Intro to Pandas
## Objectives
* Be able to serve Jupyter notebook files from local directories and connect to their development environment.
* Be able to create Pandas DataFrames from scratch.
* Understand how to run functions on Pandas DataFrames.
* Know how to read/write DataFrames from/to CSV files using Pandas.
* Understand how to navigate through DataFrames using Loc and Iloc.
* Understand how to filter and slice Pandas DataFrames.
* Understand how to create and access Pandas GroupBy objects.
* Understand how to sort DataFrames.
* Know how to merge DataFrames together whilst understanding the differences between inner, outer, left, and right merges.
* Be able to slice data using the cut() method and create new values based upon a series of bins.
* Feel more confident with fixing Python/Pandas bugs within Jupyter Notebook.
* Be able to use Google to explore additional Pandas functionality when necessary.


## Lesson 1: Introduction to Pandas & Jupyter

* Be able to serve Jupyter notebook files from local directories and connect to their development environment
* Be able to create Pandas DataFrames from scratch
* Understand how to run functions on Pandas DataFrames
* Know how to read/write DataFrames from/to CSV files using Pandas


### **Additional Resources**  

* [Formatting](https://pyformat.info/)

* [Pandas Tutorials](https://chrisalbon.com/)

* [Pandas Documentation](http://pandas.pydata.org/)

* [Visual Guide to Joins](https://blog.codinghorror.com/a-visual-explanation-of-sql-joins/)

* [Pandas Merging](https://pandas.pydata.org/pandas-docs/stable/merging.html)

* [10 Minutes to pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html) 

* [Conda Cheat Sheet](https://kapeli.com/cheat_sheets/Conda.docset/Contents/Resources/Documents/index)

* [28 Jupyter Notebook Tricks](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/) 

* [Gallery of Interesting Jupyter Notebooks](https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks#pandas-for-data-analysis) **FREE TUTORIALS AS WELL**

## Additional Course Resources

* [Pandas Summary Notebooks](Supplemental/)

* [Pandas Cheatsheet](https://www.dataquest.io/blog/pandas-cheat-sheet/)


* 01-Ins_JupyterIntro  
    * `Jupyter Notebook` is a interactive Python interpreter combining capabilities of text editor, console, and markdown file into one application.  
    * to open jupyter notebook from anaconda prompt.  move to directory you want to access and enter jupyter notebook.  A webpage where automatically open where you can navifate into any files/folders.
    ![Jupyter](images/jupyter.png)
    * The code contained within a Jupyter Notebook is not linear. For example, if two cells modify the same variable, then whichever block of code was run last will ultimately determine the value of the variable
        
* 02-Stu_NetflixRemix  
    * example of running previous code from week 3 lesson 2 activity 08 in jupyter environment
    
* 03-Ins_IntroToPandas  **--Basic Homework Manually Create DataFrame or Series--**
    * `Pandas` library allows for programmers to work with "Series" and "DataFrames", which are essentially structured lists with many built any methods that allow for easy manipulation (YOU WILL COME TO LOVE PANDAS)
        * `Pandas Series` one dimensional labeled array capable of holding any data type.  Like an array the data is linear but also like a dictionary as it has an index that acts like a "key".
        * `Pandas DataFrame` is a two dimension labeled data structure with columns of potentially different types.  Much like an excel spreadsheet each column can be considered a series.
    * Before you can do anything with pandas you must import pandas library into notebook
        * import pandas as pd
    * to create a series use the `pd.Series()` function and place a list between parantheses
    * two ways to create a `pd.DataFrame()` from scratch
        1. provide the `pd.DataFrame()` a list of dictionaries.  Each dictionary will represent a new row where the keys become the column header. While the list of dictionaries method of DataFrame creation is viable, it takes far longer to write the code for since the keys have to be re-written each time. It does allow the programmer to better understand what each row in their DataFrame will look like though.
        2. provide the `pd.DataFrame()` a dictionary of lists.  The keys of the dictionary will become the column headers and the listed values will be placed into their respective rows. The dictionary of lists method is much more time effective since the keys need only be written once. **It can be harder to read through, however, as if even one of the lists contains fewer values than the others than an error will be returned**

```python
# alias pandas as pd.  When call functions/methods will use pd.nameFunction()
import pandas as pd

# creating a Pandas series from a raw list.  Since index= argument is not inputed will come back as a number index
data_series = pd.Series(["UCLA","UC Berkley", "UC Irvine", "University of Central Florida", "Rutgers University"])

# calling variable allows us to see output of variable to console
data_series
```

```python
# First way to create pd.Dataframe() using list of dictionaries
list_dict_df = pd.DataFrame([{"STATE":"New Jersey","ABBREVIATION":"NJ"},
                            {"STATE":"New York","ABBREVIATION":"NY"}])
list_dict_df
```

```python
# Second way to create pd.Dataframe() is to use a dictionary of lists
dict_list_df = pd.DataFrame(
    {"Dynasty":["Early Dynastic Period","Old Kingdom"],
     "Pharph":["Thinis","Memphis"]
    }
)
dict_list_df.head()
```


* 04-Stu_DataFrameShop  

* 05-Ins_DataFunctions **--Homework helpful Functions/Methods--** 
    * `head()` This function returns the first `n` rows for the object based on position. It is useful for quickly testing if your object has the right type of data in it.
    * `describe()` Generate descriptive statistics that summarize the central tendency, dispersion and shape of a dataset's distribution, excluding ``NaN`` values.
    * `info()` This method prints information about a DataFrame including the index dtype and column dtypes, non-null values and memory usage.
        * Most data functions can also be performed on a Series by referencing a single column within the whole DataFrame. This is done in a similar way to referencing a key within dictionary by taking the DataFrame and following it up with brackets with the desired column's header contained within like a key.

        * Multiple columns can be referenced as well by placing all of the column headers desired within a pair of double brackets. If two sets of brackets are not used then Pandas will return an error.
        
        ```python
        # reference single column of dataframe
        data_file_pd["Amount"].head()
        # reference multiple columns within a dataframe
        data_file_pd[["Amount","Gender"]].head()
        # Mead method for series
        average = data_file_pd["Amount"].mean()
        # The sum method adds every entry in Series
        total = data_file_pd["Amount"].sum()
        # unique method will show every element of series that appears once
        unique = data_file_pd["Last Name"].unique()
        # value_counts() method counts unique values in a column
        count - data_file_pd["Gender"].value_counts()
        
        ```

* 06-Stu_TrainingGrounds  **--Homework Practice--**
    
* 07-Ins_ColumnManipulation  
    * `df.columns` attribute call allows you to call object column headers and print them to screen.
    * to reorder columns create a reference to a DataFrame followed by two brackets with the column headers placed in the order desired.  You can also remove columns by not creating a reference to them with this technique
    * To rename columns use the `df.rename` method annd place columns paramenter `columns={}` within the parantheses.

* 08-Stu_Hey_Arnold  

* 09-Ins_ReadingWritingCSV  **-- Basic Homework Practice--**
    * Create a reference to the CSV file's path and pass it in into the `pd.read_csv()` method, making certain to store the returned DataFrame within a variable. From then on, the DataFrame can be altered and manipulated like normal.
    * It is just as easy to write to a CSV file as it is to read from one. Simply use the `df.to_csv()` method, passing the path to the desired output file. By using the `index` and `header` parameters, programmers can also manipulate whether they would like the index or header for the table to be passed as well.

* 10-Stu_GoodReads  

* 11-Stu_GoodReadsSummary  **--Good Example For Homework--**


## Lesson 2: Exploring Pandas

* Understand how to navigate through DataFrames using Loc and Iloc
* Understand how to filter and slice Pandas DataFrames
* Understand how to create and access Pandas GroupBy objects
* Understand how to sort DataFrames


### **Additional Resources**  

* [Loc and iLoc indexing](https://stackoverflow.com/questions/28757389/pandas-loc-vs-iloc-vs-ix-vs-at-vs-iat) 

* [Selecting a Subset Pandas Part 1](https://medium.com/dunder-data/selecting-subsets-of-data-in-pandas-6fcd0170be9c)

* [Selecting a Subset Pandas Part 2](https://medium.com/dunder-data/selecting-subsets-of-data-in-pandas-39e811c81a0c)

* [Hello World Tutorial VS Code](https://code.visualstudio.com/docs/python/python-tutorial#_select-a-python-interpreter)


* 01-Ins_LocAndIloc  
    * The `loc()` method allows its users to select data using label based indexes. In other words, it takes in strings as the keys and returns data based upon that.
        * The `iloc()` method also allows its users to select data, but instead of using labels, it instead uses integer based indexing for selection by position.
* 02-Stu_GoodMovies  
    * **Good practice filtering dataframes
* 03-Ins_CleaningData  
    * dropping rows with missing information `df.dropna(how="any")`
    * in order to fill "NaN" values instead of removing use `df.fillna(value-<Value>)` method
    * in order to find values that have similar/misspelled values, simply run the `value_counts()` method 
    * replace similar/misspelled values, simply run the `replace()` method on the column in question and pass a dictionary into it with the keys being those value
* 04-Par_PortlandCrime  
    * **Good Practice dropping `NaN` replacing values etc
* 05-Evr_PandasRecap  
    * In order to change a non-numeric column to a numeric column, use the `df.astype(<datatype>)` method and pass in the desired datatype as the parameter
    * in order to find columns data types use `df.dtypes` attribute or `df.info()` method
* 06-Ins_GroupBy  **--Homework--**
    * `df.groupby([<Columns>])` method used to split DataFrame into multiple groups.  `.groupby()` method is a GroupBy Object and cannot be accessed like a normal DataFrame. One way to access GroupBy object is by using a data function on it.
* 07-Par_Pokemon  **--Homework--**
* 08-Ins_Sorting  
    * `df.sort_values()` method allows to sort values within a column by passing column name to sort in as parameter.  "ascending" always marked as True by default.
    * If sorting a series use `obj.order()` method.
    * also look up `df.sort_index()` for extra work
    * Something immensely helpful when dealing with sorted DataFrames is the `df.reset_index()` method. This method will recalculate the index for each row based upon their position within the new DataFrame and, as such, will allow for far simpler referencing of rows in the future.
    * Passing `drop=True` into `df.reset_index()` will ensure no new column is created when the index is reset
* 09-Stu_SearchForTheWorst  


## Lesson 3: Merging and Data Clean Project

* Merge DataFrames together whilst understanding the differences between inner, outer, left, and right merges.
* Be able to slice data using the cut() method and create new values based upon a series of bins.
* Feel more confident in their ability to fix Python/Pandas bugs within Jupyter Notebook.
* Be able to use Google to explore additional Pandas functionality when necessary.


### **Additional Resources**  

* [Pandas for Time Series Data](https://medium.com/@bingobee01/pandas-tricks-and-tips-a7b87c3748ea)

* [How to Iterate over rows in a DataFrame in Pandas](https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas)  

* [Cool Module Pandas Profiling](https://pandas-profiling.github.io/pandas-profiling/docs/#examples)

* [Pandas Merging](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html)  

* [Understanding Different Types of Merges](http://www.datasciencemadesimple.com/join-merge-data-frames-pandas-python/)


* 01-Ins_Merging  **Homework if do PyCitySchools**
    * `pd.merge()` method allows you to join two dataframes together
    * four arguments for "how" parameter
        * `how="inner"` default parameter (does not have to be declared) will only return data whose values match. Any rows that do not include matching data will be dropped from the combined DataFrame.
        * `how="outer"`  Outer joins will combine the DataFrames regardless of whether any of the rows match and must be declared as a parameter. Any rows that do not include matching data will have the values within replaced with `NaN` instead
        * `how="left"` left join will protect the data contained within left DataFrame like an outer join does whilst also dropping the rows with null data from the right DataFrame
        * `how="right"` right join will protect the data contained within right DataFrame like an outer join does whilst also dropping the rows with null data from the left DataFrame

* 02-Stu_Cryptocurrency  
    * Alternatively, you can create custom suffixes by adding a `suffixes = (_x,_y)` argument to `pd.merge` \_x and \_y can be replaced with any text you wish

* 03-Ins_Binning  **Homework**
    * `pd.cut` is a "binning" method that allows users to place values into groups.  Three parameters must be passed in
        * pass Series that is going to be cut `df["<column>"]`
        * bins allow Pandas to determine range between values
        * labels must have equal length to number of bins

* 04-Stu_TedTalks  

* 05-Ins_Mapping **Homework for formatting**
    * `df.map()` method allows users to style columns.  example `df[<COLUMN>].map("${:.2f}".format)`
    * **Format mapping only really works once and will return errors if the same code is run multiple times without restarting the kernel. Because of this, formatting is usually applied near the end of an application. Format mapping can also change the datatype of a column**

* 06-Stu_CleaningKickstarter  

* 07-Ins_IntroToBugfixing  

* 08-Stu_BugfixingBonanza


# Pandas Homework - Pandas, Pandas, Pandas

## Background

The data dive continues!

Now, it's time to take what you've learned about Python Pandas and apply it to new situations. For this assignment, you'll need to complete **one of two** (not both)  Data Challenges. Once again, which challenge you take on is your choice. Just be sure to give it your all -- as the skills you hone will become powerful tools in your data analytics tool belt.

### Before You Begin

1. Create a new repository for this project called `pandas-challenge`. 

2. Clone the new repository to your computer.

3. Inside your local git repository, create a directory for the Pandas Challenge you choose. Use folder names corresponding to the challenges: **HeroesOfPymoli** or  **PyCitySchools**.

4. Add your Jupyter notebook to this folder. This will be the main script to run for analysis.

5. Push the above changes to GitHub or GitLab.

## Option 1: Heroes of Pymoli

![Fantasy](Images/Fantasy.png)

Congratulations! After a lot of hard work in the data munging mines, you've landed a job as Lead Analyst for an independent gaming company. You've been assigned the task of analyzing the data for their most recent fantasy game Heroes of Pymoli.

Like many others in its genre, the game is free-to-play, but players are encouraged to purchase optional items that enhance their playing experience. As a first task, the company would like you to generate a report that breaks down the game's purchasing data into meaningful insights.

Your final report should include each of the following:

### Player Count

* Total Number of Players

### Purchasing Analysis (Total)

* Number of Unique Items
* Average Purchase Price
* Total Number of Purchases
* Total Revenue

### Gender Demographics

* Percentage and Count of Male Players
* Percentage and Count of Female Players
* Percentage and Count of Other / Non-Disclosed

### Purchasing Analysis (Gender)

* The below each broken by gender
  * Purchase Count
  * Average Purchase Price
  * Total Purchase Value
  * Average Purchase Total per Person by Gender

### Age Demographics

* The below each broken into bins of 4 years (i.e. &lt;10, 10-14, 15-19, etc.)
  * Purchase Count
  * Average Purchase Price
  * Total Purchase Value
  * Average Purchase Total per Person by Age Group

### Top Spenders

* Identify the the top 5 spenders in the game by total purchase value, then list (in a table):
  * SN
  * Purchase Count
  * Average Purchase Price
  * Total Purchase Value

### Most Popular Items

* Identify the 5 most popular items by purchase count, then list (in a table):
  * Item ID
  * Item Name
  * Purchase Count
  * Item Price
  * Total Purchase Value

### Most Profitable Items

* Identify the 5 most profitable items by total purchase value, then list (in a table):
  * Item ID
  * Item Name
  * Purchase Count
  * Item Price
  * Total Purchase Value

As final considerations:

* You must use the Pandas Library and the Jupyter Notebook.
* You must submit a link to your Jupyter Notebook with the viewable Data Frames.
* You must include a written description of three observable trends based on the data.
* See [Example Solution](HeroesOfPymoli/HeroesOfPymoli_starter.ipynb) for a reference on expected format.

## Option 2: Academy of Py

![Education](Images/education.png)

Well done! Having spent years analyzing financial records for big banks, you've finally scratched your idealistic itch and joined the education sector. In your latest role, you've become the Chief Data Scientist for your city's school district. In this capacity, you'll be helping the  school board and mayor make strategic decisions regarding future school budgets and priorities.

As a first task, you've been asked to analyze the district-wide standardized test results. You'll be given access to every student's math and reading scores, as well as various information on the schools they attend. Your responsibility is to aggregate the data to and showcase obvious trends in school performance.

Your final report should include each of the following:

### District Summary

* Create a high level snapshot (in table form) of the district's key metrics, including:
  * Total Schools
  * Total Students
  * Total Budget
  * Average Math Score
  * Average Reading Score
  * % Passing Math
  * % Passing Reading
  * Overall Passing Rate (Average of the above two)

### School Summary

* Create an overview table that summarizes key metrics about each school, including:
  * School Name
  * School Type
  * Total Students
  * Total School Budget
  * Per Student Budget
  * Average Math Score
  * Average Reading Score
  * % Passing Math
  * % Passing Reading
  * Overall Passing Rate (Average of the above two)

### Top Performing Schools (By Passing Rate)

* Create a table that highlights the top 5 performing schools based on Overall Passing Rate. Include:
  * School Name
  * School Type
  * Total Students
  * Total School Budget
  * Per Student Budget
  * Average Math Score
  * Average Reading Score
  * % Passing Math
  * % Passing Reading
  * Overall Passing Rate (Average of the above two)

### Bottom Performing Schools (By Passing Rate)

* Create a table that highlights the bottom 5 performing schools based on Overall Passing Rate. Include all of the same metrics as above.

### Math Scores by Grade\*\*

* Create a table that lists the average Math Score for students of each grade level (9th, 10th, 11th, 12th) at each school.

### Reading Scores by Grade

* Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.

### Scores by School Spending

* Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
  * Average Math Score
  * Average Reading Score
  * % Passing Math
  * % Passing Reading
  * Overall Passing Rate (Average of the above two)

### Scores by School Size

* Repeat the above breakdown, but this time group schools based on a reasonable approximation of school size (Small, Medium, Large).

### Scores by School Type

* Repeat the above breakdown, but this time group schools based on school type (Charter vs. District).

As final considerations:

* Use the pandas library and Jupyter Notebook.
* You must submit a link to your Jupyter Notebook with the viewable Data Frames.
* You must include a written description of at least two observable trends based on the data.
* See [Example Solution](PyCitySchools/PyCitySchools_starter.ipynb) for a reference on the expected format.

## Hints and Considerations

* These are challenging activities for a number of reasons. For one, these activities will require you to analyze thousands of records. Hacking through the data to look for obvious trends in Excel is just not a feasible option. The size of the data may seem daunting, but pandas will allow you to efficiently parse through it.

* Second, these activities will also challenge you by requiring you to learn on your feet. Don't fool yourself into thinking: "I need to study pandas more closely before diving in." Get the basic gist of the library and then _immediately_ get to work. When facing a daunting task, it's easy to think: "I'm just not ready to tackle it yet." But that's the surest way to never succeed. Learning to program requires one to constantly tinker, experiment, and learn on the fly. You are doing exactly the _right_ thing, if you find yourself constantly practicing Google-Fu and diving into documentation. There is just no way (or reason) to try and memorize it all. Online references are available for you to use when you need them. So use them!

* Take each of these tasks one at a time. Begin your work, answering the basic questions: "How do I import the data?" "How do I convert the data into a DataFrame?" "How do I build the first table?" Don't get intimidated by the number of asks. Many of them are repetitive in nature with just a few tweaks. Be persistent and creative!

* Expect these exercises to take time! Don't get discouraged if you find yourself spending  hours initially with little progress. Force yourself to deal with the discomfort of not knowing and forge ahead. Consider these hours an investment in your future!

* As always, feel encouraged to work in groups and get help from your TAs and Instructor. Just remember, true success comes from mastery and _not_ a completed homework assignment. So challenge yourself to truly succeed!

### Copyright

Trilogy Education Services © 2019. All Rights Reserved.

```python

```
