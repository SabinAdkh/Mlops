import pandas as pd

# Loading NYC Taxi Trips Data

data_url = "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2021-01.parquet"

# Read the data in pandas 
green_data = pd.read_parquet(data_url)
print(green_data.head())

green_data.to_parquet("green_trip_data", index=False)