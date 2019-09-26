# Week 5: Matplotlib 
## Objectives
* Understand Matplotlib's pyplot interface.
* Be able to create line; bar; scatter; and pie charts.
* Be familiar with basic plot configuration options, such as xlim and ylim.
* Feel comfortable creating plots using the DataFrame.plot() method.
* Understand the advantages and disadvantages of creating charts using the DataFrame.plot() method.
* Be able to work through a complex data set using Pandas and then chart some visualizations based upon the cleaned DataFrame.
* Be able to define mean, median, and mode, and choose which one is most appropriate to describe a given data set.
* Be able to explain the meaning of variance and standard deviation.
* Be able to describe standard error and the difference between a sample and a population.
* Be able to add error bars to their plots.
* Be able to fit lines to their data.


### **Additional Resources**  
* [Numpy](http://www.numpy.org/)

* [Matplotlib Gallery](https://matplotlib.org/gallery.html)

* [Pandas Plotting](https://pandas.pydata.org/pandas-docs/stable/visualization.html)

* [Alternatives to Pie Charts](http://www.storytellingwithdata.com/blog/2014/06/alternatives-to-pies)

* [Tuple Unpacking](https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/)

* [Data to Ink Ratio](https://infovis-wiki.net/wiki/Data-Ink_Ratio)

* [Choose Right Chart for Data Viz](https://datavizcatalogue.com/search.html)

* [Matplotlib Colors](https://matplotlib.org/users/colors.html)

* [Pandas DataFrame.add() Method](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.add.html)

* [Pandas DataFrame.pivot() Method](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot.html)

* [Median vs Mean](https://creativemaths.net/blog/median/)

* [SciPy Math, Science and Engineering](https://www.scipy.org/)

* [Outliers When and What to Do](https://www.theanalysisfactor.com/outliers-to-drop-or-not-to-drop/)

* [Numpy Percentile](https://het.as.utexas.edu/HET/Software/Numpy/reference/generated/numpy.percentile.html)

* [Pandas Datafrmae.sem()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sem.html) **HOMEWORK**

* [SciPy Stats Ttest](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html)

* [SciPy Linreregress Function](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html)

* [PYOD Outlier Detection](https://www.analyticsvidhya.com/blog/2019/02/outlier-detection-python-pyod/)


## Lesson 1: Introduction to Matplotlib
* Understand Matplotlib's pyplot interface.

* Be able to create line; bar; scatter; and pie charts.

* Be familiar with basic plot configuration options, such as xlim and ylim.


* 01-Ins_BasicLineGraphs  
    * `np.arange(start,end,step)` creates a list of numbers from start to end where each number in list is `step` away from the next ones.  Comes from NumPy library and a good way to create testing data sets

    ```python
    # when using magic matplotlib notebook makes a plot interactive, but it also allows it to be updated after the initial plot. Make sure to put in first cell
    %matplotlib notebook
    # import dependencies
    import matplotlib.pyplot as plt
    import numpy as np
    ```
    
    * `plt.plot()` allows you generate plot by setting paramaters of x-axis and y-axis. `plt.show()` allows to print to screen
    * `plt.xlabel()` and `plt.ylabel()` allow you to add axis titles to the chart
* 02-Stu_NJTemp  
    
* 03-Ins_ConfiguringLinePlots  
    * controling details on plots appereance using **keyword arguments** to configure the behavior of `plot`
    
    ```python
    # Draw a horizontal line with 0.25 transparancy
    plt.hlines(0,0,10, alpha=0.25)
    ```
    
    * argument unpacking to select only first line from a list of lines `sin_handle,`
    * Additional parameters in `plt.plot()`
        * `marker=`
        * `color=`
        * `label=`
    * `plt.legend()` method allows to create a legend on chart. With `loc` argument to set location
    * `plt.savefig()` will allow to save version of chart to external file.
    
* 04-Stu_LegendaryTemperature  
* 05-Ins_Aesthetics  
    * Helpful additions to chart to help readability
        * Adding labels to the x-axis
        * Adding labels to the y-axis
        * Adding titles to plots
        * Limiting the exten of plot to bound the plot's data points
        * Adding grids can help but would discourage against this
        
* 06-Stu_RollerCoaster  

* 07-Ins_BarCharts  **--Basic Homework Knowledge--**
    * Charts and what type to use when:
        * **Bar** comparing different entities to one another
        * **Pie** displaying parts of the whole (not a preferred chart)
        * **Scatter Plots** diplaying points and where they fall with respect to two different factors
    * `plt.bar()` to draw bar chart.  `align` parameter is center to center
    * `plt.xticks` to plot where like to place x axis headers.  Need to pass list to place ticks.
    * `plt.xlim()` and `plt.ylim()` allow to set some space between bars and the edge of the chart
    
* 08-Stu_PyBars  
* 09-Ins_PieCharts  
    * `plt.pie()` sizes of wedge are passed in as array. Lists containing labels for each wedge and the colors for each wedge are also passed in.
        * pie chart allows the user to choose a wedge to `explode` using the explode option which is passed in array
        * `autopc="%1.1%%` convert values passed into percentages
        
* 10-Stu_PyPies  
* 11-Ins_ScatterPlots **--Basic Homework Knowledge--**
    * `plt.scatter()` Simply take in two sets of data and pass them.
        * change size of each dot by passing `s=<LIST>`
        
* 12-Stu_ScatterPy  
* 13-Stu_AvgRain  


## Lesson 2: Plotting with Pandas
* Feel comfortable creating plots using the `DataFrame.plot()` method

* Understand the advantages and disadvantages of creating charts using the `DataFrame.plot()` method.

* Be able to work their way through a complex data set using Pandas and then chart some visualizations based upon the cleaned DataFrame.


* 01-Stu_PlotsReview  
    * Practice identifying correct charts.
    
* 02-Ins_PandasPlot  
    * Pandas has built in Matplotlib methods in library.  
    * `DataFrame.plot()` called to create chart.  `kind="bar"` paramater allows to choose what type of chart and `figsize(20,3)` paramater allows you to control width, height in inches
    * chart can still be edited with `plt.title()` and other keyword arguments. 
    * Possible to modify a specific Pandas plot by storing the plot within a variable and then using built-in methods to modify it. For example: `PandasPlot.set_xticklabels()` will allow the user to modify the tick labels on the X axis without having to manually set the DataFrame's index.
    * When using `set_index()`  The values stored within the index will be the labels for the X axis while the values stored within the other column will be used to plot the Y axis.
    
* 03-Stu_BattlingKings  
    * `DataFrame.add()` method check out
    
* 04-Ins_GroupPlots  **--Basic Homework Knowledge--**
    * Pandas includes methos that allow to plot GroupBy objects.  
    
* 05-Stu_BikeTrippin  
    * More practice with Pandas charting :)
    * Bar and Pie Charts
    
* 06-Stu_MilesPerGallon  
    * Scatter Plot practice
    
* 07-Ins_PandasMultiLine  
    * Practice showing multiple line plots in same chart
    
* 08-Stu_WinnerWrestling-Part1  **--Good Practice--*
* 09-Stu_WinnerWrestling-Part2  
* 10-Stu_WinnerWrestling-Part3  


## Lesson 3: Introduction to Statistics
* Be able to define mean, median, and mode, and choose which one is most appropriate to describe a given data set.

* Be able to explain the meaning of variance and standard deviation.

* Be able to describe standard error and the difference between a sample and a population.

* Be able to add error bars to their plots.

* Be able to fit lines to their data.


* 01-Ins_Mean_Median_Mode  
    * median is more "resistant" to extreme fluctuations in data than the mean. Median is particularly faithful for data sets that have a large number of values that are low, or a large number that are high.
    
* 02-Ins_Variance_and_Z_Score
    *  mean, median, and mode allow us to summarize our data succinctly, there are important aspects of data that they do not reveal.
    * statistics that measure spread are **variance**, **standard deviation**, and **z-score**.
        * Variance set is a single number that describes how "far apart" its values are
        * Standard Deviation square root of the variance. standard deviation as a unit to describe how far individual numbers in a data set are away from the mean.
        * Z-score statistic that describes how far away from the mean any single number in the data set is.
        
* 03-Ins_Quartiles_and_Outliers  
    * When to remove outliers and when not to:
        * If the outliers create trends that wouldn't exist without them, you should drop them.
        * If outliers do not change your results. In this case, it is okay to drop them, but it is best to make a note of having done so.
        * If your outlier does change your results, you should not drop it.
    * **Quartiles** help in making decision to drop outliers.  Simplest way is to remove data that is "far away" from the **median**
        *  simple but common way to remove outliers is to throw away anything above the _upper quartile_, and everything below the _lower quartile_.
        * subtracting the lower quartile from the upper quartile gives us the interquartile range, which is another measure of how "spread out" a data set is.
        
* 04-Stu_Quartiles_and_Outliers 
    * Interquartile range measure spread, similar to standard deviation, but is less susceptible to outliers.
    *  boundaries can be found with the formulas `Q1 - 1.5 * IQR` and `Q3 + 1.5 * IQR`
    
* 05-Ins_Standard_Error  **--HOMEWORK--**
    * `Standard Error` a measure of the statistical accuracy of an estimate, equal to the standard deviation of the theoretical distribution of a large population of such estimates. _Standard error_ describes how far its mean is from the population's "true" mean.
    * Always think about how well samples represent the populations they describe
    * `Matplotlib.pyplot.errorbar()` [errorbar()](https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.errorbar)  **homework** 
    
* 06-Stu_Standard_Error  
* 07-Ins_Students_t_test  
    * Last activity plotted errorbars to provide a visual indicator as to how confident we were in the proximity of our sample means to the "true" population mean. Most of the error bars in the plot we generated overlapped.  If this were not the case, it would raise questions about the data.
    * `Student's t-test` used to determine how likely it is that two sample means represent the same underlying population. Student's t-test can only be used to test two sample means against each other.
        *  `t statistic` tells us how likely it is the differences are significant. The higher the t-statistic, the higher the chances they are significant.
        *  `p value` If p < 0.05 (or 0.01, depending on your standards for confidence), we should assume that the differences are not due to chance.
    
* 08-Stu_Students_t_test  

* 09-Ins_Fits_and_Regression  
    * final important piece of statistics for the day is the subject of **regressions**.  
    *  median, variance, and IQR _describe_ data sets, but do not allow us to make predictions with it.
    * Linear Regression formula `line = slope * x_axis_values + y_intercept`
    
* 10-Stu_Fits_and_Regression 


# Matplotlib Homework - The Power of Plots

## Background

What good is data without a good plot to tell the story?

So, let's take what you've learned about Python Matplotlib and apply it to a real-world situation.

### Before You Begin

1. Create a new repository for this project called `matplotlib-challenge`.
2. Clone the new repository to your computer.

3. Inside your local git repository, create a directory for the assignment **Pymaceuticals**.

4. Add your Jupyter notebook to this folder. This will be the main script to run for analysis.

5. Push the above changes to GitHub or GitLab.

## Pymaceuticals Instructions

![Laboratory](Images/Laboratory.jpg)

While your data companions rushed off to jobs in finance and government, you remained adamant that science was the way for you. Staying true to your mission, you've since joined Pymaceuticals Inc., a burgeoning pharmaceutical company based out of San Diego, CA. Pymaceuticals specializes in drug-based, anti-cancer pharmaceuticals. In their most recent efforts, they've since begun screening for potential treatments to squamous cell carcinoma (SCC), a commonly occurring form of skin cancer.

As their Chief Data Analyst, you've been given access to the complete data from their most recent animal study. In this study, 250 mice were treated through a variety of drug regimes over the course of 45 days. Their physiological responses were then monitored over the course of that time. Your objective is to analyze the data to show how four treatments (Capomulin, Infubinol, Ketapril, and Placebo) compare.

To do this you are tasked with:

* Creating a scatter plot that shows how the tumor volume changes over time for each treatment.
* Creating a scatter plot that shows how the number of [metastatic](https://en.wikipedia.org/wiki/Metastasis) (cancer spreading) sites changes over time for each treatment.
* Creating a scatter plot that shows the number of mice still alive through the course of treatment (Survival Rate)
* Creating a bar graph that compares the total % tumor volume change for each drug across the full 45 days.
* Include 3 observations about the results of the study. Use the visualizations you generated from the study data as the basis for your observations.

As final considerations:

* You must use the Pandas Library and the Jupyter Notebook.
* You must use the Matplotlib library.
* You must include a written description of three observable trends based on the data.
* You must use proper labeling of your plots, including aspects like: Plot Titles, Axes Labels, Legend Labels, X and Y Axis Limits, etc.
* Your scatter plots must include [error bars](https://en.wikipedia.org/wiki/Error_bar). This will allow the company to account for variability between mice. You may want to look into [`pandas.DataFrame.sem`](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sem.html) for ideas on how to calculate this.
* Remember when making your plots to consider aesthetics!
  * Your legends should not be overlaid on top of any data.
  * Your bar graph should indicate tumor growth as red and tumor reduction as green.
    It should also include a label with the percentage change for each bar. You may want to consult this [tutorial](http://composition.al/blog/2015/11/29/a-better-way-to-add-labels-to-bar-charts-with-matplotlib/) for relevant code snippets.
* See [Starter Workbook](Pymaceuticals/pymaceuticals_starter.ipynb) for a reference on expected format. (Note: For this example, you are not required to match the tables or data frames included. Your only goal is to build the scatter plots and bar graphs. Consider the tables to be potential clues, but feel free to approach this problem, however, you like.)

## Hints and Considerations

* Be warned: These are very challenging tasks. Be patient with yourself as you trudge through these problems. They will take time and there is no shame in fumbling along the way. Data visualization is equal parts exploration, equal parts resolution.

* You have been provided a starter notebook. Use the code comments as a **guideline** of steps you may wish to follow as you complete the assignment. You do not have to follow them step-for-step. Do not get bogged down in trying to interpret and accomplish each step.

* Between these two exercises, the Pymaceuticals one is significantly more challenging. So choose that one only if you feel somewhat comfortable with the material covered so far. The Pymaceuticals example _will_ require you to research a good bit on your own for hacked solutions to problems you'll experience along the way. If you end up choosing this exercise, feel encouraged to constantly refer to Stack Overflow and the Pandas Documentation. These are needed tools in every data analyst's arsenal.

* Don't get bogged down in small details. Always focus on the big picture. If you can't figure out how to get a label to show up correctly, come back to it. Focus on getting the core skeleton of your notebook complete. You can always re-visit old problems.

* Remember: There are many ways to skin a cat, and similarly there are many ways to approach a data problem. The key throughout, however, is to break up your task into micro tasks. Try answering questions like: "How does my Data Frame need to be structured for me to have the right X and Y axis?" "How do I build a basic scatter plot?" "How do I add a label to that scatter plot?" "Where would the labels for that scatter plot come from?". Again! Don't let the magnitude of a programming task scare you off. Ultimately, every programming problem boils down to a handful of smaller, bite-sized tasks.

* Get help when you need it! There is never any shame in asking. But as always, ask a _specific_ question. You'll never get a great answer to: "I'm lost." Good luck!

### Copyright

Trilogy Education Services © 2019. All Rights Reserved.

```python

```
