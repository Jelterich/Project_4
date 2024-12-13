# Project_4

## Required Modules:
* pandas
* numpy
* matplotlib
* seaborn
* sklearn
* kagglehub
* sqlalchemy
* os



READ:

- load-to-postgres.py will take the data from kaggle and put it into our PostgreSQL database
- Fraud_Date_Combined pulls from the database
- I need to add back in the second round of plots and then remove the category columns afterwards before the model runs.
- Need to put the PostgreSQL login info in another file and tie in.
- Need to figrue out the Kagglehub default temp download folder not recongizing. Might be a me thing. Don't want users to have to go manually put the temp file address in like we have been.
- Need to write a cell that runs the load-to-postgres.py file without having to run it separately in CMD.


The separate files allow us to use our script with multiple data sets, as long as the sets are cleaned to have the same header names.
By pulling the columns we want via SQL pull, we can do live comparrisons without re-cleaning the data. Example would be running a modeul with 7 columns, then re-running it with 2 additonal, 2 less, etc without ahving to drop and add each time.



Bonus:

If we get there, we can host the 
