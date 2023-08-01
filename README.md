## Problem statement

Loop monitors several restaurants in the US and needs to monitor if the store is online or not. All restaurants are supposed to be online during their business hours. Due to some unknown reasons, a store might go inactive for a few hours. Restaurant owners want to get a report of the how often this happened in the past.   

Build backend APIs that will help restaurant owners to achieve this goal.


###  My work
view the Jupyter Notebook about data analysis on 
[nbviewer.org](https://nbviewer.org/github/SinghaniaV/loopai/blob/master/notebooks/EDA.ipynb)

1. since, the smallest unit for which we have to measure the availability is an hour.
2. we divide menu_hours into batches of 1 hour for each day. (eg: 9AM to 12PM contains 3 batches)
3. we look for available data in each of the batches.
4. if the store was active we mark the whole hour as available. 
5. if the store was not active or the data is not available then we mark the whole hour as not available.