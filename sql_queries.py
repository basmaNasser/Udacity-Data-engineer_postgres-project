# DROP TABLES

songplay_table_drop = "drop table if exists songplay"
song_table_drop = "drop table if exists song"
artist_table_drop = "drop table if exists artist"
time_table_drop = "drop table if exists time"
user_table_drop = "drop table if exists users"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplay (songplay_id serial not null primary key, start_time bigint, user_id varchar, level varchar, song_id varchar, artist_id varchar, session_id varchar, location varchar, user_agent varchar);
""")


user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id varchar primary key, first_name varchar, last_name varchar, gender varchar, level varchar);
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS song (song_id varchar NOT NULL primary key, title varchar NOT NULL, artist_id varchar NOT NULL, year int, duration int);
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artist (artist_id varchar not null primary key, name varchar not null, location varchar, latitude float, longitude float);
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (start_time bigint primary key, hour int, day int, week int, month int, year int, weekday varchar);
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplay (songplay_id, start_time, user_id, level, song_id, artist_id, session_id , location, user_agent) VALUES (default, %s, %s, %s, %s,%s,%s,%s,%s)  ON CONFLICT DO NOTHING;
""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;               
""")

song_table_insert = ("""INSERT INTO song (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s)  ON CONFLICT DO NOTHING;
""")

artist_table_insert = ("""INSERT INTO artist (artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;
""")


time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s,%s,%s) ON CONFLICT DO NOTHING;
""")

# FIND SONGS

song_select = (""" SELECT s.song_id, a.artist_id
    FROM song s
    JOIN artist a ON s.artist_id = a.artist_id
    WHERE s.title = %s AND a.name = %s AND s.duration = %s;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop,song_table_drop, artist_table_drop, time_table_drop]