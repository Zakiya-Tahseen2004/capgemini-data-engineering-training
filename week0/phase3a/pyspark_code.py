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
