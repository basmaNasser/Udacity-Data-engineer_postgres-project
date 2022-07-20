# Project: Data Modeling with Postgres

This is Udacity Data Engineering nanodegree project 1, in this project need to create a postgres database sparkifydb for a music app called "Sparkify". The purpose of the database is to model song and log datasets (originaly stored in JSON format) with a star schema optimised for queries on song play analysis and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.

# Schema for Song Play Analysis

## Fact Table

songplays - records in log data associated with song plays i.e. records with page NextSong
songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

## Dimension Tables

users - users in the app
user_id, first_name, last_name, gender, level
songs - songs in music database
song_id, title, artist_id, year, duration
artists - artists in music database
artist_id, name, location, latitude, longitude
time - timestamps of records in songplays broken down into specific units
start_time, hour, day, week, month, year, weekday

# Project Template

test.ipynb displays the first few rows of each table to let you check your database.

create_tables.py drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts.

etl.ipynb reads and processes a single file from song_data and log_data and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables.

etl.py reads and processes files from song_data and log_data and loads them into your tables. You can fill this out based on your work in the ETL notebook.

sql_queries.py contains all your sql queries, and is imported into the last three files above.

# To run python script

ex: %run create_tables.py