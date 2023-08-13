## Problem statement

Loop monitors several restaurants in the US and needs to monitor if the store is online or not. All restaurants are supposed to be online during their business hours. Due to some unknown reasons, a store might go inactive for a few hours. Restaurant owners want to get a report of the how often this happened in the past.   

Build backend APIs that will help restaurant owners to achieve this goal.

### System requirement

- Do not assume that this data is static and precompute the answers as this data will keep getting updated every hour.
- You need to store these CSVs into a relevant database and make API calls to get the data.
  - /trigger_report endpoint that will trigger report generation from the data provided (stored in DB).
    - Output - report_id (random string).
    - report_id will be used for polling the status of report completion.
  - /get_report endpoint that will return the status of the report or the csv.

###  My ongoing work

- since, the smallest unit for which we have to measure the availability is an hour.
- we divide menu_hours into batches of 1 hour for each day. (eg: 9AM to 12PM contains 3 batches).
- we look for available data in each of the batches.
- if the store was active we mark the whole hour as available. 
- if the store was not active or the data is not available then we mark the whole hour as not available.