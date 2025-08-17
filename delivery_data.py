#Bathabile Ndzendze
#17 August 2025

import duckdb
import io

with open("delivery_data.csv","r") as f:
    csv_text = f.read() #opening the delivery_data.csv file
tbl = duckdb.from_csv_auto(io.StringIO(csv_text)) #Where the data is stored

filter_delay = duckdb.sql("SELECT * FROM tbl WHERE delay_minutes>0") #filtering the data where the delivery was delayed
print(filter_delay) #print the data

summary = duckdb.sql("SELECT city, COUNT(*) AS total_deliveries, SUM(delay_minutes) AS total_delay_minutes, FROM tbl WHERE delay_minutes>0 GROUP BY city ORDER BY total_delay_minutes DESC") #Summarise the data for delayed deliveries by city

print(summary) #print the summarised data 