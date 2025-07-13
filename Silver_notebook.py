# Databricks notebook source
# MAGIC %md
# MAGIC # DATA READING

# COMMAND ----------

df = spark.read.format('parquet')\
    .option('inferschema',True)\
    .load('abfss://bronze@datalakeforcar.dfs.core.windows.net/rawdata')


# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

df.display()

# COMMAND ----------

df = df.withColumn('model_category',split(col('model_ID'),'-')[0])
df.display()

# COMMAND ----------

df = df.withColumn('RevPerUnit',col('Revenue')/col('Units_Sold'))
df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC # AD-HOC

# COMMAND ----------

display(df.groupBy('Year','BranchName').agg(sum('Units_Sold').alias('Total_Units')).sort('Year','Total_Units', ascending=[True, False]))

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC # DATA WRITING

# COMMAND ----------

df.write.format('parquet')\
    .mode('overwrite')\
    .option('path','abfss://silver@datalakeforcar.dfs.core.windows.net/carsales')\
    .save()

# COMMAND ----------

# MAGIC %md
# MAGIC # Querying Silver Data

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from parquet.`abfss://silver@datalakeforcar.dfs.core.windows.net/carsales`

# COMMAND ----------

