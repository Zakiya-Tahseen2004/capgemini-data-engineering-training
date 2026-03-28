from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, col
from pyspark.sql.functions import avg
from pyspark.sql.functions import count
spark = SparkSession.builder.appName('Spark Playground').getOrCreate()

customers = spark.read.option("header", "true").csv("/samples/customers.csv")
sales = spark.read.option("header", "true").csv("/samples/sales.csv")
#customers = customers.dropna(subset=["customer_id"])
#sales = sales.dropna(subset=["customer_id"])

sales.groupBy("customer_id") \
    .agg(sum(col("total_amount").cast("int")).alias("total_spend")) \
    .show()

sales.groupBy("customer_id") \
    .agg(sum(col("total_amount").cast("int")).alias("total_spend")) \
    .orderBy(col("total_spend").desc()) \
    .limit(3).show()

customers.join(sales, "customer_id", "left") \
    .filter(sales.customer_id.isNull()) \
    .show()

customers.join(sales, "customer_id") \
    .groupBy("city") \
    .agg(sum(col("total_amount").cast("int")).alias("revenue")) \
    .show()

sales.groupBy("customer_id") \
    .agg(avg(col("total_amount").cast("int")).alias("avg_amount")) \
    .show()

sales.groupBy("customer_id") \
    .agg(count("*").alias("orders")) \
    .filter(col("orders") > 1) \
    .show()

sales.groupBy("customer_id") \
    .agg(sum(col("total_amount").cast("int")).alias("total_spend")) \
    .orderBy(col("total_spend").desc()) \
    .show()

