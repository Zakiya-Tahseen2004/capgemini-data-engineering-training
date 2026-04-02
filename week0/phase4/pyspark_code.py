# Initialize Spark session
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, count, when
spark = SparkSession.builder.appName('Spark Playground').getOrCreate()

customers = spark.read.option("header", "true").csv("/samples/customers.csv")
sales=spark.read.option("header", "true").csv("/samples/sales.csv")

#customers.printSchema()
#sales.printSchema()
sales_df = sales.withColumn("total_amount", col("total_amount").cast("int"))

#Task 1: Daily Sales
task1_df = sales_df.groupBy("sale_date").agg(sum("total_amount").alias("total_sales"))
task1_df.show()

#Task 2: City-wise Revenue
task2_df = customers.join(sales_df, "customer_id").groupBy("city").agg(sum("total_amount").alias("total_revenue"))
task2_df.show()

#Task 3: Top 5 Customers
task3_df = customers.join(sales_df, "customer_id").groupBy("first_name") \
    .agg(sum("total_amount").alias("total_spend")) \
    .orderBy(col("total_spend").desc()).limit(5)
task3_df.show()

#Task 4: Repeated Customers (>1 order)
task4_df = sales_df.groupBy("customer_id").agg(count("*").alias("order_count")) \
    .filter(col("order_count") > 1)
task4_df.show()

#Task 5: Customer Segmentation → Create business logic: total_spend > 10000 → Gold 5000–10000 → Silver < 5000 → Bronze
task5_df = customers.join(sales_df, "customer_id") \
    .groupBy("first_name").agg(sum("total_amount").alias("total_spend")) \
    .withColumn("segment",
        when(col("total_spend") > 100, "Gold")
        .when(col("total_spend") >= 50, "Silver")
        .otherwise("Bronze")
    )
task5_df.show()

#Task 6: Final Reporting Table 
final_df = customers.join(sales_df, "customer_id").groupBy("first_name", "city") \
    .agg(
        sum("total_amount").alias("total_spend"),
        count("sale_id").alias("order_count")
    ) \
    .withColumn("segment",
        when(col("total_spend") > 100, "Gold")
        .when(col("total_spend") >= 50, "Silver")
        .otherwise("Bronze")
    )
final_df.show()

#Task 7: Save Output 
final_df.write.mode("overwrite").csv("/samples/output/report")

