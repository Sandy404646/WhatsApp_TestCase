from pyspark.sql import SparkSession
from pyspark.sql.functions import *
# Create a Spark session
spark = SparkSession.builder.appName("SimplePySparkJob").getOrCreate()

# Read a CSV file into a DataFrame
input_file = "E:/Data Engineering/Python Samples/Employee Sample Data.xlsx"
df = spark.read.csv(input_file, header=True, inferSchema=True)

df.filter(col("firstname")=="John")

df.show()

spark.stop()
