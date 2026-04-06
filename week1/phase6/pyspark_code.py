from pyspark.sql import SparkSession
from pyspark.sql.functions import *
spark = SparkSession.builder.getOrCreate()

customers_data = [
    (1, "John Doe", "john@example.com", "Hyderabad"),
    (2, "Alice ", "alice@example.com", "Chennai"),
    (3, None, "bob@example.com", "Bangalore"),        # NULL name
    (4, "David", None, "Mumbai"),                    # NULL email
    (5, "Eva", "eva@example.com", "Hyderabad"),
    (6, "Frank", "frank@example.com", "Delhi"),
]
customers = spark.createDataFrame(customers_data, ["customer_id", "name", "email", "city"])

orders_data = [
    (101, 1, "2024-01-01", 1000),
    (102, 2, "2024-01-02", 2000),
    (103, 3, "2024-01-03", -500),     # INVALID negative value
    (104, 99, "2024-01-04", 1500),    # INVALID FK (customer_id 99)
    (105, 1, "2024-01-05", None),     # NULL amount
    (106, 5, "2024-01-06", 3000),
    (107, 5, "2024-01-07", 3000),     # duplicate-like record
]
orders = spark.createDataFrame(orders_data, ["order_id", "customer_id", "order_date", "amount"])
orders = orders.withColumn("order_date", to_date(col("order_date")))


