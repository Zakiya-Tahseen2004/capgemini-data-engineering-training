# Initialize Spark session
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.functions import sum, count

spark = SparkSession.builder.appName('Spark Playground').getOrCreate()

customers = spark.read.option("header", "true").csv("/samples/customers.csv")
sales=spark.read.option("header", "true").csv("/samples/sales.csv")

#customers.show()
#customers.printSchema()
#clean_cus = customers.dropna()
#clean_cus = customers.fillna("Unknown")

"""valid = customers.filter(
    col("customer_id").isNotNull() &
    col("first_name").isNotNull() &
    col("email").isNotNull()
)"""
#titanic= spark.read.format("parquet").load("/samples/titanic.parquet")
#titanic.show()
#products= spark.read.format("json").load("/samples/products.json")

sales.show()
clean = sales.dropna(subset=["sale_date", "total_amount"])
clean= clean.withColumn("total_amount",col("total_amount").cast("int"))
daily_sales= clean.groupBy("sale_date").agg(sum("total_amount").alias("daily_sales")).orderBy("sale_date").show()

joined= customers.join(sales, "customer_id")
cleaned = joined.filter(
    col("city").isNotNull() & col("total_amount").isNotNull()
)
cleaned= cleaned.withColumn(
    "total_amount",col("total_amount").cast("int")
)
result= cleaned.groupBy("city").agg(sum("total_amount").alias("revenue")).show()


sales.groupBy("customer_id").agg(count("*").alias("order_count")) \
    .filter(col("order_count") > 2).show()


"""df = customers.join(sales, "customer_id")
df = df.withColumn("total_amount", col("total_amount").cast("int"))
result_df= df.groupBy("city", "customer_id") \
    .agg(sum("total_amount").alias("total_spend")).show()"""


"""df = customers.join(sales, "customer_id")
df = df.withColumn("total_amount", col("total_amount").cast("int"))

result_df = df.groupBy("customer_id", "city").agg(sum("total_amount").alias("total_spend"),count("sale_id").alias("order_count")).show()"""


data = [
(1, "Ravi", "Hyderabad", 25),
(2, None, "Chennai", 32),
(None, "Arun", "Hyderabad", 28),
(4, "Meena", None, 30),
(4, "Meena", None, 30),
(5, "John", "Bangalore", -5)
]
columns = ["customer_id", "name", "city", "age"]
df = spark.createDataFrame(data, columns)

#clean_df = df.dropna().show()
clean_df = df.fillna({
    "customer_id": 0,
    "name": "Unknown",
    "city": "Unknown"
}).dropDuplicates().filter(col("age") > 0)
clean_df.show()

result_df = clean_df.groupBy("city").agg(count("*").alias("customer_count"))
result_df.show()

