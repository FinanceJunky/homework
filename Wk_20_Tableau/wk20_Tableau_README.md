## Lesson 1 - Time to Tableau Some Minds
* Import various data sources, including CSV files and Excel spreadsheets
* Be able to perform joins on multiple data sources
* Create basic visualizations
* Customize visualizations 
* Create a story board


### **_Additional Resources_**  
[Tableau Gallery](https://public.tableau.com/en-us/s/gallery)  
[Tableau Public](https://public.tableau.com/s/)  
[Tableau Desktop](https://www.tableau.com/products/desktop)  
[Tableau Prep](https://www.tableau.com/products/prep)  
[ATTR Function Explained](https://community.tableau.com/thread/114562)  
[Discrete vs Continous](https://onlinehelp.tableau.com/current/pro/desktop/en-us/datafields_typesandroles.htm)  
[Filtering Dates](https://onlinehelp.tableau.com/current/pro/desktop/en-us/filtering.htm#FilterDates)  
[Top 15 LOD Expressions](https://www.tableau.com/about/blog/LOD-expressions)  
[Dynamic Tooltips](https://playfairdata.com/how-to-make-dynamic-tooltips-in-tableau/)  
[Viz in Tooltip](https://interworks.com/blog/hcalder/2018/06/04/mastering-viz-in-tooltip-and-tooltip-filtering-in-tableau/)  
[DataViz Society](https://www.datavisualizationsociety.com/) #JOIN THIS SOCIETY!

__01-Ins_LoadingData__  
* Dimensions definition: Categorical fields that data can be split up by. Typically are discrete `("individually seperate and distinct")`. Discrete values are treated as finite and generally add headers to a view.  
* Measures definition: are the metrics or numbers that users would like to analyze. Typically treated as continous `("forming an unbroken whole, without interruption")` field values of an infinate range. Generally continous fields add axes to the view.  
__02-Ins_BasicVisuals__    
__03-Stu_Exploration__  - **example of graphical analysis homework**  
* In Tableau queries, dimensions in the view are expressed in SQL as "Group By" clauses.  
__04-Stu_NoShow__  - **example of graphical analysis homework**  
__05-Ins_EasyJoins__  
__06-Stu_FIFAPlayers__  
__07-Stu_UltimateCandy__  
__08-Ins_Storytelling__  
__09-Stu_DegreesPay__  


## Lesson 2 - Tableau My Mind
* Create groups and sets
* Create maps and use built-in U.S. Census data
* Create custom calculations and understand what a LOD calc is


### **_Additional Resources_**  
[Tableau Set Actions](https://onlinehelp.tableau.com/current/pro/desktop/en-us/actions_sets.htm)  
[Tableau Create Sets](https://onlinehelp.tableau.com/current/pro/desktop/en-us/actions_sets.htm)  
[PlayfairData Set Actions](https://playfairdata.com/how-to-use-tableau-set-actions-to-compare-the-top-n-vs-other/)  
[Sets vs Groups](https://vizualintelligenceconsulting.com/blog-tableau-groups-vs-sets/)  
[Lindsey Poulter All about Sets](https://public.tableau.com/profile/lindsey.poulter8872#!/vizhome/SetActionDrilldown/ChangeDimensions)  
[Dashboard Layout and Formatting](https://www.tableau.com/learn/tutorials/on-demand/dashboard-layouts-and-formatting)  
[Customisable Popup Charts](https://datavis.blog/2019/03/17/popup-charts/)  
[New in 2019.2](https://www.tableau.com/products/new-features#reveal--27)  
[Workbook Optimization](https://onlinehelp.tableau.com/current/pro/desktop/en-us/performance_tips.htm)  
[All about Layout](https://onlinehelp.tableau.com/current/pro/desktop/en-us/dashboards_organize_floatingandtiled.htm)  
[Blending verse Joining](https://dataanimators.com/2015/10/05/the-importance-of-granularity-to-blend-or-not-to-blend/)  


__01-Stu-Warmup__  
__02-Ins-Groups_Sets__  
__03-Stu-Groups_Sets__  
__04-Ins-Calculations__  
__05-Stu-Calculations__  
__06-Ins-Maps__  
__07-Stu-Maps1__  
__08-Stu-Maps2__  
__09-Ins-Dashboard__  
__10-Stu-Dashboard__  
__11-Ins-LOD__  
* How to think about LOD `If you’re familiar with SQL, you can think of measure filters as equivalent to the HAVING clause in a query, and dimension filters as equivalent to the WHERE clause.`  
[LOD MUST READ](https://onlinehelp.tableau.com/current/pro/desktop/en-us/calculations_calculatedfields_lod_overview.htm?_ga=2.148946806.1915779330.1561316575-1079758548.1558566782)  
* from above article `INCLUDE` level of detail expressions will have either the same level of detail as the view or a finer level of detail than the view. Therefore, values will never be replicated.`FIXED` level of detail expressions can have a finer level of detail than the view, a coarser level of detail, or the same level of detail. The need to aggregate the results of a FIXED level of detail depends on what dimensions are in the view.  `EXCLUDE` level of detail expressions always cause replicated values to appear in the view. When calculations including EXCLUDE level of detail expressions are placed on a shelf, Tableau defaults to the ATTR aggregation (as opposed to SUM or AVG) to indicate that the expression is not actually being aggregated and that changing the aggregation will have no effect on the view.`

__12-Stu-LOD__  


## Lesson 3 - The Answer, My Friend, Is Tableauing in the Wind
* Exploratory Data Analysis using Tableau
* Clean data prior to visualizations
* Create Tableau Dashboard


### **_Additional Resources_**


__01-Stu_Healthcare__  
__02-Stu_Airline__  
__03-Stu_Languages__


# Tableau Homework - Citi Bike Analytics

### Before You Begin

* This assignment will be saved to your tableau public account rather than github. 

* If you haven't already, be sure to create a tableau public account [here](https://public.tableau.com/s/).

* The free tier of tableau only lets you save to their public server. This means that each time you save your file it will be uploaded to your tableau public profile. 

* You are able to load and continue working on the same workbook.

* When you are finished with your assignment, you will turn in the URL to your tableau public workbook along with any additional files used for your analysis. 

## Background

![Citi-Bikes](Images/citi-bike-station-bikes.jpg)

Congratulations on your new job! As the new lead analyst for the [New York Citi Bike](https://en.wikipedia.org/wiki/Citi_Bike) Program, you are now responsible for overseeing the largest bike sharing program in the United States. In your new role, you will be expected to generate regular reports for city officials looking to publicize and improve the city program.

Since 2013, the Citi Bike Program has implemented a robust infrastructure for collecting data on the program's utilization. Through the team's efforts, each month bike data is collected, organized, and made public on the [Citi Bike Data](https://www.citibikenyc.com/system-data) webpage.

However, while the data has been regularly updated, the team has yet to implement a dashboard or sophisticated reporting process. City officials have a number of questions on the program, so your first task on the job is to build a set of data reports to provide the answers.

## Task

**Your task in this assignment is to aggregate the data found in the Citi Bike Trip History Logs and find two unexpected phenomena.** 

**Design 2-5 visualizations for each discovered phenomena (4-10 total). You may work with a timespan of your choosing. Optionally, you may merge multiple datasets from different periods.** 

**The following are some questions you may wish to tackle. Do not limit yourself to these questions; they are suggestions for a starting point. Be creative!**

* How many trips have been recorded total during the chosen period?

* By what percentage has total ridership grown?

* How has the proportion of short-term customers and annual subscribers changed?

* What are the peak hours in which bikes are used during summer months?

* What are the peak hours in which bikes are used during winter months?

* Today, what are the top 10 stations in the city for starting a journey? (Based on data, why do you hypothesize these are the top locations?)

* Today, what are the top 10 stations in the city for ending a journey? (Based on data, why?)

* Today, what are the bottom 10 stations in the city for starting a journey? (Based on data, why?)

* Today, what are the bottom 10 stations in the city for ending a journey (Based on data, why?)

* Today, what is the gender breakdown of active participants (Male v. Female)?

* How effective has gender outreach been in increasing female ridership over the timespan?

* How does the average trip duration change by age?

* What is the average distance in miles that a bike is ridden?

* Which bikes (by ID) are most likely due for repair or inspection in the timespan?

* How variable is the utilization by bike ID?

**Next, as a chronic over-achiever:**

* Use your visualizations (does not have to be all of them) to design a dashboard for each phenomena.
* The dashboards should be accompanied with an analysis explaining why the phenomena may be occuring. 

**City officials would also like to see one of the following visualizations:**

* **Basic:** A static map that plots all bike stations with a visual indication of the most popular locations to start and end a journey with zip code data overlaid on top.

* **Advanced:** A dynamic map that shows how each station's popularity changes over time (by month and year). Again, with zip code data overlaid on the map.

* The map you choose should also be accompanied by a write-up unveiling any trends that were noticed during your analysis.

**Finally, create your final presentation**

* Create a Tableau story that brings together the visualizations, requested maps, and dashboards.
* This is what will be presented to the officials, so be sure to make it professional, logical, and visually appealing. 

## Considerations

Remember, the people reading your analysis will **NOT** be data analysts. Your audience will be city officials, public administrators, and heads of New York City departments. Your data and analysis needs to be presented in a way that is focused, concise, easy-to-understand, and visually compelling. Your visualizations should be colorful enough to be included in press releases, and your analysis should be thoughtful enough for dictating programmatic changes. 

## Submission 

Your final submission should include:

* A link to your Tableau Public workbook that includes: 
  * 4-10 Total "Phenomenon" Visualizations 
  * 2 Dashboards
  * 1 City Official Map
  * 1 Story 
* A text or markdown file with your analysis on the phenomenons you uncovered from the data.

## Assessment

Your final product will be assessed on the following metrics:

* Analytic Rigor

* Readability

* Visual Attraction


## Hints

* You may need to get creative in how you combine each of the CSV files. Don't just assume Tableau is the right tool for the job. At this point, you have a wealth of technical skills and research abilities. Dig for an approach that works and just go with it.

* Don't just assume the CSV format hasn't changed since 2013. Subtle changes to the formats in any of your columns can blockade your analysis. Ensure your data is consistent and clean throughout your analysis. (Hint: Start and End Time change at some point in the history logs).

* Consider building your visualizations with small extracts of the data (i.e. single files) before attempting to import the whole thing. What you will find is that importing all 20+ million records of data will create performance issues quickly. Welcome to "Big Data."

* While utilizing all of the data may seem like a nice power play, consider the time-course in making your analysis. Is data from 2013 the most relevant for making bike replacement decisions today? Probably not. Don't let overwhelming data fool you. Ground your analysis in common sense.

* Remember, data alone doesn't "answer" anything. You will need to accompany your data visualizations with clear and directed answers and analysis.

* As is often the case, your clients are asking for a LOT of answers. Be considerate about their need-to-know and the importance of not "cramming in everything". Of course, answer each question, but do so in a way that is organized and presentable.

* Since this is a project for the city, spend the appropriate time thinking through decisions on color schemes, fonts, and visual story-telling. The Citi Bike program has a clear visual footprint. As a suggestion, look for ways to have your data visualizations match their aesthetic tones.

* Pay attention to labels. What exactly is "time duration"? What's the value of "age of birth"? You will almost certainly need calculated fields to get what you need.

* Keep a close eye for obvious outliers or false data. Not everyone who signs up for the program is answering honestly.

* In answering the question of "why" a phenomenon is occurring, consider adding other pieces of information on socioeconomic or other geographic data. Tableau has a map "layer" feature that you may find handy.

* Don't be afraid to manipulate your data and play with settings in Tableau. Tableau is meant to be explored. We haven't covered all that you need -- so you will need to keep an eye out for new tricks.

* Treat this as a serious endeavor! This is an opportunity to show future employers that you have what it takes to be a top-notch analyst. 

* Good luck!

### Copyright

Data Boot Camp (C) 2019. All Rights Reserved.

