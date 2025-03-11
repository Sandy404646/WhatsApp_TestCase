from pyspark.sql import SparkSession
from pyspark.sql.functions import *
# Create a Spark session
spark = SparkSession.builder.appName("SimplePySparkJob").getOrCreate()

# Read a JSON file into a DataFrame
input_file = "E:/Data Engineering/Python Samples/Employee Sample Data.xlsx"
df = spark.read.json(input_file)

##filtering first name
df.filter(col("firstname")=="John")


## To display
df.show()

spark.stop()
