# Cyclistic Case Study

## Business Task
This case study aims to understand how casual riders and annual members use Cyclistic bikes differently.

First, we need to define the notion of "use", which can be measured by the duration of the trip, 
the distance covered, the number of trips, etc. In this case study, we will focus on the 
bike type, duration and distance of the trip.

## Data Source
The data used in this case study is provided by Motivate International Inc. under the license that grants 
a non-exclusive, royalty-free, limited, perpetual license to access, reproduce, analyze, copy, modify, distribute in 
your product or service and use the Data for any lawful purpose. 
The data is available on [this link](https://divvy-tripdata.s3.amazonaws.com/index.html).

## Data Cleaning
The data is cleaned by removing duplicates, missing values, and outliers. I will use python, with the help of pandas, 
numpy, and matplotlib libraries, to clean, analyse and provide visualisation to the data.

Upon loading the data, I first check for missing values, duplicates, and outliers and remove them if identified.

To analyse the difference in trip duration and distances between casual and member riders, I will first ignore
irrelevant columns, namely `ride_id`, `rideable_type`, `start_station_name`,`end_station_name`, 
then I will add 2 new columns, `duration` and `distance`, which are calculated from the `started_at`, `ended_at` columns
and the latitude and longitude of the start and end stations respectively.

I will then group the data by `member_casual`, then compute the mean, medium, and standard deviation of the 
`duration` and `distance` columns.

And the analysis for bike types will be run by grouping the data by 'member_casual', and then compute the count of each
bike type.

## Data Analysis
The analysis will be done by comparing the mean, median, and standard deviation of the trip duration and distance
between casual and member riders. The analysis will also include the count of each bike type used by casual and member 
riders.

## Conclusion
The dataset contains almost three times as many member riders as casual riders, which could potentially mean that the
result for casual members might not be as accurate as the member riders. However, given the number of casual riders are
still substantial, the analysis should still provide a good insight into how casual riders and annual members use.

The analysis shows that casual riders tend to have longer trip duration compared to member riders, where the average 
trip duration is roughly 1.6 times longer than the member riders. The average distance covered however, are about the
same. Several reasons could explain this, such as casual riders are more likely to be tourists, which means they are 
more likely to stop and take pictures during the trip; or casual riders are more likely to ride in groups, which means
they are more likely to stop and wait for each other; or simply because riders who are more athletic are more likely to
become members. Further analysis of the geographical data could provide more insights into this.

The analysis did not identify any significant difference in the bike types used by casual and member riders.
