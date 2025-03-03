from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.appName("SimplePySparkJob").getOrCreate()

# Read a CSV file into a DataFrame
input_file = "E:/Data Engineering/Python Samples/Employee Sample Data.xlsx"
df = spark.read.csv(input_file, header=True, inferSchema=True)

##jiosdjoisjofijfioj
df.show()

spark.stop()
