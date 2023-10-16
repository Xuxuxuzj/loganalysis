import pyarrow.parquet as pq

# Specify the path to your Parquet file
parquet_file_path = "L:\\basic\Personal Archive\Z\zhangj\parameter_data_files\magnet_erdu_ilock_status.parquet"

# Read the Parquet file into a PyArrow table
table = pq.read_table(parquet_file_path)

# Convert the PyArrow table to a pandas DataFrame
df = table.to_pandas()

# Print the contents of the DataFrame
print(df)
