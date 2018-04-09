# state-data

# CIS 550 - Databases & information systems
### Spring 2018
#### Project milestone 1 - topic proposal

__Group members__: Brian Sokas (bsokas@seas.upenn.edu) , Andrew Molchan (amolchan@seas.upenn.edu) , Pavan Madduri (pmadduri@wharton.upenn.edu) ,
Joseph Haymaker (josepma@seas.upenn.edu), 

__Project idea__: A web app that allows users to compare livability of different states based on different factors such as: traffic, gun violence, educational finances, etc.

__Questions a user may ask:__
_1. What are the cost of living differences between 2 states?
1. What are the top 10 best states to live in?
1. What are the worst states to live in?
1. How dangerous is one state versus another?
1. Between two states, which one will probably assure better primary/secondary education?
1. Which states are better for retirees?
1. What are the best states to start a small business in?
1. What are the least healthy states?_


__State Data - mortality, gun violence, income, socioeconomic factors, etc.__
+ https://www.kaggle.com/jboysen/us-traffic-2015/data
+ https://www.kaggle.com/cdc/mortality/data
+ https://www.kaggle.com/jboysen/state-firearms/data
+ https://www.kaggle.com/noriuk/us-educational-finances/data
+ https://www.kaggle.com/zusmani/us-mass-shootings-last-50-years/data
+ https://www.kaggle.com/IHME/us-countylevel-mortality/data


__Map data visualization__
+ https://www.sencha.com/blog/using-the-ext-js-d3-adapter-to-create-a-custom-data-visualization/
+ https://forum.freecodecamp.org/t/us-state-map-visualization-using-d3-js/19479
+ https://jsmaps.io/america/javascript-map-of-united-states-of-america/
+ https://onextrapixel.com/8-javascript-libraries-for-interactive-map-visualizations/
+ https://github.com/CodeForPhilly/stately
+ https://www.npmjs.com/package/stately

_____________________________

# Milestone 2

##### Project Motivation

Two of the four members of this group are graduating in a little over a month(!) so quality of life in states commonly associated with tech jobs is an everyday topic. This project is an attempt to consolidate some helpful data that could prove influential in picking one state over another when deciding where to live.

##### Data Sources

Through public data portals, we found data on crime by state and metropolitan area, as well as data on mental health indicators.  As we build our app, we will also consider using data for economic quality of life indicators as well.

+ [FBI Crime Data](https://ucr.fbi.gov/crime-in-the-u.s/2016/crime-in-the-u.s.-2016/tables/table-3)
+ [Metropolitan Crime Data](https://data.world/garyhoov/crime-rates-2016-by-us-metro-areas-with-city-detail/workspace/file?filename=Crime+Rates+by+Metropolitan+Areas+2016.xls) 
+ [Behavioral Risk Factors](https://data.world/us-hhs-gov/753dcbd1-e553-420d-ba5e-c3bc7bc9ec14/workspace/file?filename=csv-1.csv)

##### Relational Schema

__FBI Crime Data__: (_**State**_, _**Area**_, Population, Violent crime, Murder and nonnegligent manslaughter, Rape (revised definition2), Rape (legacy definition3), Robbery, Aggravated assault, Property crime, Burglary, Larceny-theft, Motor vehicle theft)

__Metropolitan Crime Data__: (_**Metropolitan Statistical Area**_, Population	, Violent crime, Murder and
Nonnegligent manslaughter, Rape, Robbery, Aggravated assault, Property crime,	Burglary, Larceny-theft, Motor vehicle theft)

__Behavioral Risk Factors__: (_**Year**_, _**LocationAbbr**_, _**LocationDesc**_, Category, Topic Question, Data_Value_Unit, Data_Value_Type,	Data_Value, Data_Value_Footnote_Symbol, Data_Value_Footnote, Data_Value_Std_Err, Low_Confidence_Limit, High_Confidence_Limit, Sample_Size, _**Break\_Out**_ , _**Break\_Out\_Category**_, GeoLocation, CategoryId, TopicId, QuestionId	LocationId, BreakOutId, BreakOutCategoryid)

##### NoSQL Component

Our data, once fully processed with joins, has the opportunity to be streamlined and optimized for repetitive calls. By combining the final data extracted from our joins into a single large NoSQL table, we can eliminate the need to repeatedly call complex and costly select and join operations and simply provide the key to the NoSQL table for a quick display.

##### Definite Application Features

The major feature of our application will be to allow users to either select or ‘hover’ over a state etched on a displayed image of the United States and see informative data about that state in line with the data we are processing. This might include total firearm ownership by population percentage or average commute times. The data displayed will be unique and aggregate to the selected state.

##### Optional Application Features

If time allows, we think it would be interesting to provide more city-level data. This would entail including some sort of dots or markers on the map to indicate major metropolitan areas that we were able to extract data for. Big cities like New York, San Francisco, Seattle or L.A. could be good starting points. Additionally, it could also be neat to provide a heat-map for particular trends. For instance, if gun ownership in a state is particularly high that state will be colored a dark red, while states will lower ownership good be green or gray.

##### Technology and Tools

The application will run on the Javascript libraries and runtimes we covered in class. In particular, the backend web-server will sit on a Node JS implementation and it will integrates with an HTML/CSS front incorporating Angular JS. 

As mentioned prior, the raw data files will be stored in an AWS S3 instance. The NoSQL component of the project will be stored in an AWS DynamoDB instance. 

## Member Responsibilities

##### Brian

Brian will work on the Node JS backend for the web application, along with contributing to AWS setup for the data. Additionally, if the group decides to pursue a NoSQL option, he’ll contribute to the implementation.

##### Joey

Joey will work on the application frontend in HTML/CSS and Angular. He has already found a handy third-party library for displaying an image of the United States and building functionality on top of it to select states.

##### Andrew

Andrew will focus on developing the front-end using Angular and potentially other front-end frameworks like Bootstrap to make the app responsive. Pavan or Andrew are new to AWS and should be able to help us get the $100 credits available to students.

##### Pavan

Pavan will focus on complex SQL query design with multiple joins, subqueries, aggregation etc., and also contribute to developing the front-end using Angular. Pavan or Andrew are new to AWS and should be able to help us get the $100 credits available to students.

_____________________

# Milestone 3

### Populate the database

Now that you have a baseline schema to work on, the next part is to populate the database with the datasets you have chosen. You should clean and format data from your main and complementary sources, as needed, and perform entity resolution. 

For each of your __*6-10 questions (from Milestone 1) provide its translation to an SQL query*__.   (If you needed to change any of your original questions, provide the new questions in English and explain why you needed to change or replace them.)

You should use the __AWS Getting Started__ handout (Canvas/Files/Project/RDS_HowToConnect.pdf) to create your own __MySQL__ (cheaper!) or __Oracle database__ on __Amazon RDS__. For this milestone you should submit a text file with a full JDBC/SQLPLUS connect string, including guest user ID and password and database schema name, to us via Canvas. (From this we should be able to dump your SQL tables.) 


# CIS 550 - Databases & information systems
### Spring 2018
#### Project milestone 3


__Questions a user may ask:__
1. What are the top 10 healthy states over the past 5 years of available data? (health based on mean physically and/or mentally unhealthy days per person per year)
2. What are the 10 least healthy states over the past 5 years of avaialable data?
3. What are the 10 safest states? (Safety is based on number of violent crimes per 100,000 inhabitants)
4. What are the 10 least safe states?
5. Which states are in the top 10 for violent crime rate and have > 10% of the population experiencing frequent mental distress (14 or more mentally unhealty days per year) in alphabetical order.
6. Which state has the lowest violent crime rate that also has an above average general health level? (Health based on percent of people who self-reported fair or poor health)

__SQL translations:__
1.  SELECT State, Average_Unhealthy_Days
    FROM(
        SELECT LocationDesc AS State, AVG(Data_Value) AS Average_Unhealthy_Days
        FROM Behavior
        WHERE Year IN (2006, 2007, 2008, 2009, 2010) AND Question = 'Mean physically or mentally unhealthy days'
        GROUP BY LocationDesc
        ORDER BY Avg(Data_Value) DESC
    )
    WHERE rownum <= 10
    ORDER BY Average_Unhealthy_Days DESC
    
2.  SELECT State, Average_Unhealthy_Days
    FROM(
        SELECT LocationDesc AS State, AVG(Data_Value) AS Average_Unhealthy_Days
        FROM Behavior
        WHERE Year IN (2006, 2007, 2008, 2009, 2010) AND Question = 'Mean physically or mentally unhealthy days'
        GROUP BY LocationDesc
        ORDER BY Avg(Data_Value)
    )
    WHERE rownum <= 10
    ORDER BY Average_Unhealthy_Days

3.  SELECT *
    FROM(
        SELECT State, Violent_Crime
        FROM Crime
        WHERE Area = 'State Total'
        GROUP BY State
        ORDER BY Violent_Crime
    )
    WHERE rownum <= 10
    ORDER BY Violent_Crime

4.  SELECT *
    FROM(
        SELECT State, Violent_Crime
        FROM Crime
        WHERE Area = 'State Total'
        GROUP BY State
        ORDER BY Violent_Crime DESC
    )
    WHERE rownum <= 10
    ORDER BY Violent_Crime DESC

5.  SELECT State
    FROM Behavior b JOIN Crime c ON b.LocationDesc = c.State
    WHERE b.Question = 'Percentage with 14 or more mentally unhealthy days (Frequent Mental Distress)'
    AND Data_Value > 10 AND Year = 2010 AND c.State IN (
        SELECT State
        FROM (
            SELECT State
            FROM Crime
            WHERE Area = 'State Total'
            GROUP BY State
            ORDER BY Violent_Crime DESC
        )
        WHERE rownum <= 10
    )
    ORDER BY State
            

6.  SELECT State
    FROM(
        SELECT State, Violent_Crime
        FROM Behavior b JOIN Crime c ON b.LocationDesc = c.State
        WHERE b.Question = 'Percentage with fair or poor self-rated health' AND b.Year = 2010
        GROUP BY State
        HAVING Data_Value > AVG(Data_Value
    )
    GROUP BY State
    HAVING Violent_Crime = MIN(Violent_Crime)
    
        
